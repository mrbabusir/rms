from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Category, CategoryAdmin)



class FoodAdmin(admin.ModelAdmin): 
    list_display = ('id','name', 'name','category',)
    list_filter = ('name','category',)
    search_fields = ('name',)
    list_per_page = 10
    autocomplete_fields = ('category',)
admin.site.register(Food, FoodAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number','capacity', 'is_available',)
    list_filter = ('table_number','capacity',)
    search_fields = ('table_number',)
admin.site.register(Table, TableAdmin)

class inlineOrderitems(admin.TabularInline):
    model = Orderitems
    autocomplete_fields = ('food',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total_price','food_status','payment_status',)
    list_filter = ('user','total_price','food_status','payment_status',)
    search_fields = ('user__username',)
    list_editable = ('food_status','payment_status',)
    inlines = [inlineOrderitems,]
admin.site.register(Order, OrderAdmin)

# class OrderitemsAdmin(admin.ModelAdmin):
#     list_display = ('id','food','order','quantity',)
#     list_filter = ('food','order','quantity',)
#     search_fields = ('food__name',)
# admin.site.register(Orderitems, OrderitemsAdmin)