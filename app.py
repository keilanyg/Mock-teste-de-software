import requests

"""EXEMPLO
api_url = "https://api.example.com/data"
result = processar_dados(api_url)

print(result)
"""

"""Função que envia uma solicitação GET para api_url e recuperar dados"""
def obter_dados_API(api_url):
    response = requests.get(api_url)
    return response.json() if response.ok else None

"""Chama a função de obter dados e verifica, 
se os dados forem obtidos, ele retorna a mensagem 
com o dados processados, 
se houver erro, ou a recuperação não for bem sucedida ele retornará uma mensagem de erro."""
def processar_dados(api_url):
    data = obter_dados_API(api_url)
    if data:
        return f"Processed data: {data['message']}"
    else:
        return "Error processing data"
