import discordSuperUtils
from discord.ext import commands


bot = commands.Bot(command_prefix='-')
MusicManager = discordSuperUtils.MusicManager(bot)


@bot.event
async def on_ready():
    print('Music manager is ready.', bot.user)


@MusicManager.event()
async def on_music_error(ctx, error):
    if isinstance(error, discordSuperUtils.NotConnected):
        await ctx.send("Client not connected to a voice channel.")

    elif isinstance(error, discordSuperUtils.NotPlaying):
        await ctx.send("Client is not playing anything currently")

    else:
        raise error


@MusicManager.event()
async def on_play(ctx, player):
    await ctx.send(f"Playing {player}")


@bot.command()
async def leave(ctx):
    if await MusicManager.leave(ctx):
        await ctx.send("Left Voice Channel Lol Gang Shit")


@bot.command()
async def np(ctx):
    if player := await MusicManager.now_playing(ctx):
        await ctx.send(f"Currently playing: {player}")


@bot.command()
async def join(ctx):
    if await MusicManager.join(ctx):
        await ctx.send("Joined Voice Channel Lol Gang Shit!")


@bot.command()
async def play(ctx, *, query: str):
    player = await MusicManager.create_player(query)
    await MusicManager.queue_add(player=player, ctx=ctx)

    if not await MusicManager.play(ctx):
        await ctx.send("Added to queue")


@bot.command()
async def volume(ctx, volume: int):
    await MusicManager.volume(ctx, volume)

bot.run("ODExMzMyMDA4Njc2Mjk0NjY3.YCwp0A.wZGOn7lJEFF8IT2SHHd6jSEejA0")
