import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Test",layout='wide')


def number_field(label, columns=None, **input_params):
    c1, c2 = st.columns(columns or [1, 1])

    # Display field name with some alignment
    c1.markdown("######")
    c1.markdown(label)

    # Sets a default key parameter to avoid duplicate key errors
    input_params.setdefault("key", label)

    # Forward text input parameters
    return c2.number_input("", **input_params)



# Setting up the layout using columns
st.title("TOTEC - Total Ownership Tracking Economic Calculator")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    #st.header("OWN CAR")
    #st.subheader("Fixed costs")

    if st.button("1. Own Car"):
        st.switch_page("pages/1_owncar.py")


with col2:

    if st.button("2. Shared Car"):
        st.switch_page("pages/2_sharedcar.py")

with col3:
    if st.button("3. Results"):
        st.switch_page("pages/3_results.py")


col1, col2, col3 = st.columns([3, 2, 3])

with col1:

    st.subheader("Fixed costs")
    purchase_price = number_field("Purchase price [€]", min_value=0.0, value=20000.0, step=1000.0)
    road_tax = number_field("Road tax [€/month]", min_value=0.0, value=40.0, step=1.0)
    insurance = number_field("Insurance [€/month]", min_value=0.0, value=80.0, step=1.0)
    parking_permit = number_field("Parking permit [€/month]", min_value=0.0, value=60.0, step=1.0)
    maintenance = number_field("Maintenance [€/month]", min_value=0.0, value=70.0, step=1.0)
    inflation_rate = number_field("Inflation rate [%/year]", min_value=0.0, value=5.0, step=0.1)
    car_lifetime = number_field("Lifetime of car [years]", min_value=0, value=3, step=1)
    new_car = st.selectbox("Will you buy a car every " + str(car_lifetime) + " years?", ["Yes", "No"])

    st.subheader("Usage cost")
    gasoline_price = number_field("Gasoline price [€/liter]", min_value=0.0, value=1.99, step=0.01)
    avg_gasoline_consumption = number_field("Average gasoline car consumption [L/100Km]", min_value=0.0, value=9.0, step=0.1)
    diesel_cost = number_field("Diesel cost [€/liter]", min_value=0.0, value=1.92, step=0.01)
    electricity_cost = number_field("Electricity cost [€/kWh]", min_value=0.0, value=0.30, step=0.01)
    ev_consumption = number_field("EV consumption [kWh/Km]", min_value=0.0, value=0.5, step=0.01)
    usage_km = number_field("Use [km]", min_value=0.0, value=80.0, step=1.0)

    st.subheader("Period of usage")
    period_of_usage = st.selectbox("Select period of usage", ["Day", "Week", "Month", "Year"])

    st.subheader("Fuel type")
    fuel_type = st.radio("Please select fuel type", ["Gasoline (Petrol)", "Diesel", "Electric"])
  