import pandas as pd
from matplotlib import pyplot as plt


"""Read csv file"""
data = pd.read_csv('index.csv')

"""Create dataframe which includes Country, 2001 Legal and 2015 Legal Scores."""
df_fop = pd.DataFrame(data, columns=['Country', '2001 Legal Score', '2015 Legal Score'])

"""Drop null values."""
df_fop.dropna(inplace=True)

"""Adding new column which indicates score change."""
df_fop['Score Change'] = df_fop['2015 Legal Score'] - df_fop['2001 Legal Score']

"""Write this dataframe into a CSV file."""
df_fop.to_csv("Freedom_of_presses_by_countries.csv")

"""Updating the column 'Score Change' by their score changes if score less than 0.0 change by 'more free', 
else 'less free' """
df_fop.loc[(df_fop['Score Change'] < 0.0), 'Score Change'] = 'More Free'
df_fop.loc[(df_fop['Score Change'] != 'More Free'), 'Score Change'] = 'Less Free'
"""Print the new version of the dataframe"""
print(df_fop)

"""Mean of 2001 and 2015 Legal Scores"""
mean_freedom = df_fop.mean(axis=0)
"""Print the both 2001 and 2015 Legal Score columns mean"""
print("\nMean of 2001 Legal Score Column: ", mean_freedom[0])
print("Mean of 2015 Legal Score Column: ", mean_freedom[1])

"""Find the countries that has minimum Legal Scores in 2001"""
min_in_2001 = df_fop[df_fop['2001 Legal Score'] == df_fop['2001 Legal Score'].min()]
print("\n Countries that has minimum Legal Scores in 2001: \n", min_in_2001)

"""Find the count of both more free and less free countries"""
more_free = df_fop[(df_fop['Score Change'] == 'More Free')].count()
print("\n\nThe number of countries that has more free press than 2001: ", more_free[0])
less_free = df_fop[(df_fop['Score Change'] == 'Less Free')].count()
print("The number of countries that has less free press than 2001: ", less_free[0])
print("\n\n")

"""Preparing the data that we are going to use in pie chart"""
t_data = [more_free[0], less_free[0]]

"""Initializing the labels of chart"""
labels = ("More Free", "Less Free")
explode = (0, 0.1)

"""Initialize the pie chart"""
plt.pie(t_data, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)

"""Chart's title"""
plt.title("Press Freedom Change 2001 to 2015 of Countries by Percentage")

"""Show the plot"""
plt.show()

