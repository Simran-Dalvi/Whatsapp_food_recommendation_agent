import pandas as pd
from typing import Dict
from pathlib import Path

MENU = Path("../data/menu.csv")

# def recommend_food(prefrenceces: Dict):
def recommend_food(preference: Dict) -> pd.DataFrame:

    """
    Takes the prefrence as a dictionary.
    comapres it with our csv and 
    Recommends food based on user prefrences.
    """

    df = pd.read_csv(MENU)
    
    # Filter based on veg/ non-veg
    if preference.get("type"):
        df = df[df['type'].str.lower() == preference['type'].lower()]
    
    # Filter based on category
    if preference.get("category"):
        df = df[df['category'].str.lower() == preference['category'].lower()]

    # Filter by budget
    if preference.get("budget"):
        df = df[df["price"] <= preference['budget']]

    # Filter by style
    if preference.get("style"):
        df = df[
            df["style"].str.lower()
            == preference["style"].lower()
        ]

    # return df["dish"].tolist()
    return df.to_dict(orient = "records")



def main()-> None:
    preferences = {
    'type' : 'veg',
    'category' : 'Indian',
    'budget' : 400,
    # 'style' : 'umami'
    }

    menu_df = recommend_food(preferences)
    print(menu_df)



if __name__ == "__main__":
    main()