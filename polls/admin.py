from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice #indicates Choice objects are edited on Question admin page
    extra = 4 #provides 4 fields as default

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # OR

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline] #indicates Choice objects are edited on Question admin page

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
