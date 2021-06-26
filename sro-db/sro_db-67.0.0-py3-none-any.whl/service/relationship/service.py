from sro_db.model.relationship.model import *
from sro_db.service.base_service import BaseService

class AssociationUserStorySprintTeammemberService(BaseService):
    def __init__(self):
        super(AssociationUserStorySprintTeammemberService,self).__init__(association_user_story_sprint_team_member_table)

    def update(self, object):
        print("entrou aqui agora 123")
        print(f'user story id {object.user_story_id}')
        print(f'Team member id {object.team_member_id}')
        try:
            print("Existe relação com esse team member q está ativa? ")
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(
                    self.object.team_member_id == object.team_member_id,
                    self.object.user_story_id == object.user_story_id,
                    self.object.activate == True).first()
                # result = list(result)
                print(result.__dict__)
                if result is not None and result.activate is True: # Se já existe e está ativo, não faz nada
                    
                    print(f'{self.object.team_member_id} == {object.team_member_id}')
                    
                    print("Sim")
                    return object
                
                print('Não')

                registers = session.query(self.object).filter(self.object.user_story_id == object.user_story_id)

                if len(list(registers)) != 0: #Se existe algum ativo, inativa
                    registers.update({'activate': False})
                
                #E então cria um novo
                local_object = self.session.merge(object)
                session.add(local_object)
                # print("q q ta havendo?")
                session.commit()
                return local_object

        except:
            print("--- except ---")
            self.session.rollback() 
            raise


class AssociationDevelopmentTaskTeamMemberService(BaseService):
    def __init__(self):
        super(AssociationDevelopmentTaskTeamMemberService,self).__init__(
            association_development_task_team_member_table)

    def update(self, object):
        print("#sextou")
        try:
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(
                    self.object.team_member_id == object.team_member_id,
                    self.object.scrum_development_task_id == object.scrum_development_task_id).first()
                
                if result is not None and result.activate is True: # Se já existe e está ativo, não faz nada
                    print("Se já existe e está ativo, não faz nada")
                    print(f'Team member id {object.team_member_id}')
                    print(f'Team member id {result.team_member_id}')
                    return object

                registers = session.query(self.object).filter(
                    self.object.scrum_development_task_id == object.scrum_development_task_id)

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


class AssociationSprintScrumDevelopmentTaskService(BaseService):
    def __init__(self):
        super(AssociationSprintScrumDevelopmentTaskService,self).__init__(
            association_sprint_scrum_development_task_table)

    def update(self, object):
        try:
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(
                    self.object.sprint_id == object.sprint_id and
                    self.object.scrum_development_task_id == object.scrum_development_task_id 
                    ).first()
                if result is not None and result.activate is True: # Se já existe e está ativo, não faz nada

                    return object

                registers = session.query(self.object).filter(
                    self.object.scrum_development_task_id == object.scrum_development_task_id)

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


class AssociationSprintBacklogScrumDevelopmentActivityService(BaseService):
    def __init__(self):
        super(AssociationSprintBacklogScrumDevelopmentActivityService,self).__init__(
            association_sprint_backlog_scrum_development_activity_table)

    def update(self, object):
        try:
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(
                    self.object.sprint_backlog_id == object.sprint_backlog_id and 
                    self.object.scrum_development_task_id == object.scrum_development_task_id
                    ).first()
                if result is not None and result.activate is True: # Se já existe e está ativo, não faz nada
                    return object

                registers = session.query(self.object).filter(
                    self.object.scrum_development_task_id == object.scrum_development_task_id)

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


class AssociationAtomicUserStorySprintBacklogService(BaseService):
    def __init__(self):
        super(AssociationAtomicUserStorySprintBacklogService,self).__init__(
            association_atomic_user_story_sprint_backlog_table)

    def update(self, object):
        print("Entrou no update do user story backlog")
        try:
            with self.create_session_connection() as session:
                result = session.query(self.object).filter(
                    self.object.sprint_backlog_id == object.sprint_backlog_id, 
                    self.object.user_story_id == object.user_story_id
                    ).first()

                # print(f"Sprint backlog id: {object.sprint_backlog_id}")
                # print(f"User story id: {object.user_story_id}")
                # print(f"Result: {result.__dict__}")
                if result is not None and result.activate is True: # Se já existe e está ativo, não faz nada
                    print("Entrou no primeiro if")
                    return object

                registers = session.query(self.object).filter(
                    self.object.user_story_id == object.user_story_id)

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


