#----//////////////////////////////////////////////////////////////////////////////----
#    [                              - Main Imports -                              ]
#----\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----


import discord
import asyncio
from datetime import datetime
from colorama import Fore
from discord.ext import commands
import colorsys
import time


#----//////////////////////////////////////////////////////////////////////////////----
#    [                             - Main Variables -                             ]
#----\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----

delay = 5
g_id = 1182589258989584434
r_id = 1194231106212462623

#----//////////////////////////////////////////////////////////////////////////////----
#    [                            - Discord Bullshit -                            ]
#----\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----


ints = discord.Intents.default()
ints.members = True
bot = commands.Bot(command_prefix='!', intents=ints)


#----//////////////////////////////////////////////////////////////////////////////----
#    [                             - Main Functions -                             ]
#----\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----



def rn(timmys_dad=1):
    now = datetime.now()
    timmy = now.strftime('%H:%M:%S')
    dick = "  "  # it's too small to be visible
    if timmys_dad == 1:
        timmys_dad = f'{Fore.MAGENTA}[{Fore.LIGHTWHITE_EX}{timmy}{Fore.MAGENTA}]{Fore.RESET} | {Fore.LIGHTBLACK_EX}({Fore.GREEN}+{Fore.LIGHTBLACK_EX}){Fore.RESET}{Fore.LIGHTWHITE_EX} | '
    else:
        timmys_dad = f'{Fore.MAGENTA}[{Fore.LIGHTWHITE_EX}{timmy}{Fore.MAGENTA}]{Fore.RESET} | {Fore.LIGHTBLACK_EX}({Fore.RED}X{Fore.LIGHTBLACK_EX}){Fore.RESET}{Fore.LIGHTRED_EX} | '
    timmys_mom = f'{timmys_dad}{dick}'
    gangbang = timmys_mom
    return gangbang




async def rrrrrrrrrrrrrrrr(gld, rid):
    r = discord.utils.get(gld.roles, id=rid)

    if not r:
        print(f"{rn(2)} Role Not Found [{rid}]")
        return

    while True:
        for h in range(0, 360, 10):
            rgb = colorsys.hsv_to_rgb(h/360, 1, 1)
            cok = discord.Color.from_rgb(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

            try:
                await r.edit(color=cok)
                print(f"{rn()} Changed Color to [{cok}]")
                time.sleep(delay)
            except discord.HTTPException as e:
                print(f"{rn(2)} {e}")


@bot.event
async def on_ready():
    print(f"{rn()} Logged in [{bot.user.id}]")
    g = bot.get_guild(g_id)
    if not g:
        print(f"{rn(2)} Guild Not Found [{g_id}]")
        return
    bot.loop.create_task(rrrrrrrrrrrrrrrr(g, r_id))




#----//////////////////////////////////////////////////////////////////////////////----
#    [                             - Run The bot -                             ]
#----\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----

bot.run(process.env.token)
