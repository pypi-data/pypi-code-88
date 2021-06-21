from sro_db.config.config import Base
from sqlalchemy import Column ,ForeignKey, Integer
from sqlalchemy.orm import relationship

class association_sprint_scrum_development_task_table (Base):
    __tablename__ = 'sprint_scrum_development_task'
    scrum_development_task_id = Column(Integer, ForeignKey('scrum_development_task.id'), primary_key=True)
    sprint_id = Column(Integer, ForeignKey('sprint.id'), primary_key=True)
    sprints = relationship("Sprint")    

class association_development_task_team_member_table (Base):
    __tablename__ = 'team_member_scrum_development_task'
    scrum_development_task_id = Column(Integer, ForeignKey('scrum_development_task.id'), primary_key=True)
    team_member_id = Column(Integer, ForeignKey('team_member.id'), primary_key=True)
    team_member = relationship("TeamMember")

class association_sprint_backlog_scrum_development_activity_table (Base):
    __tablename__ = 'sprint_backlog_scrum_development_task'
    scrum_development_task_id = Column(Integer, ForeignKey('scrum_development_task.id'), primary_key=True)
    sprint_backlog_id = Column(Integer, ForeignKey('sprint_backlog.id'), primary_key=True)
    sprint_backlogs = relationship("SprintBacklog")

class association_atomic_user_story_sprint_backlog_table (Base):
    __tablename__ = 'atomic_user_story_sprint_backlog'
    user_story_id = Column(Integer, ForeignKey('user_story.id'), primary_key=True)
    sprint_backlog_id = Column(Integer, ForeignKey('sprint_backlog.id'), primary_key=True)
    sprint_backlogs = relationship("SprintBacklog")

class association_user_story_sprint_team_member_table (Base):
    __tablename__ = 'user_story_team_member'
    user_story_id = Column(Integer, ForeignKey('user_story.id'), primary_key=True)
    team_member_id = Column(Integer, ForeignKey('team_member.id'), primary_key=True)
    assigned_by = relationship("TeamMember")

