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
        ("rules", "0024_extension_image_prompt_prefix"),
    ]

    operations = [
        # Update Lineage defaults
        migrations.AlterField(
            model_name="lineage",
            name="base_max_health",
            field=models.IntegerField(default=8, verbose_name="max health"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_max_stress",
            field=models.IntegerField(default=8, verbose_name="max stress"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_actions",
            field=models.IntegerField(default=3, verbose_name="base actions"),
        ),
        # Remove base_minimum_roll from Lineage
        migrations.RemoveField(
            model_name="lineage",
            name="base_minimum_roll",
        ),
        # Rename verbose names in Lineage
        migrations.AlterField(
            model_name="lineage",
            name="base_max_arcana",
            field=models.IntegerField(default=0, verbose_name="available mana"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_spell_points",
            field=models.IntegerField(default=0, verbose_name="available mana"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_bonus_dice",
            field=models.IntegerField(default=0, verbose_name="base savvy dice"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_destiny_dice",
            field=models.IntegerField(default=0, verbose_name="base savvy dice"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_evasion",
            field=models.IntegerField(default=0, verbose_name="base physical defense"),
        ),
        migrations.AlterField(
            model_name="lineage",
            name="base_protection",
            field=models.IntegerField(default=0, verbose_name="base physical defense"),
        ),
        # Update TemplateModifier aspect choices
        migrations.AlterField(
            model_name="templatemodifier",
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
