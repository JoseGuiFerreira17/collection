# Collection API

API para gerenciamento de livros de acervo pessoal

## Documentação

A documentação para uso desta API encontra-se no arquivo DOC.md

## Como usar a aplicação?

1. Clone do  repositório
2. Entre na pasta do mesmo
3. Crie um virtualenv com Python 3
4. Ative o virtualenv
5. Instale as dependências
6. Copie o ENV_SAMPLE para um novo arquivo chamado .env e depois o abra e mude os valores das variáveis caso seja necessário
7. Execute as migrations
8. Execute os testes
9. Crie um superusuário
10. Execute a aplicação

```console
git clone https://github.com/JoseGuiFerreira17/collection.git
cd collection
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cp ENV_SAMPLE .env
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```
