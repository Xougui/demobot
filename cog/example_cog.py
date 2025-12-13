import discord
from discord import app_commands
from discord.ext import commands


class Exemple(commands.Cog):
    """
    An example cog to demonstrate the basic structure of a module.
    A 'Cog' is a class that groups commands and listeners together.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """
        The constructor method.
        It runs when the Cog is loaded.

        Args:
            bot (commands.Bot): The instance of the bot.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        A listener event.
        This specific function runs when the bot is fully ready and online.
        """
        print("Cog loaded: cog_example")

    @app_commands.command(name="example", description="An example slash command")
    async def example(self, interaction: discord.Interaction) -> None:
        """
        A simple slash command.
        Responds to /example with a message.
        """
        # interaction.response.send_message is used to reply to the command.
        await interaction.response.send_message("This is an example command!")


# This setup function is MANDATORY for every extension/cog file.
# It tells the bot how to load this specific cog.
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Exemple(bot))
