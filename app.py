from flask import Flask, request, jsonify
import requests
import time
import json
app = Flask(__name__)
@app.route('/numbers', methods=['GET'])
def get_numbers():

    urlused = request.args.getlist('url')

    a = set() 
    for url in urlused:
        try:
            intial_time = time.time()
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                numbers = data.get('numbers', [])
                a.update(numbers)
            elif response.status_code == 408:
                continue
        except Exception as e:
            continue
    a = sorted(list(a)) 
    return jsonify({"numbers": a})
if __name__ == '_main_':
    app.run(debug=True, port=3000)