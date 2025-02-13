import streamlit as st

st.title("Glaze Calculator")

# Input fields
glaze_weight = st.number_input("Enter the weight of your mixed glaze (wet, in grams):", min_value=0.0)
addition_percentage = st.number_input("Enter the percentage of addition you want to add (e.g., for 7%, enter 7):", min_value=0.0)

# Calculate button
if st.button("Calculate"):
    if glaze_weight <= 0 or addition_percentage <= 0:
        st.error("Please enter valid positive numbers.")
    else:
        addition_weight = (addition_percentage / 100) * glaze_weight
        final_weight = glaze_weight + addition_weight

        st.success(f"""
        - You need to add **{addition_weight:.2f} grams** of the addition.
        - The final mixture will weigh **{final_weight:.2f} grams**.
        """)
