import json
import discord
from discord.ext import commands


class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def plus(self, ctx, arg):
        user_id = discord.utils.find(lambda m: m.name == arg[:-5], ctx.channel.guild.members).id
        db = read_json()
        if db.setdefault(user_id) == None:
            db[user_id] = 1
        else:
            db[user_id] += 1
        write_json(db)
        await ctx.send(f'Level up, {arg}, (now: {db[user_id]}) points')

    @commands.command()
    async def minus(self, ctx, arg):
        user_id = discord.utils.find(lambda m: m.name == arg[:-5], ctx.channel.guild.members).id
        db = read_json()
        if db.setdefault(user_id) == None:
            db[user_id] = -1
        else:
            db[user_id] -= 1
        write_json(db)
        await ctx.send(f'Level down, {arg}, (now: {db[user_id]}) points')


def read_json():
    with open('db.json') as f:
        return json.load(f)


def write_json(db):
    with open('db.json', mode='w') as f:
        json.dump(db, f)
