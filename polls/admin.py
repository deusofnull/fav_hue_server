from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    # tabular inline shows these in the admin in a compressed format
    model = Choice
    extra = 3 # give some extra emtpy boxes to add choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields' : ['question_text']}),
        ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline] # include Choices in a question
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date'] # allow filter by published date
    search_fields = ['question_text'] # allow searching for question text

admin.site.register(Question, QuestionAdmin)
