from os import getenv

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


@CrewBase
class PostAi():
	"""PostAi crew"""

	agents_config = "config/agents.yml"
	tasks_config = "config/tasks.yml"

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config["researcher"],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			llm=getenv("GEMINI_LLM_MODEL"),
			verbose=True,
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config["writer"],
			llm=getenv("GROQ_MODEL_NAME"),
			verbose=True,
		)

	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config["editor"],
			llm=getenv("GROQ_MODEL_NAME"),
			verbose=True,
		)

	@task
	def research(self) -> Task:
		return Task(
			config=self.tasks_config["research"],
		)

	@task
	def write(self) -> Task:
		return Task(
			config=self.tasks_config["write"],
			output_file="article.md",
		)

	@task
	def edit(self) -> Task:
		return Task(
			config=self.tasks_config["edit"],
			output_file="article.md",
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PostAi crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
