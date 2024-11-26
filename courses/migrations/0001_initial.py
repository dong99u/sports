# Generated by Django 5.1.3 on 2024-11-26 04:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        ("centers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="강좌 제목")),
                ("description", models.TextField(verbose_name="강좌 설명")),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="수강료",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="courses/images/%Y/%m/%d/",
                        verbose_name="강좌 이미지",
                    ),
                ),
                (
                    "course_link",
                    models.URLField(
                        help_text="강좌 상세 정보를 볼 수 있는 링크를 입력하세요",
                        verbose_name="강좌 홈페이지 링크",
                    ),
                ),
                ("start_time", models.TimeField(verbose_name="강의 시작 시간")),
                ("end_time", models.TimeField(verbose_name="강의 종료 시간")),
                ("start_date", models.DateField(verbose_name="강의 시작일")),
                ("end_date", models.DateField(verbose_name="강의 종료일")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RECRUITING", "모집중"),
                            ("CLOSED", "마감"),
                            ("COMPLETED", "종료"),
                        ],
                        default="RECRUITING",
                        max_length=20,
                        verbose_name="운영상태",
                    ),
                ),
                (
                    "current_enrollment",
                    models.PositiveIntegerField(
                        default=0, verbose_name="현재 등록 인원"
                    ),
                ),
                (
                    "capacity",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="정원",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="categories.category",
                        verbose_name="카테고리",
                    ),
                ),
                (
                    "sports_center",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="centers.sportscenter",
                        verbose_name="SPORTS CENTER",
                    ),
                ),
            ],
            options={
                "verbose_name": "강좌",
                "verbose_name_plural": "강좌 목록",
                "db_table": "course",
                "ordering": ["-created_at"],
            },
        ),
    ]
