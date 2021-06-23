import factory
from .conversor_developmentTeam import ConversorDevelopmentTeam
from .conversor_epic import ConversorEpic
from .conversor_project import ConversorProject
from .conversor_sprint import ConversorSprint
from .conversor_task import ConversorTask
from .conversor_team import ConversorTeam
from .conversor_teamMember import ConversorTeamMember
from .conversor_user import ConversorUser
from .conversor_userStory import ConversorUserStory

class ConversorDevelopmentTeamFactory(factory.Factory):
    class Meta:
        model = ConversorDevelopmentTeam
        inline_args = ('organization', 'data')

class ConversorEpicFactory(factory.Factory):
    class Meta:
        model = ConversorEpic
        inline_args = ('organization', 'data')

class ConversorProjectFactory(factory.Factory):
    class Meta:
        model = ConversorProject
        inline_args = ('organization', 'data')

class ConversorSprintFactory(factory.Factory):
    class Meta:
        model = ConversorSprint
        inline_args = ('organization', 'data')

class ConversorTaskFactory(factory.Factory):
    class Meta:
        model = ConversorTask
        inline_args = ('organization', 'data')

class ConversorTeamFactory(factory.Factory):
    class Meta:
        model = ConversorTeam
        inline_args = ('organization', 'data')

class ConversorTeamMemberFactory(factory.Factory):
    class Meta:
        model = ConversorTeamMember
        inline_args = ('organization', 'data')

class ConversorUserFactory(factory.Factory):
    class Meta:
        model = ConversorUser
        inline_args = ('organization', 'data')

class ConversorUserStoryFactory(factory.Factory):
    class Meta:
        model = ConversorUserStory
        inline_args = ('organization', 'data')