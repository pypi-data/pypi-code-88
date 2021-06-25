import factory
from . import factories
import concurrent.futures

class Manager ():
    """Class responsible to controlle the offline flow (initial fill of database)
    """
    def __init__(self, data: dict) -> None:
        """Create a Manager

        Args:
            data (dict): With user, key and server to connect with jira
        """
        self.data = data
        self.scrum_project_team = factories.scrum_project_teamFactory()
        self.user = factories.userFactory()
        self.epic = factories.epicFactory()
        self.product_backlog = factories.product_backlogFactory()
        self.scrum_development_task = factories.scrum_development_taskFactory()
        self.scrum_project = factories.scrum_projectFactory()
        self.sprint_backlog = factories.sprint_backlogFactory()
        self.sprint = factories.sprintFactory()
        self.team_member = factories.team_memberFactory()
        self.user_story = factories.user_storyFactory()
        self.scrum_development_team = factories.scrum_development_teamFactory()
        self.development_task_type = factories.development_task_typeFactory()
        self.priority = factories.priorityFactory()
        self.scrum_development_task_history = factories.scrum_development_task_historyFactory()

    def f(self, action: object) -> str:
        """Run the extract method of param action

        Args:
            action (object): ETL class

        Returns:
            str: "done"
        """
        action.extract(self.data)
        return "done"

    def extract_all(self) -> None:
        """Retrieve all data from jira api and save them on mongo database
        """
        #cadastra os dados do Jira no mongo
        iterable = [self.scrum_development_task_history,
                    self.scrum_development_task, 
                    self.user, 
                    self.scrum_project,
                    self.sprint]
      
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            result_futures = list(map(lambda x: executor.submit(self.f, x), iterable))
            for future in concurrent.futures.as_completed(result_futures):
                try:
                    print('resutl is', future.result())
                except Exception as e:
                    print('e is', e, type(e))
                
    def do_all(self) -> None:
        """Run method 'do' of all ETL classes
        """
        # Cadastra os dados do mongo no SRO
        self.scrum_development_task_history.do(self.data)
        self.user.do(self.data)
        self.scrum_project.do(self.data)
        self.scrum_project_team.do(self.data)
        self.scrum_development_team.do(self.data)
        self.team_member.do(self.data)
        self.sprint.do(self.data)
        self.epic.do(self.data)                     
        self.user_story.do(self.data) 
        self.development_task_type.do(self.data)
        self.priority.do(self.data)
        self.scrum_development_task.do(self.data)

