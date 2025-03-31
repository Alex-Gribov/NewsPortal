from django import template

register = template.Library()

@register.filter
def censor(value):
    # Список нежелательных слов
    bad_words = ['Редиска', 'арбуз']
    for word in bad_words:
        value = value.replace(word, '*' * len(word))  # Заменяем слово на символы '*'
    return value
