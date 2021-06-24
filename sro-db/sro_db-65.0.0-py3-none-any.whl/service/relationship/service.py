from sro_db.model.relationship.model import *
from sro_db.service.base_service import BaseService

class AssociationDevelopmentTaskTeamMemberService(BaseService):
    def __init__(self):
        super(AssociationDevelopmentTaskTeamMemberService,self).__init__(association_development_task_team_member_table)


class AssociationSprintScrumDevelopmentTaskService(BaseService):
    def __init__(self):
        super(AssociationSprintScrumDevelopmentTaskService,self).__init__(association_sprint_scrum_development_task_table)

class AssociationSprintBacklogScrumDevelopmentActivityService(BaseService):
    def __init__(self):
        super(AssociationSprintBacklogScrumDevelopmentActivityService,self).__init__(association_sprint_backlog_scrum_development_activity_table)


class AssociationAtomicUserStorySprintBacklogService(BaseService):
    def __init__(self):
        super(AssociationAtomicUserStorySprintBacklogService,self).__init__(association_atomic_user_story_sprint_backlog_table)

class AssociationUserStorySprintTeammemberService(BaseService):
    def __init__(self):
        super(AssociationUserStorySprintTeammemberService,self).__init__(association_user_story_sprint_team_member_table)
    
    def update_assignee(self, user_story, team_member):
        print('entrou na update assignee')
        with self.create_session_connectio() as session:
            retorno = session.query(self.object).filter(self.object.user_story_id == user_story.id and self.object.team_member_id == team_member.id)
            if retorno is None:
                session.query(self.object).filter(self.object.user_story_id == user_story.id).update({'activate': False})
                session.query(self.object).create()
   
    def find_all_by_userStoryId(self, user_story):
        print('entrou')
        with self.create_session_connection() as session:   
            results = session.query(self.object).filter(self.object.user_story_id == user_story.id)
            return results

    def update(self, object):
        print(f'user story id {object.user_story_id}')
        print(f'Team member id {object.team_member_id}')
        try:
            print("Existe relação com esse team member q está ativa? ")
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(self.object.team_member_id == object.team_member_id and self.object.user_story_id == object.user_story_id and self.object.activate == True)
                result = list(result)
                if result != []: # Se já existe e está ativo, não faz nada
                    
                    print(f'{self.object.team_member_id} == {object.team_member_id}')
                    
                    print("Sim")
                    return object
                
                print('Não')

                registers = session.query(self.object).filter(self.object.user_story_id == object.user_story_id 
                and object.activate)

                if len(list(registers)) != 0: #Se existe algum ativo, inativa
                    registers.update({'activate': False})
                
                #E então cria um novo
                local_object = self.session.merge(object)
                session.add(local_object)
                session.commit()
                return local_object

        except:
            print("--- except ---")
            self.session.rollback() 
            raise

        