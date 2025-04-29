def star_border(func):
    def wrapper(message):
        result = func(message)
        border = "*" * (len(message) + 6)
        return f"{border}\n* {result} *\n{border}"
    return wrapper

def emoji(func):
    def wrapper(message):
        result = func(message)
        return f"@ {result} @"
    return wrapper
@star_border
@emoji
def format_message(message):
    return message