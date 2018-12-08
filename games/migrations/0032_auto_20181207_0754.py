# Generated by Django 2.0.5 on 2018-12-07 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runners', '0010_auto_20180903_2155'),
        ('games', '0031_auto_20181125_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstallerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('version', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('notes', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('installer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_versions', to='games.Installer')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runners.Runner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='gamelink',
            name='website',
            field=models.CharField(blank=True, choices=[('battlenet', 'Battle.net'), ('github', 'Github'), ('lemonamiga', 'Lemon Amiga'), ('mobygames', 'MobyGames'), ('origin', 'Origin'), ('pcgamingwiki', 'PCGamingWiki'), ('ubisoft', 'Ubisoft'), ('wikipedia', 'Wikipedia'), ('winehq', 'WineHQ AppDB')], max_length=32),
        ),
    ]