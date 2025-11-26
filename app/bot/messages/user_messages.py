from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.application.dtos.house import HouseDTO

from app.application.dtos.settings import ContactInfoDTO
from app.bot.keyboards.user.main_menu import main_menu_keyboard
from app.bot.messages.base import BaseMessage


class WelcomeMessage(BaseMessage):
    _text = (
        "🌅 Представь утро в собственном доме... Кофе на террасе, птицы поют...\n\n"
        "Привет! Я помогу этому образу стать реальностью!"
        "Вместе мы подберём проект, который идеально подходит именно тебе.\n\n"
        "Готов построить мечту? 🚀"
    )
    _reply_markup = main_menu_keyboard()


class HouseCardMessage(BaseMessage):
    def __init__(
        self, house: HouseDTO, total_count: int, current_offset: int = 0
    ) -> None:
        self.house = house
        self.total_count = total_count
        self.current_offset = current_offset

    @property
    def text(self) -> str:
        return (
            f"🏠 {self.house.name}\n\n"
            f"{self.house.description}\n\n"
            "📊 *Характеристики:*\n\n"
            f"• 💰 Цена: ~ {self.house.price} ₽\n"
            f"• 📐 Общая площадь: {self.house.total_area} м²\n"
            f"• 🛋️ Жилая площадь: {self.house.living_area} м²\n"
        )

    @property
    def reply_markup(self) -> InlineKeyboardMarkup:
        pagination_buttons = []

        if self.current_offset > 0:
            pagination_buttons.append(
                InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_house")
            )

        if self.current_offset < self.total_count - 1:
            pagination_buttons.append(
                InlineKeyboardButton(text="Вперёд ➡️", callback_data="next_house")
            )

        return InlineKeyboardMarkup(inline_keyboard=[pagination_buttons])


class ContactInfoMessage(BaseMessage):
    _parse_mode = "MarkdownV2"

    def __init__(self, contact_info: ContactInfoDTO) -> None:
        self.contact_info = contact_info

    @property
    def text(self) -> str:
        return (
            "📞 Контакты Dolce Building Company\n\n"
            "📍 Адрес офиса:\n"
            f"`{self.contact_info.contact_address}`\n\n"
            "📱 Телефон:\n"
            f"`{self.contact_info.contact_phone_number}`\n\n"
            "✉️ Email:\n"
            f"`{self.contact_info.contact_email}`"
        )
