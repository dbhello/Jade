from django.contrib import admin
from djangosite.supermarket.models import Employee, Goods, Sales, Salary, Purchase, Supplyer


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'education', 'phone', 'address')
    search_fields = ('name',)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description')
    search_fields = ('name',)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('goods', 'sale_price', 'sale_quantity')
    search_fields = ('goods',)
    raw_id_fields = ('goods',)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('stock_date', 'unit', 'stock_price', 'stock_quantity')
    date_hierarchy = 'stock_date'
    ordering = ('stock_date',)


class SupplyerAdmin(admin.ModelAdmin):
    list_display = ('supplyer_name', 'supplyer_person', 'supplyer_phone', 'address')
    ordering = ('supplyer_name',)


class SalaryAdmin(admin.ModelAdmin):
    list_display = ('base_salary', 'bonus')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Supplyer, SupplyerAdmin)
admin.site.register(Salary, SalaryAdmin)