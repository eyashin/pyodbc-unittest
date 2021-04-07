"""Part of the library provides SQL calls for the Python unittest framework."""
import unittest
from pyodbc_unittest import Dbtest

# change CONNECTION_STRING to real ODBC source
CONNECTION_STRING = 'DSN=mssql.local'

class TestTables(unittest.TestCase):

    def setUp(self):
        self.db = Dbtest(CONNECTION_STRING)

    def tearDown(self):
        self.db.close()
