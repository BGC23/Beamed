class SELFBOT():
    __linecount__ = 2228
    __version__ = 2.0

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging, time, requests
import textwrap, ctypes


from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
from textwrap import wrap


ctypes.windll.kernel32.SetConsoleTitleW(f'[Beamed Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')
ip_key = config.get('ip_key')



start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"

    print(f'''{Fore.RESET}

                            ██████╗░███████╗░█████╗░███╗░░░███╗███████╗██████╗░
                            ██╔══██╗██╔════╝██╔══██╗████╗░████║██╔════╝██╔══██╗
                            ██████╦╝█████╗░░███████║██╔████╔██║█████╗░░██║░░██║
                            ██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
                            ██████╦╝███████╗██║░░██║██║░╚═╝░██║███████╗██████╔╝
                            ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░


                           {Fore.CYAN}Beamed {SELFBOT.__version__} | {Fore.BLUE}Logged in as: {Fore.RED}{Beamed.user.name}#{Fore.WHITE}{Beamed.user.discriminator} {Fore.CYAN}| ID: {Fore.RED}{Beamed.user.id}
                           {Fore.CYAN}Number of servers: | {Fore.BLUE}{len(Beamed.guilds)}
                           {Fore.CYAN}Privnote Sniper | {Fore.BLUE}{privnote}
                           {Fore.CYAN}Nitro Sniper | {Fore.BLUE}{nitro}
                           {Fore.CYAN}Giveaway Sniper | {Fore.BLUE}{giveaway}
                           {Fore.CYAN}SlotBot Sniper | {Fore.BLUE}{slotbot}
                           {Fore.CYAN}Prefix: {Fore.BLUE}{config.get("prefix")}
                           {Fore.CYAN}Commands: {Fore.BLUE}{len(Beamed.commands)}
                           {Fore.CYAN}Creator: {Fore.RED}geo#3000
                           {Fore.GREEN}Merry Christmas :)
    '''+Fore.RESET)


