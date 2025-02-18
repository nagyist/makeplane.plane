# Generated by Django 4.2.7 on 2023-11-29 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('instance_name', models.CharField(max_length=255)),
                ('whitelist_emails', models.TextField(blank=True, null=True)),
                ('instance_id', models.CharField(max_length=25, unique=True)),
                ('license_key', models.CharField(blank=True, max_length=256, null=True)),
                ('api_key', models.CharField(max_length=16)),
                ('version', models.CharField(max_length=10)),
                ('last_checked_at', models.DateTimeField()),
                ('namespace', models.CharField(blank=True, max_length=50, null=True)),
                ('is_telemetry_enabled', models.BooleanField(default=True)),
                ('is_support_required', models.BooleanField(default=True)),
                ('is_setup_done', models.BooleanField(default=False)),
                ('is_signup_screen_visited', models.BooleanField(default=False)),
                ('user_count', models.PositiveBigIntegerField(default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
            ],
            options={
                'verbose_name': 'Instance',
                'verbose_name_plural': 'Instances',
                'db_table': 'instances',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='InstanceConfiguration',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField(blank=True, default=None, null=True)),
                ('category', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
            ],
            options={
                'verbose_name': 'Instance Configuration',
                'verbose_name_plural': 'Instance Configurations',
                'db_table': 'instance_configurations',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='InstanceAdmin',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('role', models.PositiveIntegerField(choices=[(20, 'Admin')], default=20)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='license.instance')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instance_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instance Admin',
                'verbose_name_plural': 'Instance Admins',
                'db_table': 'instance_admins',
                'ordering': ('-created_at',),
                'unique_together': {('instance', 'user')},
            },
        ),
    ]
