import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/')
def get_list():
    
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

@app.get('/contacto', response_class=HTMLResponse)
def get_list():
    
    return """
        <h1>Hola soy una pagina <h1/>
        <p>Soy un parafo<p/>
"""

def run():
    store.get_categories()


if __name__ == '__main__':
    run()