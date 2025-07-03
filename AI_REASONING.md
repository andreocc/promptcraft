# AI Reasoning

## 2025-07-02

### Decisão Inicial

- **Projeto:** `promptcraft`
- **Stack:** Python + Streamlit
- **Objetivo:** Criar uma ferramenta para refinar prompts de LLM usando a própria API do Gemini. A aplicação terá uma interface simples para o usuário inserir um prompt bruto, que será processado e devolvido em uma versão otimizada.

### Estrutura e Práticas

- A estrutura do projeto seguirá rigorosamente as diretrizes do `GEMINI.md` para garantir consistência e manutenibilidade.
- O uso do `justfile` simplifica a execução de tarefas comuns como `run` e `test`.
- A gestão de dependências e variáveis de ambiente foi configurada para facilitar tanto o desenvolvimento local quanto o deploy futuro.

### Próximos Passos

1. Implementar a lógica principal em `app.py`.
2. Conectar à API do Gemini para o refinamento do prompt.
3. Adicionar testes básicos para a funcionalidade de refinamento.
