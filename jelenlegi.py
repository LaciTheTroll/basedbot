from discord_slash import SlashCommand
import datetime
from discord.ext import commands
from datetime import datetime
import discord
import datetime
import requests
from random import choice, randint
import os
import random
import asyncio
import libneko
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
intents = discord.Intents.default()
intents.members = True
x = datetime.datetime.now()
client = commands.Bot(command_prefix=">", intents=intents)
slash = SlashCommand(client, sync_commands=True)

@slash.slash(name="help",description="TFR parancsok")
async def help(ctx):
    await ctx.send("Az eddigi elérhető parancsok.")

###############################################################

@client.command()
async def hitler(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("hitler.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((157, 176))
    wanted.paste(pfp, (30, 26))
    wanted.save("hitlerprofile.jpg")

    await ctx.send(file=discord.File("hitlerprofile.jpg"))

@slash.slash(name="hitler",description="Rosszabb, mint hitler")
async def hitler(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("hitler.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((157, 176))
    wanted.paste(pfp, (30, 26))
    wanted.save("hitlerprofile.jpg")

    await ctx.send(file=discord.File("hitlerprofile.jpg"))

@client.command()
async def fiveman(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("ctrl5man1woman.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((240, 234))  # A kép mérete pxben
    wanted.paste(pfp, (428, 260))  # Ez itt a szélesség / magasság. A szélesség az első
    wanted.save("5man1womanprofile.jpg")

    await ctx.send(file=discord.File("5man1womanprofile.jpg"))

@slash.slash(name="fiveman",description="5 srác 1 lány")
async def fiveman(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("ctrl5man1woman.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((240, 234))  # A kép mérete pxben
    wanted.paste(pfp, (428, 260))  # Ez itt a szélesség / magasság. A szélesség az első
    wanted.save("5man1womanprofile.jpg")
    await ctx.send(file=discord.File("5man1womanprofile.jpg"))

@client.command()
async def slap(ctx, user: discord.Member, user2: discord.Member = None):
    if user == None:
        user == ctx.author
    if user2 == None:
        user2 = ctx.author
    wanted = Image.open("batman.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((291, 251))  # A kép mérete pxben
    wanted.paste(pfp, (809, 321))
    asset = user2.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((291, 251))  # A kép mérete pxben
    wanted.paste(pfp, (497, 115))
    wanted.save("batman1.jpg")
    await ctx.send(file=discord.File("batman1.jpg"))

@slash.slash(name="slap",description="Pofozz fel valakit")
async def slap(ctx, user: discord.Member, user2: discord.Member = None):
    if user == None:
        user == ctx.author
    if user2 == None:
        user2 = ctx.author
    wanted = Image.open("batman.jpg")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((291, 251))  # A kép mérete pxben
    wanted.paste(pfp, (809, 321))
    asset = user2.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((291, 251))  # A kép mérete pxben
    wanted.paste(pfp, (497, 115))
    wanted.save("batman1.jpg")
    await ctx.send(file=discord.File("batman1.jpg"))

@slash.slash(name="hotfood",description="Forróbb, mint az étel")
async def hotfood(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("memememem.png")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((483, 426))  # A kép mérete pxben
    wanted.paste(pfp, (53, 126))  # Ez itt a szélesség / magasság. A szélesség az első
    wanted.save("hot.png")

    await ctx.send(file=discord.File("hot.png"))
    
@client.command()
async def hotfood(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("memememem.png")
    asset = user.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((483, 426))  # A kép mérete pxben
    wanted.paste(pfp, (53, 126))  # Ez itt a szélesség / magasság. A szélesség az első
    wanted.save("hot.png")

    await ctx.send(file=discord.File("hot.png"))

###############################################################

@slash.slash(name="suggest",description="Küldj be egy javaslatot")
async def suggest(ctx, *,suggestion):
    pipa="<:verified:947150019625103420>"
    iksz="<:iksz:947150399935221851>"
    suggestEmbed = discord.Embed(colour = 0xFF0000)
    suggestEmbed.set_author(name=f'Kiadva általa {ctx.author}', icon_url = f'{ctx.author.avatar_url}')
    suggestEmbed.add_field(name = 'Új javaslat!', value = f'{suggestion}')
        
    message = await ctx.send(embed=suggestEmbed)
    await message.add_reaction(f'{pipa}')
    await message.add_reaction(f'{iksz}')

@client.command(aliases=['gay-scanner', 'gayscanner','homo','gayrate','Gayrate','Gay-scanner'])
async def gay_scanner(ctx, *, user: str = None):
        """very mature command yes haha"""
        if not user:
            user = ctx.author.name
            
        await ctx.trigger_typing()

        gayness = randint(0, 100)

        if gayness <= 33:
            gayStatus = choice(["No homo",
                                "Straight-ish",
                                "No homo bro",
                                "Girl-kisser",
                                "Hella straight",
                                "Small amount of Homo detected."])
            gayColor = 0xFFC0CB
        elif 33 < gayness < 66:
            gayStatus = choice(["Possible homo",
                                "My gay-sensor is picking something up",
                                "I can't tell if the socks are on or off",
                                "Gay-ish",
                                "Looking a bit homo",
                                "lol half  g a y",
                                "safely in between for now",
                                "50:50"])
            gayColor = 0xFF69B4
        else:
            gayStatus = choice([
                                "Homo Alert",
                                "My gay-sensor is off the charts",
                                "stinky gay",
                                "big gay",
                                "hella gay",
                                "Yeah, gay","Why are you gay?"])
            gayColor = 0xFF00FF

        meter = "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"

        if gayness <= 10:
            meter = "🏳‍🌈⬛⬛⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 20:
            meter = "🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 30:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 40:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛"
        elif gayness <= 50:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛"
        elif gayness <= 60:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛"
        elif gayness <= 70:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛"
        elif gayness <= 80:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛"
        elif gayness <= 90:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛"
        else:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈"

        emb = discord.Embed(
            description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"{gayness}% gay", inline=False)
        emb.add_field(name="Comment:",
                      value=f"{gayStatus}", inline=False)
        emb.add_field(name="Gay Meter:", value=meter, inline=False)
        emb.set_author(name="Gay Meter",
                       icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
        await ctx.reply(embed=emb)

@client.command()
async def covid(ctx, *, countryName = None):
        try:
            if countryName is None:
                embed=discord.Embed(title=f"asd", colour=0x34568B, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)


            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**COVID-19 státusz:  {country}**!", description="Ez az információ nem mindig élő, ezért előfordulhat, hogy nem pontos!", colour=0x34568B, timestamp=ctx.message.created_at)
                embed2.add_field(name="**Esetek száma**", value=totalCases, inline=True)
                embed2.add_field(name="**Mai esetek**", value=todayCases, inline=True)
                embed2.add_field(name="**Összes halál**", value=totalDeaths, inline=True)
                embed2.add_field(name="**Ma elhunytak**", value=todayDeaths, inline=True)
                embed2.add_field(name="**Felépült**", value=recovered, inline=True)
                embed2.add_field(name="**Aktív**", value=active, inline=True)
                embed2.add_field(name="**Kritikus**", value=critical, inline=True)
                embed2.add_field(name="**Fertőzás / millió**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**Halál / millió**", value=deathsPerOneMillion, inline=True)
                embed2.add_field(name="**Összes teszt**", value=totalTests, inline=True)
                embed2.add_field(name="**Teszt / millió**", value=testsPerOneMillion, inline=True)

                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0x34568B, timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)

@slash.slash(name="covid19",description="Kérj le adatokat a covidról ország szerte(Az ország neve legyen angol)")
async def covid(ctx, *, orszag = None):
        try:
            if orszag is None:
                embed=discord.Embed(title=f"Nem adtál meg országot", colour=0x34568B, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)


            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{orszag}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**COVID-19 státusz:  {country}**!", description="Ez az információ nem mindig élő, ezért előfordulhat, hogy nem pontos!", colour=0x34568B)
                embed2.add_field(name="**Esetek száma**", value=totalCases, inline=True)
                embed2.add_field(name="**Mai esetek**", value=todayCases, inline=True)
                embed2.add_field(name="**Összes halál**", value=totalDeaths, inline=True)
                embed2.add_field(name="**Ma elhunytak**", value=todayDeaths, inline=True)
                embed2.add_field(name="**Felépült**", value=recovered, inline=True)
                embed2.add_field(name="**Aktív**", value=active, inline=True)
                embed2.add_field(name="**Kritikus**", value=critical, inline=True)
                embed2.add_field(name="**Fertőzás / millió**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**Halál / millió**", value=deathsPerOneMillion, inline=True)
                embed2.add_field(name="**Összes teszt**", value=totalTests, inline=True)
                embed2.add_field(name="**Teszt / millió**", value=testsPerOneMillion, inline=True)

                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0x34568B, timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)


###############################################################

@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member: discord.User, *, reason="indok nincs megadva"):
            if member == None or member == ctx.message.author:
                await ctx.channel.send("Nem bannolhatod magad")
                return
            else:
                a=client.get_channel(VIZSGÁLATI NAPLÓ ID)
                banhammer = "<:ban_hammer:947456348382179368>"
                reason = "".join(reason)
                embed = discord.Embed(title=f"Anonymous#0000 Ki lett tiltva",color=0xccffff, timestamp=ctx.message.created_at)
                embed.set_thumbnail(url="https://o.remove.bg/downloads/32d1934c-d5b1-499d-a943-424772808a77/image-removebg-preview.png")
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

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member: discord.User, *, reason="indok nincs megadva"):

            if member == None or member == ctx.message.author:
                await ctx.channel.send("Nem kickelheted magad.")
                return
            else:
                a=client.get_channel(VIZSGÁLATI NAPLÓ ID)
                
                reason = "".join(reason)
                embed = discord.Embed(title=f"{member} Ki lett rúgva",
                                      description=f"\nModerátor:{ctx.author.mention}\nIndok: {reason}",
                                      color=0x34568B, timestamp=ctx.message.created_at)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=member.avatar_url, text=f"{member.name} | {member.id}")

                embed1 = discord.Embed(title=f"{member} Ki lett rúgva",
                                       description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}",
                                       color=0x6699ff, timestamp=ctx.message.created_at)
                embed1.set_thumbnail(url=member.avatar_url)
                embed1.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await a.send(embed=embed1)
                embed2 = discord.Embed(title=f"Ki lettél rúgva innen: {ctx.guild.name}",
                                       description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}",
                                       color=0x6699ff, timestamp=ctx.message.created_at)
                embed2.set_thumbnail(url=member.avatar_url)
                embed2.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await ctx.send(embed=embed)
                await member.send(embed=embed2)

                await asyncio.sleep(0.1)
                await ctx.guild.kick(member, reason=reason)

print(f"Log rendszer aktiválva ekkor: {x.today():%x / %X}\nAdatok:")

@client.event
async def on_member_join(member):
    print(f"{member} Csatlakozott ekkor: {x.today():%x / %X} ")

@client.event
async def on_member_remove(user):
        print(f"{user} Kilépett ekkor: {x.today():%x / %X}")

@client.event
async def on_member_ban(guild, user):
        print(f"{user} bannolva lett ekkor: {x.today():%x / %X} Moderátor:Ismeretlen Indok: Ismeretlen")

@client.event
async def on_message_delete(message):
        a = client.get_channel(LOGCSATORNA IDJE)
        embed = discord.Embed(title = f"Üzenet visszavonva", description = f"{message.content}\n\n**Csatorna:**\n{message.channel.mention}", color = 0xFFFF00, timestamp = datetime.datetime.utcnow())
        embed.set_footer(icon_url = message.author.avatar_url_as(size = 128), text = str(message.author) + ' (' + str(message.author.id) + ')')
        await a.send(embed = embed)

        print(f"{message.author} Vissza vonta üzenetét itt: {message.channel} Üzenet tartalma: {message.content}")

@ban.error
async def on_command_error(ctx, error):
    fejlesztoi=client.get_channel(FEJLESZTOI CHAT ID)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen ban használat, próbáld meg így:", value=f">ban `(felhasználó)` `(indok)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID* \n`Indok:` *Szöveg*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
        await fejlesztoi.send(f"Fejlesztői hiba console: Nincs megadva felhasználó! (Ban parancs) Hibát előhozta:{ctx.message.author}")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó Kitiltása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
        await fejlesztoi.send(f"Fejlesztői hiba console: {ctx.message.author} nem rendelkezik a következő joggal: ban_members (Ban parancs)")

@kick.error
async def on_command_error(ctx, error):
    fejlesztoi=client.get_channel(FEJLESZTOI CHAT ID)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen kick használat, próbáld meg így:", value=f">kick `(felhasználó)` `(indok)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID* \n`Indok:` *Szöveg*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
        await fejlesztoi.send(f"Fejlesztői hiba console: Nincs megadva felhasználó! (Kick parancs) Hibát előhozta:{ctx.message.author}")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó Kidobása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
        await fejlesztoi.send(f"Fejlesztői hiba console: {ctx.message.author} nem rendelkezik a következő joggal: kick_members (Kick parancs)")


client.run("TOKEN")
