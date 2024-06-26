# Generated by Django 5.0.3 on 2024-05-14 11:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='users.profile')),
            ],
        ),
    ]
