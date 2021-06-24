"""
with is sed in exception handling to make the code cleaner and much more readable
"""
import os


class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val):
        self.file.close()


if __name__ == '__main__':
    print(os.getpid())
