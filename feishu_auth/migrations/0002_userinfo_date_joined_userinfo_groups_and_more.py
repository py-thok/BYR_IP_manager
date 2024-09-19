# Generated by Django 5.1.1 on 2024-09-16 06:40

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("feishu_auth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userinfo",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="password",
            field=models.CharField(default=1, max_length=128, verbose_name="password"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userinfo",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="open_id",
            field=models.CharField(max_length=255, unique=True, verbose_name="应用ID"),
        ),
    ]
