import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()
pattern = 'N%'
rows = cur.execute("SELECT * FROM states WHERE name LIKE %s COLLATE utf8_bin ORDER BY id", (pattern,))

results = cur.fetchall()

for result in results:
    print(result)
