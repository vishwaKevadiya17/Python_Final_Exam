
print("Welcome to Inventory List Analyzer!")

items = []
quantity_dict = {}
categories = set()

# Input items
while True:
    name = input("\nEnter item name: ").title()
    category = input("Enter category: ").lower()
    quantity = int(input("Enter quantity: "))

    item = (name, category, quantity)

    items.append(item)
    quantity_dict[name] = quantity
    categories.add(category)

    choice = input("\nDo you want to add more items? (y/n): ")

    if choice.lower() != "y":
        break

# Inventory Summary
print("\n========== INVENTORY SUMMARY ==========")

total_items = len(items)
total_quantity = sum(quantity_dict.values())
average = total_quantity / total_items

print("\nTotal Different Items:", total_items)
print("Explanation: You entered", total_items,
      "different items:", ", ".join(quantity_dict.keys()))

print("\nTotal Quantity in Stock:", total_quantity)
print("Explanation: Sum of all quantities:",
      " + ".join(str(q) for q in quantity_dict.values()),
      "=", total_quantity)

print("\nAverage Quantity per Item:", round(average, 2))
print("Explanation: Average =", total_quantity,
      "total /", total_items, "items")

# Most and least stocked items
most_stocked = max(quantity_dict, key=quantity_dict.get)
least_stocked = min(quantity_dict, key=quantity_dict.get)

print("\nMost Stocked Item:", most_stocked,
      "(", quantity_dict[most_stocked], "units)")
print("Explanation:", most_stocked,
      "has the highest quantity among all items.")

print("\nLeast Stocked Item:", least_stocked,
      "(", quantity_dict[least_stocked], "units)")
print("Explanation:", least_stocked,
      "has the lowest quantity.")

# Unique categories
print("\nUnique Categories (lowercase):",
      sorted(categories))
print("Explanation: Categories are taken from user input")
print("and converted to lowercase.")
print("No duplicates are shown here.")

# Sort items by quantity
sorted_items = sorted(items, key=lambda x: x[2], reverse=True)

print("\n----------------------------------------")
print("Items Sorted by Quantity (High to Low):\n")

for i, item in enumerate(sorted_items, start=1):
    print(str(i) + ".", item[0], "-", item[2], "units")

print("\nExplanation: Items are sorted using the quantity")
print("field from highest to lowest.")

# Sort categories alphabetically
print("\n----------------------------------------")
print("Categories in Alphabetical Order:\n")

for i, category in enumerate(sorted(categories), start=1):
    print(str(i) + ".", category)

print("\nExplanation: The set of unique categories was")
print("sorted alphabetically for display.")

print("\n========== END OF REPORT ==========")
