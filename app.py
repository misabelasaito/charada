from flask import Flask, jsonify
import random

app = Flask(__name__)
    
charadas = [
    {'id': 1, 'resposta':'➡ Resposta: Um buraco.', 'O que é, o que é?':'Quanto mais se tira, maior fica.'},
    {'id': 2, 'resposta':'➡ Resposta: Alho.', 'O que é, o que é?': 'Tem cabeça, tem dente, não é bicho e nem é gente.'},
    {'id': 3, 'resposta':'➡ Resposta: O piolho.', 'O que é, o que é?':'Anda sempre com os pés na cabeça.'},
    {'id': 4, 'resposta':'➡ Resposta: O abacaxi.', 'O que é, o que é?':'Tem coroa, mas não é rei, tem escamas, mas não é peixe.'},
    {'id': 5, 'resposta':'➡ Resposta: A ponte.', 'O que é, o que é?':'Sempre atravessa o rio sem se molhar.'},
    {'id': 6, 'resposta':'➡ Resposta: O pão.', 'O que é, o que é?':'Quanto mais quente, mais fresco é.'},
    {'id': 7, 'resposta':'➡ Resposta: O coco.','O que é, o que é?': 'Tem olhos, mas não pode ver, tem água, mas não pode beber.'},
    {'id': 8, 'resposta':'➡ Resposta: A cadeira.', 'O que é, o que é?':'Tem pernas, mas não anda, tem braços, mas não abraça.'},
    {'id': 9, 'resposta':'➡ Resposta: Um segredo.', 'O que é, o que é?':'Se você tem, quer compartilhar. Se compartilhar, não tem mais.'},
    {'id': 10, 'resposta':'➡ Resposta: A letra "V".','O que é, o que é?': 'Fica no meio do ovo.'}
]

@app.route('/')
def index():
    return 'API ON'

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(random.choice(charadas)), 200

@app.route('/charadas/id/<int:id>', methods=['GET'])
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem':'ERRO! Usuário não encontrado'}), 404


if __name__ == '__main__':
    app.run()