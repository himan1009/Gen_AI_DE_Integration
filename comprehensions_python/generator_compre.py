# memory efficient operations using generator comprehensions

daily_sales = [5, 10, 3, 6, 5, 8, 12, 7, 9, 4, 11, 6, 5, 10, 8]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print("Total cups sold in a day: ", total_cups)