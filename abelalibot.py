from pyrogram import Client
import pyrogram.filters as filters


do_bot=true


@updater.on_message(Filters.regex("/bot") & Filters.chat(chat_id))
def qw(client, message):
    global do_bot
    do_bot = not do_bot
    updater.send_message(
        chat_id=message.chat.id,
        text=f"Bot is {do_bot}",
        reply_to_message_id=message.message_id,
    )


updater = Client( session_name="my_ser",api_id=1493393,api_hash="be0a41fdca754698342bc5318d82e380",bot_token="1206157978:AAFZSbLYWmGKyoq-d3PobnFQtLGrEeBGItY")
@updater.on_message(~filters.channel & (filters.regex("چرا") | filters.regex("why")))
def _yhh1(client, message):
    if(do_bot):
        message.reply_text("cause I'm heartless")
        message.reply_audio("https://t.me/wawawd/2")
        message.reply_animation("https://t.me/wawawd/5")


@updater.on_message(~filters.channel & (filters.regex("تیران") | filters.regex("تهران") |  filters.regex("tehran") | filters.regex("tiran") ))
def _yhhe(client, message):
    if(do_bot):
        message.reply_text("this place is never what it seems\ntake me out la\ntake me out of la\nthis place will be the end of me\ntake me out la\ntake me out of la")
        message.reply_audio("https://t.me/wawawd/3")
        message.reply_animation("https://t.me/wawawd/4")

    


@updater.on_message(~filters.channel & filters.regex("wtf"))
def _yhhed(client, message):
    if(do_bot):
        message.reply_audio("https://t.me/sametiu/150")



@updater.on_message(~filters.channel & ((filters.regex("گفت") | filters.regex("i said"))))
def g_yhh3(client, message):
    if(do_bot):
        message.reply_text("i said ooooooh im blinded by the lights\nno i cant sleep until i feel your touch\ni said oooooooooh im downing in the night\n oh when im like this you're the one i trust hey hey hey")
        message.reply_audio("https://t.me/wawawd/8")
        message.reply_animation("https://t.me/wawawd/9")


@updater.on_message(~filters.channel & (filters.regex("مهربون") | filters.regex("عزیز") | filters.regex("بیبی")))
def _yhh6(client, message):
    if(do_bot):
        message.reply_text("oh babyyyy\n where are you now when i need you most\ni'll give it all just to hold you close\nsorry that i broke your heart your heart t t t\nand i said babyyy\n i'll treat you better than i did before \n i'll hold you down and not let you gooo\n this time i wont break your heart your heart t t t")
        message.reply_audio("https://t.me/wawawd/10")
        message.reply_animation("https://t.me/wawawd/11")


@updater.on_message(~filters.channel & filters.regex("جند"))
def _yhh7(client , message):
    if(do_bot):
        message.reply_text("never need a bitch im what a bitch need\ntryna find that one that can fix me")
        message.reply_audio("https://t.me/wawawd/12")
        message.reply_animation("https://t.me/wawawd/13")



updater.run()
