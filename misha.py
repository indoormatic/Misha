import asyncio
import os
import random

import discord
from discord.ext import commands


description = '''La waifu de Blareot.
No se toca.'''
bot = commands.Bot(command_prefix='!', description=description)
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    discord.opus.load_opus(os.path.dirname(os.path.abspath(__file__))+'/opus')

songs = asyncio.Queue()    
    
'''
async def my_background_task():
    await bot.wait_until_ready()
    while not bot.is_closed:
        if not list and hasattr(bot, "voice"):
            await bot.voice.disconnect()
        if list:
            await sendAudio(server, textChannel, voiceChannel, list[0])
            list.remove(list[0])'''
            
    
@bot.event
async def on_ready():
    status  =["with Lyner!", "EXEC_CHRONICLE_KEY/.", "Ar Tonelico II", "Ar Tonelico I", "Call of Duty"]
    np = discord.Game()
    np.name = random.choice(status)
    await bot.change_status(np, False)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------') 
       

@bot.event
async def on_message(message):
        
    if message.content == '*help*':
        await bot.send_message(message.channel, """```__**Comandos**__:
                                                    careless whisper
                                                    wake me up
                                                    careless airhorn
                                                    sax guy
                                                    donki knog
                                                    no tienes pito
                                                    risas
                                                    careless kazoo
                                                    phoenix protesta
                                                    no homo
                                                    all of the homo
                                                    ran ran ruu
                                                    rules of nature
                                                    rules of kazoo
                                                    smooth criminal
                                                    todokete
                                                    grand dad
                                                    snow halation
                                                    morth
                                                    pacman
                                                    oraoraora
                                                    PUSH START TO RICH
                                                ```""")    
    if message.content == '*careless whisper*':    
        await sendAudio(message, '/careless.mp3') 
            
    if message.content == '*wake me up*':    
        await sendAudio(message, '/wakemeup.mp3') 
            
    if message.content == '*careless airhorn*':
        await sendAudio(message, '/careless airhorn.mp3') 
        
    if message.content == '*sax guy*':
        await sendAudio(message, '/sax guy.mp3')        
        
    if message.content == '*donki knog*':
        await sendAudio(message, '/donki knog.mp3') 
        
    if message.content == '*no tienes pito*':
        await sendAudio(message, '/no tiene pito.mp3') 
        
    if message.content == '*risas*':
        await sendAudio(message, '/risas enlatadas.mp3') 
            
    if message.content == '*careless kazoo*':
        await sendAudio(message, '/careless kazoo.mp3') 
            
    if message.content == '*phoenix protesta*':
        await sendAudio(message, '/Phoenix - (Spanish) Protesto.wav')    
            
    if message.content == '*godot protesta*':
        await sendAudio(message, '/Godot - (Spanish) Objection.wav')
        
            
    if message.content == '*apollo ya lo tiene*':
        await sendAudio(message, '/Apollo - (Spanish) Gotcha.wav')
               
    if message.content == '*no homo*':
        await sendAudio(message, '/no homo.mp3')
               
    if message.content == '*all of the homo*':
        await sendAudio(message, '/all of the homo.mp3')
        
    if message.content == '*ran ran ruu*':
        await sendAudio(message, '/ran ran ruu.mp3')
        
            
    if message.content == '*apollo un momento*':
        await sendAudio(message, '/Apollo - (Spanish) Hold it.wav')
        
            
    if message.content == '*apollo protesta*':
        await sendAudio(message, '/Apollo - (Spanish) Objection.wav')
        
    if message.content == '*apollo toma ya*':
        await sendAudio(message, '/Apollo - (Spanish) Take that.wav')       
        
                    
    if message.content == '*edgey un momento*':
        await sendAudio(message, '/Edgeworth - (Spanish) hold it.wav')
        
            
    if message.content == '*edgey protesta*':
        await sendAudio(message, '/Edgeworth - (Spanish) Protesto.wav')
        
            
    if message.content == '*edgey toma ya*':
        await sendAudio(message, '/Edgeworth - (Spansih) take that.wav')
        
            
    if message.content == '*payne protesta*':
        await sendAudio(message, '/Payne - (Spanish) Protesto.wav')
        
            
    if message.content == '*karma protesta*':
        await sendAudio(message, '/Karma - (Spanish) Protesto.wav')
        
            
    if message.content == '*klavier protesta*':
        await sendAudio(message, '/Klavier - (Spanshi) Objection.wav')
        
            
    if message.content == '*kristoph protesta*':
        await sendAudio(message, '/Kristoph - (Spanish) Objection.wav')
        
            
    if message.content == '*mia protesta*':
        await sendAudio(message, '/Mia - (Spanish) objection.wav')
        
    if message.content == '*rules of nature*':
        await sendAudio(message, '/Rules of Nature.mp3')
        
    if message.content == '*rules of kazoo*':
        await sendAudio(message, '/RULES_OF_NATURE.mp3')
        
    if message.content == '*morth*':
        await sendAudio(message, '/morth.mp4.mp3')
        
    if message.content == '*pacman*':
        await sendAudio(message, '/Title Theme - PAC-MAN 256.mp3')
        
    if message.content == '*oraoraora*':
        await sendAudio(message, '/End of The World - Kingdom Hearts 1.5 ReMIX.mp3')
        
    if message.content == '*smooth criminal*':
        await sendAudio(message, '/smooth criminal.mp3')
        
    if message.content == '*PUSH START TO RICH*':
        await sendAudio(message, '/PUSH START TO RICH - Dian Shi Ma Li.mp3')
                    
    if message.content == '*mia toma ya*':
        await sendAudio(message, '/Mia - (Spanish) take that.wav')
        
            
    if message.content == '*mia un momento*':
        await sendAudio(message, '/Mia - (Spanish) un momento.wav')        
            
    if message.content == '*phoenix toma ya*':
        await sendAudio(message, '/Phoenix - (Spanish) Toma Ya.wav')
                
            
    if message.content == '*phoenix un momento*':
        await sendAudio(message, '/Phoenix - (Spanish) Un Momento.wav')
                
            
    if message.content == '*franziska protesta*':
        status = await sendAudio(message, '/Franziska - (Spanish) Protesto.mp3')
        print(status)
            
    if message.content == '*snow halation*':
        await sendAudio(message, '/snow halation.mp3')
            
    if message.content == '*grand dad*':
        await sendAudio(message, '/grand dad.mp3')
        
    if message.content == '*todokete*':
        await sendAudio(message, '/todokete.mp3')
                 
    if message.content.startswith('*leave*'):   
        bot.voice.disconnect()         
        await bot.send_message(message.channel, 'Bye bye...')
        
    if player.is_done():
        await asyncio.sleep(1)
        if player.is_done():        
            await bot.voice.disconnect()


async def sendAudio(message, audioFilename):
    global player
    voiceChannel = message.author.voice_channel
    if voiceChannel is None:
        await bot.send_message(message.channel, 'hijo de puta metete a un canal antes de poner eso')
    else:
        if not bot.is_voice_connected(message.server):
            afu = await bot.join_voice_channel(voiceChannel)
            bot.voice = afu
        player = bot.voice.create_ffmpeg_player(os.path.dirname(os.path.abspath(__file__))+audioFilename)
        player.start()            
        while not player.is_done():            
            asyncio.sleep(1)            
        player.stop()
    
'''
try:
    loop.create_task(my_background_task())
    loop.run_until_complete(bot.login('MTc3MTczNjgzMTcxODg1MDU2.CguWxA.go0XLYEy3fyWPq169lMTAxgL408'))
    loop.run_until_complete(bot.connect())
except Exception:
    loop.run_until_complete(bot.close())
finally:
    loop.close()'''
        
bot.run('MTc3MTczNjgzMTcxODg1MDU2.CguWxA.go0XLYEy3fyWPq169lMTAxgL408')        