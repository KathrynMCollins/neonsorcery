from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("horror", "0009_quirk_created_at_quirk_modified_at"),
        ("rules", "0024_extension_image_prompt_prefix"),
    ]

    operations = [
        migrations.AddField(
            model_name="quirk",
            name="extensions",
            field=models.ManyToManyField(blank=True, to="rules.extension"),
        ),
    ]
