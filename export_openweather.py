import csv
import json
import sqlite3
import sys

DB_FILE = "weather.db"

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print(f"Usage: {sys.argv[0]} --mode filename [city_id]")
    exit()

mode = sys.argv[1]
filename = sys.argv[2]
city_id = sys.argv[3] if len(sys.argv) == 4 else None


with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    if city_id:
        cur.execute("SELECT * FROM WEATHER WHERE CITY_ID = ?", (city_id,))
    else:
        cur.execute("SELECT * FROM WEATHER")
    data = cur.fetchall()

with open(filename, "w") as f:
    if mode == "--csv":
        csv.writer(f).writerows(data)
    elif mode == "--json":
        json.dump(data, f)
    else:
        html = "<table>"
        for i in data:
            html += "<tr>"
            for j in i:
                html += f"<td>{j}</td>"
            html += "</tr>"
        html += "</table>"
        f.write(html)