from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/")
def home():
    return "IT Assets Manager API is running!"

if __name__ == "__main__":
    app.run(debug=True)
 
