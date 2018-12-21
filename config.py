import urllib

CONNECTION_PARAMS = (
    "DRIVER={SQL Server Native Client 11.0};"
    "SERVER=(local)\\SQLEXPRESS;"
    "DATABASE=imdb;"
    "UID=kkrishnav;"
    "PWD='2018@Factset';"
    "Trusted_Connection=yes;"
)

CONNECTION_STRING = 'mssql+pyodbc:///?odbc_connect={0}'.format(urllib.quote_plus(CONNECTION_PARAMS))