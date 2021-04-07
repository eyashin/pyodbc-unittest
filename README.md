# pyodbc-unittest
The library provides SQL calls for the Python `unittest` framework

## Unit Test
Unit tests are typically automated tests written and run by software developers to ensure that a section of an application 
(known as the "unit") meets its design and behaves as intended.

## Database Unit Test
The SQL unit testing approach allows us to test part of database objects such as stored procedures, 
functions and schema. The advantage of SQL unit testing is to develop more robust database designs, 
because these objects have already been checked before production deployment, so SQL unit testing process 
allows us to minimize the errors, which are related to database objects.

## Quick Start
Install `pyodbc-unittest` from pypi using `pip`
```bash
pip install pyodbc-unittest
```

Import `Dbtest` object in your module
```py
import unittest
from pyodbc_unittest import Dbtest
```

Now you need to setup ODBC data source. Select the type of database you want to set up a database for, for example, 
SAP/Sybase ASE, MS SQL Server, PostgreSQL, etc. Moreover, fill the login, password and server fields.

Write your first test like in the example. Please fill in CONNECTION_STRING with the name of the ODBC data source.
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

```py
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

This example uses two main functions:
- `Dbtest.db.from_db` loads data from a DB and returns a string for comparison. 
- `Dbtest.db.from_file` loads data from a file and returns a string for comparison. 

Now we can change something in select. Digit or name.
```py
        sql = 'SELECT 2 AS ONE'
```

And, if we run `unittest` again, it will be a failed.
```bash
> python -m unittest
F
======================================================================
FAIL: test_data (test_pyodbc_unittest.TestSelect)
Create SQLVERSION.json.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\yashi\Projects\pyodbc-unittest\tests\test_pyodbc_unittest.py", line 17, in test_data
    self.assertEqual(database.from_db(sql, file_name),
AssertionError: 'ROWS[96 chars][0] = [\'int\']\nDATA[0] = {\n  "one":{\n    "0":"2"\n  }\n}\n' != 'ROWS[96 chars][0] = [\'int\']\nDATA[0] = {\n  "one":{\n    "0":"1"\n  }\n}\n'
  ROWS_OUNT = 1
  RESULT_COUNT = 1
  SQLCODE = 0
  MESSAGE =
  COLUMN_NAMES[0] = ['one']
  COLUMNN_TYPES[0] = ['int']
  DATA[0] = {
    "one":{
-     "0":"2"
?          ^
+     "0":"1"
?          ^
    }
  }


----------------------------------------------------------------------
Ran 1 test in 0.127s

FAILED (failures=1)
```
To be continued...

