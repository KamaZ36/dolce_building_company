from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.bot.messages.base import BaseMessage


class GetNumberFloorsMessage(BaseMessage):
    _text = "Сколько этажей планируете в доме?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1", callback_data="bid:floors:1"),
                InlineKeyboardButton(text="2", callback_data="bid:floors:2"),
            ],
            [
                InlineKeyboardButton(text="3", callback_data="bid:floors:3"),
            ],
        ]
    )


class GetBuildingPlaceMessage(BaseMessage):
    _text = "Уже выбрали где хотите построить дом?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да, есть участок", callback_data="bid:place:True"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Нет, еще выбираем", callback_data="bid:place:False"
                )
            ],
        ]
    )


class GetMortgageMessage(BaseMessage):
    _text = "Рассматриваете ипотеку?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да, планирую ипотеку", callback_data="bid:mortgage:True"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Нет, не планирую ипотеку", callback_data="bid:mortgage:False"
                )
            ],
        ]
    )


class GetHouseAreaMessage(BaseMessage):
    _text = "Какую общую площадь дома планируете?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📐 До 80 м²", callback_data="bid:area:80"),
                InlineKeyboardButton(
                    text="📐 80-110 м²", callback_data="bid:area:80-110"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📐 110-160 м²", callback_data="bid:area:110-160"
                ),
                InlineKeyboardButton(text="📐 160+ м²", callback_data="bid:area:160"),
            ],
        ]
    )


class GetIsReadyProjectMessage(BaseMessage):
    _text = "У вас есть готовый проект?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Есть готовый проект", callback_data="bid:project:True"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Интересует индивидуальный проект",
                    callback_data="bid:project:False",
                )
            ],
        ]
    )


class GetBudgetMessage(BaseMessage):
    _text = "Какой бюджет планируете на строительство?"

    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 6 - 8 млн", callback_data="bid:budget:6-8"
                ),
                InlineKeyboardButton(
                    text="💰 8 - 10 млн", callback_data="bid:budget:8-10"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💰 10 - 12 млн", callback_data="bid:budget:10-12"
                ),
                InlineKeyboardButton(text="💰 12+ млн", callback_data="bid:budget:12+"),
            ],
        ]
    )


class GetPhoneNumberUserMessage(BaseMessage):
    _text = "Введите ваш номер телефона: "
