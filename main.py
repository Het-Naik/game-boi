import discord
import random
from guess import guessgame
import urllib.request
import os
import requests 
import shutil

bot = discord.Client()

@bot.event
async def on_ready():
    channel = bot.get_channel(789877841344856154)
    await channel.send('yoyo')

@bot.event
async def on_message(message):
    cmd = str(message.content).lower()
    cmdl = cmd.split(' ')
    pirorate = random.randint(0, 100)
    if message.author.bot:
            return
    myid = '<@!758921556385726494>'
    botid = '<@!789877057101889556>'
    alleniteid = '<@!789204472680284202>'
    
    if cmd.startswith('piro rate '):
        if cmdl[2] == myid or cmdl[2] == botid:
            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            g = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='PIRO RATE OF ' + str(g), value = str(g) , color=0x00FF00)
            piroEmbed.add_field(name=str(g) + ' is 100 % piro ', value=':sunglasses:', inline = False)
            await message.channel.send(embed = piroEmbed)
        

        elif str(pirorate) < '20':
            """ mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            g = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='PIRO RATE OF ', value = str(g) , color=0x00FF00)
            piroEmbed.add_field(name=str(g) , value=' is ' + str(pirorate) + ' % piro' , inline = False)
            await message.channel.send(embed = piroEmbed)
             """


            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            g = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='PIRO RATE OF ', value = str(g) , color=0x00FF00)
            piroEmbed.add_field(name=str(g) + ' is ' + str(pirorate) + ' % piro', value='<:kek:783679092003307520>', inline = False)
            await message.channel.send(embed = piroEmbed)
        else:
            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            g = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='PIRO RATE OF ', value = str(g) , color=0x00FF00)
            piroEmbed.add_field(name=str(g) + ' is ' + str(pirorate) + ' % piro', value=':sunglasses:', inline = False)
            await message.channel.send(embed = piroEmbed)


    if cmd.startswith('bro trigger '):
        mention = cmdl[2]
        mention = mention.replace("<", '')
        mention = mention.replace(">", '')
        mention = mention.replace("!", '')
        mention = mention.replace("@", '')
        g = bot.get_user(int(mention))
        """ usr = message.channel.get_user(w) """
        dp = g.avatar_url
        dp = str(dp).replace('webp', 'jpg')
        dp = str(dp).replace('?size=1024', '')
        triggered  = 'https://some-random-api.ml/canvas/triggered?avatar=' + str(dp)
        print(dp)


        image_url = triggered
        filename = 'triggered.gif'

        r = requests.get(image_url, stream = True)

        if r.status_code == 200:
            r.raw.decode_content = True
            
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')

        """ str(filename).replace('.jpg', '.gif') """
        await message.channel.send(file=discord.File(filename))

    if cmd.startswith('love% of '):
        m = cmdl[2]
        w = cmdl[4]
        points = 0
        x = len(m)
        y = len(w)
        if x == y:
            points += 20
        if m[0] == 'a' or m[0] == 'e' or m[0] == 'i' or m[0] == 'o' or m[0] == 'u':
            if w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u':
                points += 30
            else:
                points += 10
        consm = 0
        vowm = 0
        consw = 0
        voww = 0
        for i in range(x):
            if m[0] == 'a' or m[0] == 'e' or m[0] == 'i' or m[0] == 'o' or m[0] == 'u':
                vowm += 1
            else:
                consm += 1

            if w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u':
                voww += 1
            else:
                consw += 1
            
            i += 1
        if consm == consw:
            points += 20
        if vowm == voww:
            points += 30

        piroEmbed = discord.Embed(title='LOVE RATE OF ', value = str(m) , color=0x00FF00)
        piroEmbed.add_field(name='love % of ' + str(m) + ' and ' + str(w) + ' is ' + str(points) + '%', value='calculated ~~completely scientifically~~', inline = False)
        await message.channel.send(embed = piroEmbed)


        """ await message.channel.send('love % of ' + str(m) + ' and ' + str(w) + ' is ' + str(points) + '%') """
    if cmd.startswith('convert to binary '):
        txt = cmdl[3:]
        binary = 'https://some-random-api.ml/binary?text=' + str(txt)
        await message.channel.send(binary)


    if cmd.startswith('sexy rate '):
        if cmdl[2] == myid or cmdl[2] == botid:
            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            g = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='SEXY RATE OF ' + str(g), value = str(g) , color=0x00FF00)
            piroEmbed.add_field(name=str(g) + ' is 100 % sexy ', value=':wink:', inline = False)
            await message.channel.send(embed = piroEmbed)
        elif str(pirorate) < '20':
            
            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            w = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='SEXY RATE OF ', value = str(w) , color=0x00FF00)
            piroEmbed.add_field(name=str(w) + ' is ' + str(pirorate) + ' % sexy', value='<:kek:783679092003307520>', inline = False)
            await message.channel.send(embed = piroEmbed)
        else:
            mention = cmdl[2]
            mention = mention.replace("<", '')
            mention = mention.replace(">", '')
            mention = mention.replace("!", '')
            mention = mention.replace("@", '')
            w = bot.get_user(int(mention))
            piroEmbed = discord.Embed(title='SEXY RATE OF ', value = str(w) , color=0x00FF00)
            piroEmbed.add_field(name=str(w) + ' is ' + str(pirorate) + ' % sexy', value=':wink:', inline = False)
            await message.channel.send(embed = piroEmbed)
            
    if cmd.lower() == 'f':
        if message.author.bot:
            return
        await message.channel.send('F')

    if cmd.lower() == 'play guess':
        await message.channel.send('Guess a number between 1 and 10.')
        answer = random.randint(1, 10)

        for z in range(3):
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()


            print(answer)

            guess = await bot.wait_for('message', check = is_correct)

            # except asyncio.TimeoutError:
            #     return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            ans = False
            for s in range(3):
                if int(guess.content) == answer:
                    ans = True
                    break
                else:
                    ans = False
            if ans == True:
                ans = 'you are right !'
            elif ans == False:
                ans = 'you are wrong :('
            await message.channel.send(ans)

        await message.channel.send('It is {}.'.format(answer))


    # if message.content == 'F' or message.content == 'f':
    #     await message.channel.send('F')




bot.run('token')



""" piroEmbed = discord.Embed(title='PIRO RATE OF ' + 'cmdl[2]', color=0xFFFFFF)
piroEmbed.add_field(name="cmdl[2] + ' is ' + str(pirorate) + ' % sexy '", inline=False)
piroEmbed.add_field(name='CLASS1 :', value='MATHS --> SARTHAK SIR\nTIME : 2:30m to 4:30pm', inline=False)
piroEmbed.add_field(name='CLASS2 :', value='CHEMISTRY --> DR.KIRTI KUMAR SHAH SIR\nTIME : 4:50pm to 6:50pm', inline=False)
piroEmbed.add_field(name='BREAK :', value='20 MINUTES BREAK WOOHOO', inline=False)
piroEmbed.add_field(name='XTRA-CLASS :', value='MATHS --> SARTHAK SIR\nTIME : 1:45pm to 2:30pm', inline=False)
"""

