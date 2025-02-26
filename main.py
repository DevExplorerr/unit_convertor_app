import streamlit as st
from utils import convert_units


def main():
    st.title("Unit Converter")

    # User input for conversion
    unit_from = st.selectbox("Select unit to convert from", [
                             "Kilometers", "Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Miles", "Yards", "Foot", "Inches", "Nautical miles"])
    unit_to = st.selectbox("Select unit to convert to", [
                           "Kilometers", "Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Miles", "Yards", "Foot", "Inches", "Nautical miles"])
    value = st.number_input("Enter value to convert", min_value=0.0)

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.success(f"{value} {unit_from} is equal to {result:.3f} {unit_to}")


if __name__ == "__main__":
    main()
