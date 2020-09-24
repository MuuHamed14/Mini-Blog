from django.contrib import admin
from .models import Post,Info

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','created_by','created_at']
    

admin.site.register(Post,PostAdmin)
admin.site.register(Info)

