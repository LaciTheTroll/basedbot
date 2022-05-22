import discord
from discord.ext import commands
from discord_slash import SlashCommand #https://pypi.org/project/discord-py-slash-command/

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="prefix", intents=intents)
slash = SlashCommand(client, sync_commands=True) # Slashez újra kell hívni a botot és adni kell neki aplikáció cuccot ami az invite link kérszítésnél lesz

@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member: discord.User, *, reason="indok nincs megadva"):

            if member == None or member == ctx.message.author:
                await ctx.channel.send("Nem bannolhatod magad")
                return
            else:
                a=client.get_channel(971856125467181148)
                banhammer = "<:ban_hammer:947456348382179368>"
                reason = "".join(reason)
                embed = discord.Embed(title=f"{member} Ki lett tiltva",
                                      description=f"\nModerátor:{ctx.author.mention}\nIndok: {reason}\nIdő: ∞",
                                      color=0x34568B, timestamp=ctx.message.created_at)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=member.avatar_url, text=f"{member.name} | {member.id}")

                embed1 = discord.Embed(title=f"{member} Ki lett tiltva",
                                       description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}\nIdő: ∞",
                                       color=0x6699ff, timestamp=ctx.message.created_at)
                embed1.set_thumbnail(url=member.avatar_url)
                embed1.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await a.send(embed=embed1)
                embed2 = discord.Embed(title=f"Bannolva lettél innen: {ctx.guild.name} {banhammer}",
                                       description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}\nIdő: ∞",
                                       color=0x6699ff, timestamp=ctx.message.created_at)
                embed2.set_thumbnail(url=member.avatar_url)
                embed2.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await ctx.send(embed=embed)
                await member.send(embed=embed2)

                await asyncio.sleep(0.1)
                await ctx.guild.ban(member, reason=reason)

client.run("TOKEN")
