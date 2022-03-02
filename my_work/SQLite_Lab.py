import sqlite3

import pandas as pd

dataset = [('VER', 1, 'RB'),
           ('HAM', 2, 'Merc'),
           ('BOT', 3, 'Merc'),
           ('PER', 4, 'RB'),
           ('SAI', 5, 'Fer')]

path_to_db = "/Users/nathanlindley/sqlite/mydata.db"
conn = sqlite3.connect(path_to_db)
cur = conn.cursor()

cur.execute('create table mytable (name, position, team)')
conn.commit()
cur.executemany('insert into mytable values (?,?,?)', dataset)
conn.commit()

for row in conn.execute('select * from mytable'):
    print(row)

for row in conn.execute('select * from mytable where position <= 3'):
    print(row)

for row in conn.execute('select team,count(team) from mytable group by team'):
    print(row)

podium = []
for row in conn.execute('select * from mytable where position <= 3'):
    podium.append(row)

podiumdf = pd.DataFrame(podium)
print(podiumdf)