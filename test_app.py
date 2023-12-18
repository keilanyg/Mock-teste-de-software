
import pytest
from unittest.mock import Mock
from app import processar_dados

@pytest.fixture
def mock_obter_dados_API(mocker):
    # Criar um mock para a função obter_dados_API
    return mocker.patch("app.obter_dados_API", return_value={"message": "Hello, world!"})

def testar_dados_processo_API_com_dados(mock_obter_dados_API):
    # Chamar a função processar_dados com o mock
    result = processar_dados("http://fake-api.com")

    # Verificar se o resultado é o esperado
    assert result == "Processed data: Hello, world!"

def testar_dados_processo_API_sem_dados(mock_obter_dados_API):
    # Configurar o mock para retornar None, simulando uma resposta de API sem sucesso
    mock_obter_dados_API.return_value = None

    # Chamar a função processar_dados com o mock
    result = processar_dados("http://fake-api.com")

    # Verificar se o resultado é o esperado
    assert result == "Error processing data"
