from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields' : ['que_text'] }),
    ('Date Information', {'fields' : ['pub_date'], 'classes' : '[collapse]' }),
    ]
    inlines = [ChoiceInline]
    list_display = ('que_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)



# admin.site.register(Question)
# admin.site.register(Choice)

# class ChoiceInline(admin.StackedInline):

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date','que_text']
