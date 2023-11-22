import discord, requests,json,random
from mal import top_list,aniname2,sug,topic_rand
from test3 import desc
def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()
def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data= json.loads(response.text)
    quote=json_data[0]['q']
    return(quote)
token=read_token()
client=discord.Client()
@client.event
async def on_ready():
     print('we have been logged in as {0.user}'.format(client))
     await client.change_presence(activity=discord.Game(name="Type !m for help"))
@client.event
async def on_message(message):
    if message.content.find("!m hello") !=-1:
     await message.channel.send("Hi!")
    elif message.content=="!m top 10":
        embed = discord.Embed(
            title='Top anime from my anime list are:',colour=discord.Colour.gold(),description=top_list(0,10))
        await message.channel.send(embed=embed)
    elif message.content=="!m top 20":
        embed = discord.Embed(
            title='Top anime from my anime list are:',colour=discord.Colour.gold(),description=top_list(10,20))
        await message.channel.send(embed=embed)
    elif message.content=="!m top 30":
        embed = discord.Embed(
            title='Top anime from my anime list are:',colour=discord.Colour.gold(),description=top_list(20,30))
        await message.channel.send(embed=embed)
    elif message.content=="!m top 40":
        embed = discord.Embed(
            title='Top anime from my anime list are:',colour=discord.Colour.gold(),description=top_list(30,40))
        await message.channel.send(embed=embed)
    elif message.content=="!m top 50":
        embed = discord.Embed(
            title='Top anime from my anime list are:',colour=discord.Colour.gold(),description=top_list(40,50))
        await message.channel.send(embed=embed)
    elif message.content == "!m aniname":
        await message.channel.send(aniname2())
    elif message.content == "!m suggest":
        await message.channel.send(sug())
    elif message.content == "!m help":
        embed = discord.Embed(
            title='Bot Commands:',colour=discord.Colour.gold(),description="Bot prefix: !m\nFew useful commands are:")
        embed.set_footer(text="Michiya-Bot is under development more commands to be added later")
        embed.add_field(name='hello', value='Say hello to the bot', inline=True)
        embed.add_field(name='quote', value='To get an inspirational quote', inline=False)
        embed.add_field(name='top{limit}', value='Get a list of top 10 anime till 50 fresh from MyAnimeList\nExample:!m top 10', inline=True)
        embed.add_field(name='aniname', value='Generate a name of random anime character', inline=False)
        embed.add_field(name='suggest', value='Get a random anime suggestion', inline=True)
        embed.add_field(name='search {name of the anime}', value='Get sypnosis of an anime', inline=False)
        embed.add_field(name='choose {A B C}', value='To choose an option from given set of options', inline=True)
        embed.add_field(name='8ball {text}', value='get a random answer for the question', inline=False)
        embed.add_field(name='topic', value='To get a random topic ', inline=True)
        embed.add_field(name='help', value='To check the commands for the bot', inline=False)
        await message.channel.send(embed=embed)
    elif message.content=="!m quote":
            quote = get_quote()
            await message.channel.send('"' + quote + '"')
    elif message.content.startswith("!m search"):
        nm = message.content.split()
        imp = nm[2:]
        word=" ".join(imp)
        x,y,z=desc(word)
        embed = discord.Embed(
            title=z, colour=discord.Colour.gold(), description=x)
        embed.add_field(name="Rating",value=y+" <a:star:833301009580425239>", inline=True)
        await message.channel.send(embed=embed)
    elif message.content.startswith("!m choose"):
        chosen_num=message.content.split()
        chosen_num_imp=chosen_num[2:]
        chosen_num_imp1=" ".join(chosen_num_imp).split()
        choose_rand=random.sample(chosen_num_imp1,1)
        chosen_final=" ".join(choose_rand)
        await message.channel.send(chosen_final)
    elif message.content.startswith("!m 8ball"):
        ball_list=["Most probably","Seems like it","Definitely NOT","If you ask me, no","Sounds good","Try again later","Probably not","Yes! Yes! Yes! Yes! YES!!","No! No! No! No! NO!!"]
        ball_list_l=" ".join(random.sample(ball_list,1))
        await message.channel.send(ball_list_l)
    elif message.content=="!m topic":
        await message.channel.send(topic_rand())
    elif str(message.channel)=="testing" and len(message.attachments)==0:
         await message.channel.purge(limit=1)
    #     if str(message.channel)=="testing" and message.content!=message.attachments:
    #        await message.channel.purge(limit=1)
client.run(token)




