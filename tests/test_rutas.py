import pytest
from app import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True  # Modo de prueba
    with app.test_client() as cliente:
        yield cliente


def test_home(cliente):
    respuesta = cliente.get('/')
    # Si se recibe un 302, seguimos la redirección
    if respuesta.status_code == 302:
        respuesta = cliente.get(respuesta.headers['Location'])
    assert respuesta.status_code == 200  # Verifica que la página cargue correctamente
