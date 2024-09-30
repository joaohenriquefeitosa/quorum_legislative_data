# Generated by Django 4.1.5 on 2024-09-27 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='votes.bill')),
            ],
        ),
        migrations.CreateModel(
            name='VoteResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_results', to='votes.person')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_results', to='votes.vote')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='primary_sponsor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sponsored_bills', to='votes.person'),
        ),
    ]
