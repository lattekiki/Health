import pandas as pd
import streamlit as st


def render_page(t):
    postop = t["postop"]

    # =========================================================
    # PAGE HEADER
    # =========================================================
    st.title(postop["title"])
    st.markdown(postop["subtitle"])

    # =========================================================
    # METRICS SECTION
    # =========================================================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            postop["metrics"]["day_label"],
            postop["metrics"]["day_val"],
            postop["metrics"]["day_stat"],
        )

    with col2:
        st.metric(
            postop["metrics"]["site_label"],
            postop["metrics"]["site_val"],
            postop["metrics"]["site_stat"],
        )

    with col3:
        st.metric(
            postop["metrics"]["removal_label"],
            postop["metrics"]["removal_val"],
            postop["metrics"]["removal_stat"],
        )

    st.markdown("---")

    # =========================================================
    # POST-OP CARE & WOUND CARE SCHEDULE
    # =========================================================
    st.subheader(postop["schedule"]["title"])
    st.markdown(postop["schedule"]["desc"])

    # =========================================================
    # WOUND CARE TABLE (Using Pandas DataFrame)
    # =========================================================
    table_data = [
        {
            postop["table"]["h1"]: f"**{postop['rows']['r1_t']}**",
            postop["table"]["h2"]: postop["rows"]["r1_d"],
            postop["table"]["h3"]: postop["rows"]["r1_a"],
        },
        {
            postop["table"]["h1"]: f"**{postop['rows']['r2_t']}**",
            postop["table"]["h2"]: postop["rows"]["r2_d"],
            postop["table"]["h3"]: postop["rows"]["r2_a"],
        },
        {
            postop["table"]["h1"]: f"**{postop['rows']['r3_t']}**",
            postop["table"]["h2"]: postop["rows"]["r3_d"],
            postop["table"]["h3"]: postop["rows"]["r3_a"],
        },
        {
            postop["table"]["h1"]: f"**{postop['rows']['r4_t']}**",
            postop["table"]["h2"]: postop["rows"]["r4_d"],
            postop["table"]["h3"]: postop["rows"]["r4_a"],
        },
    ]

    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")

    # =========================================================
    # STITCH / STAPLE REMOVAL MILESTONE
    # =========================================================
    st.subheader(postop["milestone"]["title"])
    st.markdown(postop["milestone"]["desc"])

    # =========================================================
    # INFORMATION & WARNING BOXES
    # =========================================================
    col_a, col_b = st.columns(2)

    with col_a:
        st.info(postop["info_box"])

    with col_b:
        st.warning(postop["warning_box"])