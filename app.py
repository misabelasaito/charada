from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {'id': 1, 'pergunta':'O que é, o que é?', 'Quanto mais se tira, maior fica.': '➡ Resposta: Um buraco.'},
    {'id': 2, 'pergunta':'O que é, o que é?', 'Tem cabeça, tem dente, não é bicho e nem é gente.': '➡ Resposta: Alho.'},
    {'id': 3, 'pergunta':'O que é, o que é?', 'Anda sempre com os pés na cabeça.': '➡ Resposta: O piolho.'},
    {'id': 4, 'pergunta':'O que é, o que é?', 'Tem coroa, mas não é rei, tem escamas, mas não é peixe.': '➡ Resposta: O abacaxi.'},
    {'id': 5, 'pergunta':'O que é, o que é?', 'Sempre atravessa o rio sem se molhar.': '➡ Resposta: A ponte.'},
    {'id': 6, 'pergunta':'O que é, o que é?', 'Quanto mais quente, mais fresco é.': '➡ Resposta: O pão.'},
    {'id': 7, 'pergunta':'O que é, o que é?', 'Tem olhos, mas não pode ver, tem água, mas não pode beber.': '➡ Resposta: O coco.'},
    {'id': 8, 'pergunta':'O que é, o que é?', 'Tem pernas, mas não anda, tem braços, mas não abraça.': '➡ Resposta: A cadeira.'},
    {'id': 9, 'pergunta':'O que é, o que é?', 'Se você tem, quer compartilhar. Se compartilhar, não tem mais.': '➡ Resposta: Um segredo.'},
    {'id': 10, 'pergunta':'O que é, o que é?', 'Fica no meio do ovo.': '➡ Resposta: A letra "V".'}
]

@app.route('/')
def index():
    return 'API ON'

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(random.choice(charadas)), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def busca(campo, busca):

    if campo not in ['id','texto','resposta']:
        return jsonify({'mensagem':'ERRO! Campo não encontrdo'})
    if campo == 'id':
        busca = int(busca)
        
    for charada in charadas:
        if charada[campo] == busca:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem':'ERRO! Usuário não encontrado'}), 404


if __name__ == '__main__':
    app.run()