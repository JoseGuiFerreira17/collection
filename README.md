# Collection API

API para gerenciamento de livros de acervo pessoal

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
## Após isso execute os seguintes passos:
1. Abra a sua url_base/admin/ (ex.: http://127.0.0.1:8000/admin)
2. Acesse com os dados do super usuário que você criou
3. Em 'DJANGO OAUTH TOOLKIT', em 'Applications' clique em 'Adicionar'
4. Ná pagina de adição de 'Applications', em 'Client type' selecione a opção 'Confidential'
5. Em 'Authorization grant type' selecione a opção 'Resource owner password-based'
6. Guarde os valores gerados em 'Client id' e em 'Client secret', eles serão usados na autenticação da API, e a forma de usar deve ser consultada no arquivo DOC.md

# Documentação:
## Verifique os seguintes links:
<hr>
## Sawagger
Consulte os endpoints em: http://127.0.0.1:8000/swagger/
## Redoc
Consulte os endpoints em: http://127.0.0.1:8000/redoc/
## Insomia
Importe o arquivo "collection_api_insomnia"

