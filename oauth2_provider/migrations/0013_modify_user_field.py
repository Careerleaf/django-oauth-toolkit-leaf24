from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0012_add_token_checksum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='user',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='grant',
            name='user',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='user',
            field=models.CharField(max_length=24),
        ),
    ]