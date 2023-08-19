from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    try:
        subprocess.run(['python', 'game.py'], check=True)
        return jsonify({'message': 'Python script executed successfully.'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
