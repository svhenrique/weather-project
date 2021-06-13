## Link da aplicação em funcionamento

[Weather Project](https://weather-sh.herokuapp.com/)

## Sobre

Uma aplicação feita em Django que usa a API do site  [OpenWeather](https://openweathermap.org/api) para analisar as informações do clima de uma cidade
passada pelo usuário.

## Configuração do ambiente 

### Clonando repositório

Para clonar o repositório é possível baixa-lo completamente do github e extrair em uma pasta de projeto ou utilizar o comando:

```bash
git clone https://github.com/svhenrique/weather-project.git
```

Para utilizar o comando anterior é necessário ter o Git instalado no computador.

### Configurando ambiente 

É necessária a instalação da linguagem Python. É possível baixa-la aqui:

- https://www.python.org/downloads/

Passo a passo da instalação da linguagem pode ser encontrado aqui:

- https://wiki.python.org/moin/BeginnersGuide/Download

É necessário, também, a instalação do banco de dados PostgreSQL: 

- https://www.postgresql.org/download/

e a instalação das dependências do pacote psycopg:

- https://www.psycopg.org/docs/install.html

É recomendável que se use um ambiente virtual para utilização da aplicação. Mas antes, é preciso baixar a biblioteca virtualenv e para fazer isso, basta executar o comando:


```bash
pip install virtualenv
```

Para criar um ambiente virtual no python, fazemos:

```bash
virtualenv venv
```

Após criar o ambiente virtual, se você estiver no prompt de comando (shell, terminal, cmd, etc), é preciso ativar o venv (ambiente virtual) criado, para isso utilizamos o comando:

```bash
venv/bin/activate
```

## Instalando dependências

Para instalar dependências, basta usar o comando:

```bash
pip install -r requirements.txt
```

## Configurando .env

Crie um arquivo de texto e nomeio para ".env" e salve na pasta raiz do projeto. Após isso, adicione a seguinte linha ao arquivo criado:

```bash
SECRET_KEY=COLOQUE_SUA_SECRET_KEY
```

Do lado direito, em "COLOQUE_SUA_SECRET_KEY" ponha um hash de SECRET_KEY gerado pelo Django. 

Uma das maneiras de conseguir o hash, é iniciando um novo projeto django com:

```bash
django-admin startproject projeto 
```

e pegando o hash guardado na variável SECRET_KEY no arquivo settings.py (fazer processo de coleta de SECRET_KEY em outra pasta e em outro ambiente virtual para assegurar o encapsulamento da aplicação).

## Como utilizar

Para acessar as informações de clima de uma cidade basta informar, da seguinte forma, **cidade, estado, país** respectivamente na entrada de busca e clicar em "Adicionar Cidade".
