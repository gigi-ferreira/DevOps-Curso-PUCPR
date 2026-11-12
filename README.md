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
- PostgrSQL ou contêiner com o PostgreSQL em execução.

### 3.2 - Clonar repositório
Abra um terminal e execute o comando abaixo para obter o código fonte:

```bash
git clone https://github.com/gigi-ferreira/DevOps-Curso-PUCPR.git
```