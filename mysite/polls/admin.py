from django.contrib import admin

# Register your models here.
from .models import Question , Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text' , 'pub_date' , 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question , QuestionAdmin)
admin.site.register(Choice)