from django.contrib import admin
from nature.models import *
# Register your models here.


class AllPostAdmin(admin.ModelAdmin):
    readonly_fields = ("views",)
    list_filter = ("title", "destrict", "category")
    search_fields = ("title",)
    list_display = ("title", "destrict", "category")
    list_editable = ("destrict", "category")


admin.site.register(Carusel)
admin.site.register(latest_news)
admin.site.register(HomePageMon)
admin.site.register(HomePageGallery)
admin.site.register(HomePageTop)
admin.site.register(HomePageVideo)
admin.site.register(GalleryPageGallery)
admin.site.register(AllPost, AllPostAdmin)
