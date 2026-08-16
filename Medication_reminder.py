import pandas as pd
import streamlit as st

def render_page(t):
    # Load localized text sections
    app_t = t["app"]
    dates_t = t["dates"]
    alarm = t["alarm_section"]
    med_table = t["medications_table"]
    profiles = t["medication_profiles"]
    vals = t.get("medication_values", {})

    # Header section
    col_title, col_date = st.columns([3, 1])
    with col_title:
        st.title(app_t["title_medication"])
    with col_date:
        st.markdown(
            f"<div style='text-align: right; padding-top: 15px;'><b>{dates_t['ethiopian_date_label']}:</b><br>{dates_t['ethiopian_date_sample']}</div>",
            unsafe_allow_html=True,
        )

    st.markdown(app_t["subtitle_medication"])
    st.markdown("---")

    # Alarm Reminder Section
    with st.expander(alarm["expander_title"], expanded=False):
        st.markdown(alarm["local_time_desc"])
        with st.form("alarm_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                alarm_med = st.selectbox(alarm["select_medication"], ["Metformin", "Amoxicillin", "Lisinopril", "Paracetamol"])
            with col_b:
                alarm_time_local = st.selectbox(alarm["reminder_time_local"], t["time_slots"])
            
            alarm_note = st.text_input(alarm["custom_note"])
            if st.form_submit_button(alarm["set_alarm_btn"]):
                st.success(alarm["success_message"].format(med=alarm_med, time=alarm_time_local))

    st.markdown("---")

    # Medication Database with lookup keys
    medications_db = {
        "Metformin": {
            "dose": "500 mg",
            "frequency_key": "frequency_twice",
            "route_key": "route_oral",
            "status_key": "status_active",
            "side_effects": "Nausea, vomiting, stomach upset, diarrhea, or a metallic taste in the mouth.",
            "best_taken": "Take with meals.",
            "interactions": "Alcohol, certain diuretics.",
            "adherence_risk": "High sugar levels."
        },
        "Amoxicillin": {
            "dose": "250 mg",
            "frequency_key": "frequency_every_8",
            "route_key": "route_oral",
            "status_key": "status_active",
            "side_effects": "Mild diarrhea, rash.",
            "best_taken": "Complete the full course.",
            "interactions": "Allopurinol, oral contraceptives.",
            "adherence_risk": "Antibiotic resistance."
        },
        "Lisinopril": {
            "dose": "10 mg",
            "frequency_key": "frequency_daily",
            "route_key": "route_oral",
            "status_key": "status_active",
            "side_effects": "Dry persistent cough, dizziness.",
            "best_taken": "Same time daily.",
            "interactions": "Potassium supplements, NSAIDs.",
            "adherence_risk": "Blood pressure spikes."
        },
        "Paracetamol": {
            "dose": "500 mg",
            "frequency_key": "frequency_as_needed",
            "route_key": "route_oral",
            "status_key": "status_completed",
            "side_effects": "Rare when taken as directed.",
            "best_taken": "Do not exceed daily limit.",
            "interactions": "Alcohol.",
            "adherence_risk": "Uncontrolled symptoms."
        },
    }

    # Build the table using the translation map (vals)
    table_data = []
    for name, details in medications_db.items():
        table_data.append({
            med_table["column_drug_name"]: f"**{name}**",
            med_table["column_dose"]: details["dose"],
            med_table["column_frequency"]: vals.get(details["frequency_key"], "Unknown"),
            med_table["column_route"]: vals.get(details["route_key"], "Unknown"),
            med_table["column_status"]: vals.get(details["status_key"], "Unknown"),
        })

    df = pd.DataFrame(table_data)
    st.subheader(med_table["header_active_prescriptions"])
    
    event = st.dataframe(df, use_container_width=True, hide_index=True, on_select="rerun", selection_mode="single-row", key="med_table")
    st.markdown(f"*{med_table['instruction']}*")
    st.markdown("---")

    # Handle selection
    if event.selection.rows:
        selected_index = event.selection.rows[0]
        selected_drug = list(medications_db.keys())[selected_index]
        info = medications_db[selected_drug]

        st.markdown(f"### {profiles['profile_header'].format(drug=selected_drug)}")
        col1, col2 = st.columns(2)
        with col1: st.metric(med_table["column_dose"], info["dose"])
        with col2: st.metric(med_table["column_frequency"], vals.get(info["frequency_key"], ""))

        st.markdown(f"**{med_table['column_route']}:** {vals.get(info['route_key'], '')} | "
                    f"**{med_table['column_status']}:** {vals.get(info['status_key'], '')}")

        st.markdown(f"#### {profiles['side_effects']}"); st.warning(info["side_effects"])
        st.markdown(f"#### {profiles['best_taken']}"); st.info(info["best_taken"])
        st.markdown(f"#### {profiles['interactions']}"); st.error(info["interactions"])
        st.markdown(f"#### {profiles['adherence_risk']}"); st.error(info["adherence_risk"])