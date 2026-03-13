from django.db import migrations, models


def seed_base_attributes(apps, schema_editor):
    Attribute = apps.get_model("rules", "Attribute")

    attributes = [
        {
            "identifier": "FIT",
            "kind": "phy",
            "name_de": "Fitness",
            "name_en": "Fitness",
            "description_de": "",
            "description_en": "",
        },
        {
            "identifier": "COR",
            "kind": "phy",
            "name_de": "Koordination",
            "name_en": "Coordination",
            "description_de": "",
            "description_en": "",
        },
        {
            "identifier": "WIT",
            "kind": "men",
            "name_de": "Geist",
            "name_en": "Wit",
            "description_de": "",
            "description_en": "",
        },
        {
            "identifier": "LOG",
            "kind": "men",
            "name_de": "Logik",
            "name_en": "Logic",
            "description_de": "",
            "description_en": "",
        },
    ]

    for attr in attributes:
        Attribute.objects.get_or_create(
            identifier=attr["identifier"],
            defaults=attr,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("rules", "0025_update_lineage_defaults_and_aspect_choices"),
    ]

    operations = [
        # Update kind choices: replace per/phy with phy/men
        migrations.AlterField(
            model_name="attribute",
            name="kind",
            field=models.CharField(
                choices=[("phy", "physical"), ("men", "mental")],
                max_length=3,
                verbose_name="kind",
            ),
        ),
        # Seed the four base attributes
        migrations.RunPython(seed_base_attributes, migrations.RunPython.noop),
    ]
