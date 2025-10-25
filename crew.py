from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Knowledge sources
file1 = PDFKnowledgeSource(file_paths=["file.pdf"])
file2 = PDFKnowledgeSource(file_paths=["file2.pdf"])
file3 = PDFKnowledgeSource(file_paths=["file3.pdf"])


llm = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0,
    max_tokens=1500,
)


@CrewBase
class ComplianceCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def pharma_compliance_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["pharma_compliance_expert"],
            verbose=True,
            tools=[],
            llm=llm,
        )

    @task
    def answer_compliance_question(self) -> Task:
        return Task(
            config=self.tasks_config["answer_compliance_question"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MQuestKnowledge crew"""

        return Crew(
            agents=[self.pharma_compliance_expert()],
            tasks=[
                self.answer_compliance_question(),
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[file1, file2, file3],
        )