import discord
import random
import json
import os
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Button,View
from numpy import true_divide

os.chdir("D:\Py\RpgTexto\RPGTexto\Recursos")
testingservers = [556910930395529237,824754982104465458,817213798841843783]

class Exploração(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = testingservers, name = "explorar", description = "Exploração :)")
    async def explorarr(self, ctx):

        button = ExplorationView("Explorar")
        view = View()
        view.add_item(button)
        await ctx.respond("Teste", view = view)
       
class ExplorationView(Button):
    def __init__(self, label):
        super().__init__(label=label, style= discord.ButtonStyle.green)
    async def callback(self, interaction):
        await Explorando(interaction)

'''class CombateView(Button):
    def __init__(self):
        super().__init__(label="Combate!!!", style= discord.ButtonStyle.danger, emoji= "🔪")
    async def callback(self, interaction, monster):
        await Combate(interaction, monster)'''
class FugirView(Button):
    def __init__(self):
        super().__init__(label="Fugir!", style= discord.ButtonStyle.blurple, emoji= "🐔")
    async def callback(self, interaction):
        await Fugir(interaction)
            

async def Explorando(ctx):
    Users = await Ler_Coisa("UsersData.json")
    if str(ctx.user.id) not in Users:
        await ctx.response("Se num tem conta.")
        return
    Monster = await Ler_Coisa("Monstros.json")
    MonsterSelec = random.choice(list(Monster))

    em = discord.Embed(title = "Combate", description = "Teste", color = discord.Color.red())
    monstername = Monster[MonsterSelec]["nome"]
    em.add_field(name="Nome:", value= f"{monstername}", inline= False)
    monstervida = Monster[MonsterSelec]["hp"]
    em.add_field(name="HP:", value= f"{monstervida}", inline= False)

    buttonCombate = Button(label="Combate!!!", style= discord.ButtonStyle.danger, emoji= "🔪")
    async def combate_callback(interaction):
        await Combate(interaction, MonsterSelec)
    buttonCombate.callback = combate_callback
    buttonFugir = FugirView()
    view = View()
    view.add_item(buttonCombate)
    view.add_item(buttonFugir) 
    await ctx.response.edit_message(content = None,embed = em, view = view)





async def Combate(ctx, monster):
    Users = await Ler_Coisa("UsersData.json")
    Monster = await Ler_Coisa("Monstros.json")
    playerId = ctx.user.id
    if str(playerId) not in Users:
        await ctx.response("Se num tem conta.")
        return
    
    #----------- Instancias
    monstroInstance = Monster[monster]
    monstroNome = Monster[monster]["nome"]
    monstroDano = Monster[monster]["danoBase"]
    playerDano = Users[str(playerId)]["danoBase"]



    attkMaisRapido = "Player"
    veloCashAlto = Users[str(playerId)]["veloAtk"]
    veloAlto = veloCashAlto
    veloCashBaixo = monstroInstance["veloAtk"]
    turnos = []
    if  Users[str(playerId)]["veloAtk"] < monstroInstance["veloAtk"]:
        attkMaisRapido = "Monstro"
        veloCashAlto = monstroInstance["veloAtk"]
        veloAlto = veloCashAlto
        veloCashBaixo = Users[str(playerId)]["veloAtk"]

    while Users[str(playerId)]["hpAtual"] >= 0:
        print("Se a vida do player for menor ou igual a 0")
        if monstroInstance["hp"] >= 0:
            print(veloCashAlto)
            print(veloCashBaixo)
            while veloCashAlto >= veloCashBaixo:
                veloCashAlto -= veloCashBaixo
                if attkMaisRapido == "Player":
                    monstroInstance["hp"]  -= playerDano
                    turnos.append(f"Você causou {playerDano}")
                else:
                    Users[str(playerId)]["hpAtual"] -= monstroDano
                    print("Causou dano?")
                    turnos.append(f"{monstroNome} te causou {monstroDano}")
                if monstroInstance["hp"] <= 0:
                    print("Morreu")
                    break
            print(str(veloAlto) + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            veloCashAlto = veloAlto 
        else:
            print("Morreu")
            turnos.append(f"{monstroNome} morreu...")
            break

        if attkMaisRapido != "Player":
            monstroInstance["hp"]  -= playerDano
            turnos.append(f"Você causou {playerDano}")
        else:
            Users[str(playerId)]["hpAtual"] -= monstroDano
            print("Dano aplicado")
            turnos.append(f"{monstroNome} te causou {monstroDano}")
    
    ret = "Lista: "
    for x in range(len(turnos)):
        turno = turnos[x]
        ret = ret + f"\n{turno}"
        print(turnos[x])

    await ctx.response.edit_message(content = f"```{ret}```", embed = None, view = None)
            
                    


            










async def Fugir(ctx):
    await ctx.response.edit_message(content = "Você fugiu igual um bosta!", embed = None, view = None)


'''class CombateView(View):
    @discord.ui.button(label="Combate!!", style= discord.ButtonStyle.danger, emoji="🔪")
    async def button_callback(self, button, interaction): 
        
        await interaction.response.edit_message(content = "Explorando...", view = None)'''

async def Ler_Coisa(Coisa):
    if os.path.exists(Coisa):
        with open(Coisa, 'r', encoding='utf-8') as f:
            Coisas= json.load(f)
    return Coisas

def setup(bot):
    bot.add_cog(Exploração(bot))