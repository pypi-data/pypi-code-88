# from pytone import kintone, kintone_file
import kintone
import kintone_file
kintone = kintone.Kintone(authText='bV90c3VydXlhQHplbmsuY28uanA6MjcxOG1pc3V0QQ==', domain='develfhvn', app=10)
kintone_file = kintone_file.KintoneFile(authText='bV90c3VydXlhQHplbmsuY28uanA6MjcxOG1pc3V0QQ==', domain='develfhvn')

fileKey = ''
with open("C:\\Users\\TsuruyaMasashi\\Pictures\\Saved Pictures\\276989.png", mode='rb') as f:
    response = kintone_file.uploadFile(f)
    fileKey  = response['fileKey']

# record = [
#     {
#         'company_code': '15172',
#         'company_logo': [fileKey]
#     },
# ]

new_record = [{
    'updateKey': {
        'field': 'company_code',
        'value': '15170'
    },
    'company_logo': [fileKey]
}]

kintone.update(new_record)


# where = '$id < 101 '
# field = ['$id']
# order = 'order by $id desc'
# print((kintone.select(where=where, fields=field, order=order)))
