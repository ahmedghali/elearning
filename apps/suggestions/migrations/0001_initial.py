# Generated by Django 5.2.2 on 2025-06-11 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='العنوان')),
                ('description', models.TextField(verbose_name='الوصف')),
                ('suggestion_type', models.CharField(choices=[('general', 'التدريب العام'), ('custom', 'تدريب مخصص حسب الطلب'), ('private', 'التدريب الفردي')], max_length=20, verbose_name='نوع الاقتراح')),
                ('target_audience', models.CharField(blank=True, max_length=50, verbose_name='الجمهور المستهدف')),
                ('estimated_duration', models.PositiveIntegerField(blank=True, help_text='المدة المقدرة بالساعات', null=True, verbose_name='المدة المقدَّرة')),
                ('max_participants', models.PositiveIntegerField(blank=True, null=True, verbose_name='الحد الأقصى للمشاركين')),
                ('budget_range', models.CharField(blank=True, max_length=100, verbose_name='نطاق الميزانية')),
                ('status', models.CharField(choices=[('pending', 'قيد الإنتظار'), ('reviewing', 'قيد المراجعة'), ('approved', 'تمت الموافقة'), ('rejected', 'مرفوض')], default='pending', max_length=20, verbose_name='الحالة')),
                ('admin_notes', models.TextField(blank=True, verbose_name='ملاحظات المشرف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تم إنشاؤها في')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions_user', to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
            options={
                'verbose_name_plural': 'اقتراح دورة تدريبية',
            },
        ),
    ]
