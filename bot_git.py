import discord
from discord.ext import commands
import datetime
import random

#Establish that commands are prefixed with !
bot = commands.Bot(command_prefix="!")

#Print to console that bot has logged in
@bot.event
async def on_ready():
    print(f'Logged in {bot.user}')

#Rewrite on_message method to tech the bot to respond to every photo that has been posted in any text channel
@bot.event
async def on_message(message):
    print(f'{message.channel} : {message.author} : {message.author.name} : {message.content}')

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.process_commands(message)
    else:
        if any(ext in att.filename for ext in (".jpg", ".jpeg", ".png") for att in message.attachments):
            response = ["Какая миленькая фотография (｡♥‿♥｡)", 
                        "Классненько, мне нравится! (b~_^)b", 
                        "М И Л О Т А (♡ >ω< ♡)", 
                        "Это миленько, но все-таки слишком банально (⊙_☉)",
                        "Ой, Кто это? ʕ•ᴥ•ʔ", 
                        "Противненький такой, похож на Андрея (◑○◑)", 
                        "Потрясающе! ( ͡~ ͜ʖ ͡°)", 
                        "Мне это знакомо ꈍ .̮ ꈍ", 
                        "Интересная ситуация ｜*￣∇￣｜", 
                        "Просто красиво, хочу себе такую картинку на чехол (◕‿◕✿)", 
                        "Самый милый ребёнок на свете ✌('ω')",  
                        "По-моему, это уже чересчур Ψ(☆ｗ☆)Ψ", 
                        "Если я была бы художником, то написала бы картину на основе этой милоты (๑´ㅂ`๑)"]
            await message.channel.send(random.choice(response))
        elif message.content == 'dq':
            print(f'{bot.user} logging out')
            await bot.logout()
    
        
#Teach the bot some commands
@bot.command(name = 'выйди')
async def logout(ctx):
    '''Изгоняет бота с сервера'''
    print(f'{bot.user} logging out')
    await bot.logout()

@bot.command(name = 'очисть')
async def purge(ctx):
    '''Очищает все сообщения, отправленные за последние 15 минут'''
    
    await ctx.send('Удаляю всю вашу переписку (＾ω＾)/')
    await ctx.message.channel.purge(before = (datetime.datetime.now() - datetime.timedelta(minutes=15)), bulk = False)

@bot.command(name = 'правда')
async def motd(ctx):
    '''Цитирует лучший фильм в истории кинематографа'''

    await ctx.send("Вот скажи мне, американец, в чём сила! Разве в деньгах? Вот и брат говорит, что в деньгах. У тебя много денег, и чего? Я вот думаю, что сила в правде: у кого правда, тот и сильней! Вот ты обманул кого-то, денег нажил, и чего — ты сильней стал? Нет, не стал, потому что правды за тобой нету! А тот, кого обманул, за ним правда! Значит, он сильней!", tts = True)
    await ctx.send("(ฅΦωΦ)ฅ")

bot.run("TOKEN")
