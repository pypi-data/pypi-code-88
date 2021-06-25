import re

def formatcc(text_to_search):
    ccmatches = re.search(r'(3|4|5|6|7)\d{11,18}\D',text_to_search)
    if ccmatches is not None:
            cc = ccmatches[0]
            cc = re.search(r'(3|4|5|6|7)\d{11,18}',cc)
            cc = cc[0]
            cc_end = ccmatches.span()[1]
            #print(ccmatches.span(0))
            text_to_search = text_to_search[cc_end-1:]
            if cc[0] == '3':
                pattern = re.compile(r'\D\d{4}(\D|$)')
            else:
                pattern = re.compile(r'\D\d{3}(\D|$)')
            cvv = pattern.search(text_to_search)
            if cvv is not None:
                cvv = cvv[0]
                if cc[0] == '3':
                    cvv = re.search(r'\d{4}',cvv)
                    cvv = cvv[0]
                else:
                    cvv = re.search(r'\d{4}',cvv)
                    cvv = cvv[0]
                yy = re.search(r'\D(2|202)[1-9]',text_to_search)
                if yy is not None:
                    yy = yy[0]
                    yy = re.search(r'(2|202)[1-9]',yy)
                    yy = yy[0]
                    mm = re.search(r'\W[0-1][0-9]\W',text_to_search)
                    if mm is not None:
                        mm = re.search('\d\d',mm[0])
                        mm = mm[0]
                    else:
                        return "Invalid Expiry Month."
                else:
                    return "Invalid Expiry Year."
                
            else:
                return "Invalid CVV."
            return f"{cc}|{mm}|{yy}|{cvv}"

    else:
        return "Invalid CC Number."


