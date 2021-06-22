import csv
import os


class NCsv:
    def __init__(self, link, delimiter=',', encoding='UTF-8'):
        self.link = link
        self.delimiter = delimiter
        self.encoding = encoding
        if os.access(link, os.X_OK):
            with open(link, 'r', encoding=encoding) as csv_f:
                self.csv_reader = csv.reader(csv_f, delimiter=self.delimiter)
                self.lines = [i for i in self.csv_reader]
        else:
            with open(link, 'w', encoding=encoding) as csv_f:
                self.lines = [[],[]]

    def __repr__(self):
        return f'<file: {self.link}>'

    def __str__(self):
        text = ''
        for line in self.lines:
            text = text + self.delimiter.join(line)+'\n'
        return text

    def header(self):
        return self.lines[0]

    def header_set(self, header):
        if type(header) == str:
            headers = header
            headers.replace(self.delimiter+' ', self.delimiter)
            if not len(self.lines):
                self.lines.append(headers.split(self.delimiter))
            else:
                self.lines[0] = headers.split(self.delimiter)
        if (type(header) == list) or (type(header) == tuple):
            if not len(self.lines):
                self.lines.append(header)
            else:
                self.lines[0] = list(header)

    def body(self):
        return self.lines[1:]

    def dictionary(self):
        d = []
        for i in self.body():
            line = dict()
            tmp = 0
            for j in self.header():
                try:
                    line[j] = i[tmp]
                    tmp = tmp + 1
                except IndexError:
                    break
            d.append(line)
        return d

    def add_line(self, line):
        if not self.lines[-1]:
            self.lines.pop()
        if (type(line) == list) or (type(line) == tuple):
            line = list(map(str, line))
            self.lines.append(line)
        elif type(line) == str:
            tmp = line
            tmp.replace(' ', '')
            self.lines.append(tmp.split(self.delimiter))

    def add_lines(self, lines):
        for line in lines:
            if not self.lines[-1]:
                self.lines.pop()
            if (type(line) == list) or (type(line) == tuple):
                line = list(map(str, line))
                self.lines.append(line)
            elif type(line) == str:
                tmp = line
                tmp.replace(' ', '')
                self.lines.append(tmp.split(self.delimiter))

    def save(self):
        with open(self.link, 'w', newline='',) as csv_writer:
            writer = csv.writer(csv_writer, delimiter=self.delimiter)
            for i in self.lines:
                writer.writerow(i)
        self.__init__(self.link, self.delimiter, self.encoding)
