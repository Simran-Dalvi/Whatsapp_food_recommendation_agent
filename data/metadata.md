# Food Recommendation Dataset Metadata

## Dataset Overview

This dataset contains menu items from multiple cuisines and is designed for use in a food recommendation engine. The dataset supports filtering and recommendation based on cuisine, dietary preference, budget constraints, and flavor profile.

### Dataset Size

* Total Records: 36
* Cuisine Categories: 6
* Dietary Types: 2
* Style Tags: 12

---

## Schema

| Column   | Data Type | Description                                                                    |
| -------- | --------- | ------------------------------------------------------------------------------ |
| dish     | string    | Name of the menu item offered to customers                                     |
| category | string    | Cuisine or food category to which the dish belongs                             |
| price    | integer   | Selling price of the dish in Indian Rupees (₹)                                 |
| diet     | string    | Dietary classification of the dish                                             |
| style    | string    | Primary flavor profile, texture, or eating experience associated with the dish |

---

## Column Definitions

### dish

Unique menu item name.

Examples:

* Paneer Tikka Wrap
* Kimchi Fried Rice
* Chicken Alfredo Pasta

Expected Type:

```text
string
```

---

### category

Represents the cuisine family of the dish.

Allowed Values:

```text
Indian
Chinese
Italian
American
Japanese
Korean
```

Purpose:

Used to recommend dishes matching a user's preferred cuisine.

---

### price

Represents the menu price in Indian Rupees.

Expected Range:

```text
₹160 - ₹550
```

Purpose:

Used for budget-based filtering and ranking.

Example:

```text
180
350
520
```

---

### diet

Represents dietary classification.

Allowed Values:

```text
veg
nonveg
```

Purpose:

Used to satisfy dietary preferences and restrictions.

---

### style

Represents the dominant flavor profile, texture, or eating experience.

Allowed Values:

```text
spicy
cheesy
healthy
protein
comfort
crispy
savory
creamy
umami
light
smoky
herby
```

Purpose:

Used to infer customer cravings and food preferences.

---

## Style Definitions

| Style   | Description                                            |
| ------- | ------------------------------------------------------ |
| spicy   | Hot or chili-forward dishes                            |
| cheesy  | Cheese-based or cheese-dominant dishes                 |
| healthy | Lower-calorie or nutrient-focused dishes               |
| protein | High-protein dishes suitable for fitness-focused users |
| comfort | Rich, satisfying, home-style meals                     |
| crispy  | Crunchy or fried texture                               |
| savory  | Balanced, umami-rich flavor profile                    |
| creamy  | Cream-based or smooth-textured dishes                  |
| umami   | Deep savory flavors common in Japanese cuisine         |
| light   | Easy-to-digest or lighter meals                        |
| smoky   | Grilled, BBQ, or smoked flavor notes                   |
| herby   | Herb-forward dishes with fresh aromatic flavors        |

---

## Intended Use

The dataset is intended for:

* Food recommendation systems
* Restaurant chatbot assistants
* WhatsApp ordering agents
* Menu search applications
* Preference-based filtering systems

---

## Example Query

User Preference:

```json
{
  "category": "Korean",
  "budget": 400,
  "style": "spicy"
}
```

Expected Recommendations:

```json
[
  "Kimchi Fried Rice",
  "Tteokbokki"
]
```

---

## Future Extensions

Potential fields that may be added in later versions:

* calories
* preparation_time
* rating
* allergens
* ingredients
* availability
* restaurant_branch
* popularity_score
* cuisine_region

Version: 1.0
Last Updated: May 2026
