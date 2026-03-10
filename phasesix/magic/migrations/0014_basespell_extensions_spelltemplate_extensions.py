from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magic", "0013_alter_spellorigin_image_alter_spelltype_image"),
        ("rules", "0024_extension_image_prompt_prefix"),
    ]

    operations = [
        migrations.AddField(
            model_name="basespell",
            name="extensions",
            field=models.ManyToManyField(blank=True, to="rules.extension"),
        ),
        migrations.AddField(
            model_name="spelltemplate",
            name="extensions",
            field=models.ManyToManyField(blank=True, to="rules.extension"),
        ),
    ]
