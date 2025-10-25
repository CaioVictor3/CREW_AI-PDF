import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from pathlib import Path
import yaml

_BASE = Path(__file__).resolve().parent
_knowledge_dir = _BASE / "knowledge"
_candidates = [
    _knowledge_dir / "file.pdf",
    _knowledge_dir / "rdc0044_17_08_2009.pdf",
    _knowledge_dir / "tema-7-21.pdf",
]
_existing = [str(p.name) for p in _candidates if p.exists()]
pdf_tool = PDFKnowledgeSource(file_paths=_existing) if _existing else None

def _load_yaml(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

_agents_cfg = _load_yaml(_BASE / "config" / "agent.yaml")
_tasks_cfg = _load_yaml(_BASE / "config" / "tasks.yaml")

@CrewBase
class ComplianceCrew:
    agents_config = _agents_cfg
    tasks_config = _tasks_cfg

    @agent
    def especialista_compliance(self) -> Agent:
        gemini_key = os.getenv("GEMINI_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")
        llm_kwargs = {"temperature": 0}

        if gemini_key:
            llm_model = os.getenv("GEMINI_MODEL", "gemini-1.5")
            llm = LLM(model=llm_model, provider="google", api_key=gemini_key, **llm_kwargs)
        elif openai_key:
            llm_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            llm = LLM(model=llm_model, provider="openai", api_key=openai_key, **llm_kwargs)
        else:
            raise RuntimeError(
                "Nenhuma credencial de LLM encontrada. Defina GEMINI_API_KEY ou OPENAI_API_KEY."
            )

        agent_cfg = self.agents_config.get("especialista_compliance") if isinstance(self.agents_config, dict) else None
        if not agent_cfg:
            raise RuntimeError(
                "Configuração do agente 'especialista_compliance' não encontrada em config/agent.yaml."
            )

        return Agent(config=agent_cfg, verbose=True, llm=llm)

    @task
    def responder_pergunta_compliance(self) -> Task:
        task_cfg = self.tasks_config.get("responder_pergunta_compliance") if isinstance(self.tasks_config, dict) else None
        if not task_cfg:
            raise RuntimeError(
                "Configuração da task 'responder_pergunta_compliance' não encontrada em config/tasks.yaml."
            )
        return Task(config=task_cfg)

    @crew
    def crew(self) -> Crew:
        knowledge_list = [pdf_tool] if pdf_tool else []
        return Crew(
            agents=[self.especialista_compliance()],
            tasks=[self.responder_pergunta_compliance()],
            process=Process.sequential,
            verbose=True,
            knowledge=knowledge_list,
        )
