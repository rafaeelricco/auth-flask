<p align="center">
  <img src="https://res.cloudinary.com/dnqiosdb6/image/upload/v1668801783/cover/flask-mail_ckveqy.png" alt="Cover">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS">
</p>

## 🔓 Flask Authentication

Está é uma API de autenticação construída em Python utilizando o Microframework Flask junto a boas práticas de desenvolvimento e testes. A API foi construída com o intuito de ser utilizada como base para outros projetos, e também para servir de estudo para quem deseja aprender mais sobre o Flask.

## 📂 Organização do projeto

O projeto foi organizado seguindo as práticas de [Blueprints](https://flask.palletsprojects.com/en/2.2.x/tutorial/views/), onde cada Blueprint é responsável por uma parte da aplicação, como por exemplo, o Blueprint de autenticação, que é responsável por todas as rotas de autenticação, como login, logout, registro, etc.

## 🚀 Rodando com Docker

Para rodar este projeto com Docker é extremamente simples! Mas antes, para isto você deve ter uma versão recente do `docker compose`. Dito isto, veja os comandos abaixo:

    docker compose build --no-cache (uso da flag é opcional)
    docker compose up

E o aplicativo será executado em http://localhost:3333/

## 🛠️ Rodando Manualmente

Se você preferir executá-lo diretamente em sua máquina local, é fundamental utilizar um ambiente virtual.

    pip install --no-cache-dir -r requirements.txt

Em seu terminal, rode também:

    export FLASK_APP=wsgi.py

Em seguida:

    flask run ou gunicorn -w 4 -b 0.0.0.0:3333 wsgi:app

Agora você pode acessar em:
http://127.0.0.1:333

## ✨ Principais Funcionalidades

- Operações CRUD
- Login e Logout
- Registro de Usuários
- Verificação de E-mail
- Testes Unitários

## Licença

[MIT]()
