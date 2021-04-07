"""Part of the library provides SQL calls for the Python unittest framework."""
import unittest
from pyodbc_unittest import Dbtest

# change CONNECTION_STRING to real ODBC source
CONNECTION_STRING = 'DSN=postgres.local'


class TestDbtest(unittest.TestCase):
    """Checks the connection to the database and getting the result."""

    def test_data(self):
        """Create SQLVERSION.json."""
        database = Dbtest(CONNECTION_STRING)
        sql = 'SELECT 1 AS ONE'
        file_name = 'SELECTONE'
        self.assertEqual(database.from_db(sql, file_name),
                         database.from_file(file_name))
        database.close()

if __name__ == '__main__':
    unittest.main()
