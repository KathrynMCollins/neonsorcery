from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0025_replace_exploded_dice_with_mistakes"),
    ]

    operations = [
        # Remove critical hit tracking fields
        migrations.RemoveField(
            model_name="roll",
            name="crit_count",
        ),
        migrations.RemoveField(
            model_name="roll",
            name="crit_sum",
        ),
        # Remove minimum_roll field from Roll
        migrations.RemoveField(
            model_name="roll",
            name="minimum_roll",
        ),
        # Update starting_template_points default to 12
        migrations.AlterField(
            model_name="campaign",
            name="starting_template_points",
            field=models.IntegerField(
                default=12,
                verbose_name="additional starting career points",
            ),
        ),
        # Rename seed_money verbose name to "starting fortune"
        migrations.AlterField(
            model_name="campaign",
            name="seed_money",
            field=models.IntegerField(default=2000, verbose_name="starting fortune"),
        ),
    ]
