from django.contrib import admin
from .models import flavourpaan,sweetpaan,paanaroma,specialpaan,Cart,Address,Myorder,Contact

# Register your models here.
class flavourpaanadmin(admin.ModelAdmin):
    list_display = ('name','price','description','image','offers','date','benefit')
admin.site.register(flavourpaan,flavourpaanadmin)

class sweetpaanadmin(admin.ModelAdmin):
    list_display = ('name','price','description','image','offers','date','benefit')
admin.site.register(sweetpaan,sweetpaanadmin)

class paanaromaadmin(admin.ModelAdmin):
    list_display = ('name','price','description','image','offers','date','benefit')
admin.site.register(paanaroma,paanaromaadmin)

class specialpaanadmin(admin.ModelAdmin):
    list_display = ('name','price','description','image','offers','date','benefit')
admin.site.register(specialpaan,specialpaanadmin)

class cartadmin(admin.ModelAdmin):
    list_display = ('user','name','price','quantity','date')
admin.site.register(Cart,cartadmin)

class addressadmin(admin.ModelAdmin):
    list_display = ('user','name','phone','address','address2','city','state','zip')
admin.site.register(Address,addressadmin)

class orderadmin(admin.ModelAdmin):
    list_display = ('user','address','p_id','p_name','p_price','p_image','p_quantity')
admin.site.register(Myorder,orderadmin)

class contactadmin(admin.ModelAdmin):
    list_display = ('user','name','email','phone','address','query')
admin.site.register(Contact,contactadmin)
