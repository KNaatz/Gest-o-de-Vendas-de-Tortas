#Projeto Confeitária

from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# Função para adicionar uma nova venda ao CSV
def add_venda(numero_pedido, tipo_torta, quantidade):
    with open('vendas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([numero_pedido, tipo_torta, quantidade])

# Função para ler as vendas do CSV
def read_vendas():
    if not os.path.exists('vendas.csv'):
        return []
    with open('vendas.csv', mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

@app.route('/')
def index():
    vendas = read_vendas()
    return render_template('index.html', vendas=vendas)

@app.route('/add_venda', methods=['POST'])
def add_venda_route():
    numero_pedido = request.form['numero_pedido']
    tipo_torta = request.form['tipo_torta']
    quantidade = request.form['quantidade']
    add_venda(numero_pedido, tipo_torta, quantidade)
    return redirect('/')

@app.route('/update_estoque', methods=['POST'])
def update_estoque():
    # Lógica para atualizar o estoque de ingredientes (não alteramos isso)
    pass

if __name__ == '__main__':
    app.run(debug=True)

