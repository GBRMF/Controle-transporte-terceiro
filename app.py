from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    name = request.form['name']
    action = request.form['action']
    
    if action == 'checkin':
        registrar_checkin(name)
    elif action == 'checkout':
        registrar_checkout(name)

    return redirect(url_for('home'))

def registrar_checkin(name):
    print(f'{name} fez check-in')

def registrar_checkout(name):
    print(f'{name} fez check-out')

if __name__ == '__main__':
    app.run(debug=True)