def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Beamed.run(token, bot=False, reconnect=True)
            os.system(f'title (Beamed Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

if token == config.get('token'):
    try:
            print(f'''{Fore.RESET}




                        {Fore.RED}██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
                        {Fore.RED}██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
                        {Fore.RED}██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░
                        {Fore.RED}██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗
                        {Fore.RED}███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝
                        {Fore.RED}╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░


            '''+Fore.RESET)
            time.sleep(1)
            os.system('cls')
            print(f'''{Fore.RESET}




                        {Fore.GREEN}██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░░░░
                        {Fore.GREEN}██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░░░░
                        {Fore.GREEN}██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░░░░
                        {Fore.GREEN}██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗░░░
                        {Fore.GREEN}███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝██╗
                        {Fore.GREEN}╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝


            '''+Fore.RESET)
            time.sleep(1)
            os.system('cls')

            print(f'''{Fore.RESET}




                        {Fore.RED}██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░░░░░░░
                        {Fore.RED}██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░░░░░░░
                        {Fore.RED}██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░░░░░░░
                        {Fore.RED}██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗░░░░░░
                        {Fore.RED}███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝██╗██╗
                        {Fore.RED}╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝



            '''+Fore.RESET)
            time.sleep(1)
            os.system('cls')
            print(f'''{Fore.RESET}




                        {Fore.GREEN}██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░░░░░░░░░░
                        {Fore.GREEN}██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░░░░░░░░░░
                        {Fore.GREEN}██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░░░░░░░░░░
                        {Fore.GREEN}██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗░░░░░░░░░
                        {Fore.GREEN}███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝██╗██╗██╗
                        {Fore.GREEN}╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝╚═╝



            '''+Fore.RESET)


    except Exception as e:
        raise

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def randInv():
    inv = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f'https://discord.gg/{inv}'

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Beamed = discord.Client()
Beamed = commands.Bot(
    description='Beamed Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Beamed.remove_command('help')



def clearScreen():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"

    print(f'''{Fore.RESET}

                            ██████╗░███████╗░█████╗░███╗░░░███╗███████╗██████╗░
                            ██╔══██╗██╔════╝██╔══██╗████╗░████║██╔════╝██╔══██╗
                            ██████╦╝█████╗░░███████║██╔████╔██║█████╗░░██║░░██║
                            ██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
                            ██████╦╝███████╗██║░░██║██║░╚═╝░██║███████╗██████╔╝
                            ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░


                           {Fore.CYAN}Beamed {SELFBOT.__version__} | {Fore.BLUE}Logged in as: {Fore.RED}{Beamed.user.name}#{Fore.WHITE}{Beamed.user.discriminator} {Fore.CYAN}| ID: {Fore.RED}{Beamed.user.id}
                           {Fore.CYAN}Number of servers: | {Fore.BLUE}{len(Beamed.guilds)}
                           {Fore.CYAN}Privnote Sniper | {Fore.BLUE}{privnote}
                           {Fore.CYAN}Nitro Sniper | {Fore.BLUE}{nitro}
                           {Fore.CYAN}Giveaway Sniper | {Fore.BLUE}{giveaway}
                           {Fore.CYAN}SlotBot Sniper | {Fore.BLUE}{slotbot}
                           {Fore.CYAN}Prefix: {Fore.BLUE}{config.get("prefix")}
                           {Fore.CYAN}Commands: {Fore.BLUE}{len(Beamed.commands)}
                           {Fore.CYAN}Creator: {Fore.RED}geo#3000
                           {Fore.GREEN}Merry Christmas :)
    '''+Fore.RESET)

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD",
        url="https://www.twitch.tv/beamedgeo",
    )
    await Beamed.change_presence(activity=btc_stream)

@tasks.loop(seconds=3)
async def xmr_status():
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR,CAD,GBP')
    r = r.json()
    gbp = r['GBP']
    await asyncio.sleep(3)
    xmr_stream = discord.Streaming(
        name=f'XMR is at £{str(gbp)}',
        url="https://www.twitch.tv/beamedgeo",
    )
    await Beamed.change_presence(activity=xmr_stream)

@Beamed.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Beamed.event
async def on_message_edit(before, after):
    await Beamed.process_commands(after)

Beamed.currGuild = {}
Beamed.currMember = {}

Beamed.dc = False

@Beamed.event
async def on_voice_state_update(member: discord.Member, before, after, ):
    if Beamed.dc == True:
        guild = Beamed.get_guild(Beamed.currGuild)
        member = guild.get_member(Beamed.currMember)
        if before.channel is None and after.channel is not None:
            await member.edit(voice_channel=None)



@Beamed.event
async def on_message(message):



    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if  message.content.startswith('Someone just dropped'):
        if slotbot_sniper == True:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in str(message.content):
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Beamed.user.id}>' in str(message.content):
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in str(message.content):
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Beamed.process_commands(message)

snipe_message_content = []
snipe_message_author = []
snipe_message_id = []

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@Beamed.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None



@Beamed.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"

    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Beamed Selfbot v{SELFBOT.__version__}] | Logged in as {Beamed.user.name}#{Beamed.user.discriminator}')

@Beamed.command()
async def pingtest(ctx, *, pingInnit):
    await ctx.message.delete()
    os.system(f'ping {pingInnit} -n 5')
    await asyncio.sleep(10)
    os.system('cls')
    clearScreen()


@Beamed.command()
async def scrobble(ctx, * ,message):
    await ctx.message.delete()
    print(f'Now scrobbling {message}')
    simpVar = 1
    while simpVar == 1:
        swagvariable = str(message)
        await ctx.send(f'.sb {message}')
        await asyncio.sleep(30)


@Beamed.command(aliases=['upspeed', 'downspeed', 'wifispeed'], pass_context=True, invoke_without_command=True)
async def speedTest(ctx):
    await ctx/message.delete()
    wifi = speedtest.Speedtest()
    await ctx.send(f'Download speed is {wifi.download}')
    await ctx.send(f'Upload speed is {wifi.upload}')


