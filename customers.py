# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Daniel
#
# REFLECTION
#
# Q1: .get() vs. bracket notation
# I use bracket notation (customer["email"]) when the key MUST exist, such as
# a required field in a record I just built. If it is missing, I want the
# KeyError so the bug is loud instead of hidden. I use .get() when the key
# might legitimately be missing (optional fields, messy imported data, lookup
# tables), because I can supply a safe default and the program keeps running.
# My rule of thumb: required data -> brackets, optional data -> .get().
#
# Q2: Summary dictionary pattern
# This reminds me of a PivotTable or a SUMIF in Excel, where you total values
# grouped by a category such as region. The Python version is more useful for
# large datasets because it makes one pass through the data, can handle
# millions of rows that would slow or crash a spreadsheet, and is repeatable:
# I can rerun the same script on new data instead of rebuilding the pivot by hand.


print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print("name:", customer["name"])
print("email:", customer["email"])
print("tier:", customer["tier"])
print("ytd_spend:", customer["ytd_spend"])
print(customer)

print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "555-123-4567"      # add a new field
print("After adding phone:", customer)

customer["tier"] = "platinum"           # update an existing field
print("After updating tier:", customer)

del customer["email"]                   # delete a field
print("After deleting email:", customer)

print("\n=== Exercise 3: Safe lookup ===")
email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    print(customer["email"])
except KeyError as err:
    print("Using brackets raised KeyError for key:", err)

print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

print("Iterating without .items():")
for item in customer:
    print(item)
# Difference: looping over a dict directly gives only the KEYS. .items() gives
# (key, value) pairs, so I can unpack both in the loop. Without .items() I
# would have to write customer[item] to get each value.

print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price on ${price}: ${final_price:.2f}")

print("\n=== Exercise 6: List of dicts ===")
customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 5200.00},
    {"name": "Bob", "email": "bob@example.com", "tier": "silver", "ytd_spend": 640.75},
    {"name": "Carla", "email": "carla@example.com", "tier": "bronze", "ytd_spend": 120.00},
]
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount on ${purchase}: ${discount_amount:.2f}")

print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} units left (price ${info['price']})")

print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")