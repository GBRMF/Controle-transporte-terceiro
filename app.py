from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados para armazenar os dados dos passageiros
passengers = []

# Rota para o frontend
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o check-in
@app.route('/checkin', methods=['POST'])
def checkin():
    name = request.form['name']
    cpf = request.form['cpf']
    if name and cpf:
        passengers.append({'name': name, 'cpf': cpf, 'status': 'checked-in'})
        return jsonify({'message': 'Check-in realizado com sucesso!'})
    else:
        return jsonify({'message': 'Por favor, preencha todos os campos.'})

# Rota para o check-out
@app.route('/checkout', methods=['POST'])
def checkout():
    name = request.form['name']
    cpf = request.form['cpf']
    if name and cpf:
        for passenger in passengers:
            if passenger['name'] == name and passenger['cpf'] == cpf:
                passenger['status'] = 'checked-out'
                return jsonify({'message': 'Check-out realizado com sucesso!'})
        return jsonify({'message': 'Passageiro não encontrado.'})
    else:
        return jsonify({'message': 'Por favor, preencha todos os campos.'})

if __name__ == '__main__':
    app.run(debug=True)
