import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

cur = database.cursor()

rows = cur.execute("SELECT id, name, state.name FROM cities NATURAL JOIN "
                   "states WHERE id = states.id ORDER BY id")


results = cur.fetchall()

for result in results:
    print(result)


cur.close()
database.close()