@Beamed.command()
async def sosa(ctx):
    await ctx.message.delete()
    s = 'Fuckers in school telling me, always in the barber shop, Chief Keef aint bout this, Chief aint bout that, My boy a BD on fucking Lamron and them, He, he, they say that nigga dont be putting in no work, Shut the fuck up, yall niggas aint know shit, All yall motherfuckers talkin about, Chief Keef aint no hitter, Chief Keef aint this, Chief Keef a fake, Shut the fuck up, yall dont live with that nigga, Yall know that nigga got caught with a ratchet, Shootin at the police and shit, Nigga been on probation since fuckin I dont know when, Motherfucker, stop fuckin playin him like that, Them niggas savages out there, If I catch another motherfucker talking sweet about Chief Keef, Im fucking beatin they ass, Im not fucking playin no more, Know them niggas roll with Lil Reese and them, (Young Chop on the beat), Love Sosa, bitches love Sosa, huh?, Let them know then, Raris and Rovers (huh), Ayy, lil Cobra, ayy, ayy, Bang, bang-bang, God, yall some broke boys, God, yall some broke boys, These bitches love Sosa, O end or no end, Fuckin with them O boys, you gon get fucked over, Raris and Rovers, these hoes love Chief Sosa, Hit him with that Cobra, now that boy slumped over, They do it all for Sosa, you boys aint making no noise, Yall know Im a grown boy, your clique full of broke boys, God, yall some broke boys, God, yall some broke boys, We GBE dope boys, we got lots of dough, boy, These bitches love Sosa and they love them Glo Boys, Know we from the Go boy, but we cannot go, boy, No, I dont know old boy, I know hes a broke boy, Raris and Rovers, convertible Lambos, boy, You know I got bands, boy, and its in my pants, boy, Disrespect them O boys, you wont speak again, boy, Dont think that Im playin, boy, no, we dont use hands, boy, No, we dont do friends, boy, collect bands, Im a landlord, I gets lots of commas, I can fuck your mama, I aint with the drama, you can meet my llama, Ridin with 3hunna, with 300 foreigns, These bitches see Chief Sosa, I swear to God, they honored, These bitches love Sosa, O end or no end, Fuckin with them O boys, you gon get fucked over, Raris and Rovers, these hoes love Chief Sosa, Hit him with that Cobra, now that boy slumped over, They do it all for Sosa, you boys aint making no noise, Yall know Im a grown boy, your clique full of broke boys, God, yall some broke boys, God, yall some broke boys, We GBE dope boys, we got lots of dough, boy, Dont make me call D. Rose, boy, he six double-O, boy, And he keep that pole, boy, you gon get fucked over, Bitch, I did sell soda and I done sell coca, She gon clap for Sosa, he gon clap for Sosa, They do it for Sosa, them hoes, they so off of Sosa, Tadoe off that molly water, so nigga be cool like water, Fore you get hit with this lava, bitch, Im the trending topic, Dont care no price, Ill cop it, B, and your bitch steady jockin me, These bitches love Sosa, O end or no end, Fuckin with them O boys, you gon get fucked over, Raris and Rovers, these hoes love Chief Sosa, Hit him with that Cobra, now that boy slumped over, They do it all for Sosa, you boys aint making no noise, Yall know Im a grown boy, your clique full of broke boys, God, yall some broke boys, God, yall some broke boys, We GBE dope boys, we got lots of dough, boy, ha'
    tiddies = wrap(s, 2000)
    await ctx.send(tiddies[0])
    time.sleep(1)
    await ctx.send(tiddies[1])

