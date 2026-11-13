# Projeto DevOps - Implementação de Pipeline CI/CD
## 1 - Sobre o Projeto
Este projeto tem como objetivo implementar práticas de DevOps por meio da automação dos processos de integração contínua (Continuous Integration – CI) e entrega contínua (Continuous Delivery – CD).

A solução utiliza uma aplicação desenvolvida em Python com o framework FastAPI, integrando ferramentas de análise estática de código, execução automatizada de testes, construção de imagens Docker e publicação da aplicação em ambiente de produção.

A automação foi realizada utilizando o GitHub Actions, permitindo que alterações realizadas no repositório sejam verificadas e disponibilizadas de maneira automatizada.

## 2 - Tecnologias utilizadas
- Python 3.14: Linguagem utilizada para o desenvolvimento da aplicção.
- FastAPI: Framework utilizado para disponibilizar os serviços por meio de uma API REST.
- PostgreSQL: Banco de dados relacional utilizado para manter os registros das tarefas.
- Pytest: Ferramenta utilizada para a execução de testes no código.
- Pylint: Ferramenta utilizada para verifcação da qualidade do código.
- Docker: Tecnologia utilizada para empacotar a aplicação em uma imagem de contêiner.
- Docker Hub: Repositório para armazenar e disponibilizar as imagens em Docker.
- GitHub Actions: Ferramenta utilizada para executar a pipeline de CI/CD.
- Fossa: Ferramenta de gerenciamento de licenças do código.
- Render: Plataforma utilizada para implantação e disponibilização da aplicação.

## 3 - Execução local
Para executar a aplicação localmente, é necessário possuir Python instalado, acesso ao banco de dados PostgreSQL e as dependências definidas no projeto.

### 3.1 - Pré-requisitos
- Python 3.14 instalado.
- Git.
- PostgrSQL instalado na sua máquina ou contêiner com o PostgreSQL em execução.

### 3.2 - Clonar repositório
Abra um terminal e execute o comando abaixo para obter o código fonte:

```bash
git clone https://github.com/gigi-ferreira/DevOps-Curso-PUCPR.git
```

Em seguida, acesse a pasta do projeto
```bash
cd DevOps-Curso-PUCPR
```

### 3.3 - Criar ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3.4 - Instalar dependências
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
python -m pip install -r requirements.txt
```

### 3.5 - Configurar o banco de dados
Instruções para utilização Postgres:

 - Certifique-se que o serviço PostgreSQL esteja em execução.
 - Crie um banco de dados chamado "devops".
 - A porta do banco precisa ser 5432.

As credenciais utilizadas na conexão devem corresponder às configurações do PostgreSQL instalado localmente ou imagem no Docker.

### 3.6 - Configurar as variáveis de ambiente e iniciar a aplicação
Ainda na pasta do projeto (terminal PowerShell), execute o comando abaixo para configurar as variáveis de ambiente e inicializa-las na sequência:

```powershell
$env:DATABASE_USERNAME="postgres";$env:DATABASE_PASSWORD="sua_senha"; $env:DATABASE_ADDRESS="localhost:5432"; $env:DATABASE="devops"; python -m fastapi dev app/api.py
```
Observação:  substitua "sua_senha" pela senha definida durante a instalação do PostgreSQL. As variáveis são definidas apenas para a sessão atual do terminal.

Durante a inicialização, as tabelas necessárias serão criadas automaticamente caso ainda não existam.

Após a inicialização, a aplicação estará disponível em:
- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs

#
Aluna: Gisele Ferreira da Silva
Professor: Pedro Rocha Horchulhack

Link da aplicação web disponível na plataforma Render: [Aplicação Tarefas](https://api-tarefas-e1d5.onrender.com)

#