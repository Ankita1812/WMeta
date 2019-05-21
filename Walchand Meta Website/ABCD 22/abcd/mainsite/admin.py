from django.contrib import admin
from .models import Article,Meeting,Member,Account
from .models import Contact,Home,About,Images,Send_Email

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Send_Email)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title','description','image')

admin.site.register(Images,GalleryAdmin)

class MeetAdmin(admin.ModelAdmin):
    list_display=('no','topic','date')
    list_filter=('no','date')
    search_fields = ('no', 'topic')
admin.site.register(Meeting,MeetAdmin)

class MemAdmin(admin.ModelAdmin):
    list_display=('name','post','phn_number','image')
    list_filter=('post','name')
    search_fields=('name','post')
admin.site.register(Member,MemAdmin)

class AcctAdmin(admin.ModelAdmin):
    list_display=('no','task','amount','total')

admin.site.register(Account,AcctAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('date','name','subject')
    list_filter=('date','subject')
    search_fields=('date','name','subject')

admin.site.register(Contact,ContactAdmin)