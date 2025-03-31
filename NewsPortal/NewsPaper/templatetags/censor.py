import re
from django import template

register = template.Library()


@register.filter
def censor(text):
    if not isinstance(text, str):
        raise ValueError("Фильтр 'censor' может применяться только к строкам.")

    bad_words = ['редиска']  # Замените на свои нежелательные слова
    for word in bad_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        replacement = '*' * len(word)
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    return text
