favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai",
]


unique_chais = {chai for chai in favorite_chais if len(chai)>8}
print(unique_chais)


recipies = {
    "Masala Chai": ["ginger", "cardamom", "cinnamon"],
    "Green Tea": ["green tea leaves", "water"],
    "Lemon Tea": ["lemon", "tea leaves", "water"]
}

unique_recipies = {spice for ingredients in recipies.values() for spice in ingredients}
print(unique_recipies)