from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(editable=False, max_length=255, verbose_name='token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('revoked', models.DateTimeField(blank=True, null=True, verbose_name='revoked')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refresh_token',
                                           to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Refresh token',
                'verbose_name_plural': 'Refresh tokens',
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='refreshtoken',
            unique_together={('token', 'revoked')},
        ),
    ]
