# https://youtu.be/vQw8cFfZPx0?t=697
# example code
from discord.ext import commands
import discord

import psutil
import sys
class ServerStatus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx):
        """
        Gets server status
        ctx: discord.Context
        """
        embed = discord.Embed(title="Server Status", type="rich")
        vmem = psutil.virtual_memory()
        embed.add_field(name="RAM Usage", value=f"{round(vmem.used/1000000000, 2)}GB out of {round(vmem.total/1000000000, 2)}GB")
        embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent()}%")
        embed.add_field(name="Python information", value=sys.version, inline=True)
        embed.add_field(name="Platform information", value=open("/etc/os-release", "r").read().split("\n")[0].split('"')[1], inline=True)
        await ctx.send(embed=embed)


# setup function also is good
def setup(client):
    client.add_cog(ServerStatus(client))
