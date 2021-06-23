import sys
import argparse
import os
import json
import yaml
import xmltodict
import re
import traceback
import time
import random
import string
from sretools import (SimpleTable,commandline,prepare_table)
from collections import (deque,defaultdict)
from types import FunctionType
from pygments import highlight
from pygments.lexers import (JsonLexer,YamlLexer,XmlLexer,guess_lexer)
from pygments.lexers.python import PythonLexer
from pygments.formatters import Terminal256Formatter
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer


def _j(ds) :
    return json.dumps(ds,indent=2,sort_keys=True)
def _x(ds) :
    import xml.dom.minidom as dom
    import dicttoxml
    xmlstr = dicttoxml.dicttoxml(ds).decode()
    xml = dom.parseString(xmlstr)
    return xml.toprettyxml()
def _y(ds) :
    return yaml.dump(ds,default_flow_style=False,explicit_start=True, explicit_end=False)
def _l(ds) :
    ret = ""
    if type(ds) in [list,set,tuple] :
        for i in ds :
            ret += str(i) + "\n"
    if type(ds) is dict :
        l=len(ds)+2
        fmt="{:"+str(l)+"} = {}"
        for i,v in ds.items() :
            ret += (fmt.format("."+i,v))
    return ret
def _lf(fn) :
    return open(fn,"r").read()
def _lj(fn) :
    return json.loads(_lf(fn))
def _ly(fn) :
    return yaml.safe_load(_lf(fn))
def _l2t(xjson,header=None,maxcolwidth=100) :
    data,header=prepare_table(xjson,header)
    return SimpleTable(data=data,header=header,maxwidth=maxcolwidth)
def _l2pt(xjson,header=None) :
    data,header=prepare_table(xjson,header)
    return SimpleTable(data=data,header=header).repr_pivot()
def _t(data=list(),header=None,dataonly=False,maxcolwidth=100) :
    return SimpleTable(data=data,header=header,noheader=dataonly,maxwidth=maxcolwidth)
def _pt(data=list(),header=None,dataonly=False) :
    return SimpleTable(data=data,header=header,noheader=dataonly)
def _qx(cmd) :
    try :
        ret,out,err = commandline.qx(cmd)
        if err :
            out += "\n" + err
        return out
    except :
        return traceback.format_exc()
