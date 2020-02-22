from django.contrib import admin

# Register your models here.
from .models import Question , Choice
admin.site.site_header="Pollster Admin"
admin.site.site_title="Pollster Admin Area"
admin.site.index_title="Welcome to Pollster Admin"
#admin.site.register(Question)
#admin.site.register(Choice)
# we want the choices in the question admin screen so we will use a tabular inline

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[('Hrithik' ,{'fields' : ['question_text']}),
     ('Date Information' , { 'fields' : ['pub_date'] , 
     'classes':['collapse']}) , ]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)