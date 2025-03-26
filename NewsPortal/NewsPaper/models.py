from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


    def update_rating(self):
        # Суммируем рейтинги всех постов автора, умножая на 3
        post_rating = sum(post.rating for post in self.post_set.all()) * 3
        # Суммируем рейтинги всех комментариев автора
        comment_rating = sum(comment.rating for comment in Comment.objects.filter(user=self.user))
        # Суммируем рейтинги всех комментариев к постам автора
        post_comments_rating = sum(comment.rating for post in self.post_set.all() for comment in post.comment_set.all())

        # Обновляем рейтинг
        self.rating = post_rating + comment_rating + post_comments_rating
        self.save()  # Сохраняем изменения

# Модель Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Уникальное название категории

    def __str__(self):
        return self.name

# Модель Post
class Post(models.Model):
    ARTICLE = 'AR'
    NEWS = 'NW'
    POST_TYPE_CHOICES = [
        (ARTICLE, 'Article'),
        (NEWS, 'News'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания
    categories = models.ManyToManyField(Category, through='PostCategory')  # Связь с категориями
    title = models.CharField(max_length=200)  # Заголовок статьи/новости
    content = models.TextField()  # Текст статьи/новости
    rating = models.FloatField(default=0)  # Рейтинг статьи/новости

    def __str__(self):
        return self.title

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content

# Модель PostCategory
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Модель Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Связь с постом
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментария
    rating = models.FloatField(default=0)  # Рейтинг комментария

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
