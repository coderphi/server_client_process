import subprocess  # Import the subprocess module for executing shell commands
from flask import Flask, request, jsonify  # Import Flask for creating web server and request for handling HTTP requests

app = Flask(__name__)  # Create a Flask application instance

def execute_command(command):
    """
    Execute a command and return the output.
    
    :param command: The command to be executed.
    :return: The output of the command.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode().strip()  # Decode the output bytes to string and strip whitespace
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode().strip()}"  # Return error message if command execution fails

@app.route('/api/command', methods=['POST'])  # Define a route to handle POST requests to '/api/command'
def receive_command():
    """
    Receive a command from the client, execute it, and return the result.
    """
    command = request.json.get('command')  # Extract the command from the JSON payload
    result = execute_command(command)  # Execute the command and get the result
    return jsonify({'result': result})  # Return the result as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