def _flat(ds,last=""):
    res = ""
    if type(ds) is dict :
        for k,v in ds.items() :
            if type(v) in [dict,list] :
                res += _flat(v,last+"."+k) 
            else :
                res += last+"."+k+" = "+str(v) + "\n"
    if type(ds) is list :
        for i,v in enumerate(ds) :
            if type(v) in [dict,list] :
                res += _flat(v,last+"["+str(i)+"]") 
            else :
                res += last+"["+str(i)+"] = " + str(v) + "\n"
    return res

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="code", nargs='?', default="_", help="code to compile. may be a file.")
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument("-t", "--srctype", dest="srctype", default="JSON", help="JSON,YAML or XML")
    parser.add_argument("-i", "--indent", dest="indent", default=4, help="how many spaces for indent. default 4.")
    parser.add_argument("-m", "--modules", dest="modules", help="import modules.")
    parser.add_argument("-K", "--keys", dest="keys_included", help="only keep these keys.")
    parser.add_argument("-E", "--nokeys", dest="keys_excluded", help="these keys should be excluded.")
    parser.add_argument("-F", "--functionize", dest="func", action="store_true", default=False, help="wrap code into an internal function",)
    parser.add_argument("-s", "--rawstr", dest="rawstr", action="store_true", default=False, help="output raw stings for easy grep",)
    parser.add_argument("-I", "--interactive", dest="interactive", action="store_true", default=False, help="interactive mode",)
    parser.add_argument("-p", "--plain", dest="plain", action="store_true", default=False, help="force no color code",)
    parser.add_argument("-c", "--compact", dest="compact", action="store_true", default=False, help="dump data structure in compact mode",)
    parser.add_argument("-X", "--debug", dest="debug", action="count", default=False, help="debug mode",)
    _x_args = parser.parse_args()

    if _x_args.debug >=2 :
        print("# args = ",_x_args)

    def supports_color():
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        # guess. 
        m = re.search(r"^xterm",os.environ.get("TERM","n/a"),re.IGNORECASE)
        return m or (supported_platform and is_a_tty)
    if not _x_args.plain and not supports_color() :
        _x_args.plain = True

    if _x_args.keys_included :
        _xdt_keys_included = dict()
        for w in  _x_args.keys_included.split(",") :
            recursive = 0
            if re.search(r"(\*|\/|\+)+$",w) :
                recursive = 1
                w = re.sub(r"(\*|\/|\+)+$","",w)
            if w :
                _xdt_keys_included[w.lower()] = recursive
    else :
        _xdt_keys_included = None
    if _x_args.keys_excluded :
        _xset_keys_excluded = set([w.lower() for w in _x_args.keys_excluded.split(",") if w])
    else :
        _xset_keys_excluded = None

    def cutkeys_helper(ds,inkeys,outkeys) :
        if not inkeys and not outkeys :
            return ds
        if type(ds) is dict :
            ds = {k:v for k, v in ds.items() if (not inkeys or k.lower() in inkeys) and (not outkeys or k.lower() not in outkeys)}
            for k,v in ds.items() :
                if not inkeys or (inkeys and k.lower() in inkeys and inkeys[k.lower()] != 1) :
                    ds[k] = cutkeys_helper(v,inkeys,outkeys)
        if type(ds) is list :
            for i,v in enumerate(ds) :
                if type(v) in [dict,list] :
                    ds[i] = cutkeys_helper(v,inkeys,outkeys)
        return ds
    def cutkeys(ds,inkeys=_xdt_keys_included,outkeys=_xset_keys_excluded) :
        ds = cutkeys_helper(ds,inkeys,outkeys)
        if _xset_keys_excluded :
            ds = cutkeys_helper(ds,inkeys=dict(),outkeys=outkeys)
        return ds

    def collect_keys(ds, dt) :
        if type(ds) is dict :
            for k, v in ds.items() :
                dt[k.lower()].add(k)
                collect_keys(v,dt)
        elif type(ds) in [list,tuple] :
            for i in ds :
                collect_keys(i,dt)
        else :
            pass

    def show_result(res) :
        if not res :
           return
        if type(res) is str :
            if _x_args.plain :
                print(res) 
                return
            try :
                json.loads(res)
                print(highlight(res,JsonLexer(),Terminal256Formatter()))
                return
            except :
                pass
            try :
                yaml.safe_load(res)
                print(highlight(res,YamlLexer(),Terminal256Formatter()))
                return
            except :
                pass
            try :
                xmltodict.parse(res)
                print(highlight(res,XmlLexer(),Terminal256Formatter()))
                return
            except :
                pass
            print(highlight(res,guess_lexer(res),Terminal256Formatter()))
        else :
            res = cutkeys(res)
            if _x_args.rawstr :
                print(_flat(res),end="")
            else :
                try :
                    if _x_args.plain :
                        if _x_args.compact :
                            print(json.dumps(res))
                        else :
                            print(json.dumps(res,indent=2))
                    else :
                        if _x_args.compact :
                            print(highlight(json.dumps(res),JsonLexer(),Terminal256Formatter()))
                        else :
                            print(highlight(json.dumps(res,indent=2),JsonLexer(),Terminal256Formatter()))
                except :
                    print(str(res))

    def dotexpand(_x_sin,keydt=None) :
        chgsin = _x_sin
        _x_m = re.search(r"(\w+|\]|\))(\.\w+|\.\\\w+)+",chgsin,re.DOTALL)
        res=""
        while _x_m :
            before = chgsin[:_x_m.start()]
            end = chgsin[_x_m.end():]
            chain = _x_m.group(0)
            newchain = ""
            words = chain.split(".") 
            for i,w in enumerate(words) :
                if w.startswith("\\") or (i==len(words)-1 and end.startswith("(")) :
                    nw = w.lstrip("\\")
                    newchain += "." + nw
                else :
                    try :
                        if newchain == "" :
                            stest = w
                        else :
                            stest = newchain + "." + w
                        eval(stest)
                        newchain = stest
                        continue
                    except :
                        pass
                    nw = w.lower()
                    if nw in keydt and len(keydt[nw]) == 1 :
                        nw = list(keydt[nw])[0]
                        if _x_args.debug and w != nw :
                            print("# keyword replcement : {} -> {}".format(w,nw))
                    if newchain :
                        newchain += "['"+ nw + "']"
                    else :
                        newchain += nw
            res += before + newchain 
            chgsin = end
            _x_m = re.search(r"(\w+|\]|\))(\.\w+|\.\\\w+)+",chgsin,re.DOTALL)
        return res+chgsin

    def runcode(code,data=None) :
        _ = data
        if not code :
            return
        code = code.replace("\\n","\n")
        code = dotexpand(code,_x_key_dict)
        if _x_args.debug:
            print("# run : {}".format(code))
        attempts=0 
        err=""
        while True :
            try :
                if attempts == 0 :
                    if re.search("^\w+\s*=\S+",code) or len(code.splitlines())>1 or re.search(r"^(for|while)\s+",code) :
                        attempts += 1
                        continue
                    if _x_args.debug >= 2:
                        print("# eval : [{}]".format(code))
                    res = eval(code)
                    show_result(res)
                    return
                elif attempts == 1 :
                    if _x_args.debug >= 2:
                        print("# exec : [{}]".format(code))
                    res = exec(code)
                    return
                else :
                    print(err)
                    return
            except :
                err += traceback.format_exc()
                attempts += 1
                continue

    if _x_args.infile:
        if not os.path.isfile(_x_args.infile):
            print("# {} not exists.".format(_x_args.infile))
        with open(_x_args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()
    INPUT = INPUT.strip()
    if not INPUT :
        INPUT = json.dumps({})
    try :
       if _x_args.srctype.upper() == "JSON" :
            _ = json.loads(INPUT)
       elif _x_args.srctype.upper() == "YAML" :
            _ = yaml.safe_load(INPUT)
       elif _x_args.srctype.upper() == "XML" :
            _ = xmltodict.parse(INPUT)
       else :
        print("# unsupported file type.")
        return -1
    except :
        print("# invalid JSON/YAML/XML.")
        traceback.print_exc()
        return -1

    if _x_args.debug >= 2 :
        print("# data loaded.")
        print(json.dumps(_,indent=2))

    _x_key_dict = defaultdict(set)
    collect_keys(_,dt=_x_key_dict)
    keys_extra= "_,_t,_x,_y,_j,_l,_tbl,_l2t,_l2pt,_pt,_qx,_flat".split(",")
    _x_word_completer = WordCompleter(sorted(list(set([x for x in _x_key_dict.keys()]+keys_extra))))

    if _x_args.debug >= 2 :
        print("# keys collected :", str(_x_key_dict))
        
    if _x_args.modules :
        for m in _x_args.modules.split(",")  :
            if m :
                m.strip()
                if m.startswith("from ") :
                    exec(m)
                else :
                    exec("import " + m)

    if os.path.isfile(_x_args.code) :
        code = open(_x_args.code,"r").read()
    else :
        code = _x_args.code
    if re.match(r"^\s*\_\w+\s*$",code) :
        code = code + "(_)"

    if _x_args.code and not _x_args.func :
        if not (_x_args.interactive and _x_args.code == "_") :
            runcode(code,data=_)

    if _x_args.code and _x_args.func :
        fname = "".join([random.choice(string.ascii_letters) for _ in range(20)])
        newcode = ""
        if _x_args.modules :
            for m in _x_args.modules.split(",")  :
                if m :
                    m.strip()
                    if m.startswith("from ") :
                        newcode += m + "\n"
                    else :
                        newcode += "import " + m + "\n"
        newcode += "def {}(_) :\n".format(fname)
        code = code.replace("\\n","\n")
        for ln in code.splitlines() :
            ln = ln.rstrip()
            newcode += " "*(int(_x_args.indent)) + ln + "\n"
        code = dotexpand(newcode,_x_key_dict)
        if _x_args.debug :
            print("# code to compile :")
            print(code)
        xcode = compile(code,"<string>","exec")
        cobj = None
        for c in xcode.co_consts :
            if c and type(c) not in [str,int,tuple] :
                cobj = c
                break
        if not cobj :
            print("# no code object found.")
            sys.exit(-1)
        xfunc = FunctionType(cobj, globals())
        print(xfunc(_))

    if _x_args.interactive :
        try :
            _x_session = PromptSession(lexer=PygmentsLexer(PythonLexer), completer=_x_word_completer)
        except :
            print("[dsq]$ WARN: word completion disabled on combination of {}/{}".format(sys.platform,os.environ.get("TERM")))
            _x_session = None
        _x_dotkey = True
        _x_history = deque(maxlen=200)
        _x_cmd0=""
        _x_oldsin=""
        _x_block=False
        while True :
            _x_doeval=True
            res=""
            err=""
            try :
                if _x_session :
                    _x_sin = _x_session.prompt('[dsq]$ ')
                else :
                    _x_sin = input('[dsq]$ ')
            except KeyboardInterrupt:
                continue
            except EOFError :
                break
            if not _x_sin :
                continue
            if re.match(r"^\s*\_\w+\s*$",_x_sin) :
                _x_sin = _x_sin + "(_)"
            if _x_sin.startswith("'''")  :
                if _x_block :
                    _x_sin = _x_oldsin 
                    _x_oldsin=""
                    _x_block=False
                    _x_doeval = False
                else :
                    _x_block = True
                    continue
            if _x_block :
                if _x_oldsin :
                    _x_oldsin += "\n" + _x_sin
                else :
                    _x_oldsin += _x_sin
                continue
            lastc =[int(ord(c)) for c in _x_sin][-1]
            if lastc and lastc in [65,66,67,68] : 
                _x_sin = "\\hist"
            if _x_sin in ["quit()","\\q"] :
                break
            if _x_sin in ["dotkey"] :
                _x_dotkey = True
                continue
            if _x_sin in ["nodotkey","no dotkey"] :
                _x_dotkey = False
                continue
            mqx = re.match(r"!\s*(\S.*)",_x_sin)
            if mqx :
                res = _qx(mqx.group(1))
                show_result(res)
                continue
            if _x_sin in ["\\hist","\\history"] :
                if not _x_history :
                    print("# no history found.")
                for i,cmd in enumerate(_x_history) :
                    print("# {:3} : {}".format(i,cmd))
                continue
            _x_m1 = re.match(r"\\r (\d+)",_x_sin) 
            _x_m2 = re.match(r"\\(\d+)",_x_sin) 
            if _x_m1 or _x_m2:
                if _x_m1 :
                    ix = int(_x_m1.group(1))
                if _x_m2 :
                    ix = int(_x_m2.group(1))
                if ix < len(_x_history) :
                    _x_sin = _x_history[ix]
                else :
                    continue
            _x_cmd0 = None
            if _x_dotkey and "." in _x_sin :
                _x_cmd0 = _x_sin
                _x_sin = dotexpand(_x_sin,_x_key_dict)
            try :
                if _x_cmd0 :
                    _x_history.append(_x_cmd0)
                elif not _x_sin.startswith("\\") :
                    _x_history.append(_x_sin)
                if _x_sin.startswith("\\") :
                    res = ""
                    err = "# command not recognized."
                else :
                    runcode(_x_sin,data=_)
            except :
                traceback.print_last()
                continue
            time.sleep(0.1)
        return 0


if __name__ == "__main__" :
    main()
