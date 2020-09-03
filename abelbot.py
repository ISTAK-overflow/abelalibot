from pyrogram import Client
import pyrogram.filters as filters

updater = Client("my_ser",1493393,"be0a41fdca754698342bc5318d82e380")
@updater.on_message(~filters.channel & (filters.regex("چرا") | filters.regex("why")))
def _yhh1(client, message):
    message.reply_text("cause I'm heartless")
    message.reply_audio("https://t.me/wawawd/2")
    message.reply_animation("https://t.me/wawawd/5")
254296310:AAEplfJhMN11ReDrWawg-a50hX8Kwq0tXzs


@updater.on_message(~filters.channel & (filters.regex("تیران") | filters.regex("تهران") |  filters.regex("tehran") | filters.regex("tiran") ))
def _yhh3(client, message):
    message.reply_text("this place is never what it seems\ntake me out la\ntake me out of la\nthis place will be the end of me\ntake me out la\ntake me out of la")
    message.reply_audio("https://t.me/wawawd/3")
    message.reply_animation("https://t.me/wawawd/4")
    


@updater.on_message(~filters.channel & filters.regex("wtf"))
def _yhh2(client, message):
    message.reply_audio("https://t.me/sametiu/150")



updater.run()
