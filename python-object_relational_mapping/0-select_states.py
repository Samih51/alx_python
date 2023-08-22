import sys
import MySQLdb
database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = database.cursor()

cur.execute("SELECT * FROM states ORDER BY id")