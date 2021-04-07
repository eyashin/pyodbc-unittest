# pyodbc-unittest
The library provides SQL calls for the Python `unittest` framework

## Preparing
This example contains two files SQL script and Python unittest module. I tested it in a Windows 10 x64 environment.

Python code tested on Python 3.8

SQL code writed on T-SQL language and tested on:
- MS SQL Server 2017, but you can use any other version
- Sybase/SAP ASE 15, but you can use any other version

Run the script in any empty database and configure the ODBC source on it. 
Edit `test_sample.py` and set name of the ODBC source.
```bash
CONNECTION_STRING = 'DSN=<NAME ODBC SOURCE>'
```

## Runing

Run `unittest` in directory with `test_sample.py`.
```bash
> python -m unittest
```


