from flask import Flask, render_template
import webview
import threading

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("file-scan.html")

@app.route("/url")
def url():
    return render_template("url-scan.html")

@app.route("/ip")
def ip():
    return render_template("ip-scan.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")



# Function to run Flask in the background
def run_flask():
    app.run(port=5000, debug=1, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()  # Run Flask in a separate thread
    webview.create_window("My App", "http://127.0.0.1:5000")  # Open Flask UI inside PyWebview
    webview.start()
