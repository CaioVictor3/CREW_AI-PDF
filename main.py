from crew import EquipeDefesaConsumidor



def executar_assistente_defesa_consumidor(pergunta: str):
    """
    Executa o Assistente de Defesa do Consumidor com a pergunta fornecida.

    Args:
        pergunta (str): A pergunta sobre direitos do consumidor a ser respondida.

    Returns:
        str: A resposta do agente especialista em defesa do consumidor.
    """
    if not pergunta.strip():
        return "Por favor, digite uma pergunta válida."


    instancia_equipe = EquipeDefesaConsumidor()


    resultado = instancia_equipe.equipe().kickoff(inputs={"question": pergunta})

    return resultado