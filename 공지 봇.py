import discord 

everyone = True
client = discord.Client()

@client.event
async def on_connect():
    for emoji in client.emojis:
        print(emoji)


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == (":📢:"):
        if str(user.id) == str(383584934104924170):
            if everyone == True:
                h = '@everyone'
            else:
                h = ''
            await reaction.message.remove_reaction(reaction.emoji, user)
            embed = discord.Embed(title= ':📢:ㅣ공지 사항', description=(f'{reaction.message.content}'),colour=0x594841)
            embed.set_author(name=client.get_user(int(383584934104924170)).name, icon_url=client.get_user(int(383584934104924170)).avatar_url)
            embed.set_footer(text='개발자ㅣRampaka')
            await client.get_channel(int(602891885157023774)).send(h,embed=embed)

    if str(reaction.emoji) == (":🗑:"):
        if str(user.id) == str(383584934104924170):
            await reaction.message.delete()


@client.event
async def on_message(message):
    if message.channel.id == 채널 아이디:
        if message.author.id == 유저 아이디:
            await message.add_reaction(":📢:")
            await message.add_reaction(":🗑:")

client.run('NzgxOTE5MzMxNjQ1OTE1MTQ3.X8EpIA.17clwaL1aFCHzm4OBaVw3Bv28rk')