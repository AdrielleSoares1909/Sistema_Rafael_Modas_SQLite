🛍️ Sistema de Controle de Estoque - Rafael Modas
📖 Sobre o projeto

O Sistema de Controle de Estoque - Rafael Modas é um projeto desenvolvido em Python inspirado na realidade da minha loja de roupas. O objetivo foi criar um sistema para facilitar o gerenciamento de produtos, controle de estoque e registro de vendas.

Inicialmente o projeto utilizava arquivos .txt para armazenar os dados. Durante o desenvolvimento, ele foi totalmente migrado para SQLite, proporcionando maior segurança, organização e facilidade de manutenção.

Além de servir como ferramenta para gerenciamento de estoque, este projeto representa minha evolução prática no aprendizado de Python, organização de código e banco de dados.

🚀 Tecnologias utilizadas
Python 3
SQLite
SQL
Módulo sqlite3
Módulo datetime

------------------------
📂 Estrutura do projeto
Sistema_Rafael_Modas_SQLite/
│
├── main.py                 # Menu principal
├── database.py             # Operações com o banco de dados
├── estoque.py              # Regras do estoque
├── vendas.py               # Registro e histórico de vendas
├── validacoes.py           # Validação das entradas do usuário
├── banco.db                # Banco de dados SQLite
└── README.md

-----------------------
✨ Funcionalidades

✅ Cadastro de roupas
✅ Listagem de produtos
✅ Busca por nome e tamanho
✅ Alteração de preço
✅ Remoção de produtos
✅ Registro de vendas
✅ Atualização automática do estoque
✅ Histórico de vendas
✅ Cálculo do valor total do estoque
🔒 Validações implementadas

Para deixar o sistema mais robusto, todas as entradas do usuário foram centralizadas no arquivo validacoes.py.

As validações incluem:

Impedir campos vazios;
Impedir preços menores ou iguais a zero;
Impedir estoque menor ou igual a zero;
Impedir quantidade menor ou igual a zero;
Validar tamanhos permitidos;
Validar opções do menu;
Validar datas utilizando datetime;
Mensagens claras para orientar o usuário quando uma entrada é inválida.

-------------------------
🗄️ Banco de Dados

O sistema utiliza SQLite para armazenar todas as informações.

Foram criadas duas tabelas:

Roupas
ID
Nome
Preço
Estoque
Tamanho

Vendas
ID
Nome da roupa
Tamanho
Quantidade vendida
Preço unitário
Valor total
Nome do cliente
Data da venda
-------------------

🛡️ Tratamento de erros

As operações que modificam o banco de dados possuem tratamento de exceções utilizando:

try
except sqlite3.Error
finally

Isso garante:

fechamento correto da conexão;
mensagens de erro mais claras;
maior robustez da aplicação.

-----------------------
📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

Organização de projetos Python em módulos;
Manipulação de banco de dados SQLite;
Operações CRUD;
Tratamento de exceções;
Validação de entradas do usuário;
Separação de responsabilidades entre arquivos;
Estruturação de código mais limpa e reutilizável.

------------------------
🔄 Evolução do projeto

Sistema iniciado utilizando arquivos .txt;
Migração completa para SQLite;
Separação das responsabilidades em módulos;
Implementação de validações centralizadas;
Tratamento de exceções nas operações com banco de dados;
Código mais organizado, reutilizável e preparado para futuras evoluções.

--------------------
🚀 Próximos passos

Desenvolver uma API utilizando FastAPI;
Integrar o sistema com PostgreSQL;
Criar autenticação de usuários com JWT;
Desenvolver uma interface web para gerenciamento do estoque.

----------------
👩‍💻 Autora

Adrielle Soares

Projeto desenvolvido como parte da minha evolução nos estudos de Python e Back-end, inspirado na rotina da loja Rafael Modas.
