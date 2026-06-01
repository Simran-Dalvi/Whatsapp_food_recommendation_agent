import pandas as pd
from typing import Any
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MENU_PATH = BASE_DIR / "data" / "menu.csv"
MENU_DF = pd.read_csv(MENU_PATH)

# def recommend_food(prefrenceces: Dict):
def recommend_food(preference: dict[str, Any]) -> list[str]:

    """
    Filter menu items based on user preferences.

    Args:
        preferences: Dictionary containing user preferences such as category, type, budget, and style.

    Returns:
        List of matching dish names
    """

    df = MENU_DF.copy()
    
    # Filter based on veg/ non-veg
    if preference.get("diet"):
        df = df[df['diet'].str.lower() == preference['diet'].lower()]
    
    # Filter based on category
    if preference.get("category"):
        df = df[df['category'].str.lower() == preference['category'].lower()]

    # Filter by budget
    if preference.get("budget"):
        df = df[df["price"] <= int(preference['budget'])]

    # Filter by style
    if preference.get("style"):
        df = df[
            df["style"].str.lower()
            == preference["style"].lower()
        ]

    return df["dish"].tolist()
    # return df.to_dict(orient = "records")



def main()-> None:
    preferences = {
    'diet' : 'veg',
    'category' : 'Indian',
    'budget' : 400,
    # 'style' : 'umami'
    }

    menu_df = recommend_food(preferences)
    print(menu_df)



if __name__ == "__main__":
    main()