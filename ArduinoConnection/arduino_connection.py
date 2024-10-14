import time
import uuid
import random
from datetime import datetime, timedelta

import RPi.GPIO as GPIO
import psycopg

conn = psycopg.connect(dbname="sensordata",
                       host="85.215.48.7",
                       user="postgres",
                       password="admin123",
                       port="5432")
cursor = conn.cursor()

GPIO.setmode(GPIO.BOARD)

pins = [12, 13, 15, 16, 18, 22, 7, 3]

for pin in pins:
    GPIO.setup(pin, GPIO.IN)

while True:
    bin_string = ""
    for pin in pins:
        gpio_in = GPIO.input(pin)
        bin_string += str(gpio_in)

    value = int(bin_string, 2)
    dt = datetime.now() + timedelta(hours=2)
    string_dt = dt.strftime("%Y-%m-%d %H:%M:%S")

    print()
    print("Data: ")
    print(string_dt)
    print(string_dt)
    print(bin_string)
    print(int(bin_string, 2))

    cursor.execute("INSERT INTO sensordata (timestmp, temperature) VALUES (%s, %s)", (string_dt, value))

    conn.commit()

    time.sleep(10)
