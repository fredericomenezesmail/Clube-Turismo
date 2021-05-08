# Clube Turismo  
\
Crie um diretório para o projeto e instale o python "virtual environment" dentro do diretório:

**mkdir project && cd project**  
**python3 -m venv venv**  
**source venv/bin/activate**  
\
\
Clone o repositório:  

**git clone https://github.com/fredericomenezesmail/clubeTurismo.git**  
\
\
Instale as dependências:  

**pip install -r clubeTurismo/requirements/local.txt**  
\
\
Mude de diretório, execute as migrações e inicie o servidor:  

**cd clubeTurismo**  
**python manage.py migrate**  
**python manage.py runserver**  
\
\
O servidor deve estar funcionando e as páginas estarem acessíveis em:  
**http://127.0.0.1:8000**  

Para acessar o endpoint da api o caminho é:  
**http://127.0.0.1:8000/apiclubeTurismoUsers/**  

