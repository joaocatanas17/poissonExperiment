import getData
import binomialCoefficient
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np

urlIndex = pd.read_json("C:\\Users\\Joao\\Documents\\GitHub\\poissonExperiment\\teamUrls.json")
urlIndex.set_index("URLName", inplace = True)

teamName = input("What team would you like to analyse?")

URL =urlIndex.loc[teamName, 'URL']

playersTable = getData.fetchDataFromUrl(URL)

listOfPlayers = playersTable['Player']

playersTable.set_index("Player", inplace = True)


#Start of Bernoulli Trial


# We will use stats per 90 as this data is normalised. We will also use xG per shot as the probability of a player scoring with each shot.
# This is labelled as 'npxG/Sh' in our Data Frame.
# We can also use the 'Sh/90' value to determine how many shots a player takes per game, this can be our 'n' in our trial. (We can round up or down depending on the data)

# We have these values for every player in the team so we can build a table with total attempts as columns and goals as rows.

numberOfShots = [1, 2, 3, 4, 5]

goalProbabilityTable = pd.DataFrame(columns = numberOfShots, index = listOfPlayers) # create our table with number of shots as columns and players as rows (index)
goalProbabilityTable.rename_axis('Attempts on goal', axis = 'columns')

# Populate our Table with values
for player in listOfPlayers:
    for number in numberOfShots:
        playerTrial = binomialCoefficient.BinomialCoefficient(number, 1)
        goalProbabilityTable.loc[player, number] = playerTrial.bernoulliTrial(playersTable.at[player, 'npxG/Sh'])

display(goalProbabilityTable) # The table will give us the values of P(Goals = 1) given the amount of shots taken for each player


# We can also use these values to determine the probablity that each player will score at least one goal given any amount of shots taken. For this, we only need to calculate 1 - P(Goals = 0)

goalProbabilityTable_copy = pd.DataFrame(columns = numberOfShots, index = listOfPlayers)
goalProbabilityTable_copy.rename_axis('Attempts on goal', axis = 'columns')

for player in listOfPlayers:
    for number in numberOfShots:
        playerTrial = binomialCoefficient.BinomialCoefficient(number, 0)
        goalProbabilityTable_copy.loc[player, number] = 1 - (playerTrial.bernoulliTrial(playersTable.at[player, 'npxG/Sh']))

goalProbabilityTable.style.background_gradient()

goalProbabilityTable.to_html('temp2.html')

plt.plot(numberOfShots, goalProbabilityTable.loc['Liam Delap'])
plt.plot(numberOfShots, goalProbabilityTable.loc['Sammie Szmodics'])

plt.show()