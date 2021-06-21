from sqlalchemy.orm import class_mapper
from sqlalchemy_pagination import paginate

models = []


def uml_model(model):
    models.append(class_mapper(model))
    return model


class Paginator:
    def __init__(self, query, current_page, page_size=10):
        self.current = None
        self.current_page = current_page
        self.query = query
        self.page_size = page_size
        self.max_pages = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_pages is not None and self.page_number > self.max_pages:
            raise StopIteration

        if self.current is None:
            self.load_page()

            return self.current

        if self.current.has_next:
            self.current_page = self.current.next_page
            self.load_page()

            return self.current

        raise StopIteration

    def load_page(self):
        self.current = paginate(self.query, self.current_page, self.page_size)

    @property
    def items(self):
        return self.current.items

    @property
    def page_number(self):
        return self.current_page
