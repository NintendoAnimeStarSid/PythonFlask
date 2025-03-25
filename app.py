from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
messages = []  # In-memory storage for messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    message = request.form.get('message')
    
    if name and message:
        messages.insert(0, {'name': name, 'message': message})  # Reverse order
        return redirect(url_for('messages_page'))
    else:
        return "Invalid input", 400

@app.route('/messages')
def messages_page():
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
    