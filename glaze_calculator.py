import streamlit as st

# Title of the app
st.title("Mixture Ratio Calculator")

# Input: Portion weight
portion_weight = st.number_input(
    "Enter the weight of the portion (in grams):",
    min_value=0.0,
    value=40.0,  # Default value
    step=0.1,
    format="%.2f"
)

# Constants based on the updated recipe ratio
total_mixture_weight = 140  # 100g dry material + 40g water
dry_material_percentage = 100 / total_mixture_weight  # 71.43%
water_percentage = 40 / total_mixture_weight  # 28.57%
stain_percentage = 0.07  # 7%

# Calculate dry material and water in the given portion
dry_material_weight = portion_weight * dry_material_percentage
water_weight = portion_weight * water_percentage

# Calculate the amount of stain to add
stain_weight = dry_material_weight * stain_percentage

# Display the results
st.subheader("Results:")
st.write(f"For a **{portion_weight}g** portion:")
st.write(f"- **Dry Material:** {dry_material_weight:.2f}g")
st.write(f"- **Water:** {water_weight:.2f}g")
st.write(f"- **Stain:** {stain_weight:.2f}g")
