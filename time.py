import streamlit as st
import matplotlib.pyplot as plt

st.title("Time Conversion")

# Time conversion factors (all values in seconds)
time_units = {
    "Seconds (s)": 1,
    "Minutes (min)": 60,
    "Hours (h)": 3600,
    "Days (d)": 86400,
    "Weeks (wk)": 604800
}

# User Input Form
st.subheader("Enter Conversion Details")
from_unit = st.selectbox("From Unit", list(time_units.keys()), key="from_unit")
to_unit = st.selectbox("To Unit", list(time_units.keys()), key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f", key="value")

# Perform Conversion
converted_value = None
try:
    converted_value = (value * time_units[from_unit]) / time_units[to_unit]
except KeyError:
    st.error("Invalid conversion units. Please select valid units.")
except ZeroDivisionError:
    st.error("Error: Cannot divide by zero.")
except Exception as e:
    st.error(f"Unexpected error: {e}")

if converted_value is not None:
    st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")

    # Graphical Representation (Only Selected Units)
    fig, ax = plt.subplots(figsize=(6, 4))

    # Data for graph
    units = [from_unit, to_unit]
    values = [value, converted_value]

    # Colors for bars
    colors = ['orange', 'green']

    # Plot bar graph
    ax.bar(units, values, color=colors)
    ax.set_xlabel("Units")
    ax.set_ylabel("Time Values")
    ax.set_title("Time Conversion Comparison")
    ax.tick_params(axis='x', rotation=0)

    # Show graph in Streamlit
    st.pyplot(fig)

# Explanation Section
st.subheader("How Time Conversion Works")
st.markdown(f"""
### Understanding Conversion from {from_unit} to {to_unit}
- **Time conversion** involves changing time from one unit to another.
- The conversion is done using a **base unit (seconds)** for accuracy.

### Conversion Factors:
- **1 Minute = 60 Seconds**
- **1 Hour = 60 Minutes = 3600 Seconds**
- **1 Day = 24 Hours = 86400 Seconds**
- **1 Week = 7 Days = 604800 Seconds**

### Conversion Formula:
\[
\text{{Converted Value}} = \frac{{\text{{Input Value}} \times \text{{Conversion Factor of {from_unit}}}}}{{\text{{Conversion Factor of {to_unit}}}}}
\]

- Example Calculation:
- `{value} {from_unit} = {converted_value if converted_value is not None else "N/A"} {to_unit}`

### Real-World Applications:
- **Scheduling & Planning**: Meetings, appointments, and project deadlines.
- **Sports & Racing**: Time tracking in events like marathons and F1 races.
- **Astronomy & Science**: Time calculations in space missions and physics.
""")
