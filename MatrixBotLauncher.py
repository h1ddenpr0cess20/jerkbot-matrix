import jerkbot as jb
import openai

openai.api_key = "API_KEY"
server = "https://matrix.org" #not tested with other servers
token = "TOKEN" #Matrix access token found somewhere on settings page in element
username = "USERNAME"
password = "PASSWORD"
channel = "#CHANNEL:SERVER.org"  
personality = "a sarcastic jerk"

#create AIbot and start it
bot = jb.AIbot(server, token, username, password, channel, personality)
bot.start()

input("BOT RUNNING.  Press Enter to exit") #prevents the program from exiting
    
bot.stop() #logs out
