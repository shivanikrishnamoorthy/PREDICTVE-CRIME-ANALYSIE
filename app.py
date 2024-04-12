from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('a.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Your Python code here
    result = "Python script executed successfully!"

    return result

if __name__ == '__main__':
    app.run(debug=True)
