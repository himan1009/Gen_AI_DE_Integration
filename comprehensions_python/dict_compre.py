tea_prices_inr = {
    "Masala Chai": 30,
    "Green Tea": 25,
    "Lemon Tea": 20,
    "Elaichi Chai": 35,
    "Ginger Tea": 40
}


tea_prices_usd = {tea: price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)