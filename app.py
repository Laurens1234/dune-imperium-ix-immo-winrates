import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.route('/player')
def player_win_rate():
    # Get the player's name from the request query parameter
    name = request.args.get('name')
    
    # If no name is provided, return an error response
    if not name:
        return 'No player name provided', 400

    # Call your Python script using subprocess
    # Adjust the script name and path if needed
    command = f"python player_winrate_pos.py @{name}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    
    # Return the output from your script as the HTTP response
    if process.returncode == 0:
        return stdout.decode('utf-8')
    else:
        return f"Error running script: {stderr.decode('utf-8')}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
