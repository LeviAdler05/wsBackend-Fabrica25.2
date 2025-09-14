# Projeto Anime - Guia Completo para Iniciantes

Bem-vindo(a) ao Projeto Anime! Este é um guia completo criado para que **qualquer pessoa**, mesmo com pouco conhecimento em programação, possa executar, testar e entender este projeto. Vamos começar!

---

##  Índice

1.  [O que este projeto faz?](#o-que-este-projeto-faz)
2.  [Funcionalidades Detalhadas](#funcionalidades-detalhadas)
3.  [Tecnologias Utilizadas](#tecnologias-utilizadas)
4.  [Guia de Instalação (Passo a Passo)](#guia-de-instalação-passo-a-passo)
5.  [Como Usar a Aplicação](#como-usar-a-aplicação)
6.  [Guia da API (Para Desenvolvedores)](#guia-da-api-para-desenvolvedores)
7.  [Entendendo a Estrutura de Pastas](#entendendo-a-estrutura-de-pastas)
8.  [Como Testar o Projeto](#como-testar-o-projeto)
9.  [Solução de Problemas Comuns](#solução-de-problemas-comuns)

---

## O que este projeto faz?

Este projeto é um site de catálogo de animes. Pense nele como uma pequena "Wikipedia" de animes, onde você pode ver uma lista de títulos, clicar em um para ver mais detalhes e até adicionar suas citações favoritas. Além do site, ele também possui uma "porta dos fundos" para desenvolvedores, chamada API, que permite que outros programas conversem com nossa aplicação.

## Funcionalidades Detalhadas

- **Catálogo de Animes:** Uma interface web bonita e funcional para navegar pelos animes.
- **Páginas de Detalhes:** Cada anime possui uma página com pôster, sinopse, gêneros, ano de lançamento, status e citações relacionadas.
- **CRUD Completo:** A interface web permite Criar, Ler, Atualizar e Deletar animes do catálogo.
- **Sistema de Citações:** Permite adicionar citações de personagens a cada anime.
- **Dados Automáticos:** O sistema busca informações de animes e citações de APIs externas (Jikan e AnimeChan) para popular o banco de dados.
- **API Segura:** Uma API RESTful que permite gerenciar animes e citações, protegida por um sistema de login e senha (autenticação por token JWT).

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Django
- **API:** Django REST Framework
- **Banco de Dados:** PostgreSQL
- **Interface:** HTML, CSS, Bootstrap 5
- **Containerização:** Docker e Docker Compose (para facilitar a instalação)

## Guia de Instalação (Passo a Passo)

Para executar este projeto, não é necessário instalar Python, Django ou PostgreSQL na sua máquina. O Docker cuida de tudo isso para você, criando ambientes isolados chamados "containers".

### Pré-requisitos: O que você precisa ter

1.  **Docker Desktop:** É a ferramenta que gerencia os containers. Se você não o tiver, a instalação é simples:
    -   [Instalar Docker no Windows](https://docs.docker.com/desktop/install/windows-install/)
    -   [Instalar Docker no Mac](https://docs.docker.com/desktop/install/mac-install/)
    -   [Instalar Docker no Linux](https://docs.docker.com/desktop/install/linux-install/)

2.  **Git:** Ferramenta para baixar o código-fonte do projeto. Se não tiver, [instale aqui](https://git-scm.com/downloads).

---

### 🚀 Instalação Rápida com Script (Recomendado)

Este método automatiza quase todo o processo. Você só precisa executar um arquivo.

**1. Baixe o Projeto**

Abra seu terminal (PowerShell, Prompt, etc.) e execute:
```bash
git clone https://github.com/LeviAdler05/wsBackend-Fabrica25.2.git

cd wsBackend-Fabrica25.2

```

**2. Execute o Script de Instalação**

No Windows, o PowerShell pode bloquear a execução de scripts por segurança. Se for seu caso, você só precisa rodar um comando **uma única vez na vida** para liberar.

*   **Abra o PowerShell como Administrador**.
*   Execute: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
*   Confirme com `S` e pode fechar o PowerShell de administrador.

Agora, no seu terminal **normal**, dentro da pasta `wsBackend-Fabrica25.2`, execute o script:

```powershell
./setup.ps1
```

O script irá construir os containers, iniciar a aplicação e popular o banco de dados. No final, ele mesmo te dará o último comando que você precisa rodar para criar seu usuário. Simples assim!

---

### Instalação Manual (Alternativa)

Se preferir fazer cada passo manualmente para entender o processo.

**1. Baixe o Código e Entre na Pasta**
```bash
git clone https://github.com/LeviAdler05/wsBackend-Fabrica25.2.git

cd wsBackend-Fabrica25.2

```

**2. Inicie a Aplicação com Docker**
```bash
docker-compose up --build -d
```

**3. Crie seu Usuário Administrador**
```bash
docker-compose exec web python manage.py createsuperuser
```

**4. Popule o Banco de Dados**
```bash
docker-compose exec web python manage.py import_animes
```

---

## Como Usar a Aplicação

### Acessando o Site

Com os containers em execução, a aplicação já está no ar!

- **Site Principal:** Abra seu navegador e acesse `http://localhost:8000`
- **Painel de Admin:** Acesse `http://localhost:8000/admin` e faça login com o usuário que você criou.

## Guia da API (Para Desenvolvedores)

A API permite que outros programas interajam com os dados do nosso projeto. Ela é protegida e requer um token (uma chave de acesso temporária).

### Obtendo seu Token

Use o `curl` no seu terminal (ou uma ferramenta como [Postman](https://www.postman.com/downloads/)) para pedir um token, usando o usuário e senha que você criou.

```bash
# Substitua seu_usuario e sua_senha
curl -X POST -H "Content-Type: application/json" -d '{"username": "seu_usuario", "password": "sua_senha"}' http://localhost:8000/api/token/
```

A resposta será um JSON com seu token de `access`.

### Fazendo Requisições Autenticadas

Agora, para cada requisição à API, envie seu token no cabeçalho `Authorization`.

**Exemplo (Listar Animes):**

```bash
# Substitua <seu_token_de_acesso>
curl -H "Authorization: Bearer <seu_token_de_acesso>" http://localhost:8000/api/animes/
```

Se você usa **PowerShell**, a sintaxe é um pouco diferente:

```powershell
# Passo 1: Salve o token numa variável
$token = "seu_token_de_acesso"

# Passo 2: Faça a requisição
Invoke-WebRequest -Uri http://localhost:8000/api/animes/ -Headers @{"Authorization" = "Bearer $token"}
```

## Entendendo a Estrutura de Pastas

- `projetoanime/`: Contém as configurações globais do projeto Django.
- `appanime/`: É o "coração" do projeto. Contém toda a lógica, modelos de dados, páginas e regras de negócio.
- `Dockerfile` e `docker-compose.yml`: Arquivos de receita para o Docker. Dizem a ele como construir e executar nosso projeto.
- `entrypoint.sh`: Um pequeno script que garante que as migrações do banco de dados sejam aplicadas antes de o servidor iniciar.
- `setup.ps1`: Script de instalação rápida para Windows.

## Como Testar o Projeto

Testes automatizados garantem que o código funciona como esperado. Para executar a suíte de testes (atualmente com testes básicos), use o comando:

```bash
docker-compose exec web python manage.py test
```

## Solução de Problemas Comuns

- **Erro `address already in use` ao rodar `docker-compose up`:** Significa que a porta `8000` já está sendo usada por outro programa na sua máquina. Você pode parar o outro programa ou alterar a porta no arquivo `docker-compose.yml` (ex: `"8001:8000"`).
- **Comandos `curl` não funcionam no PowerShell:** Lembre-se de usar a sintaxe do `Invoke-WebRequest` mostrada na seção da API.
- **Site não carrega:** Verifique os logs dos containers com o comando `docker-compose logs web` para ver se há alguma mensagem de erro.