from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


# Pantun


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Kosong`")
    sleep(2)
    await typew.edit("✅ `Kosong`")
    sleep(1)
    await typew.edit("☑️ `Kosong`")
    sleep(2)
    await typew.edit("✅ `Kosong`")
    sleep(1)
    await typew.edit("☑️ `Kosong`")
    sleep(2)
    await typew.edit("✅ `Kosong`")
    sleep(1)
    await typew.edit("☑️ `Kosong`")
    sleep(2)
    await typew.edit("✅ `Kosong`")
    sleep(1)
    await typew.edit("☑️ `Kosong`")
    sleep(2)
    await typew.edit("✅ `Kosong`")
    sleep(1)
    await typew.edit(
        "`Cuma Wiki Yang Paling Waras, Baik Hati, Dan Tidak Sombong 🗿`"
    )


# King Userbot Support


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@register(outgoing=True, pattern="^.alay(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Halo kak**")
    sleep(1)
    await typew.edit("**Gua liat-liat lu main bot mulu**")
    sleep(2)
    await typew.edit("**Alay banget sumpah**")
    sleep(2)
    await typew.edit("**Baru pasang ucelbot ya?**")
    sleep(2)
    await typew.edit("**Pantesan norak yahaha**")
    sleep(2)
    await typew.edit("**Kalo mau coba coba command di gc pribadi aja**")
    sleep(2)
    await typew.edit("**Jangan di publik, jijik liatnya anjg:v**")
    sleep(2)
    await typew.edit("**Intinya lo alay maen bot mulu**")
    sleep(2)
    await typew.edit("**Lawriiiiiiieeeee:v**")


# Alay maen bot mulu ngentot!


@register(outgoing=True, pattern=r"^.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@register(outgoing=True, pattern="^.perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


@register(outgoing=True, pattern="^Wiki(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih Wiki Ganteng Ye Kan😏**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Wikk Ganteng Banget🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh, Wiki Jelek Ke Pantat Panci Item😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Wiki Ke Geeran😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Wiki Jelek😁**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")


# Create by myself @localheart


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.alay`\
        \nUsage : ngeledek orang baru pasang bot\
        \n\n Cmd : `.virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `Wiki`\
        \nUsage : buat ngeledek Tonic\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
