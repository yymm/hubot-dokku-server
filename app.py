import json
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def route():
    if request.headers['Content-Type'] == 'application/json':
        content = request.get_json()
        print(content)
        if content.has_key('cmd'):
            cmd = content['cmd']
            cmd.insert(0, 'sudo')
            print(cmd)
            (stdout, stderr) = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
            return jsonify( {'stdout': stdout, 'stderr': stderr} )
        else:
            return jsonify( {'stdout': None, 'stderr': 'Invalid json data.'} )
    return jsonify( {'stdout': None, 'stderr': 'Invalid content-type.'} )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
