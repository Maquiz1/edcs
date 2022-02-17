# Generated by Django 3.1.7 on 2022-02-17 14:26

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import django_revision.revision_field
import edcs_consent.validators
import edcs_model.fields.date_estimated
import edcs_model.models.validators.date
import edcs_protocol.validators
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
            name='SubjectConsent',
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
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('citizen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is the participant a Botswana citizen? ')),
                ('legal_marriage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="If 'No', participant may not be consented.", max_length=3, null=True, verbose_name='If not a citizen, is the participant legally married to a Botswana citizen?')),
                ('marriage_certificate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="If 'No', participant may not be consented.", max_length=3, null=True, verbose_name='[Interviewer] Has the participant produced the marriage certificate as proof? ')),
                ('marriage_certificate_no', models.CharField(blank=True, help_text='e.g. 000/YYYY', max_length=9, null=True, verbose_name='What is the marriage certificate number?')),
                ('identity', django_crypto_fields.fields.identity_field.IdentityField(help_text=' (Encryption: RSA local)', max_length=71, verbose_name='Identity number')),
                ('confirm_identity', django_crypto_fields.fields.identity_field.IdentityField(help_text='Retype the identity number (Encryption: RSA local)', max_length=71, null=True)),
                ('first_name', django_crypto_fields.fields.firstname_field.FirstnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure name consist of letters only in upper case', regex='^([A-Z]+$|[A-Z]+\\ [A-Z]+)$')])),
                ('last_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure name consist of letters only in upper case', regex='^([A-Z]+$|[A-Z]+\\ [A-Z]+)$')], verbose_name='Surname')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure initials consist of letters only in upper case, no spaces.', regex='^[A-Z]{2,3}$')])),
                ('dob', models.DateField(null=True, verbose_name='Date of birth')),
                ('is_dob_estimated', edcs_model.fields.date_estimated.IsDateEstimatedField(choices=[('-', 'No'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, null=True, verbose_name='Is date of birth estimated?')),
                ('guardian_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is a minor.<BR>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edcs_consent.validators.FullNameValidator()], verbose_name="Guardian's last and first name")),
                ('subject_type', models.CharField(max_length=25)),
                ('consent_reviewed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have reviewed the consent with the participant')),
                ('study_questions', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have answered all questions the participant had about the study')),
                ('assessment_score', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have asked the participant questions about this study and the participant has demonstrated understanding')),
                ('consent_signature', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have verified that the participant has signed the consent form')),
                ('consent_copy', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Declined', 'Yes, but subject declined copy')], help_text='If declined, return copy with the consent', max_length=20, null=True, validators=[edcs_consent.validators.eligible_if_yes_or_declined], verbose_name='I have provided the participant with a copy of their signed informed consent')),
                ('may_store_genetic_samples', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Does the participant agree that a portion of the blood sample that is taken be stored for genetic analysis?')),
                ('may_store_samples', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Does the participant agree to have samples stored after the study has ended')),
                ('is_verified', models.BooleanField(default=False, editable=False)),
                ('is_verified_datetime', models.DateTimeField(editable=False, null=True)),
                ('verified_by', models.CharField(editable=False, max_length=25, null=True)),
                ('is_incarcerated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text="( if 'Yes' STOP participant cannot be consented )", max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_no], verbose_name='Is the participant under involuntary incarceration?')),
                ('is_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'No' provide witness's name on this form and signature on the paper document.", max_length=3, verbose_name='Is the participant literate?')),
                ('witness_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edcs_consent.validators.FullNameValidator()], verbose_name="Witness's last and first name")),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('swahili', 'SWAHILI')], help_text='The language used for the consent process will also be used during data collection.', max_length=25, verbose_name='Language of consent')),
                ('consent_datetime', models.DateTimeField(validators=[edcs_protocol.validators.datetime_not_before_study_start, edcs_model.models.validators.date.datetime_not_future], verbose_name='Consent date and time')),
                ('report_datetime', models.DateTimeField(editable=False, null=True)),
                ('version', models.CharField(editable=False, help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version')),
                ('updates_versions', models.BooleanField(default=False)),
                ('sid', models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Comment')),
                ('dm_comment', models.CharField(editable=False, help_text='see also edc.data manager.', max_length=150, null=True, verbose_name='Data Management comment')),
                ('consent_identifier', models.UUIDField(default=uuid.uuid4, editable=False, help_text='A unique identifier for this consent instance')),
                ('screening_identifier', models.CharField(help_text='(readonly)', max_length=50, unique=True, verbose_name='Screening identifier')),
                ('screening_datetime', models.DateTimeField(editable=False, null=True, verbose_name='Screening datetime')),
                ('clinic_type', models.CharField(choices=[('lung_cancer', 'Lung cancer clinic/institute'), ('pathology', 'Pathology'), ('other_clinic', 'Other ward/clinic other than cancer')], max_length=45, null=True, verbose_name='From which type of clinic was the patient selected?')),
                ('patient_category', models.CharField(choices=[('lung_cancer_suspect', 'Lung cancer suspect'), ('other_cancers', 'Other cancers'), ('cancer_free', 'Cancer free')], max_length=45, null=True, verbose_name='Patient Category?')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('identity_type', models.CharField(choices=[('country_id', 'Country ID number'), ('drivers', "Driver's license"), ('passport', 'Passport'), ('hospital_no', 'Hospital number'), ('country_id_rcpt', 'Country ID receipt'), ('mobile_no', 'Mobile number'), ('OTHER', 'Other')], max_length=25, verbose_name='What type of identity number is this?')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Consent',
                'verbose_name_plural': 'Subject Consents',
                'ordering': ('created',),
                'get_latest_by': 'consent_datetime',
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edcs_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSubjectConsent',
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
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('citizen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is the participant a Botswana citizen? ')),
                ('legal_marriage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="If 'No', participant may not be consented.", max_length=3, null=True, verbose_name='If not a citizen, is the participant legally married to a Botswana citizen?')),
                ('marriage_certificate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="If 'No', participant may not be consented.", max_length=3, null=True, verbose_name='[Interviewer] Has the participant produced the marriage certificate as proof? ')),
                ('marriage_certificate_no', models.CharField(blank=True, help_text='e.g. 000/YYYY', max_length=9, null=True, verbose_name='What is the marriage certificate number?')),
                ('identity', django_crypto_fields.fields.identity_field.IdentityField(help_text=' (Encryption: RSA local)', max_length=71, verbose_name='Identity number')),
                ('confirm_identity', django_crypto_fields.fields.identity_field.IdentityField(help_text='Retype the identity number (Encryption: RSA local)', max_length=71, null=True)),
                ('first_name', django_crypto_fields.fields.firstname_field.FirstnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure name consist of letters only in upper case', regex='^([A-Z]+$|[A-Z]+\\ [A-Z]+)$')])),
                ('last_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure name consist of letters only in upper case', regex='^([A-Z]+$|[A-Z]+\\ [A-Z]+)$')], verbose_name='Surname')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure initials consist of letters only in upper case, no spaces.', regex='^[A-Z]{2,3}$')])),
                ('dob', models.DateField(null=True, verbose_name='Date of birth')),
                ('is_dob_estimated', edcs_model.fields.date_estimated.IsDateEstimatedField(choices=[('-', 'No'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, null=True, verbose_name='Is date of birth estimated?')),
                ('guardian_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is a minor.<BR>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edcs_consent.validators.FullNameValidator()], verbose_name="Guardian's last and first name")),
                ('subject_type', models.CharField(max_length=25)),
                ('consent_reviewed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have reviewed the consent with the participant')),
                ('study_questions', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have answered all questions the participant had about the study')),
                ('assessment_score', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have asked the participant questions about this study and the participant has demonstrated understanding')),
                ('consent_signature', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If no, participant is not eligible.', max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_yes], verbose_name='I have verified that the participant has signed the consent form')),
                ('consent_copy', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Declined', 'Yes, but subject declined copy')], help_text='If declined, return copy with the consent', max_length=20, null=True, validators=[edcs_consent.validators.eligible_if_yes_or_declined], verbose_name='I have provided the participant with a copy of their signed informed consent')),
                ('may_store_genetic_samples', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Does the participant agree that a portion of the blood sample that is taken be stored for genetic analysis?')),
                ('may_store_samples', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Does the participant agree to have samples stored after the study has ended')),
                ('is_verified', models.BooleanField(default=False, editable=False)),
                ('is_verified_datetime', models.DateTimeField(editable=False, null=True)),
                ('verified_by', models.CharField(editable=False, max_length=25, null=True)),
                ('is_incarcerated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text="( if 'Yes' STOP participant cannot be consented )", max_length=3, null=True, validators=[edcs_consent.validators.eligible_if_no], verbose_name='Is the participant under involuntary incarceration?')),
                ('is_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'No' provide witness's name on this form and signature on the paper document.", max_length=3, verbose_name='Is the participant literate?')),
                ('witness_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edcs_consent.validators.FullNameValidator()], verbose_name="Witness's last and first name")),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('swahili', 'SWAHILI')], help_text='The language used for the consent process will also be used during data collection.', max_length=25, verbose_name='Language of consent')),
                ('consent_datetime', models.DateTimeField(validators=[edcs_protocol.validators.datetime_not_before_study_start, edcs_model.models.validators.date.datetime_not_future], verbose_name='Consent date and time')),
                ('report_datetime', models.DateTimeField(editable=False, null=True)),
                ('version', models.CharField(editable=False, help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version')),
                ('updates_versions', models.BooleanField(default=False)),
                ('sid', models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Comment')),
                ('dm_comment', models.CharField(editable=False, help_text='see also edc.data manager.', max_length=150, null=True, verbose_name='Data Management comment')),
                ('consent_identifier', models.UUIDField(default=uuid.uuid4, editable=False, help_text='A unique identifier for this consent instance')),
                ('screening_identifier', models.CharField(db_index=True, help_text='(readonly)', max_length=50, verbose_name='Screening identifier')),
                ('screening_datetime', models.DateTimeField(editable=False, null=True, verbose_name='Screening datetime')),
                ('clinic_type', models.CharField(choices=[('lung_cancer', 'Lung cancer clinic/institute'), ('pathology', 'Pathology'), ('other_clinic', 'Other ward/clinic other than cancer')], max_length=45, null=True, verbose_name='From which type of clinic was the patient selected?')),
                ('patient_category', models.CharField(choices=[('lung_cancer_suspect', 'Lung cancer suspect'), ('other_cancers', 'Other cancers'), ('cancer_free', 'Cancer free')], max_length=45, null=True, verbose_name='Patient Category?')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('identity_type', models.CharField(choices=[('country_id', 'Country ID number'), ('drivers', "Driver's license"), ('passport', 'Passport'), ('hospital_no', 'Hospital number'), ('country_id_rcpt', 'Country ID receipt'), ('mobile_no', 'Mobile number'), ('OTHER', 'Other')], max_length=25, verbose_name='What type of identity number is this?')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Consent',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name='subjectconsent',
            index=models.Index(fields=['subject_identifier', 'first_name', 'dob', 'initials', 'version'], name='edcs_consen_subject_2b16ee_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='subjectconsent',
            unique_together={('subject_identifier', 'screening_identifier'), ('first_name', 'dob', 'initials', 'version'), ('subject_identifier', 'version')},
        ),
    ]
