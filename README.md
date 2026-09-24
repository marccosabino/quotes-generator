# Quotes Generator

Um gerador de citações desenvolvido em Python que utiliza uma API externa para obter frases e possui um sistema de armazenamento local como alternativa caso a API esteja indisponível.

## 📌 Sobre o projeto

O **Quotes Generator** é um projeto desenvolvido para praticar conceitos fundamentais de Python, como consumo de APIs, tratamento de erros, organização de código e armazenamento de dados local.

A aplicação tenta obter uma citação por meio de uma API externa. Caso a API esteja indisponível ou ocorra algum erro durante a requisição, o programa utiliza citações armazenadas localmente como alternativa.

Este projeto também representa um dos primeiros passos da minha evolução no desenvolvimento com Python e servirá como base para projetos futuros envolvendo aplicações web e Inteligência Artificial.

## ⚙️ Funcionalidades

- Geração de citações através de uma API externa
- Sistema de fallback utilizando armazenamento local
- Tratamento de erros durante a comunicação com a API
- Armazenamento de citações em arquivo JSON
- Separação das responsabilidades em diferentes módulos
- Execução através do terminal

## 🛠️ Tecnologias utilizadas

- **Python**
- **Requests** — realização das requisições HTTP
- **JSON** — armazenamento das citações locais
- **Git/GitHub** — versionamento do projeto

## 📁 Estrutura do projeto

```text
quotes-generator/
│
├── data/
│   └── quotes.json
│
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   └── local_storage.py
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt

### Principais arquivos

- **`main.py`** — ponto de entrada da aplicação e responsável por coordenar o funcionamento do programa.
- **`src/api_client.py`** — responsável pela comunicação com a API externa e obtenção das citações.
- **`src/local_storage.py`** — responsável pelo acesso às citações armazenadas localmente.
- **`data/quotes.json`** — arquivo utilizado para armazenar as citações locais utilizadas pelo sistema de fallback.
- **`requirements.txt`** — lista das dependências necessárias para executar o projeto.

## 🔄 Como funciona

O funcionamento básico da aplicação segue este fluxo:

```text
              ┌─────────────────┐
              │    main.py      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Tenta acessar  │
              │      a API      │
              └────────┬────────┘
                       │
                ┌──────┴──────┐
                │             │
             Sucesso         Erro
                │             │
                ▼             ▼
       ┌──────────────┐ ┌──────────────┐
       │   Retorna a  │ │ Busca uma    │
       │   citação da │ │ citação no   │
       │     API      │ │ armazenamento│
       └──────────────┘ │    local     │
                        └──────────────┘
```

O sistema utiliza um mecanismo de **fallback** para que a aplicação continue funcionando mesmo quando a API externa não estiver disponível.

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/marccosabino/quotes-generator.git
```

### 2. Acesse a pasta do projeto

```bash
cd quotes-generator
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python main.py
```

## 📚 O que aprendi

Durante o desenvolvimento deste projeto, pratiquei:

- Consumo de APIs utilizando Python
- Utilização da biblioteca `requests`
- Tratamento de exceções
- Manipulação de arquivos JSON
- Organização de um projeto Python
- Separação de responsabilidades
- Criação de mecanismos de fallback
- Uso do Git e GitHub para versionamento

## 🔮 Próximos passos

Este projeto faz parte de uma sequência de projetos que pretendo desenvolver, aumentando gradualmente a complexidade.

### Quotes Generator 2.0

Uma evolução do projeto atual com:

- Interface web
- Histórico de citações
- Categorias
- Citações favoritas
- Melhor experiência de usuário

### AI Quote Generator

Uma versão voltada para Inteligência Artificial, com recursos como:

- Geração de citações utilizando IA
- Geração baseada em temas
- Geração baseada em sentimentos ou contexto
- Integração com um modelo de IA

A ideia é evoluir gradualmente de:

**Python → APIs → Aplicações Web → Inteligência Artificial**

## 📄 Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

## 🧹 Configuração do `.gitignore`

A pasta `__pycache__` e os arquivos `.pyc` são gerados automaticamente pelo Python e não precisam ser versionados no Git.

Da mesma forma, o ambiente virtual `.venv` e as configurações específicas do VS Code não precisam fazer parte do repositório.

O arquivo `.gitignore` deve conter:

```gitignore
__pycache__/
*.pyc
.venv/
.vscode/
```

Isso evita que arquivos gerados automaticamente ou específicos do ambiente de desenvolvimento sejam enviados para o GitHub.
