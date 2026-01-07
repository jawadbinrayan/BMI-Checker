st.subheader("BMI Checker")

height = st.number_input(
    "Enter your height (in meters)",
    min_value=0.5,
    max_value=3.0,
    step=0.01
)

weight = st.number_input(
    "Enter your weight (in kilograms)",
    min_value=10.0,
    max_value=300.0,
    step=0.5
)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("### Your BMI is:", round(bmi, 2))

    if bmi <= 18.9:
        st.warning("You are underweight")
    elif bmi <= 24.4:
        st.success("You are healthy")
    elif bmi <= 29.4:
        st.info("You are overweight")
    elif bmi <= 34.4:
        st.error("You are obese")
    else:
        st.error("You are severely obese")
