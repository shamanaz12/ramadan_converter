import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Pressure Conversion")

# Available pressure units and their conversion factors to Pascals (Pa)
pressure_units = {
    "Pascal (Pa)": 1,
    "Kilopascal (kPa)": 1000,
    "Bar": 100000,
    "Atmosphere (atm)": 101325,
    "Torr (mmHg)": 133.322,
    "Pounds per square inch (psi)": 6894.76
}

# User Input Form (Placed Above Graph)
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(pressure_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(pressure_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion
converted_value = (value * pressure_units[from_unit]) / pressure_units[to_unit]

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
ax.set_title("Pressure Conversion Comparison")
ax.tick_params(axis='x', rotation=0)

# Show graph in Streamlit
st.pyplot(fig)

# Explanation Section
st.subheader("How Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- The conversion works by using the **conversion factor** of each unit to Pascals (Pa).
- First, we **convert {from_unit} to Pascals** using the factor `{pressure_units[from_unit]}`.
- Then, we convert the result from Pascals **to {to_unit}** using the factor `{pressure_units[to_unit]}`.
- **Formula Used:**
  \[ \text{{Converted Value}} = \frac{{\text{{Input Value}} \times \text{{Conversion Factor of {from_unit}}}}}{{\text{{Conversion Factor of {to_unit}}}}} \]
- Example Calculation:
  - `{value} {from_unit} = {converted_value:.2f} {to_unit}`

### Why is This Important?
- Converting between different pressure units is crucial in physics, engineering, and meteorology.
- Understanding conversion factors ensures accurate measurements in different unit systems.

### Real-World Application
- **Kilopascal to psi**: Used in tire pressure measurements.
- **Bar to Atmosphere**: Common in meteorology and industrial applications.
- **Torr to Pascal**: Useful in vacuum pressure measurements.
""")
