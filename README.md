# SGLA - Sistema de Gerenciamento de Livros e Autores

Projeto desenvolvido na disciplina **Laboratório de Programação Backend**.

O objetivo do sistema é permitir o gerenciamento de livros e autores, onde é possível listar livros, filtrar por disponibilidade e consultar os autores cadastrados.

---

# Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Git

---

# Estrutura do Projeto

```
sgla/
│
├── backend/
│   ├── config/
│   ├── livros/
│   ├── autores/
│   ├── manage.py
│   └── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── README.md
└── .gitignore
```

---


# Como executar localmente

1. **Acesse a pasta do backend:**
   ```bash
   cd backend
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   ```

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrations (cria o banco de dados):**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

A API estará disponível em `http://127.0.0.1:8000/`

---

# Endpoints

## Autores

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/autores/` | Listar todos os autores |
| GET | `/api/autores/<id>/` | Buscar autor por ID |

## Livros

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/livros/` | Listar todos os livros |
| GET | `/api/livros/disponiveis/` | Listar livros disponíveis |
| GET | `/api/livros/lingua/<lingua>/` | Listar livros por língua |
| GET | `/api/livros/anteriores/` | Listar livros publicados antes (com parâmetro de data) |
| GET | `/api/livros/busca/<palavra>/` | Buscar livros por título |
| GET | `/api/livros/<id>/` | Buscar livro por ID |
