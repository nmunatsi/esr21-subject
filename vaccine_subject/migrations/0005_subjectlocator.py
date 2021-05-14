# Generated by Django 3.2.2 on 2021-05-14 09:03

import _socket
from django.db import migrations, models
import django.db.models.deletion
import django_crypto_fields.fields.encrypted_char_field
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.phone
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('vaccine_subject', '0004_auto_20210514_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectLocator',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('date_signed', models.DateTimeField(default=edc_base.utils.get_utcnow, verbose_name='Date Locator form signed')),
                ('permission', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has the participant given his/her permission for study staff to make home visits for follow-up purposes during the study?')),
                ('physical_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Physical address with detailed description')),
                ('call_permission', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has the participant given his/her permission for study staff to call her for follow-up purposes during the study?')),
                ('participant_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('alt_participant_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternative)')),
                ('participant_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('alt_participant_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone (alternative)')),
                ('may_call_work', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='Has the participant given his/her permission for study staff to contact her at work for follow up purposes during the study?')),
                ('work_place', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name of work place')),
                ('work_location', models.CharField(blank=True, max_length=20, null=True, verbose_name='Location of work place')),
                ('work_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Work contact number')),
                ('call_any', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has the participant given permission for studystaff to contact anyone else for follow-up purposes during the study?')),
                ('full_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='include firstname and surname (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full names of contact person')),
                ('relation_to_participant', models.CharField(blank=True, max_length=35, null=True, verbose_name='Relationship to participant')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Full physical address')),
                ('cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'EligibilityCheckList',
                'verbose_name_plural': 'EligibilityCheckList',
            },
        ),
    ]
