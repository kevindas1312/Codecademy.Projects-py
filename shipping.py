weight = 8.4

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20


print(f"{cost_ground:.2f}")

cost_ground_premium = 125.00
print(f"Ground Shipping Premium ${cost_ground_premium:.2f}")

if weight <= 2:
  drone = weight * 4.50
elif weight <= 6:
  drone = weight * 9.00
elif weight <= 10:
  drone = weight * 12.00
else:
  drone = weight * 14.25

print(f"{drone:.2f}")
