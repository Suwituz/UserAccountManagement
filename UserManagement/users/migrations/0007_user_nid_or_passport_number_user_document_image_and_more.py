# Generated by Django 4.1.7 on 2023-05-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='NID_or_passport_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='document_image',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('UNVERIFIED', 'Unverified'), ('PENDING_VERIFICATION', 'Pending_verification'), ('VERIFIED', 'Verified')], default='UNVERIFIED', max_length=100),
        ),
    ]
