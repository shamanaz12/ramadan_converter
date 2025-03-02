import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Length Conversion")

# Available length units and their conversion factors to meters
length_units = {
    "Millimeter (mm)": 0.001,
    "Centimeter (cm)": 0.01,
    "Meter (m)": 1,
    "Kilometer (km)": 1000,
    "Inch (in)": 0.0254,
    "Foot (ft)": 0.3048,
    "Yard (yd)": 0.9144,
    "Mile (mi)": 1609.34
}

# User Input Form (Placed Above Graph)
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(length_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(length_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion
converted_value = (value * length_units[from_unit]) / length_units[to_unit]

st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")

# Graphical Representation (Only Selected Units)
fig, ax = plt.subplots(figsize=(6, 4))

# Data for graph (Only from_unit and to_unit)
units = [from_unit, to_unit]
values = [value, converted_value]

# Colors for bars
colors = ['blue', 'green']

# Plot bar graph
ax.bar(units, values, color=colors)
ax.set_xlabel("Units")
ax.set_ylabel("Values")
ax.set_title("Length Conversion Comparison")
ax.tick_params(axis='x', rotation=0)

# Show graph in Streamlit
st.pyplot(fig)

# Explanation Section
st.subheader("How Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- The conversion works by using the **conversion factor** of each unit to meters.
- First, we **convert {from_unit} to meters** using the factor `{length_units[from_unit]}`.
- Then, we convert the result from meters **to {to_unit}** using the factor `{length_units[to_unit]}`.
- **Formula Used:**
  ```
  Converted Value = (Input Value * Conversion Factor of {from_unit}) / Conversion Factor of {to_unit}
  ```
- Example Calculation:
  - `{value} {from_unit} = {converted_value:.2f} {to_unit}`

### Why is This Important?
- Converting between different length units is crucial in engineering, construction, and everyday applications.
- Understanding conversion factors ensures accurate measurements in different unit systems.

### Real-World Application
- **Kilometers to Miles**: Used for travel distance measurement in different countries.
- **Inches to Centimeters**: Essential for manufacturing and product dimensions.
- **Feet to Meters**: Commonly used in real estate and architectural designs.
""")
