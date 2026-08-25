hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for a in prices :
  total_price += i
  i+=1
print("Total price : ", total_price)

average_price = (total_price/len(prices))
print("Average Haircut Price: " , round(average_price,2))

new_prices = [price-5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)) :
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue : ", round(total_revenue,2))

average_daily_revenue = total_revenue/7
print("Average Daily Revenue :", average_daily_revenue)

cuts_under_30 = [i for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under 30 :", cuts_under_30)

cuts_over_30 = [b for b in range(len(hairstyles)) if new_prices[i] >30]
print("Cuts over 30 :", cuts_under_30)
