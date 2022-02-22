import discord
import json
import os
import random
import asyncio

from discord.ext import commands, tasks

os.chdir("D:\Py\RpgTexto\RPGTexto\Recursos")
client = commands.Bot(command_prefix="!!",  case_insensitive=True)

@client.event
async def on_ready():
    print('Opa! To On!')

@client.command()
async def Perfil(ctx):

    await CriarConta(ctx.author)
    



async def Guardar_Users(Users):
    with open('UsersData.json', 'w', encoding='utf-8') as f:
        json.dump(Users, f, indent= 2,  ensure_ascii= False)

async def Ler_Users():
    if os.path.exists('UsersData.json'):
        with open('UsersData.json', 'r', encoding='utf-8') as f:
            Users= json.load(f)
    return Users


async def CriarConta(autor):
    Users = await Ler_Users()
    if str(autor.author.id) in Users:
        print("Ja está na cadastrado")
        await autor.send("Ja está cadastrado")
        return
    
    await Criar_Conta(autor.author)
    await autor.send("Você foi cadastrado com sucesso")

async def Criar_Conta(autor):
    Users= await Ler_Users()
    if not str(autor.id) in Users:
        print("Não está na lista")
        Users[autor.id] = {
            "id": autor.id,
            "nome": autor.name,
            "dinheiro": 0,
            "inventario": {}
            }
        Guardar_Users(Users)
        return True
    else:
        return False

client.run('ODg4MDg1NzczNTU4MTE2MzYz.YUNkVA.SQkLn6homzrsyBW_qiTbehK-QbU')