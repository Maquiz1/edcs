# Generated by Django 3.1.7 on 2022-02-17 14:26

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edcs_appointment.managers
import edcs_sites.models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimepointLookupModelMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAppointment',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('timepoint_status', models.CharField(choices=[('new', 'New'), ('start', 'Start'), ('open', 'Open'), ('incomplete', 'Incomplete'), ('closed', 'Closed')], default='new', max_length=15)),
                ('timepoint_opened_datetime', models.DateTimeField(editable=False, help_text="the original calculated model's datetime, updated in the signal", null=True)),
                ('timepoint_closed_datetime', models.DateTimeField(editable=False, null=True)),
                ('timepoint', models.DecimalField(decimal_places=1, help_text='timepoint from schedule', max_digits=6, null=True)),
                ('timepoint_datetime', models.DateTimeField(help_text='Unadjusted datetime calculated from visit schedule', null=True)),
                ('appt_close_datetime', models.DateTimeField(help_text='timepoint_datetime adjusted according to the nearest available datetime for this facility', null=True)),
                ('facility_name', models.CharField(help_text='set by model that creates appointments, e.g. Enrollment', max_length=25)),
                ('appt_datetime', models.DateTimeField(db_index=True, verbose_name='Appointment date and time')),
                ('appt_type', models.CharField(choices=[('clinic', 'In clinic'), ('home', 'At home'), ('hospital', 'In hospital'), ('telephone', 'By telephone')], default='clinic', help_text='Default for subject may be edited Subject Configuration.', max_length=20, verbose_name='Appointment type')),
                ('appt_status', models.CharField(choices=[('start', 'Start'), ('in_progress', 'In Progress'), ('incomplete', 'Incomplete'), ('done', 'Done'), ('cancelled', 'Cancelled')], db_index=True, default='new', help_text="If the visit has already begun, only 'in progress', 'incomplete' or 'done' are valid options", max_length=25, verbose_name='Status')),
                ('appt_reason', models.CharField(choices=[('scheduled', 'Routine / Scheduled'), ('unscheduled', 'Unscheduled')], help_text="The visit report's `reason for visit` will be validated against this. Refer to the protocol's documentation for the definition of a `scheduled` visit.", max_length=25, verbose_name='Reason for appointment')),
                ('comment', models.CharField(blank=True, max_length=250, verbose_name='Comment')),
                ('is_confirmed', models.BooleanField(default=False, editable=False)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical appointment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('timepoint_status', models.CharField(choices=[('new', 'New'), ('start', 'Start'), ('open', 'Open'), ('incomplete', 'Incomplete'), ('closed', 'Closed')], default='new', max_length=15)),
                ('timepoint_opened_datetime', models.DateTimeField(editable=False, help_text="the original calculated model's datetime, updated in the signal", null=True)),
                ('timepoint_closed_datetime', models.DateTimeField(editable=False, null=True)),
                ('timepoint', models.DecimalField(decimal_places=1, help_text='timepoint from schedule', max_digits=6, null=True)),
                ('timepoint_datetime', models.DateTimeField(help_text='Unadjusted datetime calculated from visit schedule', null=True)),
                ('appt_close_datetime', models.DateTimeField(help_text='timepoint_datetime adjusted according to the nearest available datetime for this facility', null=True)),
                ('facility_name', models.CharField(help_text='set by model that creates appointments, e.g. Enrollment', max_length=25)),
                ('appt_datetime', models.DateTimeField(db_index=True, verbose_name='Appointment date and time')),
                ('appt_type', models.CharField(choices=[('clinic', 'In clinic'), ('home', 'At home'), ('hospital', 'In hospital'), ('telephone', 'By telephone')], default='clinic', help_text='Default for subject may be edited Subject Configuration.', max_length=20, verbose_name='Appointment type')),
                ('appt_status', models.CharField(choices=[('start', 'Start'), ('in_progress', 'In Progress'), ('incomplete', 'Incomplete'), ('done', 'Done'), ('cancelled', 'Cancelled')], db_index=True, default='new', help_text="If the visit has already begun, only 'in progress', 'incomplete' or 'done' are valid options", max_length=25, verbose_name='Status')),
                ('appt_reason', models.CharField(choices=[('scheduled', 'Routine / Scheduled'), ('unscheduled', 'Unscheduled')], help_text="The visit report's `reason for visit` will be validated against this. Refer to the protocol's documentation for the definition of a `scheduled` visit.", max_length=25, verbose_name='Reason for appointment')),
                ('comment', models.CharField(blank=True, max_length=250, verbose_name='Comment')),
                ('is_confirmed', models.BooleanField(default=False, editable=False)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'ordering': ('timepoint', 'visit_code_sequence'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
            managers=[
                ('on_site', edcs_sites.models.CurrentSiteManager()),
                ('objects', edcs_appointment.managers.AppointmentManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='appointment',
            index=models.Index(fields=['subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'timepoint', 'visit_code_sequence'], name='edcs_appoin_subject_1f1d31_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'timepoint', 'visit_code_sequence')},
        ),
    ]
