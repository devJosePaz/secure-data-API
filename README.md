I've refined your README for better clarity and formatting.

-----

# Secure Data API

Uma API REST simples para gerenciar **transações financeiras** com campos sensíveis protegidos por **criptografia**. Este projeto foi desenvolvido como um desafio técnico para demonstrar habilidades em Python, FastAPI, SQLAlchemy e criptografia.

-----

## 🚀 Sobre

Esta API foi projetada para armazenar e consultar transações que contêm dados sensíveis, como o documento do usuário e o token do cartão de crédito. Para garantir a segurança e a privacidade, esses dados são criptografados antes de serem salvos no banco de dados, utilizando **criptografia assimétrica** com chaves públicas e privadas.

-----

## 🛠 Funcionalidades

  * **Criar transação** (`POST`)
  * **Listar todas as transações** (`GET`)
  * **Consultar transação por ID** (`GET`)
  * **Atualizar transação** (`PUT`) — *funcionalidade desabilitada, pois transações financeiras não devem ser alteradas após sua criação.*
  * **Excluir transação** (`DELETE`) — *funcionalidade desabilitada por questões de segurança e integridade dos dados.*

-----

## 💻 Tecnologias Utilizadas

  * **Python** 3.13
  * **FastAPI**
  * **SQLAlchemy**
  * **SQLite** (banco de dados local)
  * **Cryptography** (para criptografia assimétrica)
  * **Uvicorn** (servidor ASGI)

-----

## ⚙️ Como Usar

Siga os passos abaixo para configurar e executar a API em sua máquina local:

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    cd secure-data-API
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    # No Linux/macOS:
    source venv/bin/activate
    # No Windows:
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Gere as chaves de criptografia (públicas e privadas):**

    ```bash
    python app/services/generate_keys.py
    ```

5.  **Crie as tabelas no banco de dados:**

    ```bash
    python -m app.create_tables
    ```

6.  **Execute a API:**

    ```bash
    uvicorn app.main:app --reload
    ```

    Acesse a documentação interativa da API em: `http://127.0.0.1:8000/docs`

-----

### ⚠️ Observações Importantes

  * As chaves `.pem` (pública e privada) **não estão incluídas no repositório** por motivos de segurança. Elas devem ser geradas localmente antes de rodar a aplicação.
  * As funcionalidades de atualização (`PUT`) e exclusão (`DELETE`) de transações foram **intencionalmente desabilitadas** para garantir a integridade dos dados sensíveis, alinhando-se às boas práticas de segurança para transações financeiras.
  * Este projeto foi desenvolvido com foco em **segurança e boas práticas** no tratamento de dados sensíveis.
