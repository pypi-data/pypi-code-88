class Markdown(object):
    """构造markdown字符串： 支持链式调用"""
    def __init__(self):
        self.text = ''
    
    def __repr__(self):
        return '<Markdown(%s)> text:\n%s' % (id(self), self.text)

    def __str__(self):
        return self.text

    def add(self, text):
        """自由构造markdown， 需要自己处理语法"""
        self.text += text
        return self

    def add_line(self, line=""):
        self.text += '%s \n ' % line
        return self

    def add_header(self, header, level=3):
        """添加标题"""
        self.text += '#' * level + ' ' + header + ' \n '
        return self

    def add_ref(self, ref):
        """添加引用"""
        self.text += '> ' + ref + ' \n '
        return self

    def add_link(self, link, description=''):
        """添加链接"""
        self.text += '[%s](%s) \n ' % (description, link)
        return self

    def add_img(self, img, description=''):
        self.text += '![%s](%s) \n ' % (description, img)
        return self

    def add_list(self, item_list, order=False):
        """添加有序或无序列表"""
        if not order:
            for line in item_list:
                self.text += '%s %s \n\n ' % ('-', line)
        else:
            for index, line in enumerate(item_list):
                self.text += '%d %s \n\n' % (index+1, line)
        return self.add_blank()

    def add_form(self, name, value):
        if value:
            value = '**%s**' % value
        self.text += "%s: %s \n  \n " % (name, value)
        return self

    def add_blank(self):
        """添加新行"""
        self.text += ' \n '
        return self

    def add_bold(self, bold):
        "添加加粗行"
        self.text += self.convert_bold(bold)
        return self.add_blank()

    def add_italic(self, italic):
        "添加斜体行"
        self.text += self.convert_italic(italic)
        return self.add_blank()

    def convert_bold(self, bold):
        "返回加粗内容"
        return '**%s**' % bold

    def convert_italic(self, italic):
        "返回斜体内容"
        return '*%s*' % italic

    def convert_link(self, link, description=''):
        """添加链接"""
        if not description:
            description = link
        return '[%s](%s)' % (description, link)

if __name__ == "__main__":
    m = Markdown()
    m.add_header('Message Test')
    m.add_blank().add_ref('this is a reference info').add_blank()

    value = m.convert_link('www.baidu.com', 'baidu') + ' | ' + m.convert_link('www.google.com', 'google')
    m.add_form('links', value)
    print(m)