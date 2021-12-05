# Generated by Django 3.2.8 on 2021-12-04 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('movie', '0001_initial'),
        ('cinema', '0001_initial'),
        ('item', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coupons',
            field=models.ManyToManyField(through='accounts.CouponHold', to='item.Coupon'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_actors',
            field=models.ManyToManyField(blank=True, to='movie.Actor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_directors',
            field=models.ManyToManyField(blank=True, to='movie.Director'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_distributors',
            field=models.ManyToManyField(blank=True, to='movie.Distributor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_movies',
            field=models.ManyToManyField(blank=True, to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.grade'),
        ),
        migrations.AddField(
            model_name='profile',
            name='non_coupons',
            field=models.ManyToManyField(through='accounts.NonCouponHold', to='item.NonCoupon'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noncouponhold',
            name='non_coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.noncoupon'),
        ),
        migrations.AddField(
            model_name='noncouponhold',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='mileage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='employeeevaluationbyuser',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_by_user', to='accounts.employee'),
        ),
        migrations.AddField(
            model_name='employeeevaluationbyuser',
            name='inquiry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.question'),
        ),
        migrations.AddField(
            model_name='employeeevaluationbyuser',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='employeeevaluationbyemployer',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_by_employer', to='accounts.employee'),
        ),
        migrations.AddField(
            model_name='employeeevaluationbyemployer',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='accounts.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direct_department', to='accounts.department'),
        ),
        migrations.AddField(
            model_name='couponhold',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.coupon'),
        ),
        migrations.AddField(
            model_name='couponhold',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddIndex(
            model_name='noncouponhold',
            index=models.Index(fields=['profile'], name='non_coupon_hold_profile_idx'),
        ),
        migrations.AddIndex(
            model_name='couponhold',
            index=models.Index(fields=['profile'], name='coupon_hold_profile_idx'),
        ),
    ]
