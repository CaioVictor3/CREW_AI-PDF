import streamlit as st
from main import executar_assistente_defesa_consumidor

st.title("🛡️ Assistente de Defesa do Consumidor")
st.write(
    "Este assistente de IA ajuda você com questões sobre **Código de Defesa do Consumidor (CDC)** brasileiro"
    " baseado na Lei 8.078/1990 e regulamentações relacionadas."
)

# Sidebar for user selection
with st.sidebar:
    st.header("Selecione uma Tarefa:")
    task_type = (
        "Responder Pergunta sobre Direitos do Consumidor"  # Como temos apenas uma tarefa, ela é pré-selecionada
    )

    # Campo de entrada para a pergunta do usuário
    user_input = st.text_area("Digite sua pergunta sobre direitos do consumidor:")

# Executa o Assistente de Defesa do Consumidor quando o usuário clica no botão
if st.button("Executar Consulta de Defesa do Consumidor 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, digite sua pergunta antes de executar.")
    else:
        st.write("⏳ Processando sua solicitação... Aguarde.")

        # ✅ Chama a função do main.py
        resultado = executar_assistente_defesa_consumidor(user_input)

        # Exibe a resposta da IA
        st.subheader("✅ Resposta do Assistente de Defesa do Consumidor:")
        st.write(resultado)