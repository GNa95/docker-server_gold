# Generated by Django 3.0.5 on 2022-12-08 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityMainboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'community_mainboard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('created_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'community_reply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbEnt',
            fields=[
                ('ent_num', models.IntegerField(db_column='ENT_NUM', primary_key=True, serialize=False)),
                ('ent_nm', models.CharField(db_column='ENT_NM', max_length=50)),
                ('ent_phone', models.CharField(blank=True, db_column='ENT_PHONE', max_length=15, null=True)),
                ('ent_post_no', models.CharField(blank=True, db_column='ENT_POST_NO', max_length=10, null=True)),
                ('ent_addr', models.CharField(blank=True, db_column='ENT_ADDR', max_length=100, null=True)),
                ('map_x', models.FloatField(db_column='MAP_X')),
                ('map_y', models.FloatField(db_column='MAP_Y')),
            ],
            options={
                'db_table': 'tb_ent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbEntArea',
            fields=[
                ('ent_area_cd', models.IntegerField(db_column='ENT_AREA_CD', primary_key=True, serialize=False)),
                ('ent_area_nm', models.CharField(db_column='ENT_AREA_NM', max_length=30)),
            ],
            options={
                'db_table': 'tb_ent_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbEntType',
            fields=[
                ('ent_type_cd', models.CharField(db_column='ENT_TYPE_CD', max_length=2, primary_key=True, serialize=False)),
                ('ent_type_nm', models.CharField(db_column='ENT_TYPE_NM', max_length=12)),
            ],
            options={
                'db_table': 'tb_ent_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbGdCd',
            fields=[
                ('gd_type_cd', models.CharField(db_column='GD_TYPE_CD', max_length=10, primary_key=True, serialize=False)),
                ('gd_type_1', models.CharField(db_column='GD_TYPE_1', max_length=30)),
                ('gd_type_2', models.CharField(db_column='GD_TYPE_2', max_length=30)),
            ],
            options={
                'db_table': 'tb_gd_cd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbGds',
            fields=[
                ('gd_num', models.IntegerField(db_column='GD_NUM', primary_key=True, serialize=False)),
                ('gd_nm', models.CharField(db_column='GD_NM', max_length=100)),
                ('gd_descd', models.CharField(blank=True, db_column='GD_DESCD', max_length=100, null=True)),
                ('gd_unit', models.IntegerField(blank=True, db_column='GD_UNIT', null=True)),
                ('gd_ent_nm', models.CharField(db_column='GD_ENT_NM', max_length=30)),
            ],
            options={
                'db_table': 'tb_gds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbIrdent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irdnt_nm', models.CharField(db_column='IRDNT_NM', max_length=50)),
                ('irdnt_type', models.CharField(blank=True, db_column='IRDNT_TYPE', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tb_irdent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbRecipe',
            fields=[
                ('recipe_num', models.IntegerField(db_column='RECIPE_NUM', primary_key=True, serialize=False)),
                ('recipe_nm', models.CharField(db_column='RECIPE_NM', max_length=40)),
                ('nation_cd', models.IntegerField(blank=True, db_column='NATION_CD', null=True)),
                ('nation_nm', models.CharField(blank=True, db_column='NATION_NM', max_length=20, null=True)),
                ('type_cd', models.IntegerField(blank=True, db_column='TYPE_CD', null=True)),
                ('type_nm', models.CharField(blank=True, db_column='TYPE_NM', max_length=25, null=True)),
            ],
            options={
                'db_table': 'tb_recipe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbUnit',
            fields=[
                ('gd_unit_cd', models.CharField(db_column='GD_UNIT_CD', max_length=4, primary_key=True, serialize=False)),
                ('gd_unit_nm', models.CharField(db_column='GD_UNIT_NM', max_length=10)),
            ],
            options={
                'db_table': 'tb_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('user_id', models.CharField(max_length=50)),
                ('user_phone', models.CharField(max_length=40)),
                ('user_addr', models.CharField(max_length=40)),
                ('user_level', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'tb_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThSearch1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('recipe_nm', models.CharField(db_column='RECIPE_NM', max_length=50)),
                ('ht_date', models.DateTimeField(auto_now_add=True, db_column='HT_DATE', null=True)),
            ],
            options={
                'db_table': 'th_search1',
            },
        ),
        migrations.CreateModel(
            name='ThSearch2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irdnt_nm', models.CharField(db_column='IRDNT_NM', max_length=50)),
                ('gd_nm', models.CharField(db_column='GD_NM', max_length=100)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ThSearch1')),
            ],
            options={
                'db_table': 'th_search2',
            },
        ),
    ]
