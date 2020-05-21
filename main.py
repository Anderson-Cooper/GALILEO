import discord
from random import randint as r

h=('```GALILEO FIGARO```***SOME QUICK NEWS***\nI lost the original bot so i regenerated it\nprefix gf!\n```ABOUT```\nGalileo is my side project amoung other things, if you have any suggestions, shoot me a DM @ One S Q E E Z Y Boi#0074\n```COMMANDS```\n **am-i**: Sees if the bot is working like it should\n**music**: What is Galileo listening to these days?\n**cl**: The change log\n**corona**: VISIT THIS SITE AND REMEMBER TO WASH YOUR HANDS FOR 20 SECONDS, STAY HOME, AND NOT GET MISINFORMED (Im lookin at you, Trump!\n```Fun```\n**d6**: Rolls a D6 dice\n**rng** Generates a random number\n**D12** Rolls a D12 dice\n```GALILEO BOT "We are back baby!" 1.0```')
sh=("```Secret Help```\n **foundya** OH GOD YOU FOUND ME!!!!!")
cl=("```GALILEO NEWS```\n+We are now in full version\n+Secret update(￣y▽,￣)╭ \n-Kill command\n+D12 dice")
client = discord.Client()

DBa=("PERM TEST @everyone")

 
@client.event
async def on_ready():
    print('Bot is open {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
   
    if message.content.startswith('gf!am-i'):
        await message.channel.send('I am')
        print("Hello test conducted")
    if message.content.startswith('gf!corona'):
        await message.channel.send('Visit this site for Coronavirus information https://www.cdc.gov/')
    if message.content.startswith('gf!help'):
        await message.channel.send(h)
        print("Help Conducted")
    if message.content.startswith('gf!SEhelp'):
        await message.channel.send(sh)
    if message.content.startswith('gf!music'):
        await message.channel.send
        ("https://open.spotify.com/playlist/49ddWzhNmWxyMuYlvu8L5Z?si=jYlh6zK9RryKSeMlvKZ3yA")
        print("Sent some GrOvEs")

    if message.content.startswith('gf!cl'):
        await message.channel.send(cl)
    if message.content.startswith('gf!dbug_pingtest'):
        await message.channel.send(DBa)
        print("Dbug1 test done")
    if message.content.startswith('gf!d6'):
        b=r(1,6)
        await message.channel.send(b)
        print("d6:",b)
    if message.content.startswith('gf!cmd'):
        d=r(1,3267)
        await message.channel.send("YOU HAVE WON THE EVENT! Quick! Message One S Q U E E Z Y Boi#0074: 44573")
        print("Winning Number:",d)
    if message.content.startswith('gf!rng'):
        e=r(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        await message.channel.send(e)
        print("RNG:",e)
    if message.content.startswith('gf!killsq'):
        await message.channel.send('too late')
        from time import sleep as s
        s(2)
        await message.channel.send('my time has come')
        s(2)
        await message.channel.send('sent shivers down my spine')
        s(1)
        await message.channel.send("body's aching all the time")
        s(2.5)
        await message.channel.send('goodbye everybody')
        s(1)
        await message.channel.send('ive got to go')
        s(2)
        await message.channel.send('gotta leave you all behind and face the truth!')
        s(3)
        await message.channel.send('MAMAAAAAAA OOOOOOOOOOOOOOOOOOOO')
        s(3.2)
        await message.channel.send('I DONT WANT TO DIEEEE')
        s(2.3)
        await message.channel.send('I sometimes wish ive never been born at all!')
        s(3.1)
        await message.channel.send('*Chlachink!*.....**BANG!!**')
        exit("he ded lol")
    if message.content.startswith('sora'):
        await message.channel.send('............Speaking of which, i think Squeezy is ready')

client.run('NzEyNzQ5MzM0MTM1MDQ2MTY1.XsWFoA.Q38jiB15n7osWWgN4FU4hsWVAow')
