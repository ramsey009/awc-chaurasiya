# Generated by Django 3.2.5 on 2021-08-03 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='TeenAgeGirl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awc_center_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Awc Center Name')),
                ('girl_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Teen Age Girl Name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='SectorEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superviser_name', models.CharField(blank=True, max_length=180, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=180, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='GravidWomenInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Project Name')),
                ('awc_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Awc Name')),
                ('gravid_women_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Gravid Women Name')),
                ('husband_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Husband Name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='EditReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField(default=20, verbose_name='Serial Number')),
                ('sector_incharge_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Sector Incharge Name')),
                ('mobile_no', models.CharField(blank=True, max_length=180, null=True, verbose_name='Worker Name')),
                ('awc_center_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Awc Center name')),
                ('awc_center_code', models.IntegerField(default=20, verbose_name='Awc Center Code')),
                ('village_council', models.CharField(blank=True, max_length=180, null=True, verbose_name='Village Council')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='ChildInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children_age', models.CharField(blank=True, max_length=180, null=True, verbose_name='Children Age')),
                ('project_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Project Name')),
                ('awc_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Awc Name')),
                ('child_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Child Name')),
                ('fathers_name', models.CharField(blank=True, max_length=180, null=True, verbose_name="Father's Name")),
                ('mothers_name', models.CharField(blank=True, max_length=180, null=True, verbose_name="Mother's Name")),
                ('dob', models.DateField(blank=True, max_length=8, null=True, verbose_name='Date of Birth')),
                ('mobile_no', models.CharField(blank=True, max_length=180, null=True, verbose_name='Mobile No')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=60, null=True)),
                ('weight', models.CharField(blank=True, max_length=180, null=True, verbose_name='Weight')),
                ('height', models.CharField(blank=True, max_length=180, null=True, verbose_name='Height')),
                ('amusc', models.CharField(blank=True, max_length=180, null=True, verbose_name='Amusc')),
                ('condition', models.CharField(blank=True, choices=[('General', 'General'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=60, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='AwcEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awc_center_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Awc Center name')),
                ('awc_center_code', models.IntegerField(default=20, verbose_name='Awc Center Code')),
                ('village_council', models.CharField(blank=True, max_length=180, null=True, verbose_name='Village Council')),
                ('village', models.CharField(blank=True, max_length=180, null=True, verbose_name='Village')),
                ('worker_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Worker Name')),
                ('worker_mobile_no', models.CharField(blank=True, max_length=180, null=True, verbose_name='Worker Name')),
                ('supporter_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Worker Name')),
                ('supporter_mobile_no', models.CharField(blank=True, max_length=180, null=True, verbose_name='Worker Name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=180, unique=True)),
                ('email', models.EmailField(max_length=180, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=180)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user_roll', models.CharField(max_length=60, verbose_name='user roll')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
