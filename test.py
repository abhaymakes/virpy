from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_script():
    
        # Capture both stdout and stderr
        # result = subprocess.run(["python", "testing.py", "-m", "file", "-if", "/input-files/5hashes.txt", "-of", "pdf"], capture_output=True, text=True, encoding="utf-8")

    command = [
        "cmd", "/k"
    "python", "testing.py", 
    "-m", "file", 
    "-if", "input-files/5hashes.txt", 
    "-of", "pdf"
]
    subprocess.Popen(command)

@app.route('/run-script', methods=['GET'])
def trigger_script():
    run_script()

if __name__ == '__main__':
    app.run()
