from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('../database/database.db')
    c = conn.cursor()
    c.execute("SELECT name, date, hour || ':' || minute || ':' || CASE WHEN length(second) = 1 THEN '0' || second ELSE second END AS time, type_connection, \
        CASE \
            WHEN time_connected < 60 THEN CAST(time_connected AS INTEGER) || 's' \
            WHEN time_connected >= 60 AND time_connected < 3600 THEN CAST(time_connected / 60 AS INTEGER) || 'm ' || time_connected % 60 || 's' \
            ELSE CAST(time_connected / 3600 AS INTEGER) || 'h ' || CAST((time_connected % 3600) / 60 AS INTEGER) || 'm ' || time_connected % 60 || 's' \
        END AS duration \
        FROM Connections ORDER BY date, hour, minute, second, name")


    data = c.fetchall()
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
