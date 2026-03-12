from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("horror", "0011_add_trait_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomTraitEffect",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="description"),
                ),
                ("xp_cost", models.IntegerField(verbose_name="xp cost")),
            ],
            options={
                "verbose_name": "custom trait effect",
                "verbose_name_plural": "custom trait effects",
                "ordering": ("xp_cost",),
            },
        ),
        migrations.AddField(
            model_name="quirk",
            name="custom_trait_effect",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="horror.customtraiteffect",
                verbose_name="custom trait effect",
            ),
        ),
    ]
