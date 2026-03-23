import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model & scaler
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

st.title("Student Dropout Prediction System")

st.sidebar.header("Student Information")

# =================
# DEMOGRAPHICS
# =================

Marital_status = st.sidebar.number_input("Marital status",0,10)

Application_mode = st.sidebar.number_input("Application mode",0,20)

Application_order = st.sidebar.number_input("Application order",0,10)

Course = st.sidebar.number_input("Course",0,10000)

Daytime_evening_attendance = st.sidebar.number_input("Daytime attendance",0,1)

Previous_qualification = st.sidebar.number_input("Previous qualification",0,50)

Previous_qualification_grade = st.sidebar.number_input(
"Previous qualification grade",0.0,200.0
)

Nationality = st.sidebar.number_input("Nationality",0,200)

Mothers_qualification = st.sidebar.number_input("Mother qualification",0,50)

Fathers_qualification = st.sidebar.number_input("Father qualification",0,50)

Mothers_occupation = st.sidebar.number_input("Mother occupation",0,50)

Fathers_occupation = st.sidebar.number_input("Father occupation",0,50)

Admission_grade = st.sidebar.number_input("Admission grade",0.0,200.0)

Displaced = st.sidebar.number_input("Displaced",0,1)

Educational_special_needs = st.sidebar.number_input(
"Special needs",0,1
)

Debtor = st.sidebar.number_input("Debtor",0,1)

Tuition_fees_up_to_date = st.sidebar.number_input(
"Tuition fees up to date",0,1
)

Gender = st.sidebar.number_input("Gender",0,1)

Scholarship_holder = st.sidebar.number_input(
"Scholarship holder",0,1
)

Age_at_enrollment = st.sidebar.number_input(
"Age at enrollment",15,70
)

International = st.sidebar.number_input(
"International student",0,1
)

# =================
# SEMESTER 1
# =================

Curricular_units_1st_sem_credited = st.sidebar.number_input(
"1st sem credited",0
)

Curricular_units_1st_sem_enrolled = st.sidebar.number_input(
"1st sem enrolled",0
)

Curricular_units_1st_sem_evaluations = st.sidebar.number_input(
"1st sem evaluations",0
)

Curricular_units_1st_sem_approved = st.sidebar.number_input(
"1st sem approved",0
)

Curricular_units_1st_sem_grade = st.sidebar.number_input(
"1st sem grade",0.0,20.0
)

Curricular_units_1st_sem_without_evaluations = st.sidebar.number_input(
"1st sem without evaluations",0
)

# =================
# SEMESTER 2
# =================

Curricular_units_2nd_sem_credited = st.sidebar.number_input(
"2nd sem credited",0
)

Curricular_units_2nd_sem_enrolled = st.sidebar.number_input(
"2nd sem enrolled",0
)

Curricular_units_2nd_sem_evaluations = st.sidebar.number_input(
"2nd sem evaluations",0
)

Curricular_units_2nd_sem_approved = st.sidebar.number_input(
"2nd sem approved",0
)

Curricular_units_2nd_sem_grade = st.sidebar.number_input(
"2nd sem grade",0.0,20.0
)

Curricular_units_2nd_sem_without_evaluations = st.sidebar.number_input(
"2nd sem without evaluations",0
)

# =================
# ECONOMIC
# =================

Unemployment_rate = st.sidebar.number_input(
"Unemployment rate",0.0,20.0
)

Inflation_rate = st.sidebar.number_input(
"Inflation rate",-5.0,20.0
)

GDP = st.sidebar.number_input(
"GDP",-10.0,10.0
)

# =================
# PREDICTION
# =================

if st.button("Predict"):

    data = [[

    Marital_status,
    Application_mode,
    Application_order,
    Course,
    Daytime_evening_attendance,
    Previous_qualification,
    Previous_qualification_grade,
    Nationality,
    Mothers_qualification,
    Fathers_qualification,
    Mothers_occupation,
    Fathers_occupation,
    Admission_grade,
    Displaced,
    Educational_special_needs,
    Debtor,
    Tuition_fees_up_to_date,
    Gender,
    Scholarship_holder,
    Age_at_enrollment,
    International,
    Curricular_units_1st_sem_credited,
    Curricular_units_1st_sem_enrolled,
    Curricular_units_1st_sem_evaluations,
    Curricular_units_1st_sem_approved,
    Curricular_units_1st_sem_grade,
    Curricular_units_1st_sem_without_evaluations,
    Curricular_units_2nd_sem_credited,
    Curricular_units_2nd_sem_enrolled,
    Curricular_units_2nd_sem_evaluations,
    Curricular_units_2nd_sem_approved,
    Curricular_units_2nd_sem_grade,
    Curricular_units_2nd_sem_without_evaluations,
    Unemployment_rate,
    Inflation_rate,
    GDP

    ]]

    data = scaler.transform(data)

    pred = model.predict(data)

    prob = model.predict_proba(data)

    st.subheader("Prediction Result")

    if pred[0]==1:

        st.error("High risk of dropout")

    else:

        st.success("Low risk")

    st.write(
        "Dropout probability:",
        round(prob[0][1]*100,2),
        "%"
    )