"""Declares :class:`RelationalDatabaseRepository`."""
import ioc
from sqlalchemy.exc import NoResultFound

from . import query


class Repository:
    """A repository implementation for use with :mod:`sqlalchemy`."""

    #: Provides the factory function to create a database session. If
    #: :attr:`session_factory` is a string, it is assumed to identify a callable
    #: that is provided through the :mod:`python-ioc` module (i.e. available
    #: by calling :func:`ioc.require`). Otherwise, :attr:`session_factory` must
    #: be a callable that returns an asynchronous SQLAlchemy database session.
    session_factory: str = 'AsyncSessionFactory'

    @property
    def exists_query(self):
        raise NotImplementedError

    @property
    def reconstruct_query(self):
        raise NotImplementedError

    async def get(self, **params):
        """Reconstruct a domain object that is identified by the given
        parameters. The default implementation assumes that the :attr:`factory`
        atrribute is specified and that the factory object exposes the
        ``fromdao`` method, which takes a single row result as its sole
        positional argument.
        """
        assert hasattr(self, 'factory') # nosec
        q = self.get_reconstruct_query(**params)
        try:
            return self.factory.fromdao(await self.query(q))
        except NoResultFound:
            raise self.DoesNotExist

    async def get_declarative(self, q, allow_none=False):
        """Return a declarative SQLAlchemy model instance."""
        result = await self.execute_query(q)

    def get_exists_query(self, *args, **kwargs):
        """Return a boolean indicating if an entity exists. Must return
        a :class:`~unimatrix.ext.orm.query.NamedQuery` instance.
        """
        return self.exists_query(*args, **kwargs)

    def get_reconstruct_query(self, *args, **kwargs) -> query.NamedQuery:
        """Return a :class:`~unimatrix.ext.orm.query.NamedQuery` instance
        that fetches the data to reconstruct a single domain entity.
        """
        return self.reconstruct_query(*args, **kwargs)

    async def execute_query(self, q):
        return await self.session.execute(q)

    async def exists(self, **params):
        return await self.query(self.get_exists_query(**params))

    async def persist_declarative(self, dao, flush=False, merge=False):
        """Persist the declarative SQLAlchemy ORM object `dao`.

        Args:
            flush (boolean): indicates if the SQLAlchemy session should be
                flushed after adding (or merging) `dao`.
            merge (boolean): indicates if the object should be `merged`
                to the session instead of `added`. Default is ``False``. Refer
                to the SQLAlchemy documentation for more information.

        Returns:
            The declarative SQLAlchemy object `dao`. If `flush` was ``True``,
            then its properties are immediately updated to reflect the persisted
            state e.g. to update the value of an auto-incrementing integer
            primary key.
        """
        if merge:
            dao = await self.session.merge(dao)
        else:
            self.session.add(dao)
        if flush:
            await self.session.flush()
        return dao

    async def query(self, q):
        """Run a :class:`~unimatrix.ext.orm.query.NamedQuery` and return
        the result(s).
        """
        return await q.run(self.session)

    async def __aenter__(self):
        self._manages_session = False
        if getattr(self, 'session', None) is None:
            if isinstance(self.session_factory, str):
                self.session = ioc.require(self.session_factory)()
            elif callable(self.session_factory):
                self.session = self.session_factory()
            else:
                raise NotImplementedError(
                    'Provide an inversion-of-control key as the session_factory'
                    ' attribute or implement it as a method.'
                )

        self._manages_session = not self.session.sync_session.in_transaction()

        # Determine if there is a transaction running. If a transaction is
        # running, start a savepoint, else begin a new one.
        begin = self.session.begin
        if not self._manages_session:
            begin = self.session.begin_nested
        self.tx = begin()
        await self.tx.__aenter__()
        return self

    async def __aexit__(self, cls, exc, tb):
        try:
            # self.tx is not set if an exception was raised due to
            # improperly configured inversion-of-control.
            if hasattr(self, 'tx'):
                await self.tx.__aexit__(cls, exc, tb)
        finally:
            if self._manages_session:
                await self.session.close()


class RelationalDatabaseRepository(Repository):
    """A repository implementation for use with :mod:`sqlalchemy`."""
