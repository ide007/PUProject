from django.db import models


class MainTable(models.Model):
    class Distinction(models.TextChoices):
        yes = 'ОТЛЧ',
        no = '---'

    code_region_fbdp = models.IntegerField(
        verbose_name="Код региона-района ФБДП",
        blank=True,
        help_text="Код региона-района ФБДП",
        max_length=5,
    )
    code_region_last_change_ils = models.IntegerField(
        verbose_name="Код региона-района последнего изменения ИЛС",
        blank=True,
        help_text="Код региона-района последнего изменения ИЛС",
        max_length=5,
        default=0
    )
    region_code_entry_info_about_death = models.IntegerField(
        verbose_name="Код региона внесения сведений о смерти",
        help_text="Код региона внесения сведений о смерти",
        max_length=5,
        default=0
    )
    ils_update_region_code = models.IntegerField(
        verbose_name="Код региона актуализации ИЛС",
        help_text="Код региона актуализации ИЛС",
        max_length=5,
        default=0
    )
    snils = models.CharField(
        verbose_name="СНИЛС",
        help_text="СНИЛС",
        max_length=14,
        unique=True,
        blank=True,
    )
    new_snils = models.CharField(
        verbose_name="Новый СНИЛС (в случае УПРЗ)",
        help_text="Новый СНИЛС (в случае УПРЗ)",
        max_length=14,
        null=True,
    )
    identifier_fbdp = models.CharField(
        verbose_name="Идентификатор ФБДП",
        help_text="Идентификатор ФБДП",
        max_length=30,
        unique=True,
        blank=True,
    )
    surname_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия фамилии",
        help_text="Признак отличия фамилии",
    )
    surname_spu = models.CharField(
        verbose_name="Фамилия СПУ",
        help_text="Фамилия СПУ",
        max_length=60,
        blank=True,
    )
    surname_fbdp = models.CharField(
        verbose_name="Фамилия ФБДП",
        help_text="Фамилия ФБДП",
        max_length=60,
        blank=True,
    )
    name_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия имени",
        help_text="Признак отличия имени",
    )
    name_spu = models.CharField(
        verbose_name="Имя СПУ",
        help_text="Имя СПУ",
        max_length=20,
        blank=True,
    )
    name_fbdp = models.CharField(
        verbose_name="Имя ФБДП",
        help_text="Имя ФБДП",
        max_length=20,
        blank=True,
    )
    patronymic_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия отчества",
        help_text="Признак отличия отчества",
    )
    patronymic_spu = models.CharField(
        verbose_name="Отчество СПУ",
        help_text="Отчество СПУ",
        max_length=20,
        null=True,
    )
    patronymic_fbdp = models.CharField(
        verbose_name="Отчество ФБДП",
        help_text="Отчество ФБДП",
        max_length=20,
        null=True,
    )
    gender_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Пол признак отличия",
        help_text="Пол признак отличия",
    )
    gender_spu = models.CharField(
        verbose_name="Пол СПУ",
        help_text="Пол СПУ",
        max_length=1,
        blank=True,
    )
    gender_fbdp = models.CharField(
        verbose_name="Пол ФБДП",
        help_text="Пол ФБДП",
        max_length=1,
        blank=True,
    )
    date_of_birth_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия даты рождения",
        help_text="Признак отличия даты рождения",
    )
    date_of_birth_spu = models.DateField(
        verbose_name="Date of Birth"
    )

    def __str__(self):
        return self.snils
