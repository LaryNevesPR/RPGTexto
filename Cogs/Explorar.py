import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Button,View


testingservers = [556910930395529237,824754982104465458]

class Exploração(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = testingservers, name = "explorar", description = "Exploração :)")
    async def explorarr(self, ctx):

        view = MyView()
        await ctx.respond("Teste", view = view)
       
class MyView(View):
    @discord.ui.button(label="Dungeon!", style= discord.ButtonStyle.green, emoji="🔪")
    async def button_callback(self, button, interaction): 
        
        await interaction.response.edit_message(content = "Explorando...", view = None)


def setup(bot):
    bot.add_cog(Exploração(bot))