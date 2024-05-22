from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # substitua 'form.html' pelo nome do seu arquivo HTML

@app.route('/check', methods=['POST'])
def check():
    name = request.form.get('name')
    cpf = request.form.get('cpf')
    action = request.form.get('action')
    
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