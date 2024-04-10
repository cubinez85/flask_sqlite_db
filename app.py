from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


@app.route('/')
def index():

    cursor.execute("select * from Users")
    content = cursor.fetchall()

    cursor.execute("select * from Users")
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('sqlite.html', labels=labels, content=content)



if __name__ == "__main__":
    app.run(debug=True)
