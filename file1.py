import streamlit as st 

loan  = st.number_input("Enter the Loan Amount ")
tenure = st.number_input("Enter the Loan Period in Years")
ROI = st.number_input("Enter the Rate of interest annual")
# P * R * (1+R)^N / [(1+R)^N-1]

if st.button("Calculate EMI"):
    monthly_ROI = ROI/(12*100)
    tenure_in_months = tenure*12
    emi = loan*monthly_ROI*((1+monthly_ROI)**tenure_in_months)/(((1+monthly_ROI)**tenure_in_months)-1)


    total_emi = emi*tenure_in_months
    total_interest = total_emi-loan

    st.write(f"EMI amount per month will be {emi:,.2f}")
    st.write(f"Total interest you gonna pay is {total_interest:,.2f}")
    st.write(f"Total amount you gonna pay is {total_emi:,.2f}")