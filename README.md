# ProjetoAnime

## Descrição
Projeto Django de site de animes, consumindo APIs externas (Jikan e AnimeChan) para exibir informações e quotes de animes. Possui CRUD completo e importação de animes via AJAX.

## Funcionalidades
- CRUD completo de animes e quotes.
- Importação de animes e quotes via APIs externas.
- Interface dinâmica com AJAX.
- API REST usando Django REST Framework.
- Página funcional com Django Templates.

## Tecnologias
- Django 5.2
- Django REST Framework
- SQLite (pode ser trocado para MySQL/PostgreSQL)
- jQuery para AJAX
- HTML, CSS

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/LeviAdler05/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2

    Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

    Instale as dependências:

pip install -r requirements.txt

    Rode as migrations:

python manage.py migrate

    Inicie o servidor:

python manage.py runserver

Endpoints

    /animes/ → Lista de animes

    /animes/<id>/ → Detalhes do anime

    /importar-animes/ → Importação via AJAX

    /api/animes/ → API REST completa

    /api/quotes/ → API REST completa

Docker

O projeto inclui Docker-compose para facilitar a execução (veja docker-compose.yml).


---

## **4️⃣ docker-compose.yml**

```yaml
version: "3.9"

services:
  web:
    image: python:3.13
    container_name: projetoanime_web
    working_dir: /app
    volumes:
      - .:/app
    command: >
      sh -c "pip install --upgrade pip &&
             pip install -r requirements.txt &&
             python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1