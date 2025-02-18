import pytest
import PyPDF2
from app import app
from io import BytesIO

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

def test_home(cliente):
    respuesta = cliente.get('/')
    if respuesta.status_code == 302:
        respuesta = cliente.get(respuesta.headers['Location'])
    assert respuesta.status_code == 200

def test_reportes(cliente):
    respuesta = cliente.get('/system_report')
    if respuesta.status_code == 302:
        respuesta = cliente.get(respuesta.headers['Location'])
    assert respuesta.status_code == 200
    assert b'Informe' in respuesta.data


#En este test se verifica que la página de exportación de datos se cargue correctamente tuve que modificar el código de la función export_csv para que se pueda ejecutar el test
def test_export_csv(cliente):
    respuesta = cliente.get('/export_csv')
    assert respuesta.status_code == 200  # Verifica que la página cargue correctamente
    assert respuesta.content_type == 'text/csv'  # Verifica que el contenido es CSV
    assert b'Fecha y Hora' in respuesta.data  # Verifica que los datos contienen 'Fecha y Hora'
    assert b'Procesos Activos' in respuesta.data  # Verifica que los datos contienen 'Procesos Activos'
    assert b'Uso de CPU (%)' in respuesta.data  # Verifica que los datos contienen 'Uso de CPU (%)'
    assert b'Uso de Disco (%)' in respuesta.data  # Verifica que los datos contienen 'Uso de Disco (%)'
    assert b'Uso de Memoria (%)' in respuesta.data  # Verifica que los datos contienen 'Uso de Memoria (%)'

def test_export_pdf(cliente):
    respuesta = cliente.get('/export_pdf')
    
    # Verifica que la respuesta sea exitosa
    assert respuesta.status_code == 200

    # Verifica que el tipo de contenido sea PDF
    assert 'application/pdf' in respuesta.content_type  

    # Leer el PDF desde los datos binarios de la respuesta
    pdf_data = respuesta.data
    pdf_file = BytesIO(pdf_data)
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extraer el texto del primer página del PDF
    page = pdf_reader.pages[0]
    text = page.extract_text()

    # Verifica que el texto esperado esté presente en el PDF
    assert 'Fecha y Hora' in text
    assert 'Procesos Activos' in text
    assert 'Uso de CPU (%)' in text
    assert 'Uso de Disco (%)' in text
    assert 'Uso de Memoria (%)' in text