"""iterable list of tokens"""

class TokenError(Exception):
    """ parser exception"""

class TokenList:
    """helper class to iterate tokens"""
    def __init__(self, tok):
        self.tok = tok.copy()
        self.pos = 0

    def raise_token_error(self,comment:str):
        """ raport exceptions """
        raise TokenError(f'TokenError at postion:{self.pos} {comment}')

    def pop(self):
        """remove first token"""
        self.pos += 1
        return self.tok[self.pos-1]

    def peek(self):
        """see first token"""
        return self.tok[self.pos] if self.pos<len(self.tok) else None

    def next_is(self, tok_type):
        """check type on firts token"""
        return self.peek()[0] == tok_type if self.pos<len(self.tok) else False

    def expect_pop(self, tok_type, comment):
        """pop next item throw if unexpected token type"""
        if not self.peek() or not self.peek()[0] == tok_type:
            self.raise_token_error(comment)
        return self.pop()