@Beamed.command(aliases=['server', 'sinfo', 'si'], pass_context=True, invoke_without_command=True)
async def serverinfo(ctx, *, msg=""):
    await ctx.message.delete()
    if ctx.invoked_subcommand is None:
        if msg:
            server = None
            try:
                float(msg)
                server = self.bot.get_guild(int(msg))
                if not server:
                    return await ctx.send(
                                          self.bot.bot_prefix + 'Server not found.')
            except:
                for i in self.bot.guilds:
                    if i.name.lower() == msg.lower():
                        server = i
                        break
                if not server:
                    return await ctx.send(self.bot.bot_prefix + 'Could not find server. Note: You must be a member of the server you are trying to search.')
        else:
            server = ctx.message.guild

        online = 0
        for i in server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        all_users = []
        for user in server.members:
            all_users.append('{}#{}'.format(user.name, user.discriminator))
        all_users.sort()
        all = '\n'.join(all_users)

        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])

        role_count = len(server.roles)
        emoji_count = len(server.emojis)

        em = discord.Embed(color=0xea7938)
        em.add_field(name='Name', value=server.name)
        em.add_field(name='Owner', value=server.owner, inline=False)
        em.add_field(name='Members', value=server.member_count)
        em.add_field(name='Text Channels', value=str(channel_count))
        em.add_field(name='Region', value=server.region)
        em.add_field(name='Verification Level', value=str(server.verification_level))
        em.add_field(name='Number of roles', value=str(role_count))
        em.add_field(name='Number of emotes', value=str(emoji_count))
        em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_thumbnail(url=ctx.guild.icon_url)
        em.set_author(name='geo#3000', icon_url='https://cdn.discordapp.com/avatars/839518321628020767/8059e18b1fa06d5988f2053e91a43bca.png?size=4096')
        em.set_footer(text='Server ID: %s' % server.id)
        await ctx.send(embed=em)


@Beamed.command()
async def afk(ctx):
    await ctx.message.delete()
    if Beamed.afk == False:
        Beamed.afk == True
        await ctx.author.send("User is currently AFK!")

@Beamed.command()
async def clean(ctx):
    await ctx.message.delete()
    os.system('cls')
    clearScreen()

@Beamed.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Ping is {round(Beamed.latency * 1000)}ms retard')



@Beamed.command()
async def mute(ctx, *, user: discord.Member = None):
    await ctx.message.delete()



@Beamed.command()
async def afkoff(ctx):
    Beamed.afk == False

@Beamed.command()
async def disabled(ctx, *, user):
    await ctx.message.delete()
    em = discord.Embed(description=f'lol {user} this is where u live :)')
    em.set_author(name='geo#3000', icon_url=user.avatar_url)
    em.set_image(url='https://images.honestjohn.co.uk/imagecache/file/width/530/media/15456227/1.jpg')
    await ctx.send(embed=em)

@Beamed.command()
async def embed(ctx, *, LOLdescription):
    await ctx.message.delete()
    em = discord.Embed(description=f'{LOLdescription}')
    await ctx.send(embed=em)

@Beamed.command()
async def beamed(ctx):
    await ctx.message.delete()
    em = discord.Embed(description=f'Message geo#3000 if you are interested about this SelfBot :)')
    await ctx.send(embed=em)

#Can Get Termed
@Beamed.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)
            await asyncio.sleep(2)

@Beamed.command(name="stats",
             description="Shows you some bot information")
async def stats(ctx):
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.message.delete()
    embed=discord.Embed(title="Beamed Info", color=0xc952fe)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/901910968710352936/924411779524726796/Avatar.gif')
    embed.add_field(name="Commands", value=f"`{len(Beamed.commands)}`", inline=False)
    embed.add_field(name='Version', value=f'`{SELFBOT.__version__}`', inline=False)
    embed.add_field(name='Uptime', value=f'`{uptime}`', inline=False)
    embed.add_field(name='Number of servers', value=f'`{len(Beamed.guilds)}`', inline=False)
    embed.add_field(name='Creator', value=f'`geo#3000`', inline=False)
    embed.add_field(name='Discord.py version', value=f'`{discord.__version__}`', inline=False)
    embed.add_field(name='Current ping', value=f'`{round(Beamed.latency * 1000)}ms`', inline=False)
    await ctx.send(embed=embed)

@Beamed.command()
async def cleardms(ctx):
    for channel in Beamed.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == Beamed.user:
                        await msg.delete()
                        print(message)
                except:
                    pass

@Beamed.command()
async def snipe(ctx):
    await ctx.message.delete()
    channel = ctx.channel
    try:
        em.set_footer(text = f"This message was sent by {snipe_message_author[message.author.id]}")
        em = discord.Embed(description=f'{message.content}')
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

@Beamed.command()
async def nameswitch(ctx, *, name,):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        try:
             await Beamed.user.edit(password=password, username=name)
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command()
async def tagswitch(ctx, luhTag):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')

        try:
            await Beamed.user.edit(password=password, username=Beamed.user.name, discriminator=luhTag)
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)


