def units(prev, curr):
    return curr - prev

def energy_cost(u):
    if u <= 100:
        return u * 10
    elif u <= 200:
        return 1000 + (u - 100) * 15
    elif u <= 300:
        return 2500 + (u - 200) * 22
    elif u <= 700:
        return 4700 + (u - 300) * 30
    else:
        return 16700 + (u - 700) * 35

def make_challan(name, ref, prev, curr, u, energy, fixed, tv, gst, total, late_total):
    line = "-" * 42
    text = "########## IESCO - BIJLI BILL ##########\n"
    text += f"Consumer : {name}   Ref: {ref}\n"
    text += f"Reading  : {prev} -> {curr}\n"
    text += f"Units consumed {u}\n"
    text += line + "\n"
    text += f"{'Energy cost (slabs)':<28}Rs {energy:>9.2f}\n"
    text += f"{'Fixed / meter charges':<28}Rs {fixed:>9.2f}\n"
    text += f"{'TV license fee':<28}Rs {tv:>9.2f}\n"
    text += f"{'GST (17% of energy)':<28}Rs {gst:>9.2f}\n"
    text += line + "\n"
    text += f"{'Payable within due date':<28}Rs {total:>9.2f}\n"
    text += f"{'Payable after due date':<28}Rs {late_total:>9.2f}\n"
    text += "Due date : 2026-10-15\n"
    text += "#" * 42 + "\n"
    return text

consumers = []

while True:
    name = input("Consumer name: ")
    ref = input("Reference number: ")

    try:
        prev = float(input("Previous reading: "))
        curr = float(input("Current reading: "))
    except ValueError:
        print("Invalid reading! Please enter numbers only.\n")
        continue

    if curr < prev:
        print("Current reading cannot be less than previous. Skipping.\n")
        continue

    u = units(prev, curr)
    energy = energy_cost(u)
    fixed = 200
    tv = 35
    gst = energy * 0.17
    total = energy + fixed + tv + gst
    late_total = total * 1.10

    challan = make_challan(name, ref, prev, curr, u, energy, fixed, tv, gst, total, late_total)
    print(challan)

    file = open("bills.txt", "a")
    file.write(challan + "\n")
    file.close()

    consumer = {"name": name, "ref": ref, "units": u, "total": total}
    consumers.append(consumer)

    again = input("Bill another consumer? (y/n): ")
    if again.lower() != "y":
        break

total_units = 0
total_revenue = 0
for c in consumers:
    total_units += c["units"]
    total_revenue += c["total"]

print("Total units billed:", total_units)
print(f"Total revenue: Rs {total_revenue:.2f}")