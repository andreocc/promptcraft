import streamlit as st
import google.generativeai as genai
import os

# --- Configuração da Página ---
st.set_page_config(
    page_title="PromptCraft 🚀",
    page_icon="✨",
    layout="centered",
)

# --- Funções Core ---
def refinar_prompt(prompt_bruto: str, api_key: str) -> str:
    """
    Envia o prompt bruto para a API Gemini com instruções de refinamento.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        instrucao_de_refinamento = f"""Refine o seguinte prompt para um modelo de linguagem generativo. O objetivo é torná-lo mais claro, focado e contextualizado para obter os melhores resultados possíveis. 

**Prompt Bruto:**
{prompt_bruto}

**Sua Tarefa:**
1.  **Claridade:** Reescreva o prompt para ser o mais específico e direto possível. Elimine ambiguidades.
2.  **Contexto:** Adicione contexto relevante que possa ajudar o modelo a entender a tarefa.
3.  **Estrutura:** Formate o prompt de uma maneira lógica, talvez usando markdown ou seções.
4.  **Persona (se aplicável):** Sugira uma persona para o LLM assumir (ex: 'Aja como um especialista em marketing...').

**Prompt Refinado:**"""

        response = model.generate_content(instrucao_de_refinamento)
        return response.text

    except Exception as e:
        st.error(f"Ocorreu um erro ao contatar a API do Gemini: {e}")
        return ""

# --- Interface do Usuário (UI) ---
st.title("PromptCraft 🚀")
st.caption("Uma ferramenta para refinar e otimizar seus prompts de LLM com IA.")

st.sidebar.header("🔑 Configuração da API")
api_key = st.sidebar.text_input("Sua Chave da API Gemini", type="password")

st.markdown("### 1. Insira seu prompt bruto abaixo")
prompt_usuario = st.text_area(
    "Seu prompt aqui...",
    height=150,
    placeholder="Ex: me fale sobre carros",
)

if st.button("✨ Refinar Prompt", use_container_width=True):
    if not api_key:
        st.warning("Por favor, insira sua chave da API Gemini na barra lateral para continuar.")
    elif not prompt_usuario:
        st.warning("Por favor, insira um prompt para refinar.")
    else:
        with st.spinner("Refinando seu prompt com a magia da IA... ✨"):
            prompt_refinado = refinar_prompt(prompt_usuario, api_key)
        
        if prompt_refinado:
            st.markdown("### 2. Seu prompt, agora otimizado!")
            st.code(prompt_refinado, language="markdown")
            st.balloons()
            if st.button("📋 Copiar Resultado", use_container_width=True):
                st.code(f'st.code("{prompt_refinado}")') # Simula a cópia
                st.success("Copiado para a área de transferência!")

st.sidebar.markdown("---")
st.sidebar.info(
    "Esta é uma aplicação de exemplo construída com Streamlit e Gemini. "
    "Lembre-se de nunca compartilhar suas chaves de API."
)
