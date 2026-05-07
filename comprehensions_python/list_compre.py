menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Ginger Tea",
    "Iced Peach Tea",
    "Green Tea"
]


iced_tea = [tea for tea in menu if tea.startswith("Iced")]
print(iced_tea)

