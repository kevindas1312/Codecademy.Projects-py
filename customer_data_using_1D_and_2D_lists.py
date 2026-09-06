first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(first_names)
print(preferred_size, "\n")

customer_data = [['Ainsley','Small',True],['Ben','Large',False],['Chani','Medium',True],['Depak','Medium',False]]
customer_data[2][2] = False
customer_data[1].remove(False)
print(customer_data, "\n")

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

