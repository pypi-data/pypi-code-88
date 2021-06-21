import factory
from .product_backlog import product_backlog
from .scrum_development_task import scrum_development_task
from .scrum_project import scrum_project
from .scrum_project_team import scrum_project_team
from .scrum_development_team import scrum_development_team
from .sprint import sprint
from .team_member import team_member
from .user_story import user_story
from .epic import epic
from .user import user
from .sprint_backlog import sprint_backlog
# from .task_extra import task_extra
from .development_task_type import DevelopmentTaskType
from .priority import Priority
from .scrum_development_task_history import scrum_development_task_history

class priorityFactory(factory.Factory):
	class Meta:
		model = Priority

class scrum_development_task_historyFactory(factory.Factory):
	class Meta:
		model = scrum_development_task_history

class development_task_typeFactory(factory.Factory):
	class Meta:
		model = DevelopmentTaskType

class product_backlogFactory(factory.Factory):
	class Meta:
		model = product_backlog
		  
class scrum_development_taskFactory(factory.Factory):
	class Meta:
		model = scrum_development_task
		  
class scrum_projectFactory(factory.Factory):
	class Meta:
		model = scrum_project
		  
class scrum_project_teamFactory(factory.Factory):
	class Meta:
		model = scrum_project_team
		  
class scrum_development_teamFactory(factory.Factory):
	class Meta:
		model = scrum_development_team
		  
class sprintFactory(factory.Factory):
	class Meta:
		model = sprint
		  
class team_memberFactory(factory.Factory):
	class Meta:
		model = team_member
		  
class user_storyFactory(factory.Factory):
	class Meta:
		model = user_story
		  
class epicFactory(factory.Factory):
	class Meta:
		model = epic
		  
class userFactory(factory.Factory):
	class Meta:
		model = user
		  
class sprint_backlogFactory(factory.Factory):
	class Meta:
		model = sprint_backlog

# class task_extraFactory(factory.Factory):
# 	class Meta:
# 		model = task_extra

