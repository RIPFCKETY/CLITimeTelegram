# Coded By R.I.P
# My Telegram : t.me/RIP_PROJECTS/

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name; system('clear' if name == 'posix' else 'cls')
import random
import pytz

class color:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
        reset='\033[0m'
        yellow='\033[93m'

try:
    account = Client(
     "", # session name
     api_id="", # get from https://my.telegram.org/auth
     api_hash="", # get from https://my.telegram.org/auth
     phone_number = "", # your phone number account
     password="") # if you have a password step 2 write here but if you don't have leave empty
    
    print(f"{color.blue}CLI Bot Connected To Your Account Successfully\n")
    print(f"{color.green}CLI Time Is Running...\n\n{color.reset}")
except :
     exit()

scheduler = AsyncIOScheduler(timezone=pytz.timezone('us/newyork')) # Set Your Timezone

async def SelfTime():
    photos = [p async for p in account.get_chat_photos("me")]
    await account.delete_profile_photos([p.file_id for p in photos[1:]])
    fonts  = ["/fonts/Orbitron-VariableFont_wght.ttf" , "/fonts/ArchitectsDaughter-Regular.ttf" , "/fonts/BrunoAce-Regular.ttf" , "/fonts/Cormorant-Italic-VariableFont_wght.ttf" , "/fonts/Cormorant-VariableFont_wght.ttf" , "/fonts/Gruppo-Regular.ttf" , "/fonts/Lexend-VariableFont_wght.ttf" , "/fonts/MateSC-Regular.ttf" , "/fonts/SpaceMono-Bold.ttf" , "/fonts/Nunito-VariableFont_wght.ttf"]
    colors = ["grey" , "white" , "black"]
    photo  = ["p1.jpg" , "p2.jpg" , "p3.jpg" , "p4.jpg"]
    country_time_zone = pytz.timezone('us/newyork') # Set Your Time Country
    country_time = datetime.now(country_time_zone)
    time_now = country_time.strftime("%H:%M")
    img = Image.open(f"images/{random.choice(photo)}")
    font = ImageFont.truetype(random.choice(fonts), 50)
    text = time_now
    draw = ImageDraw.Draw(img)
    textwidth, textheight = draw.textsize(text, font)
    width, height = img.size  
    x=width/50-textwidth/50
    y=height/50-textheight/20
    draw.text((x, y), text, font=font, fill=random.choice(colors))
    img.save("images/time.png")
    await account.set_profile_photo(photo="images/time.png")
    print(f"\n{color.green}[INFO]{color.reset} - {color.yellow}Changed{color.reset} - {color.yellow}Time Now : {color.green}{time_now}{color.reset}\n")

scheduler.add_job(SelfTime, "interval", seconds=60)
scheduler.start()
account.run()