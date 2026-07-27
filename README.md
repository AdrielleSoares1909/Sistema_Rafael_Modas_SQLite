# 🛍️ Sistema de Controle de Estoque - Rafael Modas

## 📖 Sobre o projeto

O **Sistema de Controle de Estoque - Rafael Modas** foi desenvolvido com o objetivo de simular a gestão de uma pequena loja de roupas. O projeto nasceu inspirado na realidade da minha própria loja, buscando resolver tarefas comuns do dia a dia, como cadastro de produtos, controle de estoque, registro de vendas e acompanhamento do histórico de vendas.

Durante o desenvolvimento, o projeto evoluiu significativamente. Inicialmente os dados eram armazenados em memória e posteriormente em arquivos `.txt`. Nesta versão, toda a persistência foi migrada para **SQLite**, aproximando o sistema de uma aplicação utilizada no mercado.

Além de atender às necessidades da loja, este projeto faz parte da minha jornada de aprendizado em desenvolvimento Backend com Python.

---

# 🚀 Tecnologias utilizadas

* Python 3
* SQLite
* SQL
* VS Code
* Git
* GitHub

---

# 🏗️ Arquitetura do projeto

O projeto foi organizado em camadas para facilitar a manutenção e reutilização do código.

```text
Sistema_Rafael_Modas_SQLite/

│
├── main.py          # Menu principal da aplicação
├── estoque.py       # Regras de negócio relacionadas ao estoque
├── vendas.py        # Regras de negócio das vendas
├── database.py      # Comunicação com o banco SQLite
├── app.db           # Banco de dados SQLite
└── README.md
```

Essa separação permite que cada arquivo tenha uma responsabilidade específica, seguindo boas práticas utilizadas em projetos profissionais.

---

# 💾 Banco de Dados

O sistema utiliza o **SQLite** como banco de dados relacional.

Foram criadas duas tabelas:

## Tabela `roupas`

Armazena todos os produtos cadastrados.

Campos:

* ID
* Nome
* Preço
* Estoque
* Tamanho

---

## Tabela `vendas`

Responsável por armazenar todo o histórico das vendas realizadas.

Campos:

* ID
* Nome do produto
* Tamanho
* Quantidade vendida
* Preço unitário
* Valor total da venda
* Nome do cliente
* Data da venda

---

# ✅ Funcionalidades

O sistema possui as seguintes funcionalidades:

### 📦 Gerenciamento de Estoque

* Cadastro de roupas
* Listagem de todas as roupas
* Busca por nome e tamanho
* Alteração de preço
* Remoção de produtos

---

### 🛒 Controle de Vendas

* Registro de vendas
* Atualização automática do estoque
* Validação de estoque disponível
* Cálculo automático do valor da venda
* Registro do cliente
* Registro da data da venda

---

### 📊 Relatórios

* Histórico completo de vendas
* Cálculo do valor total do estoque utilizando SQL (`SUM`)

---

# 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram aplicados diversos conceitos importantes de programação e banco de dados.

### Python

* Funções
* Modularização
* Organização em camadas
* Condicionais
* Laços de repetição
* Tratamento de retorno de funções
* Manipulação de tuplas

### SQL

* CREATE TABLE
* INSERT
* SELECT
* UPDATE
* DELETE
* WHERE
* SUM
* FETCHONE
* FETCHALL

### Banco de Dados

* SQLite
* Persistência de dados
* CRUD completo
* Relacionamento entre regras de negócio e banco de dados

---

# 🎯 Objetivo do projeto

Mais do que desenvolver um sistema funcional, este projeto teve como objetivo colocar em prática conceitos fundamentais de desenvolvimento Backend.

Ao longo do desenvolvimento foram implementadas melhorias como:

* Migração do armazenamento em memória para SQLite;
* Separação entre regras de negócio e acesso ao banco de dados;
* Reutilização de funções;
* Organização do código em módulos;
* Validação das operações de estoque;
* Implementação de um fluxo completo de vendas.

---

# 📈 Próximos passos

O projeto continuará evoluindo com novas funcionalidades.

Planejamento das próximas versões:

* API REST utilizando FastAPI;
* SQLAlchemy como ORM;
* Validação de dados com Pydantic;
* Documentação automática com Swagger;
* Integração com PostgreSQL;
* Autenticação de usuários;
* Controle de permissões.

---


# 👩‍💻 Desenvolvedora

**Adrielle Soares**

Este projeto faz parte do meu processo de aprendizado em Desenvolvimento Backend com Python e representa minha evolução prática na construção de aplicações utilizando banco de dados e organização de código em camadas.

Estou constantemente estudando e aprimorando meus conhecimentos para atuar como Desenvolvedora Backend Python.

