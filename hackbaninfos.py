@client.command()
async def banlist(ctx):
    bans = await ctx.guild.bans() #Getting a list of all ban entries
    for ban_entry in bans: #Looping through all entries
        reason = ban_entry.reason #Getting Reason
        loop = [f"{u[1]} ({u[1].id})" for u in bans]
        reason = ban_entry.reason #Getting Reason
        _list = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])
        await ctx.send(f"```ini\n{_list} Indok: {reason}```")
