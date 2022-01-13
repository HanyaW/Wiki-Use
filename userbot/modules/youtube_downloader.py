# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Geez - Projects


from youtube_dl import YoutubeDL

from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd


@flicks_cmd(pattern="yt(a|v|sa|sv) (.*)")
async def download_from_youtube_(event):
    opt = event.pattern_match.group(1).lower()
    if opt == "a":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("Give me a (youtube) URL to download audio from!")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("`Give A Direct Audio Link To Download`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "v":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("Give me a (youtube) URL to download video from!")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("`Give A Direct Video Link To Download`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "sa":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("Give me a (youtube) search query to download audio from!"
                                    )
        xx = await event.edit("`Searching on YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("`Downloading audio song...`")
    elif opt == "sv":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("Give me a (youtube) search query to download video from!"
                                    )
        xx = await event.edit("`Searching YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("`Downloading video song...`")
    else:
        return
    await download_yt(xx, event, url, ytd)


CMD_HELP.update({
    "ytdownload":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}yta` <(youtube) link>\
   \nUsage : Unduh audio dari tautan.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ytv <(youtube) link>`\
   \nUsage : Unduh video dari tautan.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ytsa <(youtube) kueri penelusuran>`\
   \nUsage : Cari dan unduh audio dari youtube.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ytsv <(youtube) search query>`\
   \nUsage : Cari dan unduh video dari youtube."
})
