from flask import Flask, render_template, request, redirect
import webview
import threading
import subprocess
import os
from datetime import datetime


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

@app.route("/reports")
def reports():
    base_dir = './generated-reports'
    scan_types = ['file', 'url', 'ip']
    report_files = []

    for scan_type in scan_types:
        scan_dir = os.path.join(base_dir, scan_type)
        try:
            files = os.listdir(scan_dir)
            for file in files:
                full_path = os.path.join(scan_dir, file)
                if os.path.isfile(full_path):
                    size_bytes = os.path.getsize(full_path)
                    size_kb = round(size_bytes / 1024, 2)
                    modified_time = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M')

                    report_files.append({
                        'name': file,
                        'type': scan_type,
                        'path': f"/generated-reports/{scan_type}/{file}",
                        'size_kb': size_kb,
                        'modified': modified_time
                    })
        except FileNotFoundError:
            continue

    return render_template("reports.html", files=report_files)



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
    webview.create_window("My App", "http://127.0.0.1:5000", min_size=(1000, 750))  # Open Flask UI inside PyWebview
    webview.start()
