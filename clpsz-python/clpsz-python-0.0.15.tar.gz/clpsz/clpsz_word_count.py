import click
from clpsz.ufile import read_file_as_list


RESULT = {}
LETTERS = set()


def init_letters():
    for i in range(26):
        LETTERS.add(chr(ord('a') + i))
        LETTERS.add(chr(ord('A') + i))
    LETTERS.add("'")


def process_line(line):
    start = False
    word = ''
    for letter in line:
        if letter in LETTERS:
            word += letter
            if not start:
                start = True
        else:
            if start:
                RESULT[word] = RESULT.get(word, 0) + 1
                start = False
                word = ''


@click.command()
@click.option('-s', '--src', 'src', help='srt file path')
def main(src):
    main1(src)


def main1(src):
    init_letters()
    lines = read_file_as_list(src)
    for line in lines:
        process_line(line)
    for k, v in RESULT.iteritems():
        print("{} {}".format(k, v))


if __name__ == '__main__':
    main1('/tmp/ta.srt')
