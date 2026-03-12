from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from transmeta import TransMeta

from armory.mixins import SearchableCardListMixin
from homebrew.models import HomebrewModel, HomebrewQuerySet
from discretion.models import DiscretionModel
from rules.models import Extension, ModifierBase, modifiers_for_qs
from rules.models import Skill, Attribute, Knowledge


class QuirkQuerySet(HomebrewQuerySet):
    def for_extensions(self, extension_qs):
        return self.filter(
            Q(extensions__id__in=extension_qs.all())
            | Q(extensions__id__in=Extension.objects.filter(is_mandatory=True))
        )


class QuirkCategory(SearchableCardListMixin, models.Model, metaclass=TransMeta):
    name = models.CharField(_("name"), max_length=30)

    class Meta:
        ordering = ("id",)
        translate = ("name",)
        verbose_name = _("quirk category")
        verbose_name_plural = _("quirk categories")

    def __str__(self):
        return self.name

    def child_item_qs(self, extension_qs=None):
        if extension_qs is not None:
            return self.quirk_set.for_extensions(extension_qs).distinct()
        return self.quirk_set.distinct()

    def as_dict(self, extension_qs=None):
        return {
            "name": self.name,
            "objects": [
                obj.as_dict() for obj in self.child_item_qs(extension_qs=extension_qs)
            ],
        }


class Quirk(HomebrewModel, DiscretionModel, metaclass=TransMeta):
    objects = QuirkQuerySet.as_manager()

    extensions = models.ManyToManyField("rules.Extension", blank=True)

    name = models.CharField(_("name"), max_length=60)
    category = models.ForeignKey(
        QuirkCategory, verbose_name=_("category"), on_delete=models.CASCADE
    )
    positive_effects = models.TextField(_("positive effects"), blank=True, null=True)
    negative_effects = models.TextField(_("negative effects"), blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    custom_trait_effect = models.ForeignKey(
        "horror.CustomTraitEffect",
        verbose_name=_("custom trait effect"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ("id",)
        translate = ("name", "description", "positive_effects", "negative_effects")
        verbose_name = _("quirk")
        verbose_name_plural = _("quirks")

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "category": self.category.name,
            "description": self.description,
            "positive_effects": self.positive_effects,
            "negative_effects": self.negative_effects,
            "modifiers": modifiers_for_qs(self.quirkmodifier_set.all()),
        }


class QuirkModifier(ModifierBase):
    quirk = models.ForeignKey(Quirk, verbose_name=_("quirk"), on_delete=models.CASCADE)


class CustomTraitEffect(models.Model):
    description = models.CharField(_("description"), max_length=200)
    xp_cost = models.IntegerField(_("xp cost"))

    class Meta:
        ordering = ("xp_cost",)
        verbose_name = _("custom trait effect")
        verbose_name_plural = _("custom trait effects")

    def __str__(self):
        sign = "+" if self.xp_cost > 0 else ""
        return f"{self.description} (XP: {sign}{self.xp_cost})"
