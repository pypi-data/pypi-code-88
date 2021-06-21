chiffres = ['','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
nombres = ['','dix','vingt','trente','quarante','cinquante','soixante','soixante','quatre-vingt','quatre-vingt']

def unite(x):
    if len(str(x))==3:
        x = str(x)
    elif len(str(x))==2:
        x= '0'+str(x)
    elif len(str(x)) ==1:
        x = '00'+str(x)

    if int(x[-2:])<20:
        dizaines = chiffres[int(x[-2:])]
    elif int(x[-2:]) in [21,31,41,51,61]:
        dizaines = nombres[int(x[-2])]+' et un'
    elif int(x[-2:]) == 71:
        dizaines = 'soixante et onze'
    elif int(x[-2]) in [7,9]:
        dizaines = nombres[int(x[-2])]+'-'+chiffres[int(x[-1])+10]
    elif int(x[-1])==0:
        dizaines = nombres[int(x[-2])]
    else:
        dizaines = nombres[int(x[-2])]+'-'+chiffres[int(x[-1])]

    if x[0] == '0':
        return dizaines
    else:
        if x[0] == '1':
            centaines = 'cent'
        elif x[0] =='0':
            centaines = ''
        else:
            centaines = chiffres[int(x[0])]+' cent'
        if dizaines!='':
            centaines+=' '
        return centaines+dizaines

def nombre2lettres(x):
    y=x.replace(u'\xa0', u'')

    if len(y)<=3:
        total = unite(y)
    else:
        sp=''
        if unite(y[-3:]) != '':
            sp= ' '
        if len(y) == 4  and x[-4] == '1':
            total = 'mille'+sp+unite(y[-3:])
        elif len(y) <= 6 :
            total = unite(y[-6:-3])+' mille'+sp+unite(y[-3:])
        elif len(y) == 7 and y[-7] == '1' and y[-6:-3] != '000':
            total = 'un million '+unite(y[-6:-3])+' mille'+sp+unite(y[-3:])
        elif len(y) == 7 and y[-7] == '1':
            total = 'un million'+sp+unite(y[-3:])
        elif len(y) <=9 and y[-6:-3] =='000':
            total= unite(y[-9:-6])+' millions'+sp+unite(y[-3])
        elif len(y) <= 9:
            total = unite(y[-9:-6])+' millions '+unite(y[-6:-3])+' mille'+sp+unite(y[-3:])

    if total[-4:] in ['cent','ingt'] and len(total)>5 and str(x)[-2:]!='20':
        total += 's'
    return total

def conv(x):
    x=round(float(x),2)
    x=str(x)
    e,c = x.split('.')[0],x.split('.')[1]
    if len(c)==1:
        c=c+'0'
    if int(c)==0:
        c=''
    elif int(c)==1:
        c='un centime'
    else:
        c=nombre2lettres(c)+' centimes'
    if int(e)==0:
        if c=='':
            return 'zéro euro'
        else:
            return c
    elif int(e)==1:
        e='un euro'
    elif len(e)>6 and e[-6:]=='000000':
        e=nombre2lettres(e)+" d'euros"
    else:
        e=nombre2lettres(e)+' euros'
    if c=='':
        return e
    else:
        return e+' et '+c

if __name__ == '__main__':
	result=conv(str(input('Saisissez la somme en chiffres  :')))
	print(result)
