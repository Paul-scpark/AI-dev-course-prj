# Generated by Django 4.1.3 on 2022-11-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_account_delete_test_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='사용자 이름')),
                ('email', models.EmailField(max_length=128, verbose_name='사용자 이메일')),
                ('password', models.CharField(max_length=300, verbose_name='비밀번호')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
                ('create_dt', models.DateField(auto_now_add=True, verbose_name='가입 날짜')),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
