# Generated by Django 3.2.7 on 2021-09-17 09:36

import db.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cre_user_id', models.CharField(editable=False, max_length=20, verbose_name='作成者ユーザID')),
                ('cre_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='作成プログラムID')),
                ('cre_dt', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('upd_user_id', models.CharField(editable=False, max_length=20, verbose_name='最終更新者ユーザID')),
                ('upd_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='最終更新プログラムID')),
                ('upd_dt', db.models.UpdateDateTimeField(blank=True, verbose_name='更新日時')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('last_name', models.CharField(max_length=9, verbose_name='姓')),
                ('first_name', models.CharField(max_length=9, verbose_name='名')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'ユーザ',
                'verbose_name_plural': 'ユーザ',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cre_user_id', models.CharField(editable=False, max_length=20, verbose_name='作成者ユーザID')),
                ('cre_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='作成プログラムID')),
                ('cre_dt', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('upd_user_id', models.CharField(editable=False, max_length=20, verbose_name='最終更新者ユーザID')),
                ('upd_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='最終更新プログラムID')),
                ('upd_dt', db.models.UpdateDateTimeField(blank=True, verbose_name='更新日時')),
                ('cd', models.CharField(max_length=20, verbose_name='コード')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=40, null=True, verbose_name='説明')),
            ],
            options={
                'verbose_name': 'ロール',
                'verbose_name_plural': 'ロール',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cre_user_id', models.CharField(editable=False, max_length=20, verbose_name='作成者ユーザID')),
                ('cre_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='作成プログラムID')),
                ('cre_dt', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('upd_user_id', models.CharField(editable=False, max_length=20, verbose_name='最終更新者ユーザID')),
                ('upd_pgm_id', models.CharField(editable=False, max_length=100, verbose_name='最終更新プログラムID')),
                ('upd_dt', db.models.UpdateDateTimeField(blank=True, verbose_name='更新日時')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrole_role', to='custom_auth.role', verbose_name='ロールコード')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrole_user', to=settings.AUTH_USER_MODEL, verbose_name='ユーザID')),
            ],
            options={
                'verbose_name': 'ユーザロール',
                'verbose_name_plural': 'ユーザロール',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(through='custom_auth.UserRole', to='custom_auth.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]