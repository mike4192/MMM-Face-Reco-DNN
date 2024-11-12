from flask import Flask, request
import threading
import time
import logging
import sys

app = Flask(__name__)

# logging.getLogger('werkzeug').disabled = True
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

recognition_active = False

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)  # Only log errors and critical issues

@app.route('/trigger', methods=['POST'])
def trigger():
    print("Got trigger")
    global recognition_active
    data = request.json
    recognition_active = data.get("trigger", False)
    print(f"recognition_active: {recognition_active}")
    return "Success", 200

def start_listener():
    app.run(port=5000)  # Choose any free port



listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True
listener_thread.start()

while True:
    print("sleeping...")
    time.sleep(1)

