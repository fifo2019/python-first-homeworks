import collections
import json
import os
import sqlite3
import time
import urllib, requests

DB_FILE = "weather.db"
APPID = "ea574594b9d36ab688642d5fbeab847e"

countries_cityids = collections.defaultdict(set)

with open('city.list.json', 'r', encoding='UTF-8') as f:
    for data in json.load(f):
        country = data["country"]
        city_id = data["id"]
        countries_cityids[data["country"]].add(city_id)

while True:
    country = input("Input country code: ").upper()
    if country in countries_cityids:
        break
    print("Unknown country!")

for i, city_id in enumerate(countries_cityids[country]):
    if i != 0:
        time.sleep(1)
    response = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={APPID}").read()
    data = json.loads(response)
    name = data["name"]
    dt = data["dt"]
    temp = data["main"]["temp"]
    weather_id = data["weather"][0]["id"]
    print(f"Город: {name}, Дата: {dt}, Температура: {temp}, Погода: {weather_id}")
    if not os.path.isfile(DB_FILE):
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("""
                CREATE TABLE WEATHER (
                CITY_ID INTEGER PRIMARY KEY,
                NAME VARCHAR(255),
                DT DATE,
                TEMP INTEGER,
                WEATHER_ID INTEGER)""")
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT OR REPLACE INTO WEATHER VALUES (?, ?, ?, ?, ?)", (city_id, name, dt, temp, weather_id))
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM WEATHER WHERE CITY_ID = ?", (city_id,))
        print(cur.fetchone())
