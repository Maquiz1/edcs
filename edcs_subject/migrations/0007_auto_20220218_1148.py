# Generated by Django 3.1.7 on 2022-02-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0006_auto_20220218_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallungcancertreatment',
            name='date_start_treatment',
            field=models.DateField(blank=True, max_length=45, null=True, verbose_name='Date started Treatment?'),
        ),
        migrations.AlterField(
            model_name='historicallungcancertreatment',
            name='lung_cancer_stage',
            field=models.CharField(choices=[('one', 'One (1)'), ('two', 'Two (2)'), ('three', 'Three (3)'), ('four', 'Four (4)'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='What is the stage of lung cancer?'),
        ),
        migrations.AlterField(
            model_name='historicallungcancertreatment',
            name='treatment',
            field=models.CharField(choices=[('chemotherapy', 'Chemotherapy'), ('radiation', 'Radiation'), ('surgical_resection', 'Surgical resection'), ('immunotherapy', 'Immunotherapy'), ('tyrosine_kinase_inhibitor', 'Tyrosine kinase inhibitor '), ('1_2above', '1 & 2 above'), ('OTHER', 'Others'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Type of treatment?'),
        ),
        migrations.AlterField(
            model_name='lungcancertreatment',
            name='date_start_treatment',
            field=models.DateField(blank=True, max_length=45, null=True, verbose_name='Date started Treatment?'),
        ),
        migrations.AlterField(
            model_name='lungcancertreatment',
            name='lung_cancer_stage',
            field=models.CharField(choices=[('one', 'One (1)'), ('two', 'Two (2)'), ('three', 'Three (3)'), ('four', 'Four (4)'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='What is the stage of lung cancer?'),
        ),
        migrations.AlterField(
            model_name='lungcancertreatment',
            name='treatment',
            field=models.CharField(choices=[('chemotherapy', 'Chemotherapy'), ('radiation', 'Radiation'), ('surgical_resection', 'Surgical resection'), ('immunotherapy', 'Immunotherapy'), ('tyrosine_kinase_inhibitor', 'Tyrosine kinase inhibitor '), ('1_2above', '1 & 2 above'), ('OTHER', 'Others'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Type of treatment?'),
        ),
    ]
