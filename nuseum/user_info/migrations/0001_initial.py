# Generated by Django 4.1.5 on 2023-10-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_nickname', models.CharField(max_length=10, null=True, verbose_name='카드 닉네임')),
                ('user_birthday', models.CharField(max_length=10, null=True, verbose_name='사용자 생년월일')),
                ('user_gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=10, null=True, verbose_name='사용자 성별')),
                ('user_height', models.CharField(max_length=3, null=True, verbose_name='사용자 신장')),
                ('user_weight', models.CharField(max_length=3, null=True, verbose_name='사용자 몸무게')),
            ],
            options={
                'verbose_name': '사용자 정보',
                'verbose_name_plural': '사용자 정보',
                'db_table': 'USERINFO_TB',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User_Affliction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affliction', models.CharField(max_length=200, verbose_name='고민')),
                ('affliction_detail', models.CharField(default='None', max_length=200, verbose_name='고민상세')),
            ],
            options={
                'verbose_name': '사용자 고민',
                'verbose_name_plural': '사용자 고민',
                'db_table': 'USERAFFLICTION_TB',
            },
        ),
        migrations.CreateModel(
            name='User_Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.CharField(default='None', max_length=100, verbose_name='알러지')),
            ],
            options={
                'verbose_name': '알러지',
                'verbose_name_plural': '알러지',
                'db_table': 'USERALLERGY_TB',
            },
        ),
    ]
