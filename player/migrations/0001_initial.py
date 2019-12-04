# Generated by Django 2.2.7 on 2019-12-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Photo', models.CharField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('Overall', models.IntegerField()),
                ('Potential', models.IntegerField()),
                ('Club', models.CharField(max_length=100)),
                ('Value', models.CharField(max_length=100)),
                ('Wage', models.CharField(max_length=100)),
                ('PreferredFoot', models.CharField(max_length=100)),
                ('InternationalReputation', models.IntegerField()),
                ('WeakFoot', models.IntegerField()),
                ('SkillMoves', models.IntegerField()),
                ('Position', models.CharField(max_length=100)),
                ('JerseyNumber', models.IntegerField()),
                ('Height', models.CharField(max_length=100)),
                ('Weight', models.CharField(max_length=100)),
                ('Crossing', models.IntegerField()),
                ('Finishing', models.IntegerField()),
                ('HeadingAccuracy', models.IntegerField()),
                ('ShortPassing', models.IntegerField()),
                ('Volleys', models.IntegerField()),
                ('Dribbling', models.IntegerField()),
                ('Curve', models.IntegerField()),
                ('FKAccuracy', models.IntegerField()),
                ('LongPassing', models.IntegerField()),
                ('BallControl', models.IntegerField()),
                ('Acceleration', models.IntegerField()),
                ('SprintSpeed', models.IntegerField()),
                ('Agility', models.IntegerField()),
                ('Reactions', models.IntegerField()),
                ('Balance', models.IntegerField()),
                ('ShotPower', models.IntegerField()),
                ('Jumping', models.IntegerField()),
                ('Stamina', models.IntegerField()),
                ('Strength', models.IntegerField()),
                ('LongShots', models.IntegerField()),
                ('Aggression', models.IntegerField()),
                ('Interceptions', models.IntegerField()),
                ('Positioning', models.IntegerField()),
                ('Vision', models.IntegerField()),
                ('Penalties', models.IntegerField()),
                ('Composure', models.IntegerField()),
                ('Marking', models.IntegerField()),
                ('StandingTackle', models.IntegerField()),
                ('SlidingTackle', models.IntegerField()),
                ('GKDiving', models.IntegerField()),
                ('GKkicking', models.IntegerField()),
                ('GKPositioning', models.IntegerField()),
                ('GKReflexes', models.IntegerField()),
            ],
        ),
    ]