from flask import Flask, request
import os

app = Flask(__name__)

def _sum(arr):
    sum=0

    for val in arr:
        sum = sum + val

    return(sum)


@app.route('/calculate', methods=['POST'])
def calculate_value():
    return { 'calculatedValue': _sum(request.get_json()) }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port)
