import discord
from discord.ext import commands

CHANNEL_ID = '542204839304626207'
embed = discord.Embed


class Observer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        content = message.content
        channel = message.guild.get_channel(542204839304626207)
        # self.on_message_delete = self.on_message_delete(message)
        await channel.send(content=content, embed=embed)
