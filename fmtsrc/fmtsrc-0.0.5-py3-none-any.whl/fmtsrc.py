import sys,io,platform
import unicodedata,re
import urllib.request
def main():
    args=sys.argv
    unicodeform=None
    getOS=_check_os
    string=None
    valType='string'
    encoding=None
    linesep=None
    exportTo=None
    exportEncoding=None
    if type(args) is str:
        args=[args]
    for arg in args:
        argl = arg.lower()
        if argl.startswith('os='):
            oss=_trim(arg[3:])
        elif argl.startswith('url='):
            string=_trim(arg[4:])
            valType='URL'
        elif argl.startswith('file='):
            string=_trim(arg[5:])
            valType='File'
        elif argl.startswith('encoding='):
            encoding=_trim(arg[9:])
        elif argl.startswith('unicodeform='):
            unicodeform=_trim(arg[12:])
        elif argl.startswith('linesep='):
            linesep=_trim(arg[8:])
        elif argl.startswith('export='):
            exportTo=_trim(arg[7:])
        elif argl.startswith('e_encoding='):
            exportTo=_trim(arg[11:])
    ## URLまたはfileを入力した場合は接続先から文章を取得
    if valType == 'URL':
        string = _URL2TEXT(string,encoding)
    elif valType == 'File':
        string = _FILE2TEXT(string,encoding)
    else:
        string = None
    if string == None:
        print('Input Source.')
        sys.exit()
    ## 改行文字を設定
    if linesep == None:
        if getOS == 'Windows':
            linesep = '\r\n'
        else:
            linesep = '\n'
    string = re.sub(r'\r\n|\r|\n', linesep, string)
    # MacのデフォルトUnicodeはNFD、それ以外はNFC
    if unicodeform == None:
        if getOS == 'Mac':
            unicodeform = 'NFD'
        else:
            unicodeform = 'NFC'
    # UnicodeForm名称が正しいかチェック
    _check_unicodeform_name(unicodeform)
    #入力した文字列をNFC/NFDに変換
    string=unicodedata.normalize(unicodeform, string)
    if exportTo == None:
        print(string)
    else:
        # 出力エンコーディングが指定されていなければ入力と同じ
        if exportEncoding == None:
            exportEncoding = encoding
        _export(exportTo,string,encoding)
def _URL2TEXT(url,encoding):
    fp = urllib.request.urlopen(url)
    if encoding == None:
        text=fp.read().decode('utf-8')
    else:
        text = fp.read().decode(encoding)
    fp.close()
    return text
def _FILE2TEXT(path,encoding):
    if encoding == None:
        encoding = 'UTF-8'
    with open(path, encoding=encoding) as f:
        text = f.read()
    return text
def _check_unicodeform_name(unicodeform):
    if unicodeform == 'NFC':
        return True
    elif unicodeform =='NFD':
        return True
    elif unicodeform == 'NFKC':
        return True
    elif unicodeform == 'NFKD':
        return True
    else:
        print('Unicode Form Type is invalid(',unicodeform,')')
        sys.exit()
def _export(path,string,encoding):
    with open(path, mode='w') as f:
        f.write(string)
def _trim(string):
    if len(string) == 0:
        return ''
    elif string[0] == '\'' or string[0] == '\"':
        return string[1:-1]
    else :
        return string
def _check_os():
    pf = platform.system()
    if pf == 'Windows':
        return pf
    elif pf == 'Darwin':
        return 'Mac'
    elif pf == 'Linux':
        return pf
main()
