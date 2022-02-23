import discord
import json
import os
import random
import asyncio

from discord.ui import Button
from discord.ext import commands, tasks
from numpy import true_divide

os.chdir("D:\Py\RpgTexto\RPGTexto\Recursos")
client = discord.Bot(command_prefix="!!",  case_insensitive=True)

for filename in os.listdir("D:\Py\RpgTexto\RPGTexto\Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")

testingservers = [556910930395529237,824754982104465458]

@client.event
async def on_ready():
    print('Opa! To On!')

@client.slash_command(guild_ids = testingservers, name = "perfil", description = "Visualizar o Perfil")
async def perfil(ctx):
    await CriarConta(ctx)
    Users = await Ler_Users()

    perfilDinehiro = Users[str(ctx.author.id)]["dinheiro"]
    hpmax = Users[str(ctx.author.id)]["hpMax"]
    hpatual = Users[str(ctx.author.id)]["hpAtual"]
    manamax = Users[str(ctx.author.id)]["manaMax"]
    manaatual = Users[str(ctx.author.id)]["manaAtual"]

    avatar = ctx.author.avatar
    
    embed = discord.Embed(title = f"{ctx.author.name}", description = "Seu perfil", color = discord.Color.dark_green())
    
    embed.set_author(name = "Perfil", icon_url="https://truth.bahamut.com.tw/s01/202107/e32881d802fb00c6ffbc857148fd8a0b.JPG")
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="Nome:", value= f"{ctx.author}", inline= False)
    embed.add_field(name="Hp:", value= f"{hpatual}/{hpmax}", inline= True)
    embed.add_field(name="Mana:", value= f"{manaatual}/{manamax}", inline= True)
    embed.add_field(name="Dinheiro:", value= f"${perfilDinehiro}", inline= False)
    
    await ctx.respond(embed=embed)



async def Guardar_Users(Users):
    with open('UsersData.json', 'w', encoding='utf-8') as f:
        json.dump(Users, f, indent= 2,  ensure_ascii= False)


async def Ler_Users():
    if os.path.exists('UsersData.json'):
        with open('UsersData.json', 'r', encoding='utf-8') as f:
            users= json.load(f)
    return users


async def CriarConta(ctx):
    Users = await Ler_Users()
    if str(ctx.author.id) in Users:
        print("Ja está na cadastrado")
        return
    
    await Criar_Conta(ctx.author)
    await ctx.respond("Você foi cadastrado com sucesso")

async def Criar_Conta(autor):
    Users= await Ler_Users()
    if not str(autor.id) in Users:
        print("Não está na lista")
        Users[autor.id] = {
            "id": autor.id,
            "nome": autor.name,
            "dinheiro": 0,
            "hpMax": 100,
            "hpAtual": 100,
            "manaMax": 50,
            "manaAtual": 50,
            "defesaBase": 2,
            "danoBase": 10,
            "inventario": {}
            }
        await Guardar_Users(Users)
        return True
    else:
        return False

client.run('ODg4MDg1NzczNTU4MTE2MzYz.YUNkVA.SQkLn6homzrsyBW_qiTbehK-QbU')