import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Select, View


class SimpleSelectView(View):
    """
    A view that demonstrates a simple select menu.
    """

    @discord.ui.select(
        placeholder="Choose an option",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Option A", description="This is the first option.", emoji="🇦"
            ),
            discord.SelectOption(
                label="Option B", description="This is the second option.", emoji="🇧"
            ),
            discord.SelectOption(
                label="Option C", description="This is the third option.", emoji="🇨"
            ),
        ],
    )
    async def select_callback(self, interaction: discord.Interaction, select: Select) -> None:
        """
        The callback for the select menu. This is called when a user makes a choice.
        """
        # Get the chosen option
        chosen_option = select.values[0]
        # Disable the select menu after a choice has been made
        select.disabled = True
        # Update the message to show the selected option
        await interaction.response.edit_message(
            content=f"You selected: **{chosen_option}**", view=self
        )
        # Send a followup message (ephemeral)
        await interaction.followup.send(
            f"Thanks for selecting {chosen_option}!", ephemeral=True
        )


class SelectorExamples(commands.Cog):
    """A cog for demonstrating discord.ui.Select functionality."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initializes the SelectorExamples cog."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Called when the cog is ready."""
        print("Cog loaded: SelectorExamples")

    @app_commands.command(
        name="select_menu", description="Shows an example of a select menu."
    )
    async def select_menu(self, interaction: discord.Interaction) -> None:
        """Sends a message with a view containing a select menu."""
        view = SimpleSelectView()
        await interaction.response.send_message(
            "This is a select menu example:", view=view
        )


async def setup(bot: commands.Bot) -> None:
    """Sets up the SelectorExamples cog."""
    await bot.add_cog(SelectorExamples(bot))
