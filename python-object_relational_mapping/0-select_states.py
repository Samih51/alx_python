import sys
import MySQLdb
database = MySQLdb.connect(host = "localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

results = cur.execute("SELECT * FROM states ORDER BY id")
for result in results:
    print (result)