from django.contrib import admin
from blog.models import Category,Blog

# Register your models here.

class FlatPageAdmin(admin.ModelAdmin):
	fieldsets = (
		(None,{
		'fields':('title','body'),
	}),
	( 'test',{
#		'classes':('collapse',),
		'description':('test',),
		'fields':('body',)
	}),
)
	

                                                                        
admin.site.register(Category)
admin.site.register(Blog,FlatPageAdmin)
