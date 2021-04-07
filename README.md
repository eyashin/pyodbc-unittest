## pyodbc-unittest
The library provides SQL calls for the Python `unittest` framework

# Unit Test
Unit tests are typically automated tests written and run by software developers to ensure that a section of an application 
(known as the "unit") meets its design and behaves as intended.

# Database Unit Test
The SQL unit testing approach allows us to test part of database objects such as stored procedures, 
functions and schema. The advantage of SQL unit testing is to develop more robust database designs, 
because these objects have already been checked before production deployment, so SQL unit testing process 
allows us to minimize the errors which are related to database objects.

# Quick Start
Install `pyodbc-unittest` from pypi using `pip`
```bash
pip install pyodbc-unittest
```

Import `Dbtest` object in your module
```py
import unittest
from pyodbc_unittest import Dbtest
```

Now you need to setup ODBC data source. Select the type of database you want to set up a database for, for example, SAP Sybase, SQL Server, Postgress, etc. And fill the login, password and server fields.

Wtite you first test. Please fill CONNECTION_STRING with the ODBC data source name.
```py
CONNECTION_STRING = r'DSN=mssql.local'

class TestSelect(unittest.TestCase):

    def test_data(self):
        database = Dbtest(CONNECTION_STRING)
        sql = 'SELECT 1 AS ONE'
        file_name = 'SELECTONE'
        self.assertEqual(database.from_db(sql, file_name),
                         database.from_file(file_name))
        database.close()
```

And run `unittest`
```bash
> python -m unittest
.
----------------------------------------------------------------------
Ran 1 test in 0.112s

OK
```
An artifact named `SELECTONE.json` was created that contains all the information about the result set.

```json
{
  "rowcount": 1,
  "resultcount": 1,
  "error": 0,
  "errormessage": "",
  "names": "[[\"one\"]]",
  "types": "[[\"int\"]]",
  "sizes": "[[10]]",
  "datas": [
    "{\"columns\":[\"one\"],\"index\":[0],\"data\":[[\"1\"]]}"
  ]
}
```

You can directly dive into the examples at  [`tests/`](./tests). 

The exampe use two main functions:
. `Dbtest.db.from_db` loads data from a DB and returns a string for comparison. 
. `Dbtest.db.from_file` loads data from a file and returns a string for comparison. 

