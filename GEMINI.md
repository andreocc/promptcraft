# GEMINI.md

> Diretrizes para desenvolvimento, automaÃ§Ã£o e colaboraÃ§Ã£o eficiente com assistentes LLM neste projeto.

---

## ðŸ‘¤ Sobre

Autor: **AndrÃ©**  
Arquiteto de SoluÃ§Ãµes com foco em **inovaÃ§Ã£o**, **sustentabilidade tÃ©cnica** e **escalabilidade**.  
Ambientes: Microsoft Windows, Linux.  
Ferramentas: automaÃ§Ã£o ponta a ponta, infraestrutura como cÃ³digo, UI interativas, agentes de IA.

---

## ðŸ“Œ Premissas & PreferÃªncias

- **Linguagens preferidas:** Python, Streamlit, Bash, Batch, PowerShell. PHP/JS somente se necessÃ¡rio.
- **Editor padrÃ£o:** VSCode com integraÃ§Ã£o via `justfile`.
- **VCS:** Git â€” nunca use `rm` ou `mv`; sempre `git rm`, `git mv`.
- **CÃ³digo explicÃ¡vel apÃ³s 6 meses, sem depender de LLMs.**
- **Arquitetura modular:** arquivos pequenos, autocontenidos e coesos.
- **SaÃ­das com logs semÃ¢nticos. Emojis sÃ£o aceitÃ¡veis se agregarem legibilidade.**

---

## ðŸ“¦ Estrutura Inicial do Projeto

Ao inicializar um projeto, gere automaticamente:

```
ðŸ“ raiz/
 â”œâ”€ README.md
 â”œâ”€ AI_REASONING.md
 â”œâ”€ justfile
 â”œâ”€ .env.dist
 â”œâ”€ VERSION
 â”œâ”€ CHANGELOG.md
 â”œâ”€ .gitignore
 â”œâ”€ .cache/       # TTL padrÃ£o: 1 dia
 â””â”€ test/
     â””â”€ test_placeholder.py
```

---

## ðŸš€ AplicaÃ§Ã£o MÃ­nima

- Python + Streamlit.
- Um campo de entrada de texto e botÃ£o.
- Um log simples (ex: `st.write(input)`).
- Arquivo principal: `main.py` ou `app.py`.
- ExecutÃ¡vel com: `just run`.

---

## ðŸ¤– InteraÃ§Ã£o com LLM (Gemini)

- **SDK padrÃ£o:** `google-generativeai>=1.0`
- Use `.env` com:
  ```env
  GOOGLE_GENAI_USE_VERTEXAI=true
  GOOGLE_CLOUD_PROJECT=meu-projeto
  ```
- Evite `SERPAPI_API`, salvo exceÃ§Ãµes justificadas.
- **AI_REASONING.md Ã© a memÃ³ria tÃ©cnica viva do projeto.** Consulte e atualize.
- Este `GEMINI.md` deve ser lido antes de qualquer contribuiÃ§Ã£o LLM.

---

## ðŸ§  Contexto DinÃ¢mico e AssistÃªncia Agentic

- Toda interaÃ§Ã£o com LLMs deve considerar:
  - Arquivos modificados
  - Comandos executados (just/git)
  - Linter ativo
  - Logs recentes
- O LLM Ã© tratado como um engenheiro jÃºnior:
  - Faz sugestÃµes
  - Usa ferramentas
  - Justifica aÃ§Ãµes
  - Espera aprovaÃ§Ã£o para mudanÃ§as crÃ­ticas

```md
Exemplo:
- LLM sugere refatoraÃ§Ã£o: mostra `diff` + explicaÃ§Ã£o.
- Espera comando de aprovaÃ§Ã£o: â€œApliqueâ€, â€œRejeiteâ€ ou â€œAltereâ€.
```

---

## ðŸ§¾ AI_REASONING.md

> Documenta *porquÃªs tÃ©cnicos*.  
Inclua:
- DecisÃµes tomadas (ex: troca de biblioteca)
- Alternativas descartadas
- LimitaÃ§Ãµes tÃ©cnicas
- HistÃ³rico de iteraÃ§Ã£o com IA

---

## âš™ï¸ justfile (targets obrigatÃ³rios)

```just
run:         # Executa app local
test:        # Roda todos os testes
list:        # Lista targets disponÃ­veis
```

---

## ðŸ§ª Testes

- Devem ser rÃ¡pidos e executÃ¡veis com `just test`.
- Um bug = um novo teste.
- Merge na `main` sÃ³ com testes passando.

---

## ðŸ” ConfiguraÃ§Ãµes & Segredos

- `.env` â†’ nÃ£o versionado (valores reais)
- `.env.dist` â†’ documentado (placeholders como `foo`, `1234`)
- ProduÃ§Ã£o: use Secret Manager ou plataforma de deploy.

---

## ðŸ“¦ Versionamento

- **SemVer:** Exemplo: `1.2.3`
- Arquivos:
  - `VERSION`
  - `CHANGELOG.md`
- A cada release:
  - Tags Docker: `projeto-x:v1.2.3`, `projeto-x:latest`

---

## ðŸ§µ SessÃµes e Estado

- SessÃµes mantÃªm contexto de execuÃ§Ã£o (ambiente, comandos, paths).
- O LLM deve retomar de onde parou, exceto se explicitamente resetado.
- Para controle de estado: `.session.json` (opcional).

---

## ðŸ§  DiagnÃ³stico de Impacto

> Para qualquer bug ou comportamento inesperado:

1. Liste atÃ© 3 causas provÃ¡veis, ranqueadas por probabilidade.
2. Para cada causa, proponha soluÃ§Ã£o de no mÃ¡ximo 1 linha.
3. Justifique se for optar por nÃ£o agir.

---

## âœ… Checklist Operacional

Antes de marcar como "concluÃ­do":

- [ ] Rodou `just test`?
- [ ] Validou o comportamento manualmente?
- [ ] Atualizou `README.md`?
- [ ] Atualizou `AI_REASONING.md`?
- [ ] O cÃ³digo Ã© consistente com o restante do projeto?

---

## ðŸ§° Ferramentas Utilizadas

| Ferramenta       | Uso                         |
|------------------|------------------------------|
| VSCode           | IDE principal                |
| just             | Task runner                  |
| git              | Versionamento                |
| Streamlit        | UI interativa                |
| docker           | Build/Deploy                 |
| Vertex AI        | Backend LLM                  |
| Google ADK       | IntegraÃ§Ã£o com Gemini SDK    |
| Secret Manager   | GestÃ£o de segredos (prod)    |

---

## ðŸ“š ConvenÃ§Ãµes para Assistentes LLM

- Prefira respostas executÃ¡veis (`just`, shell ou cÃ³digo completo).
- Nunca altere arquivos sem exibir o `diff` e explicar.
- Para cÃ³digos longos, forneÃ§a apenas patch relevante.
- Mantenha rastreabilidade. O que nÃ£o estÃ¡ em `AI_REASONING.md`, nÃ£o existe.

---

## â˜‘ï¸ ConclusÃ£o

Este projeto adota um modelo **agentic**, modular e rastreÃ¡vel.  
**ConsistÃªncia vence genialidade isolada.**  
**DocumentaÃ§Ã£o mÃ­nima Ã© obrigatÃ³ria.**  
**LLMs sÃ£o bem-vindos, mas precisam seguir processo.**

> â€œSe o assistente propÃ´s, o humano decide. Se o humano decidiu, o assistente executa.â€

---