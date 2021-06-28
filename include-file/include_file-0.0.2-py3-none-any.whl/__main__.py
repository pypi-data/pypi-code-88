import argparse
import logging
from fileinput import FileInput
from pathlib import Path

from include_file.models import Embed, File, Gitbook, Include, Link, Markdown, Repo, Repository


def get_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', '--log_level', type=int, default=20)
  parser.add_argument('-u', '--user', type=str, required=True)

  # Flags
  parser.add_argument('-g', '--glob', type=str, default=None)
  parser.add_argument('-p', '--path', type=Path, default=Path("."))
  parser.add_argument('-s', '--stem', action='store_true')
  parser.add_argument('-v', '--validate', action='store_true')
  parser.add_argument('-e', '--embed_path', type=str, default=".include_file")

  # Gitbook Flags
  parser.add_argument('-y', '--summary_path', default="")
  parser.add_argument('-d', '--deploy_branch', default="deploy")
  parser.add_argument('-t', '--toc', default="")
  parser.add_argument('-url', '--url_path', type=str, default="")
  parser.add_argument('--home', action='store_true')

  # Custom Flags
  parser.add_argument('--include', default='include')
  parser.add_argument('--link', default='link')
  parser.add_argument('--repo', default="repo")

  return parser.parse_args()


if __name__ == "__main__":
  arg = get_parser()
  logging.basicConfig(format='%(asctime)s %(levelname)-6s [%(filename)s:%(lineno)d] %(message)s',
                      datefmt='%m%d:%H%M%S')
  logging.getLogger().setLevel(arg.log_level)

  Include.INCLUDE, Link.LINK, Repo.REPO = arg.include, arg.link, arg.repo

  if arg.summary_path:
    book = Gitbook(arg.user, arg.path, arg.glob, arg.embed_path, arg.stem, arg.deploy_branch, arg.home, arg.url_path)
    book.summary = Markdown(book, book.path / arg.summary_path)
    if arg.toc:
      book.toc = File(book, book.path / arg.toc)
      table_of_contents = book.table_of_contents()
      book.toc.path.write_text(table_of_contents)
      if book.home:
        book.organize_images()
    for markdown in File.files(book):
      line2txt = {}
      logging.info("Markdown: %s", markdown.path)
      for embed in Embed.embeds(markdown):
        logging.info("Embed: %s", embed.name)
        line2txt[embed.line] = embed.to_markdown()
      with FileInput(markdown.path, inplace=True) as file:
        for i, line in enumerate(file, 1):
          if i in line2txt:
            print(line2txt[i], end="")
          else:
            print(line, end="")
  else:
    repo = Repository(arg.user, arg.path, arg.glob, arg.embed_path, arg.stem)
