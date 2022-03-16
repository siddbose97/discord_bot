import discord
import time
import asyncio
from pycoingecko import CoinGeckoAPI
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
cg = CoinGeckoAPI()

# TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    dark_price = (cg.get_price(ids="darkcrypto", vs_currencies='usd'))["darkcrypto"]["usd"]
    sky_price = (cg.get_price(ids="darkcrypto-share", vs_currencies='usd'))["darkcrypto-share"]["usd"]
    ratio = "{:.2f}".format(sky_price/dark_price)
    output = f"Current Ratio: {ratio} Sky to Dark"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=output))

client.run(TOKEN)


# async def send_update(priceList, unit, numDecimalPlace=None):
#         if numDecimalPlace == 0:
#             numDecimalPlace = None # round(2.3, 0) -> 2.0 but we don't want ".0"

#         price_now = priceList[unit]
#         price_now = round(price_now, numDecimalPlace)
#         pct_change = priceList[f'{unit}_24h_change']

#         nickname = f'{ticker.upper()} {get_currencySymbol(unit)}{price_now}'
#         status = f'{get_currencySymbol(unit)} 24h: {pct_change:.2f}%'
#         await client.get_guild(config['guildId']).me.edit(nick=nickname)
#         await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
#                                                                name=status))
#         await asyncio.sleep(config['updateFreq'] / numUnit) # in seconds