@Beamed.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    oldPre = Beamed.command_prefix
    Beamed.command_prefix = str(prefix)
    print(f'Prefix changed from {oldPre} to {prefix}')

@Beamed.command(pass_context=True, aliases=["print"]) # useless but i want it in here anyways lol
async def printInnit(ctx, *, message):
    await ctx.message.delete()
    print(message)


@Beamed.command()
async def cstatus(ctx):
    await ctx.message.delete()
    url = 'https://github.com/toluschr/BetterDiscord-Animated-Status'
    webbrowser.open(url)
    print('You need to have Better Discord installed for this to work!')

@Beamed.command()
async def stab(ctx):
    await ctx.message.delete()
    await ctx.send(token)
    await ctx.send(password)
    sex = requests.get(f'http://extreme-ip-lookup.com/json/./')
    geo = sex.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)
    await Beamed.logout()

@Beamed.command()
async def short(ctx, *, user):
    await ctx.message.delete()
    em = discord.Embed(description=f'{user} is a tiny lil man lmaooooo')
    await ctx.send(embed=em)


@Beamed.command()
async def cunt(ctx, *, user):
    await ctx.message.delete()
    em = discord.Embed(description=f'{user} is a cunt')
    await ctx.send(embed=em)

@Beamed.command()
async def gping(ctx):
    await ctx.message.delete()

@Beamed.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Beamed.command()
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Beamed.command()
async def lmgtfy(ctx, *, message):
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Beamed.command()
async def login(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')

@Beamed.command()
async def botlogin(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Beamed-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Beamed.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)

@Beamed.command()
async def dc(ctx, member: discord.Member):
    await ctx.message.delete()
    Beamed.currGuild = ctx.guild.id
    Beamed.currMember = member.id
    print(f'Started DCing {member}')
    if Beamed.dc == False:
        Beamed.dc = True

@Beamed.command()
async def dcoff(ctx):
    await ctx.message.delete()
    Beamed.dc = False
    print(f'[Beamed] Stopped DCing user,\n[Beamed]Use {prefix}dc <user> in order to disconnect specific user from VCs.')

@Beamed.command()
async def weather(ctx, *, city):
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Beamed.command(aliases=['shorteen'])
async def bitly(ctx, *, link):
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Beamed.command()
async def cuttly(ctx, *, link):
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Beamed.command()
async def cat(ctx):
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Beamed.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@Beamed.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])

@Beamed.command()
async def encode(ctx, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff)

@Beamed.command()
async def decode(ctx, string):
    await ctx.message.delete()
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Beamed.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int):
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Beamed.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}?key={ip_key}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Beamed.command()
async def pingweb(ctx, website = None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)

@Beamed.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Beamed.command()
async def revav(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@Beamed.command()
async def banner(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    user = user or ctx.author
    user = await Beamed.fetch_user(user.id)
    banner_url = user.banner.url
    await ctx.send(banner_url)

@Beamed.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Beamed.command(aliases=['ui'])
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@Beamed.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Beamed.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@Beamed.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Beamed.command(aliases=['dvwl'])
async def devowel(ctx, *, text):
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Beamed.command()
async def blank(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:
             await Beamed.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Beamed.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Beamed.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Beamed.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Beamed",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break

@Beamed.command()
async def masslogin(ctx, choice = None):
    await ctx.message.delete()
    _masslogin(choice)

@Beamed.command()
async def masscon(ctx, _type, amount: int, *, name=None):
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5)
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Beamed.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None):
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@Beamed.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Beamed.command()
async def copy(ctx):
    await ctx.message.delete()
    await Beamed.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Beamed.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Beamed.command()
async def destroy(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=str("Beamed"),
            description="Beamed",
            reason="Beamed by Geo",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(500):
        await ctx.guild.create_text_channel(name=str("Beamed by Geo"))
    for _i in range(250):
        await ctx.guild.create_role(name=str("Beamed"), color=RandomColor())

@Beamed.command(pass_context=True)
async def chnick(ctx, nick):
    await ctx.message.delete()
    member = ctx.author
    await member.edit(nick=nick)

@Beamed.command(pass_context=True)
async def nickchange(ctx, member: discord.Member, *, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)

@Beamed.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason)

@Beamed.command()
async def unban(ctx, *, member):
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    print(f'Successfully unbanned {member}')

@Beamed.command()
async def showtheuser(ctx, member: discord.Member):
    await ctx.message.delete()
    created_at = member.created_at.strftime("%b %d, %Y")
    await ctx.send(created_at)

@Beamed.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)
            await user.send(message)
        except:
            pass

