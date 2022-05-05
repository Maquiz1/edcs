# Generated by Django 3.1.7 on 2022-05-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0009_auto_20220505_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaloccupationalhistory',
            name='industries_worked',
            field=models.CharField(choices=[('textile_industry', 'Textile industry'), ('chemical_production_industry', 'Chemical production industry'), ('food_processing_industry', 'Food processing industry'), ('drug_industry', 'Drug industry'), ('milling_industry', 'Milling industry'), ('construction_industry', 'Construction industry'), ('gas_fuel_stations', 'Gas / fuel stations'), ('cement_industry', 'Cement industry'), ('N/A', 'Not applicable'), ('OTHER', 'Other')], default='N/A', max_length=45, verbose_name='If yes, what kind of industry did you work?'),
        ),
        migrations.AlterField(
            model_name='occupationalhistory',
            name='industries_worked',
            field=models.CharField(choices=[('textile_industry', 'Textile industry'), ('chemical_production_industry', 'Chemical production industry'), ('food_processing_industry', 'Food processing industry'), ('drug_industry', 'Drug industry'), ('milling_industry', 'Milling industry'), ('construction_industry', 'Construction industry'), ('gas_fuel_stations', 'Gas / fuel stations'), ('cement_industry', 'Cement industry'), ('N/A', 'Not applicable'), ('OTHER', 'Other')], default='N/A', max_length=45, verbose_name='If yes, what kind of industry did you work?'),
        ),
    ]
