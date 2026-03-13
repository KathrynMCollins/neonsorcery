from django.db import migrations, models


NEW_ASPECT_CHOICES = [
    ("base_languages", "languages"),
    ("base_contacts", "contacts"),
    ("base_max_health", "max health"),
    ("base_max_arcana", "available mana"),
    ("base_spell_points", "available mana"),
    ("base_actions", "actions"),
    ("base_protection", "physical defense"),
    ("base_evasion", "physical defense"),
    ("base_bonus_dice", "savvy dice"),
    ("base_destiny_dice", "savvy dice"),
    ("base_rerolls", "rerolls"),
    ("base_base_stress", "base stress"),
    ("base_max_stress", "max stress"),
]


class Migration(migrations.Migration):

    dependencies = [
        ("body_modifications", "0015_alter_bodymodification_image_and_more"),
        ("rules", "0025_update_lineage_defaults_and_aspect_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bodymodificationmodifier",
            name="aspect",
            field=models.CharField(
                blank=True,
                choices=NEW_ASPECT_CHOICES,
                max_length=40,
                null=True,
                verbose_name="aspect",
            ),
        ),
    ]
