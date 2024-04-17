import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_command(command):
    """
    Execute a command and return the output.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess>
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode().strip()}"

@app.route('/api/command', methods=['POST'])
def receive_command():
    command = request.json.get('command')
    result = execute_command(command)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

