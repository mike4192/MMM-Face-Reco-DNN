import requests

# Define the Flask server URL
url = 'http://localhost:5000/trigger'

# Define the payload you want to send
data = {'trigger': False}  # Set to True to start recognition, False to stop

try:
    # Send the POST request to the Flask server
    response = requests.post(url, json=data)

    # Check the response from the server
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error sending notification: {e}")
