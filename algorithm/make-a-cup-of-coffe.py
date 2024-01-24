# Exercise: Make a cup of coffee
# Introduction
# In this exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product. 

# Instructions
# Step 1: Start with the inputs - what is needed to make a cup of instant coffee?

# Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.

# Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it. 

# Step 4: The algorithm when complete should have as its final result a cup of coffee.

# Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out. 




# Make a cup of coffee - solution
# Solution algorithm

# Input 
# Ingredients required:

# Cup

# Hot water

# Coffee granules

# Optional:

# Milk

# Cream 

# Sugar

# Output
# A cup of coffee.

# Steps
# 1. Add drinking water to an electric kettle. 

# 2. Put the kettle on to boil water.

# 3. While waiting, prepare coffee.

# 4. Add coffee granules to the cup.

# 5. If water is boiled, pour water into a cup, else continue to wait.

# 6. If milk or cream is required, add and stir.

# 7. If sugar is required, add and stir.

# 8. Return coffee.


def make_coffee():
    # Step 1: Input - Gather the ingredients
    cup = "Coffee Mug"
    hot_water = "Boiled Water"
    coffee_granules = "Coffee Granules"

    # Optional Ingredients
    milk = "Milk"
    cream = "Cream"
    sugar = "Sugar"

    # Step 2: Output - Result of the algorithm
    result = "A Cup of Coffee"

    # Step 3: Steps to make coffee
    print("1. Add drinking water to an electric kettle.")
    print("2. Put the kettle on to boil water.")
    print("3. While waiting, prepare coffee.")
    print(f"4. Add {coffee_granules} to the {cup}.")

    # Check if water is boiled
    water_boiled = input("Has the water boiled? (yes/no): ").lower()
    if water_boiled == "yes":
        print(f"5. Pour {hot_water} into the {cup}.")
    else:
        print("5. Continue waiting for the water to boil.")

    # Optional: Add milk and cream
    if input("Do you want to add milk? (yes/no): ").lower() == "yes":
        print(f"6. Add {milk} and stir.")
    if input("Do you want to add cream? (yes/no): ").lower() == "yes":
        print(f"7. Add {cream} and stir.")

    # Optional: Add sugar
    if input("Do you want to add sugar? (yes/no): ").lower() == "yes":
        print(f"8. Add {sugar} and stir.")

    # Step 9: Return coffee
    print("9. Return to the coffee.")

    # Step 10: Output - Enjoy
    print(result)

# Run the function to make a cup of coffee
make_coffee()