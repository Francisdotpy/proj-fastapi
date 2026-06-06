from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    # verifica se o status code (200, 404, etc) que o get pra root (/) retornou
    # é igual o HTTPStatus.OK (200)
    # se der certo (200) continua pro proximo asset, se nao, encerra o teste
    assert response.json() == {'message': 'Hello World'}
    # verifica se o json que o get em root
    # puxou é igual a 'message': 'Hello World'
