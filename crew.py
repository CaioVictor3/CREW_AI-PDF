from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Fontes de conhecimento
arquivo1 = PDFKnowledgeSource(file_paths=["file1.pdf"])


llm = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0,
    max_tokens=1500,
)


@CrewBase
class EquipeDefesaConsumidor:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def especialista_defesa_consumidor(self) -> Agent:
        return Agent(
            config=self.agents_config["especialista_defesa_consumidor"],
            verbose=True,
            tools=[],
            llm=llm,
        )

    @task
    def responder_pergunta_consumidor(self) -> Task:
        return Task(
            config=self.tasks_config["responder_pergunta_consumidor"],
        )

    @crew
    def equipe(self) -> Crew:
        """Cria a equipe de Defesa do Consumidor"""

        return Crew(
            agents=[self.especialista_defesa_consumidor()],
            tasks=[
                self.responder_pergunta_consumidor(),
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[arquivo1],
        )