import streamlit as st


def render_page(t):
    st.title("📝 Data Input & Logging")
    st.markdown("Add new medical records, logs, or medication reminders.")

    form_category = st.selectbox(
        "Select Category to Update",
        [
            "Medication",
            "ANC Record",
            "Chronic Log (BP/Sugar)",
            "Post-OP Log",
        ],
    )

    with st.form("health_data_form"):
        st.subheader(f"New Entry: {form_category}")

        patient_name = st.text_input("Patient Full Name")
        entry_date = st.date_input("Date")

        if form_category == "Medication":
            med_name = st.text_input("Medication Name & Dosage")
            instructions = st.text_area(
                "Side effects & Warning notes to watch for"
            )
            schedule = st.selectbox(
                "Frequency", ["Once daily", "Twice daily", "Every 8 hours"]
            )
        elif form_category == "ANC Record":
            gest_week = st.number_input(
                "Gestational Age (Weeks)", min_value=1, max_value=42, value=12
            )
            notes = st.text_area("Clinical Notes & Supplements")
        elif form_category == "Chronic Log (BP/Sugar)":
            metric_val1 = st.number_input("Value 1 (e.g., Systolic / FBS)", value=120)
            metric_val2 = st.number_input(
                "Value 2 (e.g., Diastolic - optional)", value=80
            )
        else:
            recovery_notes = st.text_area("Daily Recovery Notes")

        submitted = st.form_submit_button("Save Entry")
        if submitted:
            st.success(
                f"Successfully saved new record for **{patient_name or 'Patient'}** under **{form_category}**!"
            )