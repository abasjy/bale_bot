from balethon import Client
import requests as r

token = "1318129827:exhwk4RrgrIOYUA3jeq7BhNQ1FJCq6Xe2PUBcnjK"
bot = Client(token)

@bot.on_message()
async def start(message):
    if message.text == "/start":
     await message.reply("""سلام دوست عزیز به ربات H_O خوش آمدی❤   
                         دستورات من :
                         جوک 
                         دلار
                         دانستنی""")
     

    if message.text == "جوک":
        jok = r.get("https://alanbecker.pythonanywhere.com/webservices/jok").json()['result']
        await message.reply(f"😂جوک برای شما: {jok}")
        
        
    if message.text == "دلار":
        doler = r.get("https://alanbecker.pythonanywhere.com/webservices/dollar").json()['result']
        await message.reply(f"💵قیمت دلار :» {doler}")
        
        
    if message.text == "دانستنی":
        danestani = r.get("https://alanbecker.pythonanywhere.com/webservices/danestani").json()['result']
        await message.reply(f"❓دانستنی برای شما: {danestani}")       
    
    
bot.run()