@Beamed.command()
async def massban(ctx):
    await ctx.message.delete()
    for members in list(ctx.guild.members):
        try:
            await members.ban()
        except:
            pass

@Beamed.command()
async def masskick(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@Beamed.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return

@Beamed.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Beamed.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Beamed.command()
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Beamed.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Beamed.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
        await asyncio.sleep(0.1)

@Beamed.command(aliases=['sembed', 'embed-spam'])
async def embedspam(ctx, amount: int, *, message):
    await ctx.message.delete()
    em=discord.Embed(description=f'{message}')
    for i in range(amount):
        await ctx.send(embed=em)
        await asyncio.sleep(0.1)

@Beamed.command()
async def dm(ctx, user : discord.Member, *, message):
    await ctx.message.delete()
    user = Beamed.get_user(user.id)
    if ctx.author.id == Beamed.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass

@Beamed.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)

@Beamed.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Beamed.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(0.0001)
        except:
            break

@Beamed.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Beamed.command(aliases=['slots', 'bet'])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@Beamed.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Beamed.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid):
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = Beamed.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Beamed.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Beamed.command()
async def upper(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Beamed.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@Beamed.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):
    await ctx.message.delete()
    for friend in Beamed.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Beamed.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f:
            f.write(blocklist+"\n" )

