# promptcraft

Otimizador de prompts para LLMs.

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/promptcraft.git
   cd promptcraft
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

Copie o arquivo de exemplo de variáveis de ambiente e preencha com seus dados:

```bash
cp .env.dist .env
```

**Variáveis necessárias:**
- `GOOGLE_GENAI_USE_VERTEXAI`: `true` para usar Vertex AI.
- `GOOGLE_CLOUD_PROJECT`: ID do seu projeto no Google Cloud.

## 🏃 Execução

Para iniciar a aplicação localmente, use o `just`:

```bash
just run
```

A aplicação estará disponível em `http://localhost:8501`.

## 🧪 Testes

Para executar os testes automatizados:

```bash
just test
```

## 🚢 Deploy

Esta aplicação é otimizada para deploy na [Streamlit Community Cloud](https://streamlit.io/cloud).
