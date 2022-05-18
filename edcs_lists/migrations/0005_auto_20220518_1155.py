# Generated by Django 3.1.7 on 2022-05-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_lists', '0004_auto_20220506_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='HIVSubtype',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'HIV Subtype',
                'verbose_name_plural': 'HIV Subtype',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='SomaticMutations',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Somatic Mutations',
                'verbose_name_plural': 'Somatic Mutations',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.AddIndex(
            model_name='somaticmutations',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_27e1bb_idx'),
        ),
        migrations.AddIndex(
            model_name='hivsubtype',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_110cb6_idx'),
        ),
    ]
