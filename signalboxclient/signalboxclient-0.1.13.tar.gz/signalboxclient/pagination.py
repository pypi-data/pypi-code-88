
def pageQuery(page: int = None):
    return f'p.page={1 if page is None else page}'


class Pagination:
    def __init__(self, pageCount, totalItemCount, pageNumber, hasPreviousPage, hasNextPage, isFirstPage, isLastPage):
        self.pageCount = pageCount
        self.totalItemCount = totalItemCount
        self.pageNumber = pageNumber
        self.hasPreviousPage = hasPreviousPage
        self.hasNextPage = hasNextPage
        self.isFirstPage = isFirstPage
        self.isLastPage = isLastPage

class PaginatedResponse:
    def __init__(self, **kwargs):
        self.items = kwargs['items']
        self.pagination = Pagination(**kwargs['pagination'])