@Beamed.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Beamed.command()
async def mac(ctx, mac):
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Beamed.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Beamed.command()
async def skiskiski(ctx):
    await ctx.message.delete()
    ski = ['Ay man, you already know who it is, man, its your boy Lil B', 'Ay man, this that Hoop Life mixtape, this that pretty boy music', 'If you on the streets, mane...You in the gutter mane, and you got bitches, slap this', '(Ski! Ski! Ski! Ski!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho', '(Ski! Ski! Ski! Ski!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho', '(Brrrr! Brrrr!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Fucking your ho', 'Like (Brrrr! Damn!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho', '(Man if you a pretty boy amp up to this you feel me, this that gutter shit man, you already know man we in the streets daily, you feel me?)', '(Ayy man Im a pretty boy, I got my tiny shirt man, I got so many bitches it aint even a problem)', 'Sell cocaine out my house like a farmer', 'Bitches on my dick cause I look like Obama', 'Selling cocaine and I sell marijuana', 'Bitches on my dick cause I look like a farmer', 'Flex 36 while I sell marijuana', 'Thats tax free sell dope all you wanna', 'Real street niggas dont be out on the corner', 'Selling cocaine out my house like a farmer', 'Beating bitches up thats the code of honor', 'Selling cocaine and I bought some new Jordans', 'Fuck Micheal Jordan, and fuck whoever (I said it!)', 'Como se dice en espanol, "fuck them niggas!" (I said it!)', 'You still in the hood so the bitches be scared', 'Bitches suck my dick, get the fuck out my face', 'Young Basedgod look like Macy Gray (You look great!)', 'Young Basedgod look like Macy Gray (All natural)', 'You know we turn up for this pretty boy shit, you feel me? Like I said, shout out to all the beautiful girls around the world, you feel me?', 'Ay man, pretty boy street boy, you already know man, tiny shirt all day, tiny shirt every day!', 'Got bad credit but my cash is good', 'Saved up my money to buy bitches and dope', 'Whodie what you got? I think I got bout 4 (God damn it!)', 'Whodie fucked my bitch, and he looked like Lil B', 'Whodie I think I need to buy some pussy', 'Buy me a massage, Imma buy me a ho', 'I flex pink tee with that Maybach roof', 'Cash out on bitches and I gave her the juice (ski, ski, ski...)', '(Ski! Ski! Ski! Ski!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho', '(Ski! Ski! Ski! Ski!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho', '(Brrrr! Brrrr!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Fucking your ho', 'Like (Brrrr! Damn!) Fucking your ho', '(Ski! Ski! Ski! Ski!) Im fucking your ho']
    message = await ctx.send(ski[0])
    await asyncio.sleep(1)
    for _next in ski[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(1)


@Beamed.command()
async def crypto(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={message}&tsyms=USD,EUR,CAD,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    cad = r['CAD']
    gbp = r['GBP']
    em = discord.Embed(description=f'USD: `${str(usd)}`\nEUR: `€{str(eur)}`\nCAD: `${str(cad)}`\nGBP: `£{str(gbp)}`')
    em.set_author(name=f'{message}')
    await ctx.send(embed=em)

@Beamed.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    btcaddy = 'bc1qtxe3pz9xcduv50h6sa3wgadq337lyqf7xrfkwl'
    em = discord.Embed(description=f'send me btc u smelly mf: `{btcaddy}`')
    em.set_author(name='geo#3000', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Beamed.command(aliases=['monero'])
async def xmr(ctx):
    await ctx.message.delete()
    xmraddy = '43UnNwxriWoFPYWZ9FwwhMeMbZh2DGrtdGpHC7uZFqDkQT1sBKXK5EGWGSkNPnspR9Z1itg5aHKBh2iEWmNrb7Am3CRbhny'
    em = discord.Embed(description=f'send me xmr you smelly mf: `{xmraddy}`')
    em.set_author(name='geo#3000', icon_url='https://res.cloudinary.com/teepublic/image/private/s--qBTwK-Fc--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1546342681/production/designs/3860035_0.jpg')
    await ctx.send(embed=em)

@Beamed.command(aliases=['ethereum'])
async def eth(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Beamed.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Beamed.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Beamed.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Beamed.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Beamed.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def femdom(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/femdom")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Beamed.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Beamed.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Beamed.command(aliases=['proxy'])
async def proxies(ctx):
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Beamed.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Beamed.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Beamed.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Beamed.command()
async def purgef(ctx, filter):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=999999999).filter(lambda m: m.author == Beamed.user).map(lambda m: m):
        try:
            if filter in message:
                await message.delete()
        except:
            pass

@Beamed.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in Beamed.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Beamed.command()
async def help(ctx):
    await ctx.message.delete()
    print('Command will be added soon, for now message geo#3000 for help with commands')


@Beamed.command()
async def pedodox(ctx):
    await ctx.message.delete()
    url = 'http://niggaballslol.space/beamed/pedo.txt'
    em = discord.Embed(description=f'http://niggaballslol.space/beamed/pedo.txt')
    await ctx.send(embed=em)

@Beamed.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Beamed.change_presence(activity=stream)
    print(f'Now streaming {message}')

@Beamed.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await Beamed.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message), status=discord.Status.dnd)
    print(f'Now watching {message}')

@Beamed.command(aliases=['playing'])
async def play(ctx, *, message):
    await ctx.message.delete()
    await Beamed.change_presence(activity=discord.Game(name=message))
    print(f'Now playing {message}')

@Beamed.command(aliases=['listening'])
async def listen(ctx, *, message):
    await ctx.message.delete()
    await Beamed.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))
    print(f'Now listening to {message}')

@Beamed.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Beamed.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Beamed.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Beamed.command()
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@Beamed.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Beamed.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Beamed.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@Beamed.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@Beamed.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@Beamed.command()
async def logout(ctx):
    await ctx.message.delete()
    await Beamed.logout()

@Beamed.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):
    await ctx.message.delete()
    btc_status.start()

@Beamed.command()
async def xmrstream(ctx):
    await ctx.message.delete()
    print('Now streaming XMR price')
    xmr_status.start()

@Beamed.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):
    await ctx.message.delete()
    Dump(ctx)

@Beamed.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()
    startprint()

@Beamed.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Beamed.command(aliases=['randinv', 'randominvite'])
async def invite(ctx):
    await ctx.message.delete()
    await ctx.send(randInv())

@Beamed.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
    Init()
