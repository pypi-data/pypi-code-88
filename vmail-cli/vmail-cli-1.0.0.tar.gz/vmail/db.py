from urllib.parse import quote_plus

import click
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.exc import ArgumentError, OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


def get_db_connection(config):
    """Initialize a database connection for the given configuration."""
    try:
        engine = create_engine(
            '{dialect}://{username}:{password}@{host}:{port}/{name}'.format(
                dialect=config['database']['type'].get(str),
                host=config['database']['host'].get(str),
                port=config['database']['port'].get(int),
                username=config['database']['username'].get(str),
                password=quote_plus(config['database']['password'].get(str)),
                name=config['database']['name'].get(str),
            )
        )
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
    except ArgumentError as error:
        raise click.ClickException(
            f"Invalid database configuration.\nDetails: {error}"
        )
    except OperationalError as error:
        raise click.ClickException(
            f"Could not connect to the database.\nDetails: {error}"
        )
    return Session()


class Domains(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('domain', String(255), nullable=False, unique=True)

    accounts = relationship('Accounts', back_populates='domain')
    aliases = relationship('Aliases', back_populates='source_domain')


class Accounts(Base):
    __tablename__ = 'accounts'
    __table_args__ = (
        UniqueConstraint('username', 'domain', name='unique_account'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), nullable=False)
    domain_name = Column(
        'domain',
        String(255),
        ForeignKey('domains.domain'),
        nullable=False,
    )
    password = Column(String(255), nullable=False)
    quota = Column(Integer, default=0)
    enabled = Column(Boolean, default=False)
    sendonly = Column(Boolean, default=False)

    domain = relationship('Domains', back_populates='accounts')

    @property
    def email(self):
        return f'{self.username}@{self.domain_name}'


class Aliases(Base):
    __tablename__ = 'aliases'
    __table_args__ = (
        UniqueConstraint(
            'source_username',
            'source_domain',
            'destination_username',
            'destination_domain',
            name='unique_alias',
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    source_username = Column(String(64), nullable=False)
    source_domain_name = Column(
        'source_domain',
        String(255),
        ForeignKey('domains.domain'),
        nullable=False,
    )
    destination_username = Column(String(64), nullable=False)
    destination_domain_name = Column(
        'destination_domain', String(255), nullable=False
    )
    enabled = Column(Boolean, default=False)

    source_domain = relationship('Domains', back_populates='aliases')

    @property
    def source_email(self):
        return f'{self.source_username}@{self.source_domain_name}'

    @property
    def destination_email(self):
        return f'{self.destination_username}@{self.destination_domain_name}'
