async def stages(self, ctx, *, nothing = None, where: discord.TextChannel):
    #get regular, ranked and league
    regular_embed = discord.Embed(name = "Regular Battle",colour=0x000000)
    regular_embed.add_field(title="Now",content=f"{regular[0]["stage_a"]}\n{regular[0]["stage_b"]}")