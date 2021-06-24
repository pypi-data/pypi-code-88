import unittest
import os
from appteka.reporter import HtmlReporter
from appteka.reporter import LatexReporter


FILE_HTML = "tmp.html"
FILE_LATEX = "tmp.tex"


class TestHtmlReporter(unittest.TestCase):
    def setUp(self):
        _clear()

    def tearDown(self):
        _clear()

    def test_empty(self):
        rep = HtmlReporter()
        rep.report(FILE_HTML)
        with open(FILE_HTML) as buf:
            text = buf.read()
        self.assertEqual(text, "")

    def test_begin_end(self):
        rep = HtmlReporter()
        rep.begin()
        rep.end()
        rep.report(FILE_HTML)

        with open(FILE_HTML) as buf:
            text = buf.read()
        waited = ""
        waited += "<html>\n"
        waited += "<head><Meta charset='UTF-8'/></head>\n"
        waited += "<body>\n"
        waited += "</body>\n"
        waited += "</html>\n"
        self.assertEqual(text, waited)

    def test_header_pic_and_text(self):
        rep = HtmlReporter()
        rep.begin()
        rep.add_header("Test")
        rep.add_header("Test", 2)
        rep.add_pic("test.png")
        rep.add_text("test")
        rep.end()
        rep.report(FILE_HTML)

        with open(FILE_HTML) as buf:
            text = buf.read()
        waited = ""
        waited += "<html>\n"
        waited += "<head><Meta charset='UTF-8'/></head>\n"
        waited += "<body>\n"
        waited += "<h1>Test</h1>\n"
        waited += "<h2>Test</h2>\n"
        waited += "<img src='test.png' width='800'>\n"
        waited += "<pre>test</pre>\n"
        waited += "</body>\n"
        waited += "</html>\n"
        self.assertEqual(text, waited)


class TestLatexReporter(unittest.TestCase):
    def setUp(self):
        _clear()

    def tearDown(self):
        _clear()

    def test_touch(self):
        rep = LatexReporter()
        rep.begin()
        rep.add_header("Test h1")
        rep.add_header("Test h2", 2)
        rep.add_header("Test h3", 3)
        rep.add_header("Test h4", 4)
        rep.add_pic("test.png")
        rep.add_text("test")
        rep.end()
        rep.report(FILE_LATEX)

        waited = ""
        waited += "\n\\HeaderCommandOne{Test h1}\n"
        waited += "\n\\HeaderCommandTwo{Test h2}\n"
        waited += "\n\\HeaderCommandThree{Test h3}\n"
        waited += "\n{Test h4}\n"
        waited += "\n\\InsertPicCommand{" + os.path.abspath("test.png")
        waited += "}\n"
        waited += "\n\\TraceTextCommand{test}\n"

        with open(FILE_LATEX) as buf:
            text = buf.read()
        self.assertEqual(text, waited)


def _clear():
    try:
        os.remove(FILE_HTML)
    except Exception:
        pass

    try:
        os.remove(FILE_LATEX)
    except Exception:
        pass
