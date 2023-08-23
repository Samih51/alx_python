import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

cur = database.cursor()

rows = cur.execute("SELECT cities.id, cities.name, states.name FROM "
                   "cities JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id")


results = cur.fetchall()

for result in results:
    print(result)


cur.close()
database.close()
