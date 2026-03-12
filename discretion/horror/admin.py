from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from horror.models import CustomTraitEffect, QuirkModifier, Quirk, QuirkCategory
from portal.admin import ShortDescriptionListFilter


class QuirkModifierInline(TabularInline):
    model = QuirkModifier


@admin.register(Quirk)
class QuirkAdmin(ModelAdmin):
    inlines = [QuirkModifierInline]
    list_display = ("name_de", "name_en", "category", "custom_trait_effect")
    list_filter = (
        ShortDescriptionListFilter,
        "category",
    )
    fields = (
        "name_de",
        "name_en",
        "category",
        "custom_trait_effect",
        "description_de",
        "description_en",
        "positive_effects_de",
        "positive_effects_en",
        "negative_effects_de",
        "negative_effects_en",
        "extensions",
    )


admin.site.register(QuirkCategory, ModelAdmin)
admin.site.register(CustomTraitEffect, ModelAdmin)
