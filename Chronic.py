import pandas as pd
import streamlit as st


def render_page(t):
    st.title("🩺 Chronic Condition Monitoring")
    st.markdown(
        "Monitor vital metrics such as blood pressure, blood glucose, and symptom logs."
    )

    condition_type = st.selectbox(
        "Select Condition", ["Hypertension", "Type 2 Diabetes", "Asthma"]
    )

    if condition_type == "Hypertension":
        st.info("Target BP: Below 130/80 mmHg")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Latest Systolic", "124 mmHg", "-2 mmHg")
        with col2:
            st.metric("Latest Diastolic", "82 mmHg", "+1 mmHg")

        st.markdown("---")
        st.subheader("📊 Weekly Blood Pressure (BP) Records")
        st.markdown(
            "Track your daily blood pressure readings (Morning and Evening)."
        )

        bp_data = {
            "Day / Date": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            "Morning BP (mmHg)": [
                "122/80",
                "126/82",
                "120/78",
                "128/84",
                "124/81",
                "122/79",
                "125/80",
            ],
            "Evening BP (mmHg)": [
                "125/82",
                "128/85",
                "124/80",
                "130/86",
                "126/82",
                "123/80",
                "125/81",
            ],
            "Status / Notes": [
                "Normal",
                "Normal",
                "Optimal",
                "Elevated",
                "Normal",
                "Normal",
                "Normal",
            ],
        }

        bp_df = pd.DataFrame(bp_data)
        st.dataframe(bp_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("📚 Hypertension Counseling & Complications")

        tab_htn_diet, tab_htn_comp = st.tabs(
            ["🥗 Lifestyle & Dietary Guidance", "⚠️ Complications & Warning Signs"]
        )

        with tab_htn_diet:
            st.info(
                "**Recommended Lifestyle Practices for Hypertension:**\n"
                "- **Sodium Reduction:** Limit salt intake significantly. Avoid heavily salted foods, processed meats, and excessive bouillon cubes.\n"
                "- **DASH Diet:** Focus on fresh fruits, vegetables, whole grains, and low-fat dairy products.\n"
                "- **Physical Activity:** Engage in regular moderate exercise, such as brisk walking, for at least 30 minutes most days of the week.\n"
                "- **Weight & Stress Management:** Maintain a healthy weight and practice stress-reduction techniques."
            )

        with tab_htn_comp:
            st.error(
                "🚨 **ACUTE HYPERTENSIVE CRISIS (Seek Immediate Medical Care):**\n"
                "- **Hypertensive Emergency (BP > 180/120 mmHg):** Accompanied by severe headache, chest pain, shortness of breath, sudden vision changes, numbness, or confusion.\n\n"
                "📉 **LONG-TERM CHRONIC COMPLICATIONS:**\n"
                "- **Cardiovascular Disease:** Increased strain on heart muscles leading to heart failure, coronary artery disease, or heart attacks.\n"
                "- **Stroke / Cerebrovascular Accident:** High pressure damaging brain blood vessels, risking blockages or ruptures.\n"
                "- **Hypertensive Nephropathy:** Gradual damage to renal blood vessels leading to chronic kidney disease.\n"
                "- **Vision Loss:** Damage to retinal blood vessels (hypertensive retinopathy)."
            )

    elif condition_type == "Type 2 Diabetes":
        st.info("Target Fasting Blood Sugar: 80 - 130 mg/dL")
        st.metric("Latest Fasting Glucose", "110 mg/dL", "Normal")

        st.markdown("---")
        st.subheader("📊 RBS Daily QID Log (Random Blood Sugar - 4 Times/Day)")
        st.markdown(
            "Track your blood sugar levels four times daily: Fasting (Morning), Post-Lunch, Post-Dinner, and Bedtime."
        )

        rbs_data = {
            "Day / Date": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            "Morning (Fasting)": [
                "110 mg/dL",
                "105 mg/dL",
                "115 mg/dL",
                "108 mg/dL",
                "112 mg/dL",
                "110 mg/dL",
                "106 mg/dL",
            ],
            "Post-Lunch": [
                "145 mg/dL",
                "150 mg/dL",
                "140 mg/dL",
                "160 mg/dL",
                "148 mg/dL",
                "138 mg/dL",
                "142 mg/dL",
            ],
            "Post-Dinner": [
                "155 mg/dL",
                "148 mg/dL",
                "162 mg/dL",
                "150 mg/dL",
                "145 mg/dL",
                "152 mg/dL",
                "149 mg/dL",
            ],
            "Bedtime": [
                "130 mg/dL",
                "125 mg/dL",
                "135 mg/dL",
                "128 mg/dL",
                "132 mg/dL",
                "126 mg/dL",
                "129 mg/dL",
            ],
        }

        rbs_df = pd.DataFrame(rbs_data)
        st.dataframe(rbs_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("📚 Diabetes Counseling & Education")

        tab_dm_diet, tab_dm_comp = st.tabs(
            [
                "🥗 Dietary Guidelines",
                "⚠️ Acute & Chronic Complications Guide",
            ]
        )

        with tab_dm_diet:
            st.info(
                "**Recommended Nutritional Habits for Diabetes:**\n"
                "- **Complex Carbohydrates:** Choose whole grains, barley (gebta), sorghum, and fiber-rich vegetables over refined starches like white bread or polished teff in excess.\n"
                "- **Portion Control:** Maintain consistent meal sizes to prevent sharp glucose spikes.\n"
                "- **Healthy Fats & Proteins:** Incorporate legumes (lentils, chickpeas/shiro), lean meats, and healthy plant fats.\n"
                "- **Sugar Intake:** Strictly avoid sugary beverages, sodas, and heavy sweets."
            )

        with tab_dm_comp:
            st.error(
                "🚨 **ACUTE COMPLICATIONS (Requires Urgent Medical Action):**\n\n"
                "1. **Hypoglycemia (Low Blood Sugar - Below 70 mg/dL):**\n"
                "   - *Symptoms:* Shakiness, sweating, dizziness, confusion, rapid heartbeat, intense hunger.\n"
                "   - *Immediate Action:* Consume 15g of fast-acting carbohydrates (e.g., half a cup of juice or 3 glucose tablets).\n\n"
                "2. **Diabetic Ketoacidosis (DKA):**\n"
                "   - *Symptoms:* Nausea, vomiting, abdominal pain, shortness of breath, fruity-scented breath, high ketone levels, confusion.\n"
                "   - *Note:* Medical emergency common in unmanaged blood glucose.\n\n"
                "3. **Hyperglycemic Hyperosmolar State (HHS):**\n"
                "   - *Symptoms:* Extremely high blood sugar (>600 mg/dL), severe dehydration, dry mouth, confusion, or drowsiness."
            )

            st.warning(
                "📉 **LONG-TERM CHRONIC COMPLICATIONS:**\n"
                "- **Diabetic Nephropathy:** Progressive kidney damage leading to potential chronic kidney failure.\n"
                "- **Diabetic Neuropathy:** Nerve injury causing tingling, numbness, or burning pain in the extremities.\n"
                "- **Cardiovascular Disease:** Elevated long-term risk of heart attack and stroke.\n"
                "- **Diabetic Retinopathy:** Damage to retinal blood vessels leading to potential vision loss."
            )

    elif condition_type == "Asthma":
        st.info(
            "Target Peak Flow: >80% of personal best | Daily Controller Compliance"
        )
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Peak Expiratory Flow", "420 L/min", "+15 L/min")
        with col2:
            st.metric("Inhaler Adherence", "92%", "Good")

        st.markdown("---")
        st.subheader("📚 Asthma Counseling & Acute Exacerbation Guide")

        tab_asthma_mgmt, tab_asthma_attack = st.tabs(
            ["🌬️ Daily Management & Triggers", "🚨 Signs of Acute Exacerbation"]
        )

        with tab_asthma_mgmt:
            st.info(
                "**Daily Control & Prevention:**\n"
                "- **Controller Medication:** Take daily preventer inhalers as prescribed, even when feeling well.\n"
                "- **Identify Triggers:** Avoid known allergens such as dust, pollen, smoke, strong chemical fumes, and cold air.\n"
                "- **Peak Flow Monitoring:** Check your peak flow meter every morning to track lung function trends."
            )

        with tab_asthma_attack:
            st.error(
                "🚨 **SIGNS OF AN ASTHMA ATTACK (Acute Exacerbation):**\n"
                "Recognize these early warning signs and symptoms that indicate your airways are narrowing:\n\n"
                "- **Severe Shortness of Breath:** Difficulty catching your breath or feeling breathless with minimal exertion.\n"
                "- **Wheezing:** A high-pitched whistling sound when breathing out.\n"
                "- **Persistent Cough:** Especially worse at night or early in the morning, triggered by exercise or cold air.\n"
                "- **Chest Tightness:** A feeling of pressure or constriction across the chest area.\n"
                "- **Peak Flow Drop:** Readings falling below 50-80% of your personal best.\n\n"
                "⚠️ **EMERGENCY ACTION:** If quick-relief rescue inhalers (e.g., Salbutamol) do not provide relief, or if you experience bluish lips/face, severe confusion, or inability to speak full sentences, seek **immediate emergency medical care**."
            )

    st.markdown("### Recent Log History")
    st.write("No critical anomalies reported in the last 7 days.")