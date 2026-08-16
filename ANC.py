import streamlit as st


def render_page(t):
    st.title("🤰 Antenatal Care (ANC) Dashboard")
    st.markdown(
        "Track maternal health progress, scheduled visits, and vital milestones."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Gestational Age", "24 Weeks", "2nd Trimester")
    col2.metric("Next ANC Visit", "Sept 12, 2026", "In 28 days")
    col3.metric("Fetal Heart Rate", "145 bpm", "Normal")

    st.markdown("### ANC Visit Schedule")
    st.markdown(
        """
    - **ANC 1:** Completed (Week 12)
    - **ANC 2:** Completed (Week 20)
    - **ANC 3:** **Upcoming (Week 28)** — *Action required: Bring lab results.*
    - **ANC 4:** Scheduled (Week 36)
    """
    )

    st.markdown("---")

    # --- COUNSELING SECTION ---
    st.subheader("📚 Maternal Counseling & Guidance")
    st.markdown(
        "Essential health education and precautions for a safe pregnancy."
    )

    tab_danger, tab_diet, tab_hygiene = st.tabs(
        ["🚨 Danger Signs", "🥗 Diet & Nutrition", "🧼 Personal Hygiene"]
    )

    with tab_danger:
        st.error(
            "**Seek immediate medical attention if you experience any of the following danger signs:**\n"
            "- Severe vaginal bleeding\n"
            "- Swelling of the face, hands, or fingers (sign of pre-eclampsia)\n"
            "- Severe, persistent headaches or blurred vision\n"
            "- High fever or chills\n"
            "- Reduced or absent fetal movement\n"
            "- Sudden gush of fluid from the vagina (water breaking early)"
        )

    with tab_diet:
        st.info(
            "**Recommended Dietary Practices:**\n"
            "- **Balanced Meals:** Include a mix of carbohydrates, proteins (lean meats, beans, lentils), and fresh vegetables.\n"
            "- **Iron & Folic Acid:** Take prescribed supplements regularly to prevent anemia.\n"
            "- **Hydration:** Drink plenty of clean, filtered water throughout the day.\n"
            "- **Foods to Avoid:** Unpasteurized dairy, raw or undercooked meats and eggs, and excess caffeine."
        )

    with tab_hygiene:
        st.success(
            "**Hygiene & Wellness Guidelines:**\n"
            "- **Handwashing:** Wash hands frequently with soap and water, especially before eating and after using the restroom.\n"
            "- **Body Care:** Maintain clean clothing and practice regular bathing.\n"
            "- **Infection Prevention:** Avoid harsh chemical soaps or douching in the vaginal area to maintain natural flora balance.\n"
            "- **Rest:** Ensure adequate rest and sleep in a well-ventilated room."
        )