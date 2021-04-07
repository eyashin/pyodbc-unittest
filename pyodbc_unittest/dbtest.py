""" Part of the library provides SQL calls for the Python unittest framework """
import os
import pyodbc
from pyodbc_unittest.dbresult import Dbresult


class Dbtest:
    """ This class used for connect to database """
	#pylint: disable-msg=too-many-arguments
    def __init__(self, conection_string: str):
		# pylint: disable=c-extension-no-member
        self.con = pyodbc.connect(conection_string)
        self.con.autocommit = True
        self.string = None

    def run(self, sql: str):
        # pylint: disable=c-extension-no-member
        """ Runs SQL query and return cursor """
        result = Dbresult()
        cursor = self.con.cursor()
        try:
            result.load_from_cursor(cursor.execute(sql))
        except pyodbc.ProgrammingError as ex:
            result.error = int(ex.args[0])
            result.errormessage = ex.args[1]
        cursor.close()
        return result

    def execute(self, sql: str) -> bool:
        # pylint: disable=c-extension-no-member
        """ Runs SQL query and return status """
        cursor = self.con.cursor()
        try:
            cursor.execute(sql)
        except pyodbc.ProgrammingError:
            return False
        cursor.close()
        return True

    def to_str(self, dbresult, comparedata=True, rowscount=True,
               columnnames=True, columnntypes=True, error=True) -> str:
        """ Converts data to string for comparison """
        result = ''
        if dbresult is None:
            return result
        if rowscount:
            result += 'ROWS_OUNT = ' + str(dbresult.rowcount) + '\n'
            result += 'RESULT_COUNT = ' + str(dbresult.resultcount) + '\n'
        if error:
            result += 'SQLCODE = ' + str(dbresult.error) + '\n'
            result += 'MESSAGE = ' + str(dbresult.errormessage) + '\n'
        for i in range(dbresult.resultcount):
            if columnnames:
                result += 'COLUMN_NAMES[' + \
                    str(i) + '] = ' + str(dbresult.names[i]) + '\n'
            if columnntypes:
                result += 'COLUMNN_TYPES[' + \
                    str(i) + '] = ' + str(dbresult.types[i]) + '\n'
            if comparedata:
                result += 'DATA[' + str(i) + '] = ' + \
                    str(dbresult.datas[i].to_json(indent=2)) + '\n'
        self.string = result
        return result

    def from_db(self, sql: str, file_name=None, createfile='Y', comparedata=True,
                rowscount=True, columnnames=True, columnntypes=True, error=True):
        """ Loads data from a DB and returns a string for comparison """
        if sql is None:
            return None
        data = self.run(sql)
        if (createfile) and (file_name is not None):
            if not file_name.endswith('.json'):
                file_name += '.json'
            if not os.path.isfile(file_name):
                data.save_to_file(file_name)
        return self.to_str(data, comparedata, rowscount,
                           columnnames, columnntypes, error)

    def from_file(self, file_name: str, comparedata=True, rowscount=True,
                  columnnames=True, columnntypes=True, error=True):
        """ Loads data from a file and returns a string for comparison """
        if file_name is None:
            return None
        data = Dbresult()
        if not data.load_from_file(file_name):
            return ''
        return self.to_str(data, comparedata, rowscount,
                           columnnames, columnntypes, error)

    def close(self):
        """ Close connection """
        if self.con:
            self.con.close()
