import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

cur = database.cursor()

rows = cur.execute("SELECT * FROM states WHERE name = '{}' "
                   "ORDER BY id".format(sys.argv[4]))


results = cur.fetchall()

for result in results:
    print(result)
