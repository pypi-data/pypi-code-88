import hashlib
import json

from .util import sha256sum

class Rule:
    def __init__(self, output, name, args):
        self.output = output
        self.hash = hashlib.sha256(
                str([name] + list(args)).encode('utf-8')).digest()

    def __getattr__(self, name):
        return getattr(self.output, name)

    def add_file(self, path):
        with self.output.con as con:
            con.execute("insert into files (path, rule, hash) values (?, ?, ?)",
                    (path, self.hash, sha256sum(path)))

    def cleanup(self):
        with self.output.con as con:
            con.execute("delete from files where rule = ?",
                (self.hash,))
            con.execute("delete from rules where hash = ?",
                (self.hash,))

def rule(name):
    def dec(f, name):
        def m(output, *args):
            rule = Rule(output, name, args)
            out = output.get(rule)
            if out is None:
                rule.cleanup()
                result = f(rule, *args)
                output.put(rule, result)
                return result
            else:
                return out.result
        return m

    if callable(name):
        return dec(name, name.__name__)
    else:
        return lambda f: dec(f, name)
