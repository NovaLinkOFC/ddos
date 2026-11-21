from flask import Flask, request, send_from_directory
import os

cwd = os.getcwd()
app = Flask(__name__, static_url_path='', static_folder=os.path.join(cwd, 'web'))

def get_str_from_resource(rsc):
    file_path = os.path.join(cwd, 'web', rsc)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return "Teste de post no servidor"
    if request.method == 'GET':
        return get_str_from_resource('index.html')

@app.route("/<path:path>")
def resources(path):
    file_path = os.path.join(cwd, 'web', path)
    if os.path.isfile(file_path):
        return send_from_directory(os.path.join(cwd, 'web'), path)
    return get_str_from_resource('index.html')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000, threaded=True)
