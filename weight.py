import streamlit as st
import matplotlib.pyplot as plt

st.title("Weight Conversion")

# Weight conversion factors (all values in kilograms)
weight_units = {
    "Milligrams (mg)": 0.000001,
    "Grams (g)": 0.001,
    "Kilograms (kg)": 1,
    "Metric Tons (t)": 1000,
    "Pounds (lb)": 0.453592,
    "Ounces (oz)": 0.0283495,
    "Stones (st)": 6.35029
}

# User Input Form (Placed Above Graph)
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(weight_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(weight_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion with Error Handling
converted_value = None

try:
    converted_value = (value * weight_units[from_unit]) / weight_units[to_unit]
except KeyError:
    st.error("Invalid conversion units. Please select valid units.")
except ZeroDivisionError:
    st.error("Error: Cannot divide by zero.")
except Exception as e:
    st.error(f"Unexpected error: {e}")

# Display conversion result
if converted_value is not None:
    st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")

    # Graphical Representation (Only Selected Units)
    fig, ax = plt.subplots(figsize=(6, 4))

    # Data for graph
    units = [from_unit, to_unit]
    values = [value, converted_value]

    # Colors for bars
    colors = ['blue', 'red']

    # Plot bar graph
    ax.bar(units, values, color=colors)
    ax.set_xlabel("Units")
    ax.set_ylabel("Weight Values")
    ax.set_title("Weight Conversion Comparison")
    ax.tick_params(axis='x', rotation=0)

    # Show graph in Streamlit
    st.pyplot(fig)

# Explanation Section
st.subheader("How Weight Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- **Weight conversion** is changing the weight from one unit to another.
- The conversion is done using a **base unit (kilograms)** for accuracy.

### Conversion Factors:
- **1 Gram = 0.001 Kilograms**
- **1 Pound = 0.453592 Kilograms**
- **1 Ounce = 0.0283495 Kilograms**
- **1 Metric Ton = 1000 Kilograms**
- **1 Stone = 6.35029 Kilograms**

### Conversion Formula:
\[
\text{{Converted Value}} = \frac{{\text{{Input Value}} \times \text{{Conversion Factor of {from_unit}}}}}{{\text{{Conversion Factor of {to_unit}}}}}
\]
- Example Calculation:
  - `{value} {from_unit} = {converted_value if converted_value is not None else "N/A"} {to_unit}`

### Real-World Applications:
- **Health & Fitness**: Weight tracking in gyms and medical records.
- **Shipping & Logistics**: Measuring package weights for transportation.
- **Cooking & Baking**: Measuring ingredient weights in recipes.
""")
