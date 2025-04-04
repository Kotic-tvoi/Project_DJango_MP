from django.db import models

from price.constants import MAX_LENGTH_TITLE

# Добавить после подключения партнёров.
# User = get_user_model()


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=MAX_LENGTH_TITLE)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(PublishedModel):
    # Продумать ограничения на поля и проверку ввода
    # Неудобно отображается поле ввода числа.
    article = models.CharField('Общий артикул', max_length=MAX_LENGTH_TITLE)
    article_wb = models.PositiveIntegerField('Aртикул WB')
    article_ozon = models.PositiveIntegerField('Артикул OZON')
    name = models.TextField('Название товара')
    # Автозаполнение для загрузки из Excel
    pub_date = models.DateTimeField(
        'Дата и время выхода продукта',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    # После показать просчёт всех цен с учётом скидок
    price = models.DecimalField(max_digits=6, decimal_places=0)


    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article',
        verbose_name='Категория',
    )


    # Добавить после добавления партнёров.
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='posts',
    #     verbose_name='Автор публикации',
    # )


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        # Продумать порядок публикации товаров.
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name
