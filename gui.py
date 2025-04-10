from flask import Flask, render_template, request, redirect
import webview
import threading
import subprocess


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("scan.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route('/run-script', methods=['POST'])
def run_script():
    uploaded_file = request.files.get('file_path')
    scan_mode = request.form.get('scan_mode', 'file')
    output_format = request.form.get('output_format', 'csv')
    delay = request.form.get('delay', 3)
    skip_vpn = request.form.get('skip_vpn', 'no') == 'yes'
    headless = request.form.get('headless', 'no') == 'yes'

    if not uploaded_file or uploaded_file.filename == '':
        return "Missing file", 400

    input_file_path = f"./input-files/{uploaded_file.filename}"

    print(input_file_path)

    # return "Success"

    command = [
        'python',
        'testing.py',
        '-if', input_file_path,
        '-m', scan_mode,
        '-of', output_format,
        '-dl', str(delay)
    ]

    if skip_vpn:
        command.append('-sv')
    if headless:
        command.append('-hl')

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error during script execution:", e)

    return redirect('/')



# Function to run Flask in the background
def run_flask():
    app.run(port=5000, debug=1, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()  # Run Flask in a separate thread
    webview.create_window("My App", "http://127.0.0.1:5000")  # Open Flask UI inside PyWebview
    webview.start()
