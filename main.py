import hello
import settings
from settings import *

#paths
path_to_sound = "D:\Programing\python\discord\sound"

@bot.event 
async def on_ready():
	print(f"{FGREEN}[BOT START WORKING]{RESET_ALL}")
	print("-")
	print()

@bot.command()
async def list(ctx):
	if (ctx.message.channel.id == text_channel_id) and (ctx.message.author.id == root_id_1) or (ctx.message.author.id == root_id_2):
		dir_list = os.listdir(path_to_sound) 
		for i in dir_list:
			if i != "hello.mp3":
				text = "" + i
			await ctx.send(text)

#tts
@bot.command(pass_context=True)
async def join(ctx):
	if (ctx.message.channel.id == text_channel_id) and (ctx.message.author.id == root_id_1) or (ctx.message.author.id == root_id_2):
		if (ctx.author.voice):														
			channel = ctx.message.author.voice.channel
			voice = await channel.connect()

			@bot.event
			async def on_message(message):
				if (message.channel.id == text_channel_id) and (message.author.id == root_id_1) or (message.author.id == root_id_2):
					if message.content[0] != "-" and message.content[0] != "$" and (message.author!=bot.user):
						if message.content[0] == '.':
							source = FFmpegPCMAudio(path_to_sound + "\." + message.content[1:] + ".mp3")
							voice.play(source)
						elif message.content[0] != '.':	
							tts = gtts.gTTS(message.content[0:], lang='ru')
							tts.save(path_to_sound + 'hello.mp3')
							source = FFmpegPCMAudio(path_to_sound + 'hello.mp3')
							voice.play(source)
					await bot.process_commands(message)

@bot.command(pass_context=True)
async def leave(ctx):
	if (ctx.message.channel.id == text_channel_id):
		if (ctx.voice_client):
			await ctx.guild.voice_client.disconnect()
			await ctx.send("Ну... я пошел)")
		else:
			await ctx.send("Меня нет в канале")

bot.run(TOKEN)	
