from pymessenger import Bot
from src.routes import *
from flask import Flask
from threading import Thread
import subprocess

app = Flask(__name__)

def run_ngrok():
    command = f"./ngrok/ngrok http --domain={os.getenv('NGROK_DOMAIN')} 8080"
    subprocess.run(command, shell=True)

def run_flask():
    app.run(port=8080)

def keep_alive():
    ngrok_thread = Thread(target=run_ngrok)
    ngrok_thread.start()

    flask_thread = Thread(target=run_flask)
    # flask_thread.start()

if __name__ == "__main__":
    ngrok_thread = Thread(target=run_ngrok)
    ngrok_thread.start()
  
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    # keep_alive()
