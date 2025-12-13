import discord
from discord import app_commands
from discord.ext import commands


class DirectMessage(commands.Cog):
    """
    A cog that adds a command to send direct messages (DMs) to users.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Cog loaded: DirectMessage (dm.py)")

    @app_commands.command(
        name="dm", description="Sends a direct message to a user as the bot."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def dm(
        self, interaction: discord.Interaction, member: discord.Member, content: str
    ) -> None:
        """
        /dm [member] [content]
        Sends a private message to the specified member.
        Only admins can use this.
        """
        try:
            server_name = interaction.guild.name
            # Format the message to look official
            message_to_send = (
                f"**Message from the moderators of {server_name}:**\n\n{content}"
            )

            # Send the DM
            await member.send(message_to_send)

            # Confirm to the admin (ephemeral=True means only the admin sees this confirmation)
            await interaction.response.send_message(
                f"The message has been sent to {member.mention}!", ephemeral=True
            )

        except discord.Forbidden:
            # This happens if the user has blocked the bot or disabled DMs
            await interaction.response.send_message(
                "I cannot send DMs to this user. They may have DMs disabled.",
                ephemeral=True,
            )
        except Exception as e:
            print(f"An error occurred in the 'dm' command: {e}")
            await interaction.response.send_message(
                "An error occurred while trying to send the message.", ephemeral=True
            )

    @dm.error
    async def dm_error(
        self, interaction: discord.Interaction, error: app_commands.AppCommandError
    ) -> None:
        """
        Catches errors specifically for the 'dm' command.
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You must have administrator permissions to use this command.",
                ephemeral=True,
            )
        else:
            print(f"An unexpected error occurred in the 'dm' command: {error}")
            await interaction.response.send_message(
                "An unexpected error occurred. Please check the console.",
                ephemeral=True,
            )


async def setup(bot: commands.Bot) -> None:
    """Sets up the DirectMessage cog.

    Args:
        bot (commands.Bot): The bot instance.
    """
    await bot.add_cog(DirectMessage(bot))
