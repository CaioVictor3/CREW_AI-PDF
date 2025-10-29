import streamlit as st
from main import executar_assistente_defesa_consumidor

st.title("🛡️ Assistente de Defesa do Consumidor")
st.write(
    "Este assistente de IA ajuda você com questões sobre **Código de Defesa do Consumidor (CDC)** brasileiro"
    " baseado na Lei 8.078/1990 e regulamentações relacionadas."
)

with st.sidebar:
    st.header("Selecione uma Tarefa:")
    task_type = (
        "Responder Pergunta sobre Direitos do Consumidor"  
    )

    
    user_input = st.text_area("Digite sua pergunta sobre direitos do consumidor:")


if st.button("Executar Consulta de Defesa do Consumidor 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, digite sua pergunta antes de executar.")
    else:
        st.write("⏳ Processando sua solicitação... Aguarde.")

        resultado = executar_assistente_defesa_consumidor(user_input)

        st.subheader("✅ Resposta do Assistente de Defesa do Consumidor:")
        st.write(resultado)