# Generated by Django 2.1.2 on 2018-10-24 10:41

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
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('used', models.DateTimeField(blank=True, null=True, verbose_name='Used')),
                ('invited', models.DateTimeField(blank=True, null=True, verbose_name='Invited')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='InvitationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Invitation code')),
                ('private', models.BooleanField(default=True)),
                ('max_invites', models.PositiveIntegerField(default=1, verbose_name='Max number of invitations')),
                ('num_invites', models.PositiveIntegerField(default=1, verbose_name='Remaining invitations')),
                ('invited_users', models.ManyToManyField(related_name='invitations', through='django_hunger2.Invitation', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_hunger2.InvitationCode'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='invitation',
            unique_together={('user', 'code')},
        ),
    ]
