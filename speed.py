import streamlit as st
import matplotlib.pyplot as plt

st.title("Speed Conversion")

# Speed units and their conversion factors to meters per second (m/s)
speed_units = {
    "Meters per second (m/s)": 1,
    "Kilometers per hour (km/h)": 0.277778,
    "Miles per hour (mph)": 0.44704,
    "Feet per second (ft/s)": 0.3048,
    "Knots (kt)": 0.514444
}

# User Input Form
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(speed_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(speed_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion
converted_value = (value * speed_units[from_unit]) / speed_units[to_unit]

st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")

# Graphical Representation (Only Selected Units)
fig, ax = plt.subplots(figsize=(6, 4))

# Data for graph (Only from_unit and to_unit)
units = [from_unit, to_unit]
values = [value, converted_value]

# Colors for bars
colors = ['orange', 'brown']

# Plot bar graph
ax.bar(units, values, color=colors)
ax.set_xlabel("Units")
ax.set_ylabel("Values")
ax.set_title("Speed Conversion Comparison")
ax.tick_params(axis='x', rotation=0)

# Show graph in Streamlit
st.pyplot(fig)

# Explanation Section
st.subheader("How Speed Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- The conversion works by using the **conversion factor** of each unit to meters per second (m/s).
- First, we **convert {from_unit} to meters per second** using the factor `{speed_units[from_unit]}`.
- Then, we convert the result from meters per second **to {to_unit}** using the factor `{speed_units[to_unit]}`.
- **Formula Used:**
  \[
  \text{{Converted Value}} = \frac{{\text{{Input Value}} \times \text{{Conversion Factor of {from_unit}}}}}{{\text{{Conversion Factor of {to_unit}}}}}
  \]

- Example Calculation:
  - `{value} {from_unit} = {converted_value:.2f} {to_unit}`

### Why is This Important?
- Speed conversion is **essential** in physics, aviation, transportation, and automotive industries.
- Engineers, scientists, and drivers frequently convert speeds for **accurate measurements and safety regulations**.

### Real-World Application
- **Kilometers per hour to Miles per hour**: Used for speed limits when traveling internationally.
- **Knots to Meters per second**: Crucial in aviation and marine navigation.
- **Feet per second to Meters per second**: Used in sports science and ballistic calculations.

### Summary
- **Speed conversion ensures standardization across different measurement systems.**
- **Understanding conversion factors helps in quick and accurate calculations.**
""")
