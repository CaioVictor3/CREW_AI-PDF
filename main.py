from crey import ComplianceCrew
import streamlit as st


def run_compliance_assistant(pergunta: str):
    crew_instance = ComplianceCrew()

    result = crew_instance.crew().kickoff(inputs={"pergunta": pergunta})

    return result


def main():
    st.title("Compliance Assistant")
    pergunta = st.text_input("Pergunta sobre compliance")
    if st.button("Enviar"):
        if not pergunta:
            st.warning("Escreva uma pergunta antes de enviar.")
            return
        with st.spinner("Processando..."):
            try:
                resposta = run_compliance_assistant(pergunta)
                st.success("Resposta recebida")
                st.write(resposta)
            except Exception as e:
                st.error(f"Erro ao executar: {e}")


if __name__ == "__main__":
    main()
