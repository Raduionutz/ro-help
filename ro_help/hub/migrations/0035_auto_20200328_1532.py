# Generated by Django 3.0.4 on 2020-03-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0034_auto_20200326_0201"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="resourcetag",
            options={"ordering": ("name",), "verbose_name": "Resource tag", "verbose_name_plural": "Resource tags"},
        ),
        migrations.AlterField(
            model_name="registerngorequest",
            name="avatar",
            field=models.ImageField(
                help_text="Image should be 500x500px", max_length=300, upload_to="", verbose_name="Avatar"
            ),
        ),
        migrations.AlterField(
            model_name="registerngorequest",
            name="resource_types",
            field=models.TextField(
                help_text="The types of resources you anticipate you will need.",
                max_length=500,
                verbose_name="Resource tags",
            ),
        ),
    ]
