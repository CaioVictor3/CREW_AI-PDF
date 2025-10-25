import streamlit as st
from main import run_compliance_assistant

st.title("Assistente de Compliance Farmacêutico")
st.write("Faça uma pergunta sobre compliance farmacêutico e receba uma resposta baseada em documentos relevantes.")

with st.sidebar:
    st.header("Selecione uma tarefa")
    tipo_tarefa = "Responder pergunta sobre conformidade"

    pergunta_usuario = st.text_area("Digite sua pergunta sobre o assunto")
    
    if st.button("Executar Verificação de Conformidade"):
        if not pergunta_usuario.strip():
            st.warning("Por favor, insira uma pergunta antes de executar a verificação.")
        else:
            with st.spinner("Processando sua pergunta..."):
                # Chamada da função que executa o Crew
                resultado = run_compliance_assistant(pergunta_usuario)

            st.subheader("Resposta:")
            st.write(resultado)
