import subprocess
from flask import Flask, request, send_file

app = Flask(__name__)

html = open("main.html").read()

@app.route('/')
def return():
    if request.path == request.full_path():
        return html
    else: 
        subprocess.run("sh", "run.sh", request.args.get("username"))
        return send_file(request.args.get("username" + "/results.png"))