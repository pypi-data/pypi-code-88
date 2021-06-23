from typing import List


class Progress(object):
    """ Helper class used to track progress.

    Sets and reads the progress of different items declared in
    a tree like structure with ready state for itself and all children.

    Note:
        childrend_count() and children_ready_count() are intended mostly for UI purposes.

    TODO:
        Save & read of progress is in the Worker class.
        It needs to be refactored and moved here.

    Examples:
        >>> progress = Progress(id="my_progress")
        ... progress.update(ready=False, count=100, page='1')
        ... progress.update(ready=False, count=100, page='2')
        ... progress.update(ready=True)
    """

    _id: str
    _overall: dict
    _items: List

    def __init__(self, id, progress=None):
        self._id = id

        if progress:
            self._overall = progress.get('overall')
            self._items = [Progress(id=item['id'], progress=item) for item in progress['items']]
        else:
            self._overall = {
                'ready': False,
                'page': 1,
                'count': 0,
            }
            self._items = []

    def __getitem__(self, item):
        items = [i for i in self._items if i._id == item]
        if len(items) == 0:
            item = Progress(id=item)
            self._items.append(item)
            return item
        if len(items) == 1:
            return items[0]
        return None

    def update(self, ready: bool, count: int = None, page: str = None):
        """

        Args:
            ready: Mark progress as done or not.
            count: Set the count of the work that was done.
            page: Set the page of the work that was done. (In case we need to save & resume from a particular page)

        """
        self._overall['ready'] = ready

        if count:
            self._overall['count'] = count
        if page:
            self._overall['page'] = page

    def to_dict(self) -> dict:
        """Returns the tree representation of this progress and all children.

        Returns:
            A recursive dict representation of this item and all it's children::

                {
                    id: str,                        # name of this object
                    overall:
                    {
                        ready: bool,                # whether this and all children are ready
                        page: str,                  # `page` as set by `update` function
                        count: int,                 # `count` as set by `update` function
                        children_count: int,        # count of all children
                        children_ready_count: int   # count of all ready children
                    },
                    items: [list of all children to_dict() representation]
                }
        """

        return {
            'id': self._id,
            'overall': {
                'ready': self.is_ready(),
                'page': self.get_page(),
                'count': self.count(),
                'children_count': self.children_count(),
                'children_ready_count': self.children_ready_count()
            },
            'items': [item.to_dict() for item in self._items]
        }

    def is_ready(self) -> bool:
        """Returns whether this progress's state is ready or not.

        Compute recursively all children's ready state.

        Returns:
            Whether all children are ready if any, self ready state otherwise.
        """

        # Leaf node, return ready state
        if len(self._items) == 0:
            return self._overall['ready']
        else:
            # Compute downwards the ready state
            is_ready = True
            for item in self._items:
                is_ready = is_ready and item.is_ready()
            return is_ready

    def get_page(self):
        """The value for the ``page`` attribute as set with the ``update`` function.

        Returns:
            Page Value.
        """

        return self._overall['page']

    # Only for UI
    def count(self) -> int:
        """The value for the ``count`` attribute as set with the ``update`` function.

        Returns:
            Count Value.
        """

        return self._overall['count']

    # Only for UI
    def children_count(self) -> int:
        """The count of all children.

        Returns:
            Count of all children.

        """
        return len(self._items)

    # Only for UI
    def children_ready_count(self):
        """The count of all children that are ready.

        Returns:
            Count of all children that are ready.

        """
        return len([i for i in self._items if i.is_ready()])
