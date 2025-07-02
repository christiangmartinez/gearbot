import sqlite3

con = sqlite3.connect("gear.db")
cur = con.cursor()

cur.execute("CREATE TABLE gear_query(search_term, query_date, gear_list)")
