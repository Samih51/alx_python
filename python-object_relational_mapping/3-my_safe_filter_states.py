import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

cur = database.cursor()

rows = cur.execute("SELECT * FROM states "
                   "ORDER BY id")


results = cur.fetchall()

for result in results:
    if result[1] == sys.argv[4]:
        print(result)


cur.close()
database.close()
