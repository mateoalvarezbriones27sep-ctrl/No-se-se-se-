import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5 , name = 'he'):
    await ctx.send(name * count_heh)

@bot.command()
async def adios(ctx,name):
    await ctx.send(f'ADIOS {name}')

@bot.command()
async def suma(ctx):
    a, b = random.randint(1, 10), random.randint(1, 10)
    await ctx.send(f'¿Cuánto es {a} + {b}?')
    
    msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
    
    if msg.content == str(a + b):
        await ctx.send('¡Correcto!')
    else:
        await ctx.send(f'Incorrecto, la repuesta era {a + b}')

@bot.command()
async def add_1(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def add_2(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def add_3(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def add_4(ctx, left: int, right: int):
    await ctx.send(left / right)

bot.run("Pon tu token")

