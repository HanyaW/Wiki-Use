from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sadboy(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


# Create by myself @localheart


@register(outgoing=True, pattern="^.stres(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Kosong☑️**")
    await typew.edit("**Kosong✅**")
    sleep(1)
    await typew.edit("**Kosong☑️**")
    await typew.edit("**Kosong✅**")
    sleep(2)
    await typew.edit("**Kosong☑️**")
    await typew.edit("**Kosong✅**")
    sleep(2)
    await typew.edit("**Kosong☑️**")
    await typew.edit("**Kosong✅**")
    sleep(2)
    await typew.edit("**Kosong!☑️**")
    await typew.edit("**Kosong!✅**")
    sleep(2)
    await typew.edit("**Kosong!☑️**")
    await typew.edit("**Kosong!✅**")
    sleep(3)
    await typew.edit("**Kosong✨**")


@register(outgoing=True, pattern="^.lahk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern="^.wah(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit(
        "`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`"
    )
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")


CMD_HELP.update(
    {
        "skyzubot": "`.stres`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \nUsage: misi."
    }
)
