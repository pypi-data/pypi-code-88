
_d = {' ': '0',
        'ا': '1', 
        'ب': '2', 
        'پ': '3', 
        'ت': '4', 
        'ث': '5', 
        'ج': '6', 
        'چ': '7', 
        'ح': '8', 
        'خ': '9', 
        'د': '10', 
        'ذ': '11', 
        'ر': '12', 
        'ز': '13', 
        'ژ': '14', 
        'س': '15', 
        'ش': '16', 
        'ص': '17', 
        'ض': '18', 
        'ط': '19', 
        'ظ': '20', 
        'ع': '21', 
        'غ': '22', 
        'ف': '23', 
        'ق': '24', 
        'ک': '25', 
        'گ': '26', 
        'ل': '27', 
        'م': '28', 
        'ن': '29', 
        'و': '30', 
        'ه': '31', 
        'ی': '32'}

_d2 = {'0': 'J', '1': 'G', '2': 'S', '3': '5', '4': '0', '5': 'FN', '6': '4', '7': 'MN', '8': '96', '9':'1'}

def encode(s):
  try:
    s2 = 0
    h = len(s) - 1
    for i in s:
      s2 += 33 ** h *  int(_d[i])
      h -= 1
    s3 = ''
    for i in str(s2):
      s3 += _d2[i]
    return s3
  except: 
    return 'jijis'

def decode(s):
  try:
    s2 = ''
    for i in s:
      for k, v in _d2.items():
        if i == 'F':
          i = 'FN'
        if i == 'M':
          i = 'MN'
        if i == '9':
          i = '96'
        if i == v:
          s2 += k
    s2 = int(s2)
    s3 = ''
    while s2 > 0:
      for k, v in _d.items():
        if v == str(s2 % 33):
          s3 += k
      s2 = s2 // 33
    return s3
  except:
    return 'jijis'



NOTME = 'FN404FN01SFN96496FN04096FNMNMN1041G1FN150SFN4FNFN964J55JJ1MN0JGFNFNMNSS4JJ1S504J1MN05MNSJ1JFNSMN96GG0MN'

d3 = {NOTME: ['چ', 'GJ', '5J', 'ث',
              '55FN15', '5FN4G196', '5FN1SJ0', 'S96']}

print(decode(NOTME))
