import discord # noqa
import os
import event
import managedMessages
from utility import loadData
from constants import Constants
from discord.ext import commands

# TODO: Decide if I want to use descriptors for agruments in funcs and mehts.
# example def doSomething(arg1: str, arg2: int)

if __name__ == "__main__":
    """Instanciate the discord.py client/bot and load event data if it exists.
    """

    # Instanciate the client and set the command prefix.
    client = commands.Bot(Constants.CMD_PREFIX)

    # Remove the default help command.
    client.remove_command('help')

    # TODO: Deserialize orgEvent data.
    # Create empty list that will hold all the event objects
    client.orgEvents = []
    # Instanciate managedMessages class and store in client.
    client.managedMessages = managedMessages.ManagedMessages()
    # client.orgEvents = loadData('eventData.pkl')
    # if client.orgEvents is None:
    #     client.orgEvents = []
    #     print('No record found. Starting clean.')
    # else:
    #     # Check if all objects from loaded data are event.Event instances.
    #     for item in client.orgEvents:
    #         if not isinstance(item, event.Event):
    #             client.orgEvents = []
    #             print('Error in data file. Starting clean.')
    #             break


# Check functions
def isAdmin(ctx):
    return ctx.author.id == 312381318891700224

# Events
@client.event
async def on_ready():
    print('Ready.')

# Commands
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')


@client.command()
@commands.check(isAdmin)
async def checkTest(ctx):
    await ctx.send('Yes, you are admin')

# Load cogs
for filename in os.listdir('./cogs'):
    # Files in exclusion list will not be loaded.
    exclusionList = [
        '__init__.py',
        'experimentalCog.py',
        'messageWithoutCommand.py',
        'asyncCog.py']
    if filename not in exclusionList:
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            # TODO: Add try catch?


# TODO: Make sure every assignments are encapsulated somehow to conform to
# sphinx documentation.

# TODO: BEFORE BOT CAN BE INVITED TO OFFICIAL SERVER A NEW TOKEN MUST BE MADE
# Get client token from file.
token = loadData('token.json')
# Run client by passing in token.
client.run(token)
