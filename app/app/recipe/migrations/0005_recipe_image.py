# Generated by Django 2.1.3 on 2020-08-26 15:49

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to=recipe.models.recipe_image_file_path),
        ),
    ]