from django.db import migrations


CUSTOM_TRAIT_EFFECTS = [
    # (description, xp_cost)  negative = spend XP (benefit), positive = gain XP (drawback)
    ("Add 1 success to a roll", -3),
    ("Add 3 more dice to a roll", -2),
    ("Remove a 1 from a roll", -2),
    ("Ignore 1 point of specific damage type", -1),
    ("Pick 2 actions to perform together for half the action cost", -1),
    ("Remove 1 success from a roll", 3),
    ("Remove 3 dice from a roll", 2),
    ("Add an extra 1 to a roll", 2),
    ("Take extra 1 point of specific damage type", 1),
    ("Pick 1 action that costs double action time", 1),
]


def add_custom_trait_data(apps, schema_editor):
    CustomTraitEffect = apps.get_model("horror", "CustomTraitEffect")
    QuirkCategory = apps.get_model("horror", "QuirkCategory")

    for description, xp_cost in CUSTOM_TRAIT_EFFECTS:
        CustomTraitEffect.objects.create(description=description, xp_cost=xp_cost)

    QuirkCategory.objects.create(
        name_de="Custom Traits",
        name_en="Custom Traits",
    )


def remove_custom_trait_data(apps, schema_editor):
    CustomTraitEffect = apps.get_model("horror", "CustomTraitEffect")
    QuirkCategory = apps.get_model("horror", "QuirkCategory")

    CustomTraitEffect.objects.filter(
        description__in=[d for d, _ in CUSTOM_TRAIT_EFFECTS]
    ).delete()
    QuirkCategory.objects.filter(name_de="Custom Traits").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("horror", "0012_customtraiteffect_quirk_custom_trait_effect"),
    ]

    operations = [
        migrations.RunPython(add_custom_trait_data, remove_custom_trait_data),
    ]
