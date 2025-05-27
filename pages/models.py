from django.db import models
from django.utils import timezone

class Category(models.Model):
  name = models.CharField("Название", max_length=150)

  def __str__(self):
    return self.name

class Article(models.Model):
  is_on_feed = models.BooleanField("Отображать на главной странице?", default=False)
  title = models.CharField("Заголовок", max_length=300)
  created_at = models.DateField(default=timezone.now)
  short_title = models.CharField("Короткий заголовок", max_length=150)
  description = models.TextField("Полное описание", max_length=12000)
  short_description = models.TextField("Краткое описание", max_length=1200)  # исправлена опечатка
  image = models.ImageField("Изображение", upload_to='article_images/')

  def __str__(self):
    return self.title
    
class Contact(models.Model):
  email = models.CharField("Электронная почта", max_length=100)
  phone = models.CharField("Телефон", max_length=100)
  address = models.CharField("Адрес", max_length=100)
  vk_link = models.CharField("Ссылка на VK", max_length=100)

  def __str__(self):
    return f"{self.email} / {self.phone}"

class MainPage(models.Model):
  hero_title = models.CharField("Заголовок на баннере", max_length=100)
  hero_link = models.CharField("Ссылка с баннера", max_length=100)

  joining_step_1_title = models.CharField("Шаг 1 — заголовок", max_length=100)
  joining_step_1_description = models.CharField("Шаг 1 — описание", max_length=100)

  joining_step_2_title = models.CharField("Шаг 2 — заголовок", max_length=100)
  joining_step_2_description = models.CharField("Шаг 2 — описание", max_length=100)

  joining_step_3_title = models.CharField("Шаг 3 — заголовок", max_length=100)
  joining_step_3_description = models.CharField("Шаг 3 — описание", max_length=100)

  joining_step_4_title = models.CharField("Шаг 4 — заголовок", max_length=100)
  joining_step_4_description = models.CharField("Шаг 4 — описание", max_length=100)

  right_image = models.ImageField("Изображение справа", upload_to="main_page/right_image")

  def __str__(self):
    return "Главная страница"