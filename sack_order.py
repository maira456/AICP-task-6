# Constants
COST_CEMENT = 3
COST_GRAVEL = 2
COST_SAND = 2
SPECIAL_PACK_CEMENT = 1
SPECIAL_PACK_SAND = 2
SPECIAL_PACK_GRAVEL = 2
SPECIAL_PACK_PRICE = 10
WEIGHT_LIMITS = {
    'C': (24.9, 25.1),
    'G': (49.9, 50.1),
    'S': (49.9, 50.1)
}

# Function to check the contents and weight of a single sack
def check_single_sack():
    while True:
        contents = input("\n\t\tEnter the contents (C for cement, G for gravel, S for sand): ")
        if contents not in WEIGHT_LIMITS:
            print("Invalid contents. Please enter C, G, or S.")
            continue

        weight_message = f"\n\t\tEnter the weight of the {contents} sack in kilograms ({WEIGHT_LIMITS[contents][0]} to {WEIGHT_LIMITS[contents][1]}): "
        try:
            weight = float(input(weight_message))
            if not WEIGHT_LIMITS[contents][0] < weight < WEIGHT_LIMITS[contents][1]:
                print(f"Weight out of range. Please enter a weight between {WEIGHT_LIMITS[contents][0]} and {WEIGHT_LIMITS[contents][1]}.")
                continue

            print(f"Accepted sack - Contents: {contents}, Weight: {weight} kg")
            return contents, weight
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to check a customer's order for delivery
def check_customer_order():
    total_weight = 0
    rejected_sacks = 0

    num_cement = int(input("Enter the number of sacks of cement: "))
    num_gravel = int(input("Enter the number of sacks of gravel: "))
    num_sand = int(input("Enter the number of sacks of sand: "))

    for _ in range(num_cement):
        sack = check_single_sack()
        if sack is None:
            rejected_sacks += 1
        else:
            total_weight += sack[1]

    for _ in range(num_gravel):
        sack = check_single_sack()
        if sack is None:
            rejected_sacks += 1
        else:
            total_weight += sack[1]

    for _ in range(num_sand):
        sack = check_single_sack()
        if sack is None:
            rejected_sacks += 1
        else:
            total_weight += sack[1]

    print(f"Total weight of the order: {total_weight} kg")
    print(f"Number of rejected sacks: {rejected_sacks}")

    return total_weight, num_cement, num_gravel, num_sand

# Function to calculate the price for a customer's order
def calculate_order_price(total_weight, num_cement, num_gravel, num_sand):
    num_special_packs = min(
        num_cement // SPECIAL_PACK_CEMENT,
        num_sand // SPECIAL_PACK_SAND,
        num_gravel // SPECIAL_PACK_GRAVEL
    )

    regular_price = (num_cement * COST_CEMENT + num_gravel * COST_GRAVEL + num_sand * COST_SAND) - num_special_packs * SPECIAL_PACK_PRICE
    print(f"Regular price for the order: ${regular_price}")

    if num_special_packs > 0:
        new_price = regular_price - num_special_packs * SPECIAL_PACK_PRICE
        amount_saved = num_special_packs * SPECIAL_PACK_PRICE
        print(f"Discount applied: ${SPECIAL_PACK_PRICE} for each special pack")
        print(f"New price for the order: ${new_price}")
        print(f"Amount saved: ${amount_saved}")

# Main program
while True:
    print("\n============= Menu ==============:")
    print("\t\t\t1. Check the contents and weight of a single sack")
    print("\t\t\t2. Check a customer's order for delivery")
    print("\t\t\t3. Calculate the price for a customer's order")
    print("\t\t\t4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        check_single_sack()
    elif choice == '2':
        total_weight, num_cement, num_gravel, num_sand = check_customer_order()
    elif choice == '3':
        calculate_order_price(total_weight, num_cement, num_gravel, num_sand)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
