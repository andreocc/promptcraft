# GEMINI.md

> Diretrizes para desenvolvimento, automação e colaboração eficiente com assistentes LLM neste projeto.

---

## 👤 Sobre

Autor: **André**  
Arquiteto de Soluções com foco em **inovação**, **sustentabilidade técnica** e **escalabilidade**.  
Ambientes: Microsoft Windows, Linux.  
Ferramentas: automação ponta a ponta, infraestrutura como código, UI interativas, agentes de IA.

---

## 📌 Premissas & Preferências

- **Linguagens preferidas:** Python, Streamlit, Bash, Batch, PowerShell. PHP/JS somente se necessário.
- **Editor padrão:** VSCode com integração via `justfile`.
- **VCS:** Git — nunca use `rm` ou `mv`; sempre `git rm`, `git mv`.
- **Código explicável após 6 meses, sem depender de LLMs.**
- **Arquitetura modular:** arquivos pequenos, autocontenidos e coesos.
- **Saídas com logs semânticos. Emojis são aceitáveis se agregarem legibilidade.**

---

## 📦 Estrutura Inicial do Projeto

Ao inicializar um projeto, gere automaticamente:

```
📁 raiz/
 ├── README.md
 ├── AI_REASONING.md
 ├── justfile
 ├── .env.dist
 ├── VERSION
 ├── CHANGELOG.md
 ├── .gitignore
 ├── .cache/       # TTL padrão: 1 dia
 └── test/
     └── test_placeholder.py
```

---

## 🚀 Aplicação Mínima

- Python + Streamlit.
- Um campo de entrada de texto e botão.
- Um log simples (ex: `st.write(input)`).
- Arquivo principal: `main.py` ou `app.py`.
- Executável com: `just run`.

---

## 🤖 Interação com LLM (Gemini)

- **.0`
- Use `.env` com:
  ```env
  GOOGLE_GENAI_USE_VERTEXAI=true
  GOOGLE_CLOUD_PROJECT=meu-projeto
  ```
- Evite `SERPAPI_API`, salvo exceções justificadas.
- **AI_REASONING.md é a memória técnica viva do projeto.** Consulte e atualize.
- Este `GEMINI.md` deve ser lido antes de qualquer contribuição LLM.

---

## 🧩 Contexto Dinâmico e Assistência Agentic

- Toda interação com LLMs deve considerar:
  - Arquivos modificados
  - Comandos executados (just/git)
  - Linter ativo
  - Logs recentes
- O LLM é tratado como um engenheiro júnior:
  - Faz sugestões
  - Usa ferramentas
  - Justifica ações
  - Espera aprovação para mudanças críticas

```md
Exemplo:
- LLM sugere refatoração: mostra `diff` + explicação.
- Espera comando de aprovação: “Aplique”, “Rejeite” ou “Altere”.
```

---

## 🧠 AI_REASONING.md

> Documenta *porquês técnicos*.  
Inclua:
- Decisões tomadas (ex: troca de biblioteca)
- Alternativas descartadas
- Limitações técnicas
- Histórico de iteração com IA

---

## ⚡ justfile (targets obrigatórios)

```just
run:         # Executa app local
test:        # Roda todos os testes
list:        # Lista targets disponíveis
```

---

## 🧪 Testes

- Devem ser rápidos e executáveis com `just test`.
- Um bug = um novo teste.
- Merge na `main` só com testes passando.

---

## 🔐 Configurações & Segredos

- `.env` → não versionado (valores reais)
- `.env.dist` → documentado (placeholders como `foo`, `1234`)
- Produção: use Secret Manager ou plataforma de deploy.

---

## 📦 Versionamento

- **SemVer:** Exemplo: `1.2.3`
- Arquivos:
  - `VERSION`
  - `CHANGELOG.md`
- A cada release:
  - Tags Docker: `projeto-x:v1.2.3`, `projeto-x:latest`

---

## 🧑‍💻 Sessões e Estado

- Sessões mantêm contexto de execução (ambiente, comandos, paths).
- O LLM deve retomar de onde parou, exceto se explicitamente resetado.
- Para controle de estado: `.session.json` (opcional).

---

## 🩺 Diagnóstico de Impacto

> Para qualquer bug ou comportamento inesperado:

1. Liste até 3 causas prováveis, ranqueadas por probabilidade.
2. Para cada causa, proponha solução de no máximo 1 linha.
3. Justifique se for optar por não agir.

---

## ✅ Checklist Operacional

Antes de marcar como "concluído":

- [ ] Rodou `just test`?
- [ ] Validou o comportamento manualmente?
- [ ] Atualizou `README.md`?
- [ ] Atualizou `AI_REASONING.md`?
- [ ] O código é consistente com o restante do projeto?

---

## 🛠️ Ferramentas Utilizadas

| Ferramenta       | Uso                         |
|------------------|----------------------------|
| VSCode           | IDE principal               |
| just             | Task runner                 |
| git              | Versionamento               |
| Streamlit        | UI interativa               |
| docker           | Build/Deploy                |
| Vertex AI        | Backend LLM                 |
| Google ADK       | Integração com Gemini SDK   |
| Secret Manager   | Gestão de segredos (prod)   |

---

## 📚 Convenções para Assistentes LLM

- Prefira respostas executáveis (`just`, shell ou código completo).
- Nunca altere arquivos sem exibir o `diff` e explicar.
- Para códigos longos, forneça apenas patch relevante.
- Mantenha rastreabilidade. O que não está em `AI_REASONING.md`, não existe.

---

## ☑️ Conclusão

Este projeto adota um modelo **agentic**, modular e rastreável.  
**Consistência vence genialidade isolada.**  
**Documentação mínima é obrigatória.**  
**LLMs são bem-vindos, mas precisam seguir processo.**

> “Se o assistente propôs, o humano decide. Se o humano decidiu, o assistente executa.”
