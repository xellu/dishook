import os, re, time
from discord_webhook import *

os.system("title DisHook")
os.system("cls")


c = 0
errors = 0
command = ""
value = ""


#----webhook elements----#

#basic
url = ""
message = ""
#embed
author_name = ""
author_url = ""
author_icon = ""
title = ""
description = ""
footer = ""
color = "#fff"
#fields
field_name = ""
field_value = ""

try:
    open(".webhook")
except:
    open(".webhook", "w").write("""
<url: https://discord.com/webhook_url>
<color: 5600ff> 
<message: message>

<title: title>
<description: description>

<author.name: author>
<author.url: https://github.com/xellu/>

{field name,field value}

<footer: footer>""")
    print("edit .webhook and re-run the executor")
    time.sleep(3)
    os._exit(0)

for letter in open(".webhook", "r", encoding="ansi").read():
    if letter == "<":
       c = 1


    if letter == ">":
        c = 0
        command += ">"
        if command == " ":
            print(f"\033[31mCommand '{command}' not found")
        elif command == "<color>":
            value = re.sub(r'.', '', value, count = 1)
            embed.set_color(value)
        elif command == "<url>":
            value = re.sub(r'.', '', value, count = 1)
            hook = DiscordWebhook(url=value)
            embed = DiscordEmbed(description="")
        elif command == "<author.name>":
            value = re.sub(r'.', '', value, count = 1)
            author_name = value
        elif command == "<author.url>":
            value = re.sub(r'.', '', value, count = 1)
            author_url = value
        elif command == "<author.icon>":
            value = re.sub(r'.', '', value, count = 2)
            author_icon = value
        elif command == "<title>":
            value = re.sub(r'.', '', value, count = 1)
            embed.set_title(title=value)
        elif command == "<description>":
            value = re.sub(r'.', '', value, count = 1)
            embed.set_description(description=value)
        elif command == "<footer>":
            value = re.sub(r'.', '', value, count = 1)
            embed.set_footer(text=value)
        elif command == "<message>":
            value = re.sub(r'.', '', value, count = 1)
            hook.set_content(value)
        else:
            print(f"\033[31mCommand '{command}' not found")
            errors += 1
            

        command = ""
        value = ""


    if letter == ":":
        c = 2


    if letter == "{":
        c = 3
    if letter == "}":
        c = 0
        field_name = re.sub(r'.', '', field_name, count = 1)
        field_value = re.sub(r'.', '', field_value, count = 1)
        embed.add_embed_field(name=field_name, value=field_value)
    if letter == ",":
        if c == 3:
            c = 4

    if c == 1:
        command += letter
    if c == 2:
        value += letter 
    if c == 3:
        field_name += letter
    if c == 4:
        field_value += letter

def send():
    try:
        if author_name != "":
            embed.set_author(name=author_name, url=author_url, icon_url=author_icon)
        hook.add_embed(embed)
        hook.execute()
    except Exception as error:
        errors += 1
        return f"Error while posting the request: \033[1;31m{error}"
    else:
        return "OK"



status = send()
if status == "OK":
    print("\033[32mWebhook posted")
elif "Error" in status:
    print(f"\033[31m{status}")
else:
    print("\033[33mStatus unknown")
    errors += 1

print(f"\n\033[1;30mExecuted with {errors} errors")
time.sleep(1)