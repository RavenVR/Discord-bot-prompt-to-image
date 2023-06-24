import hikari, lightbulb, random, json, os, openai, requests
from PIL import Image
from io import BytesIO
# Defining the bot
guild_id = guild ID
token = token
bot = lightbulb.BotApp(token=token default_enabled_guilds=guild_id, intents=hikari.Intents.ALL)

# OpenAI token
openai.api_key = 'OPEN AI KEY'


@bot.command
@lightbulb.option("prompt", "The prompt for the AI")
@lightbulb.command("ai-txt-to-image", "Text to image")
@lightbulb.implements(lightbulb.SlashCommand)
async def aiimggenerator(ctx):
    PROMPT = str(ctx.options.prompt)
    await ctx.respond("loading...")
    
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
    )
    response = requests.get(response['data'][0]['url'])
    await ctx.edit_last_response(response.content)

# Start the bot
bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name=f"random number: {random.randint(1,100)}",
        type=hikari.ActivityType.WATCHING,
    ),
)
