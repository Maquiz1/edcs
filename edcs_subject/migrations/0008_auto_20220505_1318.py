# Generated by Django 3.1.7 on 2022-05-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0007_auto_20220505_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookingfuel',
            name='smoke_from_neighbor',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=45, verbose_name='Does smoke from your neighbors cooking  or burnings enter your house?'),
        ),
        migrations.AlterField(
            model_name='historicalcookingfuel',
            name='smoke_from_neighbor',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=45, verbose_name='Does smoke from your neighbors cooking  or burnings enter your house?'),
        ),
    ]
