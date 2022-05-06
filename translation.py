from django.utils.translation import ugettext_lazy as _

from modeltranslation.translator import register, TranslationOptions

from . import models

# Transaltions


@register(models.Division)
class DivisionTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(models.District)
class DistrictTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(models.CityArea)
class CityAreaTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(models.Upazila)
class UpazilaTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(models.Union)
class UnionTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
