import json

import discord
from discord.ext import commands


class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def plus(self, ctx, arg):
        objective_user_id = str(discord.utils.find(lambda m: m.name == arg[:-5], ctx.channel.guild.members).id)
        command_author_id = str(ctx.author.id)
        print(objective_user_id, command_author_id)
        if objective_user_id == command_author_id:
            await ctx.send('Cannot increment yourself')
        else:
            db = read_json()
            if objective_user_id in db:
                db[objective_user_id]['points'] += 1
            else:
                db[objective_user_id] = {'points': 1, 'golds': None}
            write_json(db)
            await ctx.send(f'Level up, {arg}, (now: {db[objective_user_id]["points"]} points)')

    @commands.command()
    async def minus(self, ctx, arg):
        user_id = str(discord.utils.find(lambda m: m.name == arg[:-5], ctx.channel.guild.members).id)
        if user_id == ctx.author:
            await ctx.send('Cannot decrement yourself')
        else:
            db = read_json()
            if user_id in db:
                db[user_id]['points'] -= 1
                db[user_id]['wallet'] -= 1
            else:
                db[user_id]['points'] = -1
                db[user_id]['wallet'] = 1
            write_json(db)
            await ctx.send(f'Level down, {arg}, (now: {db[user_id]}) points')

    @commands.command()
    async def status(self, ctx):
        member = ctx.author
        db = read_json()
        user_id = str(member.id)
        if db.setdefault(user_id) is None:
            db[user_id] = 0
        await ctx.send(f'{db[user_id]} points')


def read_json():
    with open('db.json') as f:
        return json.load(f)


def write_json(db):
    with open('db.json', mode='w') as f:
        json.dump(db, f)
