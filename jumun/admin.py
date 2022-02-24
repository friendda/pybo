from django.contrib import admin
from .models import jumun_T
## Register your models here.


class JumunAdmin(admin.ModelAdmin):
    list_display =('eng_flag','jumun_date','jumun_id','jumun_name','jumun_con','brand', 'prd_name','prd_color','quantity','wholesale','whole_pr','note','sup_pr','name','phone','address','jumun_id2','date2',)
admin.site.register(jumun_T, JumunAdmin)
