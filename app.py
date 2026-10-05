from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os dados do sensor e a temperatura
banco_em_memoria = []


# Rota para receber a leitura do sensor (Método POST)
@app.route('/sensores/clima', methods=['POST'])
def registrar_leitura():
    dados = request.get_json()

    # Adiciona a temperatura informada à nossa lista
    if 'id' not in dados or 'temperatura' not in dados:
        return jsonify({
            "erro": "Os campos 'id' e 'temperatura' são obrigatórios."
        }), 400

    banco_em_memoria.append(dados)

    return jsonify({
        "mensagem": "Leitura registrada com sucesso!",
        "dados": dados
    }), 201


# Rota para consultar o resumo das leituras (Método GET)
@app.route('/sensores/clima', methods=['GET'])
def listar_todos():
    # TODO (3)
    # Filtro usando Query Parameter: /sensores/clima?acima_de=30

    acima_de = request.args.get('acima_de')

    # Se o parâmetro acima_de foi informado
    if acima_de is not None:
        try:
            valor = float(acima_de)
        except ValueError:
            return jsonify({
                "erro": "O parâmetro 'acima_de' deve ser um número."
            }), 400

        leituras_filtradas = [
            leitura
            for leitura in banco_em_memoria
            if float(leitura['temperatura']) > valor
        ]

        return jsonify({
            "total_registros": len(leituras_filtradas),
            "leituras": leituras_filtradas
        }), 200

    # Caso nenhum filtro seja informado, retorna todas as leituras
    return jsonify({
        "total_registros": len(banco_em_memoria),
        "leituras": banco_em_memoria
    }), 200


# Rota para buscar um sensor específico pelo ID passado na URL
@app.route('/sensores/clima/<sensor_id>', methods=['GET'])
def buscar_por_id(sensor_id):
    for leitura in banco_em_memoria:
        if leitura['id'] == sensor_id:
            return jsonify(leitura), 200

    # Se o laço terminar e não encontrar o ID, retorna 404 Not Found
    return jsonify({
        "erro": f"Sensor '{sensor_id}' não encontrado."
    }), 404


# Rota para remover um sensor específico da lista
@app.route('/sensores/clima/<sensor_id>', methods=['DELETE'])
def deletar_sensor(sensor_id):
    global banco_em_memoria

    tamanho_original = len(banco_em_memoria)

    # Recria a lista mantendo apenas os sensores
    # com ID diferente do informado
    banco_em_memoria = [
        leitura
        for leitura in banco_em_memoria
        if leitura['id'] != sensor_id
    ]

    if len(banco_em_memoria) < tamanho_original:
        return jsonify({
            "mensagem": f"Sensor '{sensor_id}' removido com sucesso."
        }), 200

    return jsonify({
        "erro": f"Sensor '{sensor_id}' não encontrado para exclusão."
    }), 404


# TODO (2)
# Rota para atualizar a temperatura de um sensor específico
@app.route('/sensores/clima/<sensor_id>', methods=['PUT'])
def atualizar_sensor(sensor_id):
    dados = request.get_json()

    # Verifica se a temperatura foi enviada
    if 'temperatura' not in dados:
        return jsonify({
            "erro": "O campo 'temperatura' é obrigatório."
        }), 400

    # Procura o sensor pelo ID
    for leitura in banco_em_memoria:
        if leitura['id'] == sensor_id:

            # Atualiza a temperatura
            leitura['temperatura'] = dados['temperatura']

            return jsonify({
                "mensagem": f"Sensor '{sensor_id}' atualizado com sucesso.",
                "dados": leitura
            }), 200

    # Sensor não encontrado
    return jsonify({
        "erro": f"Sensor '{sensor_id}' não encontrado."
    }), 404


# Função de teste
def emTeste():
    pass


if __name__ == '__main__':
    app.run(debug=True)


# TODO (1)
# Teste de Validação (Tratamento de Erros):
#
# Enviar um POST via Postman/Insomnia/Bruno contendo apenas:
#
# {
#     "temperatura": 25.0
# }
#
# O que aconteceu?
#
# A API deve retornar:
#
# {
#     "erro": "Os campos 'id' e 'temperatura' são obrigatórios."
# }
#
# HTTP Status: 400

### O que foi implementado