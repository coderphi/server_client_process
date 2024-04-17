import requests  # Import the requests library for making HTTP requests

def send_command(command):
    """
    Sends a command to the server and prints the result.
    
    :param command: The command to be sent to the server.
    """
    url = 'http://127.0.0.1:5000/api/command'  # URL of the server to send the command to
    payload = {'command': command}  # Payload data containing the command
    response = requests.post(url, json=payload)  # Send a POST request to the server with the payload
    if response.status_code == 200:  # Check if the request was successful
        print(response.json().get('result'))  # Print the result returned by the server
    else:
        print('Error:', response.text)  # Print an error message if the request failed

if __name__ == '__main__':
    while True:  # Start an infinite loop to continuously accept user input
        command = input('Enter command (type "exit" to quit): ')  # Prompt the user to enter a command
        if command.lower() == 'exit':  # Check if the user wants to exit
            break  # Exit the loop if the user enters 'exit'
        send_command(command)  # Send the user-entered command to the server for processing
