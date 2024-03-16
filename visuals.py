#The dataset used in this model has been modified. The original is found on Kaggle.
#Link is https://www.kaggle.com/datasets/thedevastator/uncovering-state-by-state-car-theft-trends-in-20
#Credit goes to Joe Boutros for providing this dataset.

import matplotlib.pyplot as plt
import pandas as pd


def bar_graph_thefts():
    # Creating the dataframe
    df = pd.read_csv(r'C:\Users\adjma\PycharmProjects\CapstoneWGU964\2015_State_Top10Report_wTotalThefts.csv')

    # Convert the 'Thefts' column to numeric if it's not already
    df['Thefts'] = pd.to_numeric(df['Thefts'], errors='coerce')

    # Filter dataframe to select only certain rows based on a condition
    selected_df = df[df['Thefts'] > 500]  #Selecting rows where Thefts > 500

    # Enlarge the figure size
    plt.figure(figsize=(12, 8))

    # Bar graph
    plt.bar(selected_df['Make/Model'], selected_df['Thefts'])

    #Tile
    plt.title("# of Thefts by Make and Model")

    #Setting the X and Y labels
    plt.xlabel('Make/Model')
    plt.ylabel('Thefts')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def bar_graphs_states():
    df = pd.read_csv(r'C:\Users\adjma\PycharmProjects\CapstoneWGU964\2015_State_Top10Report_wTotalThefts.csv')

    df['Thefts'] = pd.to_numeric(df['Thefts'], errors='coerce')

    # Drop rows with NaN values in 'Thefts' column
    df = df.dropna(subset=['Thefts'])

    #Get the number of thefts by state and sort
    thefts_by_state = df.groupby('State')['Thefts'].sum()
    states_sorted = thefts_by_state.sort_values(ascending=False)

    #Find top ten states with the most thefts
    top_states = states_sorted.head(10)

    # Enlarge the figure size
    plt.figure(figsize=(12, 8))

    # Bar graph
    plt.bar(top_states.index, top_states.values)

    #Title
    plt.title('States with the Most Thefts')

    #X and Y labels
    plt.xlabel('State')
    plt.ylabel('Number of Thefts')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def pie_chart_years():
    df = pd.read_csv(r'C:\Users\adjma\PycharmProjects\CapstoneWGU964\2015_State_Top10Report_wTotalTheftsandModelYear.csv')

    # Convert the 'Model Year' column to numeric if it's not already
    df[('Model Year')] = pd.to_numeric(df['Model Year'], errors='coerce')

    model_years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
                   2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                   2010, 2011, 2012, 2013, 2014, 2015]

    decades = {
    "1990s": sum(1990 <= year < 2000 for year in model_years),
    "2000s": sum(2000 <= year < 2010 for year in model_years),
    "2010s": sum(2010 <= year < 2020 for year in model_years)
    }

    total_vehicles = len(df['Model Year'])
    percentages = {decade: (count / total_vehicles) * 100 for decade, count in decades.items()}

    labels = percentages.keys()
    sizes = percentages.values()
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Percentage of Stolen Vehicles by Decade')
    plt.show()

