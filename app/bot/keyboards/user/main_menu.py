from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    buttons = (
        "📚 Каталог проектов",
        "📊 Расчитать стоимость",
        "💎 Завершенные проекты",
        "🏢 Контакты",
    )

    keyboard = [[KeyboardButton(text=text)] for text in buttons]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
