import discord
from discord.ext import commands
import random
import os
import csv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
     print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def zaba(ctx, count=5):
     await ctx.send(':frog:' * count)

@bot.command()
async def suma(ctx, a: int, b: int):
     await ctx.send(f'{a} + {b} = {a + b}')

@bot.command()
async def licz(ctx, a: int, w, b: int):
     if w == '+':
        await ctx.send(f'{a} + {b} = {a + b}')
     if w == '-':
          await ctx.send(f'{a} - {b} = {a - b}')
     if w == '*':
          await ctx.send(f'{a} * {b} = {a * b}')
     if w == '/':
          await ctx.send(f'{a} / {b} = {a / b}')

@bot.command()
async def tlumacz(ctx, args):
     lang = {
     "Hello, World" : "Cześć, Świat",
     "Hi" : 'Cześć',
     'Fruit' : "Owoc",
     "Tea" : "Herbata"
     }
     if args in lang:
          await ctx.send(f'Słowo {args} to po polsku {lang[args]}')
     else:
          await ctx.send("Nie ma takiego słowa")

@bot.command()
async def img(ctx):
     with open('images/img2.jpg', 'rb') as f:
          img  = discord.File(f)
          await ctx.send(file=img)

@bot.command()
async def rand_img(ctx):
     img_url = random.choice(os.listdir('images'))
     with open(f'images/{img_url}', 'rb') as f:
          img = discord.File(f)
          await ctx.send(file=img)

@bot.command()
async def ind_img(ctx,index: int):
     img_url = os.listdir('images')[index]
     with open(f'images/{img_url}', 'rb') as f:
          img = discord.File(f)
          await ctx.send(file=img)

@bot.command()
async def bank_account(ctx):
     client_data = [
          {'AccNum' : '1234', 'CtlName' : "Jan Kowalski", 'Balance' : 123, 'Currency' : 'PLN'},
          {'AccNum' : '0001', 'CtlName' : "Anna Nowak", 'Balance' : 1000, 'Currency' : 'EUR'},
          {'AccNum' : '3333', 'CtlName' : "Piotr Nowak", 'Balance' : 5, 'Currency' : 'USD'},
          {'AccNum' : '3364', 'CtlName' : "Logan Paul", 'Balance' : 10230, 'Currency' : 'BTC'},
     ]
     filename = 'clients.csv'
     with open(filename, 'w', newline='', encoding='utf-8') as f:
          fieldnames = client_data[0].keys()
          writer = csv.DictWriter(f, fieldnames=fieldnames)
          writer.writeheader()
          writer.writerows(client_data)
          await ctx.send('Dane zostały zapisane do pliku')
     with open(filename, 'rb') as f:
          file = discord.File(f)
          await ctx.send(file=file)



bot.run('!put discord token here!')