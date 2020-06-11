# Generated by Django 2.2.13 on 2020-06-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0014_translations_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boostrap3blockquoteplugin',
            name='reverse',
            field=models.BooleanField(blank=True, default=False, help_text='Reverses the position by adding the Bootstrap 3 "blockquote-reverse" class.', verbose_name='Reverse quote'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='img_responsive',
            field=models.BooleanField(blank=True, default=True, help_text='Adds the Bootstrap 3 ".img-responsive" class.', verbose_name='.img-responsive'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='thumbnail',
            field=models.BooleanField(blank=True, default=False, help_text='Adds the Bootstrap 3 ".img-thumbnail" class.', verbose_name='.img-thumbnail'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='use_original_image',
            field=models.BooleanField(blank=True, default=False, help_text='Outputs the raw image without cropping.', verbose_name='Use original image'),
        ),
        migrations.AlterField(
            model_name='boostrap3jumbotronplugin',
            name='grid',
            field=models.BooleanField(blank=True, default=False, help_text='Adds a ".container" element inside the "Jumbotron" for use outside of a grid.', verbose_name='Add container'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='pause',
            field=models.BooleanField(blank=True, default=True, help_text='Pauses the carousel on hover.', verbose_name='Pause'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='wrap',
            field=models.BooleanField(blank=True, default=True, help_text='Loops carousel animation.', verbose_name='Wrap'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='add_list_group_class',
            field=models.BooleanField(blank=True, default=True, help_text='Adds the list-group and subsequent list-group-item classes.', verbose_name='.list-group'),
        ),
    ]
