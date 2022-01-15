from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.alfatihah(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**SURAT ALFATIHAH**")
    sleep(1)
    await typew.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await typew.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**māliki yaumid-dīn**")
    sleep(1)
    await typew.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await typew.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await typew.edit(
        "**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**"
    )
    sleep(1)
    await typew.edit("**Amin..**")


# Create by myself @localheart

@register(outgoing=True, pattern="^.ayatkursi(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**AYAT KURSI**")
    sleep(2)
    await typew.edit("**allāhu lā ilāha illā huw**")
    sleep(2)
    await typew.edit("**al-ḥayyul-qayyụm**")
    sleep(2)
    await typew.edit("**lā ta`khużuhụ sinatuw wa lā na`ụm**")
    sleep(2)
    await typew.edit("**lahụ mā fis-samāwāti wa mā fil-arḍ**")
    sleep(2)
    await typew.edit("**man żallażī yasyfa'u 'indahū illā bi`iżnih**")
    sleep(2)
    await typew.edit("**ya'lamu mā baina aidīhim wa mā khalfahum**")
    sleep(2)
    await typew.edit("**wa lā yuḥīṭụna bisyai`im min 'ilmihī illā bimā syā`**")
    sleep(2)
    await typew.edit("**wasi'a kursiyyuhus-samāwāti wal-arḍ**")
    sleep(2)
    await typew.edit("**wa lā ya`ụduhụ ḥifẓuhumā**")
    sleep(2)
    await typew.edit("**wa huwal-'aliyyul-'aẓīm**")


# Create by myself @localheart

CMD_HELP.update(
    {
        "surat": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.alfatihah`\
    \n↳ : Surat Alfatihah."
    }
)
