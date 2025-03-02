import streamlit as st
import matplotlib.pyplot as plt

st.title("Temperature Conversion")

# Temperature conversion formulas
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Temperature units dictionary
temperature_units = {
    "Celsius (°C)": "C",
    "Fahrenheit (°F)": "F",
    "Kelvin (K)": "K"
}

# User Input Form
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(temperature_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(temperature_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion
converted_value = None
if from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)":
    converted_value = celsius_to_fahrenheit(value)
elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)":
    converted_value = fahrenheit_to_celsius(value)
elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)":
    converted_value = celsius_to_kelvin(value)
elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)":
    converted_value = kelvin_to_celsius(value)
elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)":
    converted_value = fahrenheit_to_kelvin(value)
elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)":
    converted_value = kelvin_to_fahrenheit(value)
else:
    converted_value = value  # If same unit selected

# ✅ Fix: Ensure converted_value is not None before formatting
if converted_value is not None:
    st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
else:
    st.write("### Error: Conversion could not be performed.")

# Graphical Representation (Only Selected Units)
fig, ax = plt.subplots(figsize=(6, 4))

# Data for graph
units = [from_unit, to_unit]
values = [value, converted_value]

# Colors for bars
colors = ['red', 'blue']

# ✅ Fix: Ensure valid values before plotting
if None not in values:
    ax.bar(units, values, color=colors)
    ax.set_xlabel("Units")
    ax.set_ylabel("Temperature Values")
    ax.set_title("Temperature Conversion Comparison")
    ax.tick_params(axis='x', rotation=0)
    st.pyplot(fig)

# Explanation Section
st.subheader("How Temperature Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- **Celsius (°C)** is based on the freezing and boiling points of water.
- **Fahrenheit (°F)** is mostly used in the U.S. for weather and cooking.
- **Kelvin (K)** is used in scientific calculations and absolute temperature measurements.

### Conversion Formulas:
- **Celsius to Fahrenheit**: \( F = (C \times \frac{9}{5}) + 32 \)
- **Fahrenheit to Celsius**: \( C = (F - 32) \times \frac{5}{9} \)
- **Celsius to Kelvin**: \( K = C + 273.15 \)
- **Kelvin to Celsius**: \( C = K - 273.15 \)
- **Fahrenheit to Kelvin**: \( K = (F - 32) \times \frac{5}{9} + 273.15 \)
- **Kelvin to Fahrenheit**: \( F = (K - 273.15) \times \frac{9}{5} + 32 \)

### Example Calculation:

- `{value} {from_unit} = {converted_value:.2f} {to_unit}`

### Real-World Application:
- **Weather Forecasting**: Different countries use **Celsius** or **Fahrenheit**.
- **Scientific Research**: **Kelvin** is used in space science and physics.
- **Cooking & Baking**: Recipes often use **Fahrenheit** in the U.S. and **Celsius** in Europe.

### Summary:
- **Different temperature units suit different purposes.**
- **Conversion ensures standardization across different regions and industries.**
""")
