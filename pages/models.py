from django.db import models

class StaticPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Слаг (для URL)")
    content = models.TextField(verbose_name="Содержимое")

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"

    def __str__(self):
        return self.title

