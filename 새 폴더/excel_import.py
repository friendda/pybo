import openpyxl
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()

from jumun.models import jumun_T


wb = openpyxl.load_workbook('jumun.xlsx')
sheet1 = wb['Sheet1']
rows = sheet1['A2':'K27']

##for row in rows:
##    print(row[8].value)


for row in rows:

    dict = {}
    dict['jumun_id']=row[0].value
    dict['jumun_name']=row[1].value
    dict['consumer']=row[2].value
    dict['brand']=row[3].value
    dict['prd_name']=row[4].value
    dict['option']=row[5].value
    dict['quantity']=row[6].value
    dict['d_price']=row[7].value
    dict['memo']=row[8].value
    dict['status']=row[9].value
    dict['exposure']=row[10].value

    jumun_T(**dict).save()
