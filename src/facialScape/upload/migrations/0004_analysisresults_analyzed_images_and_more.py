# Generated by Django 4.2.6 on 2023-10-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("upload", "0003_analysisresults_delete_imageupload"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysisresults",
            name="analyzed_images",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="analysisresults",
            name="total_images",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="analysisresults",
            name="zip_file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]
