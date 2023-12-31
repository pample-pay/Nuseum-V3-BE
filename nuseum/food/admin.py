from django.contrib import admin
from .models import Food_List, Nutro_Name,Food_Market, Product_List, User_Food_List
from user_info.models import User_Allergy, User_Affliction

class FoodList(admin.ModelAdmin):
    list_display = (
        'food_category',
        'food_name',
        'food_info',
        'allergy_info',
        'display_afflictions',
        'nutro_name1',
        'nutro_contents1',
        'nutro_name2',
        'nutro_contents2',
        'nutro_name3',
        'nutro_contents3',
        'nutro_name4',
        'nutro_contents4',
        'nutro_name5',
        'nutro_contents5',
    )
    def display_afflictions(self, obj):
        return ', '.join([str(affliction) for affliction in obj.affliction_info.all()])
    display_afflictions.short_description = '고민'  # 필드 이름
    
    search_fields = ('food_category','food_name','food_info','allergy_info','display_afflictions','nutro_name1',
        'nutro_contents1','nutro_name2','nutro_contents2', 'nutro_name3','nutro_contents3', 'nutro_name4','nutro_contents4', 'nutro_name5','nutro_contents5',)

class NutroName(admin.ModelAdmin):
    list_display = (
        'nutro_name',
    )
    search_fields = ('nutro_name',)

class MarketName(admin.ModelAdmin):
    list_display = (
        'market_name',
    )
    search_fields = ('market_name',)

class ProductList(admin.ModelAdmin):
    list_display =(
        'product_name',
        'product_url',
        'market_id',
        'display_foodid',
    )
    def display_foodid(self, obj):
        return ', '.join([str(foodid) for foodid in obj.food_id.all()])
    display_foodid.short_description = '식품명'  # 필드 이름

    search_fields = ('product_name','product_url','market_id','display_foodid')

class UserFoodList(admin.ModelAdmin):
    list_display = (
        'user_id_c',
        'food_category',
        'list_rank',
        'user_food_list',
    )
    search_fields = ('user_id_c','food_category','list_rank','user_food_list')


admin.site.register(Nutro_Name, NutroName)
admin.site.register(Food_Market, MarketName)
admin.site.register(Product_List, ProductList)
admin.site.register(Food_List, FoodList)
admin.site.register(User_Food_List, UserFoodList)

# class FoodList(admin.ModelAdmin):
#     list_display = (
#         'food_category',
#         'food_name',
#         'food_info',
#         'allergy_info',
#         'display_afflictions',
#         'display_nutro',        
#     )
    
#     def display_afflictions(self, obj):
#         return ', '.join([str(affliction) for affliction in obj.affliction_info.all()])
#     display_afflictions.short_description = '사용자 고민'  # 필드 이름
    
#     def display_nutro(self, obj):
#         nutro_info = [f'{content.nutro.nutro_name}: {content.contents}' for content in obj.nutro_info.all()]
#         return ', '.join(nutro_info)
#     display_nutro.short_description = '영양성분 정보'  # 필드 이름

#     search_fields = ('food_category','food_name','food_info','allergy_info','display_afflictions', 'display_nutro',)
