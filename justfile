# Task runner para o projeto promptcraft

# Lista os targets disponíveis
list:
    @just -l

# Inicia a aplicação Streamlit localmente
run:
    @streamlit run app.py

# Executa os testes com pytest
test:
    @pytest
