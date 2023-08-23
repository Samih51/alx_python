import sys
import MySQLdb

database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

rows = cur.execute("SELECT cities.name, states.name FROM "
                   "cities JOIN states ON cities.state_id = states.id ")


results = cur.fetchall()
city_names = []
for result in results:
    if result[1] == sys.argv[4]:
        city_names.append(result[0])
    
print(", ".join(city_names))

cur.close()
database.close()
