import requests
import time
import json

# Abre as credenciais sensíveis localizadas em outro arquivo
with open("secrets.json", "r", encoding="utf-8") as secrets_file:
    secrets = json.load(secrets_file)

CHANNEL_ID = secrets["channel_id"]
WRITE_API_KEY = secrets["write_api_key"]
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Caminho para a API de cotação
API_URL = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,CNY-BRL"

# Função que organiza os dados recebidos da API
def enviar_para_thingspeak(usd, eur, cny):
    payload = {
        "api_key": WRITE_API_KEY,
        "field1": usd,
        "field2": eur,
        "field3": cny
    }

    # Espera a resposta do HTTP e responde conforme o código recebido
    response = requests.get(THINGSPEAK_URL, params=payload)
    if response.status_code == 200 and response.text != "0":
        print("Sucesso ao enviar")
    else:
        print(f"Erro ao enviar: {response.status_code} | Resposta: {response.text}")

# Roda o código indefinadamente ou até encontrar um erro
while True:
    try:
        # Pega os dados da API
        resposta = requests.get(API_URL)

        # Se a resposta da conexão for 200, salva e envia para o ThingSpeak
        if resposta.status_code == 200:
            dados = resposta.json()

            usd = float(dados['USDBRL']['bid'])
            eur = float(dados['EURBRL']['bid'])
            cny = float(dados['CNYBRL']['bid'])
            
            enviar_para_thingspeak(usd, eur, cny)
        
        # Se o código HTTP não for de sucesso, avisa o erro e faz um relatório sobre qual foi o erro
        else:
            print("Erro ao obter dados da API:", resposta.status_code)
    
    # Se qualquer erro acontecer na execução, ele é relatado aqui.
    except Exception as e:
        print("Erro ao tentar executar:", e)

    time.sleep(15)
