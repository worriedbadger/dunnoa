def glaze_calculator():
    print("Welcome to the Glaze Calculator!")
    
    # Step 1: Enter the weight of the mixed glaze (wet)
    glaze_weight = float(input("Enter the weight of your mixed glaze (wet, in grams): "))
    
    # Step 2: Enter the percentage of addition you want to add
    addition_percentage = float(input("Enter the percentage of addition you want to add (e.g., for 7%, enter 7): "))
    
    # Step 3: Calculate how much of the addition to weigh out
    addition_weight = (addition_percentage / 100) * glaze_weight
    
    # Step 4: Calculate the final mixture weight
    final_weight = glaze_weight + addition_weight
    
    # Display the results
    print("\nResults:")
    print(f"- You need to add {addition_weight:.2f} grams of the addition.")
    print(f"- The final mixture will weigh {final_weight:.2f} grams.")

# Run the calculator
glaze_calculator()