from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Tag


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self) -> None:
        counter = 0
        
        for form in self.forms:
            counter += 1 if form.cleaned_data.get('is_main') else 0

        if counter == 0:
            raise ValidationError('Укажите основной раздел!')
        elif counter > 1:
            raise ValidationError('Основным может быть только один раздел!')
        
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]
