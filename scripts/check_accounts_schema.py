import os
import sys
import django
from django.db import connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wub_portal.settings')
django.setup()

with connection.cursor() as cursor:
    cursor.execute('SELECT DATABASE()')
    print('database=', cursor.fetchone())
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    print('tables count=', len(tables))
    for table in tables[:50]:
        print(table)
    print('---')
    cursor.execute("SHOW TABLES LIKE 'accounts_customuser'")
    tables = cursor.fetchall()
    print('accounts_customuser=', tables)
    if tables:
        cursor.execute('SHOW COLUMNS FROM accounts_customuser')
        cols = cursor.fetchall()
        for col in cols:
            print(col)
