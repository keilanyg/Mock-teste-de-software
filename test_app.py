import pytest
from unittest.mock import Mock
from app import processar_dados

"""Fixture para criar uma simulação para a função obter_dados_API
 e define seu valor de retorno como {"message": "Testes de Mock!"}."""
@pytest.fixture
def mock_obter_dados_API(mocker):
    # Criar um mock para a função obter_dados_API
    return mocker.patch("app.obter_dados_API", return_value={"message": "Testes de Mock!"})


"""Casos de Teste"""

"""1 - Chama a função processar_dados com uma URL de API falsa 
e verifica se o resultado é o esperado."""
def testar_dados_processo_API_com_dados(mock_obter_dados_API):
    result = processar_dados("http://fake-api.com")
    assert result == "DADO PROCESSADO: Testes de Mock!"
    

"""2 - Simula uma resposta de API malsucedida definindo seu valor
de retorno como None, teste para verificar se não há nenhum dado."""
def testar_dados_processo_API_sem_dados(mock_obter_dados_API):
    mock_obter_dados_API.return_value = None
    result = processar_dados("http://fake-api.com")
    assert result == "ERRO AO PROCESSAR DADO"
    

"""3 - Para Mensagem Vazia:"""
def testar_mensagem_vazia(mock_obter_dados_API):
       mock_obter_dados_API.return_value = {"message": ""}
       result = processar_dados("http://fake-api.com")
       assert result == "DADO PROCESSADO: "
       