from docs_translate.file_translator import FileTranslator
from docs_translate.files_worker import FilesWorker
from docs_translate.logs import logger
from docs_translate.settings import Settings
from docs_translate.reserved_word import ReservedWords


class App:
    def __init__(self) -> None:
        self.settings = Settings()
        self.reserved_words = ReservedWords(self.settings.reserved_words)

    def process(self) -> None:
        files_to_process = FilesWorker(self.settings).get_files()
        logger.info(f'Processing: {", ".join([f.name for f in files_to_process])}')
        for file_path in files_to_process:
            copy_path = FilesWorker(self.settings).create_file(file_path)
            with FileTranslator(self.settings, self.reserved_words, file_path, copy_path=copy_path) as processing_file:
                processing_file.translate()
            logger.success('Processed: {file_path} --> {copy_path}'.format(file_path=file_path, copy_path=copy_path))


def run() -> None:
    try:
        App().process()
        exit(0)
    except Exception as err:
        logger.exception(err)
        exit(1)


if __name__ == "__main__":
    run()
