from django.db import models

# Create your models here.

##class jumun_T(models.Model):
##    jumun_date = models.DateTimeField(blank = True, null = True)
##    jumun_id = models.CharField(max_length=30)
##    jumun_name = models.CharField(max_length=30)
##    consumer = models.CharField(max_length=30)
##    brand = models.CharField(max_length=30)
##    prd_name = models.CharField(max_length=50)
##    option = models.CharField(max_length=150)
##    quantity = models.SmallIntegerField(verbose_name="수량")
##    d_price = models.IntegerField(verbose_name = "도매가격")
##    memo = models.TextField(blank = True)
##    status = models.CharField(max_length=30, blank = True)
##    exposure = models.CharField(max_length=10, default = "O")
##
##    def __str__(self):
##        return self.id
        

class jumun_T(models.Model):
    eng_flag = models.CharField(verbose_name = "영문",max_length=10,blank =True, null = True )
    jumun_date = models.CharField(verbose_name = "주문일",max_length=30, blank =True, null = True)
    jumun_id = models.CharField(verbose_name = "주문ID",max_length=30, blank =True, null = True)
    jumun_name = models.CharField(verbose_name = "주문자",max_length=30, blank =True, null = True)
    jumun_con = models.CharField(verbose_name = "위탁자",max_length=30, blank =True, null = True)
    brand = models.CharField(verbose_name = "브랜드",max_length=30, blank =True, null = True)
    prd_name = models.TextField(verbose_name = "상품명", blank =True, null = True)
    prd_color = models.TextField(verbose_name = "색상", blank =True, null = True)
    quantity = models.SmallIntegerField(verbose_name="수량", blank = True, null = True)
    wholesale = models.CharField(verbose_name = "중도매", max_length=30, blank =True, null = True)
    whole_pr = models.CharField(verbose_name = "도매가", max_length=30, blank =True, null = True)
    note = models.TextField(verbose_name = "비고", blank =True, null = True)
    sup_pr = models.CharField(verbose_name = "공급가",max_length=30, blank =True, null = True)
    name = models.CharField(verbose_name = "이름",max_length=30, blank =True, null = True)
    phone = models.CharField(verbose_name = "전화번호",max_length=30, blank =True, null = True)
    address = models.TextField(verbose_name = "주소", blank =True, null = True)
    jumun_id2 =models.CharField(verbose_name = "ID",max_length=30, blank =True, null = True)
    date2 = models.CharField(verbose_name = "나온날짜",max_length=30, blank =True, null = True)
    

#파일업로드 test모
##class Document(models.Model):
##    title = models.CharField(max_length=200)
##    uploadedFile = models.FileField(upload_to="result/")
##    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    
