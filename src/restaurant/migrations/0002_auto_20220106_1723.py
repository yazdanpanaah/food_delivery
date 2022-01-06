# Generated by Django 3.2.9 on 2022-01-06 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220106_1723'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('food_menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='foodmenu_id', to='restaurant.foodmenu')),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='food',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='food_id',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AddField(
            model_name='food',
            name='meal_id',
            field=models.ManyToManyField(related_name='meal_id', to='restaurant.Meal'),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal',
            field=models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], default='dinner', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='adress_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adress_id', to='accounts.adress'),
        ),
        migrations.AlterField(
            model_name='department',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_id', to='restaurant.category'),
        ),
        migrations.AlterField(
            model_name='department',
            name='manager_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='maneger', to='accounts.manager'),
        ),
        migrations.AlterField(
            model_name='food',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_id2', to='restaurant.category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_id', to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Food_Menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='restaurant.order'),
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='Food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='foodid', to='restaurant.food'),
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Department', to='restaurant.department'),
        ),
        migrations.AddField(
            model_name='department',
            name='food_id',
            field=models.ManyToManyField(related_name='foodmenu_id', through='restaurant.FoodMenu', to='restaurant.Food'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(related_name='orederitem_id', through='restaurant.OrderItem', to='restaurant.FoodMenu'),
        ),
    ]
