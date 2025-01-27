# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="• Versi •", callback_data="about"),
                InlineKeyboardButton(text="• Tutup •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• Versi •", callback_data="about"),
                InlineKeyboardButton(text="• Tutup •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• Versi •", callback_data="about"),
                InlineKeyboardButton(text="• Tutup •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 3", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• Versi •", callback_data="about"),
                InlineKeyboardButton(text="• Tutup •", callback_data="close"),
            ],
        ]
        return buttons

    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="• Versi •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="Join Asupan 1", url=client.invitelink),
                InlineKeyboardButton(text="Join Asupan 2", url=client.invitelink2),
                InlineKeyboardButton(text="Join Asupan 3", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="• Tutup •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 1", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return button
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Join Asupan 1", url=client.invitelink),
                InlineKeyboardButton(text="Join Asupan 2", url=client.invitelink2),
                InlineKeyboardButton(text="Join Asupan 3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
