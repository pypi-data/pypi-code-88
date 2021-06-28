class PageNumMissing(BaseException):

     def __init__(self):
        self.message = f"page number not found in note pages. Please correct the page num of preview page in note pages.."