'''Dans cet exemple on va voir dans quel cas utiliser une followup.send ou une response 
dans le cadre d'une interaction ( commande slash )

Pour cela on va simplement créer une commande slash @app_commands.command 
avec comme nom "followup_or_response" qui enverra un message de réponse et une followup.send
'''


# tout d'abord : les imports :
import discord
from discord.ext import commands
from discord import app_commands


class FollowupOrResponse(commands.Cog):
    '''Simple classe pour nos commandes'''

    def __init__(self, bot: commands.Bot): # initialisation de la classe ( obliatoire )
        self.bot = bot 
    

    # Attention ici : intendation a respecter, il ne faut pas coder dans la fonction 
    # Ni en dehors de la classe

    @app_commands.command(
            name="followup_or_response", 
                          description="Example de followup.send ou response.send_message"
                          )
    async def followup_or_response(self, interaction: discord.Interaction): # discord.Interaction est l'objet qui va contenir les infos de l'interaction
        '''Fonction qui enverra un message de réponse et une followup.send'''

        # On répond a la commande avec un message de réponse avec defer ( on indique une réflexion)

        await interaction.response.defer(ephemeral=True) # ON AS UTIILISER DEFER POUR POUVOIR ENVOYER UNE FOLLOWUP APRES
        # Dans ce cas on à répondu a l'interaction avec un message de "réflexion" ( thinking... )
        # mais on aurait pu aussi envoyer directement un message avec response.send_message
        # await interaction.followup.send("Ceci est un message de réponse !")
        # Donc ici on informe l'utilisateur que la commande est en cours de traitement
        # et on va devoir répondre 
        # MAIS PAS AVEC await interaction.response.send_message
        # Car on a déjà répondu a l'interaction avec defer
        # on envoie donc une followup.send :

        # On envoie un message de followup ( visible uniquement par l'utilisateur qui a utilisé la commande )
        await interaction.followup.send("Ceci est un message de followup !", ephemeral=True)

        # On peut envoyer AUTANT DE FOLLOWUP QUE L'ON VEUT ! 
        # Mais il faut obligatoirement avoir répondu a l'interaction AVANT avec response.send_message ou response.defer
        await interaction.followup.send("Ceci est un second message de followup !", ephemeral=True)
        await interaction.followup.send("Ceci est un troisième message de followup !", ephemeral=True)
        # ...


async def setup(bot: commands.Bot): # fonction setup obligatoire dans un cog
    await bot.add_cog(FollowupOrResponse(bot)) # on ajoute la classe du cog au bot