import re
import sys
import random
import string 


def main() :


    def listexpand(code) :
        if not code or "[]" not in code :
            return code
        def listexpand_helper(code) :
            print("# code = ",code)
            if "[]" not in code :
                return code
            tvar = "_" + "".join([random.choice(string.ascii_letters) for _ in range(3)])
            l,x = code.split("[]",1)
            return "[ {} for {} in {} ]".format(listexpand_helper(tvar+x),tvar,l)
        res = ""
        xcode = code
        _x_m = re.search(r"(\w|\.|\[\])+",xcode,re.DOTALL)
        while _x_m :
            before = xcode[:_x_m.start()]
            end = xcode[_x_m.end():]
            chain = _x_m.group(0)
            res += before + listexpand_helper(chain)
            xcode = end
            _x_m = re.search(r"(\w|\.|\[\])+",xcode,re.DOTALL)
        res += xcode
        return res

    print(listexpand(sys.argv[1]))


main()

