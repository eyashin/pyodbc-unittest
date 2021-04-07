""" Part of the library provides SQL calls for the Python unittest framework """
import os
import re
import json
import numpy as np
import pandas as pd


class Dbresult:
    """ This class used for convert data from DB to Pandas DataFrame """

	# pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.rowcount = 0
        self.resultcount = 0
        self.error = 0
        self.errormessage = ''
        self.names = []
        self.types = []
        self.sizes = []
        self.raw = []
        self.datas = []
        self.data = None

    def load_from_cursor(self, cursor):
        """ Load data from cursor """
        self.rowcount = cursor.rowcount
        self.resultcount = 0
        while True:
            if cursor.description:
                names = []
                types = []
                sizes = []
                columncount = 0
                for row in cursor.description:
                    if row[0] != '':
                        names.append(row[0])
                    else:
                        names.append('_unnamed' + str(columncount) + '_')
                    types.append(re.findall(r"'(.+)'", str(row[1]))[0])
                    sizes.append(row[3])
                    columncount += 1
                self.names.append(names)
                self.types.append(types)
                self.sizes.append(sizes)
                rows = cursor.fetchall()
                self.raw.append(rows)
                dataframe = pd.DataFrame(np.array(rows, dtype='U255'))
                if dataframe.shape[0] > 0:
                    dataframe.columns = names
                self.datas.append(dataframe)
                self.data = dataframe
                self.resultcount += 1

            if not cursor.nextset():
                break

    def save_to_file(self, file_name) -> bool:
        """ Save data to file """
        if file_name is None:
            return False
        # do not save error query!
        if self.error != 0:
            return False
        if not file_name.endswith('.json'):
            file_name += '.json'
        data = dict()
        data['rowcount'] = self.rowcount
        data['resultcount'] = self.resultcount
        data['error'] = self.error
        data['errormessage'] = self.errormessage
        data['names'] = json.dumps(self.names)
        data['types'] = json.dumps(self.types)
        data['sizes'] = json.dumps(self.sizes)
        data['datas'] = []
        for item in self.datas:
            data['datas'].append(item.to_json(orient='split'))

        with open(file_name, 'w') as file:
            file.write(json.dumps(data, indent=2))

        print('Data file', file_name, 'created.')
        return True

    def load_from_file(self, file_name) -> bool:
        """ Load data from file """
        if file_name is None:
            return False
        if not file_name.endswith('.json'):
            file_name += '.json'
        if not os.path.isfile(file_name):
            return False

        data = dict()
        with open(file_name, 'r') as file:
            data = json.loads(file.read())
        self.rowcount = data['rowcount']
        self.resultcount = data['resultcount']
        self.error = data['error']
        self.errormessage = data['errormessage']
        self.names = json.loads(data['names'])
        self.types = json.loads(data['types'])
        self.sizes = json.loads(data['sizes'])
        for item in data['datas']:
            dataframe = pd.read_json(item, orient='split',
                              dtype='string', convert_dates=False)
            self.datas.append(dataframe)
            self.data = dataframe

        return True
