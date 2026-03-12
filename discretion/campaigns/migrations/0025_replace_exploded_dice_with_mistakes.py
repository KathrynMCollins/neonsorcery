from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0024_alter_campaign_backdrop_image_alter_campaign_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="roll",
            name="exploded_dice_count",
        ),
        migrations.RemoveField(
            model_name="roll",
            name="exploded_dice_sum",
        ),
        migrations.AddField(
            model_name="roll",
            name="mistakes_count",
            field=models.IntegerField(default=0, verbose_name="mistakes count"),
        ),
        migrations.AddField(
            model_name="roll",
            name="complete_fumble",
            field=models.BooleanField(default=False, verbose_name="complete fumble"),
        ),
    ]
