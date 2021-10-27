# -*- coding: utf-8 -*-
"""databaseCreation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tb8pgbPO75FpJytoMUsmegUI9xSwNWmP
"""

import pandas as pd

#FOR TESTING PURPOSES ONLY. Delete this cell later
import sqlite3

#create connection to database
conn = sqlite3.connect('artInfo.db')

#create cursor instance
c = conn.cursor()

#create the table
c.execute("""Create Table Art (
          artistID INTEGER PRIMARY KEY,
          firstName TEXT,
          lastName TEXT,
          artID INTEGER,
          info TEXT,
          image BLOB NOT NULL
          )""")

#save the changes
conn.commit()

#close the connection
#conn.close()

#sample data
c.execute("INSERT INTO Art VALUES(1,'john','doe',0101,'mickey mouse','1.jpg')")

sql = '''select * from Art t'''

pd.read_sql(sql, conn)