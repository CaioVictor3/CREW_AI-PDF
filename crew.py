from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
import os
from langchain_google_generativeai import ChatGoogleGenerativeai

from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeai(model="gemini-1.5-flash", verbose=True, temperature=0)

search_tool = PDFSearchTool(
    pdf='knowledge/file1.pdf',
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-flash",
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
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
            tools=[search_tool],
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
        )