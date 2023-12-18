import requests

def obter_dados_API(api_url):
    response = requests.get(api_url)
    return response.json() if response.ok else None

def processar_dados(api_url):
    data = obter_dados_API(api_url)
    if data:
        return f"Processed data: {data['message']}"
    else:
        return "Error processing data"
