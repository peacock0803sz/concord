import os

import discord.ext.commands
import observer
import point

if __name__ == '__main__':
    BOT_TOKEN = os.environ['CONCORD_TOKEN']
    bot = discord.ext.commands.Bot('/')
    # bot.add_cog(observer.Observer(bot))
    bot.add_cog((point.Count(bot)))

    bot.run(BOT_TOKEN)
