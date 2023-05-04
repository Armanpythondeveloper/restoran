from django.contrib import admin

# Register your models here.
from .models import IndexInfo,IndexSecondInfo,IncludeIndex,MenuInclude,MenuContent,Xohararner,XohararVernagir,Clients,Client_B,Book_Table

from .models import Team,ContactForm


@admin.register(IndexInfo)

class AminIndexInfo(admin.ModelAdmin):

    list_display = ['text1']
    list_display_links = ['text1']
    search_fields = ['text1']

admin.site.register(IndexSecondInfo)
admin.site.register(IncludeIndex)
admin.site.register(MenuInclude)
admin.site.register(MenuContent)
admin.site.register(Xohararner)
admin.site.register(XohararVernagir)
admin.site.register(Clients)
admin.site.register(Client_B)
admin.site.register(Book_Table)
admin.site.register(Team)
admin.site.register(ContactForm)