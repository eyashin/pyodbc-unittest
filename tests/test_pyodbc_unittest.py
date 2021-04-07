"""Part of the library provides SQL calls for the Python unittest framework."""
import unittest
from pyodbc_unittest import Dbtest

# change CONNECTION_STRING to real ODBC source
CONNECTION_STRING = 'DSN=postgres.local'


class TestDbtest(unittest.TestCase):
    """Checks the connection to the database and getting the result."""

    def setUp(self):
        self.database = Dbtest(CONNECTION_STRING)

    def tearDown(self):
        self.database.close()

    def test_version(self):
        """Create SQLVERSION.json."""
        sql = 'SELECT 1 AS ONE'
        file_name = 'SQLVERSION'
        self.assertEqual(self.database.from_db(sql, file_name),
                         self.database.from_file(file_name))


if __name__ == '__main__':
    unittest.main()
