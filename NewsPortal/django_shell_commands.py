# Команды Django

from django.contrib.auth.models import User
from NewsPaper.models import Author, Category, Post, Comment

# 1. Создание пользователей
user1 = User.objects.create_user('user1', password='password1')
user2 = User.objects.create_user('user2', password='password2')

# 2. Создание авторов
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# 3. Добавление категорий
category1 = Category.objects.create(name='Категория 1')
category2 = Category.objects.create(name='Категория 2')
category3 = Category.objects.create(name='Категория 3')
category4 = Category.objects.create(name='Категория 4')

# 4. Добавление статей и новостей
post1 = Post.objects.create(title='Статья 1', content='Содержимое статьи 1', author=author1)
post2 = Post.objects.create(title='Статья 2', content='Содержимое статьи 2', author=author2)

# Присвоение категорий
post1.categories.add(category1, category2)  # Статья 1 имеет 2 категории
post2.categories.add(category3)

# 5. Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий к статье 1')
comment2 = Comment.objects.create(post=post1, user=user2, text='Еще один комментарий к статье 1')
comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий к статье 2')
comment4 = Comment.objects.create(post=post2, user=user2, text='Другой комментарий к статье 2')

# 6. Применение лайков и дислайков
post1.like()  # Предполагается, что метод like() реализован в модели Post
post1.dislike()  # Предполагается, что метод dislike() реализован в модели Post
comment1.like()  # Аналогично для комментариев

# 7. Обновление рейтингов пользователей
user1.refresh_from_db()
user2.refresh_from_db()

# 8. Вывод имени пользователя и рейтинга лучшего пользователя
best_user = User.objects.order_by('-rating').first()  # Предполагается, что поле rating существует
print(f'Лучший пользователь: {best_user.username}, Рейтинг: {best_user.rating}')

# 9. Вывод информации о лучшей статье
best_post = Post.objects.order_by('-likes').first()  # Предполагается, что поле likes существует
print(f'Дата добавления: {best_post.created_at}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating}, Заголовок: {best_post.title}, Превью: {best_post.content[:100]}')

# 10. Вывод всех комментариев к лучшей статье
comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(f'Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}')
