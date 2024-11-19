def capitalize(text):
    """Возвращает строку с первой заглавной буквой."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.capitalize()