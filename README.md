# Cotação de Moedas com ThingSpeak

Este projeto em Python acessa periodicamente a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter a cotação atual do **Dólar (USD)**, **Euro (EUR)** e **Yuan Chinês (CNY)** em relação ao Real (BRL), e envia esses dados para um canal no **ThingSpeak**, onde é possível gerar gráficos e visualizações em tempo real.

## 📦 Requisitos

- Python 3.x
- Biblioteca `requests`

Instale as dependências com:

```bash
pip install requests
```

## ⚙️ Configuração

Antes de rodar o projeto, você precisa adicionar seus dados dentro de um arquivo chamado `secrets.json`.

### Como obter essas credenciais

1. Acesse: [https://thingspeak.com](https://thingspeak.com)
2. Crie uma conta ou faça login.
3. Vá em **Channels** > **New Channel**
4. Adicione um nome e no mínimo 3 campos (Field1, Field2, Field3).
5. Salve o canal e copie:
   - **Channel ID**
   - **Write API Key** (em **API Keys**)

### Estrutura do `secrets.json`

Assim que terminar de pegar suas credenciais, adicione-as ao JSON e salve.  
Lembre-se de manter o `secrets.json` na **raiz do projeto**, junto com o código Python.

```json
{
  "channel_id": SEU_CHANNEL_ID,
  "write_api_key": "SUA_WRITE_API_KEY"
}
```

## ▶️ Executando

Após configurar o `secrets.json`, execute o script com:

```bash
python main.py
```

A cada 15 segundos, ele:
- Coleta as cotações de USD, EUR e CNY.
- Exibe no terminal.
- Envia os dados para o ThingSpeak.

## 🛡️ Segurança

Nunca adicione seu `secrets.json` ao GitHub.  
Recomenda-se usar um `.gitignore` com:

```
secrets.json
```

---

Feito por **Nicholas Lima** como ferramenta de estudo
