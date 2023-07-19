from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        
    ]
    second = [
        
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            
           
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
       
    ]
    return buttons
