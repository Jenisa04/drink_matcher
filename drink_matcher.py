# drink_matcher.py

import streamlit as st
import pandas as pd
from scipy.stats import pearsonr, spearmanr

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.7);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


st.set_page_config(page_title="Drink Matcher Playground", layout="centered")

st.title("🥤 DRINK MATCHER PLAYGROUND")
st.subheader("Exploring Pearson & Spearman Correlation")

st.markdown("---")
st.header("📊 Pearson Match Score (Ratings-based)")

st.markdown("Rate each drink from **1–100** (how much each user likes it).")

drinks = ["Matcha", "Coffee", "Tea"]

col1, col2 = st.columns(2)
ratings_a, ratings_b = [], []

with col1:
    st.subheader("Me")
    for drink in drinks:
        val = st.number_input(f"{drink}", min_value=0, max_value=100, value=50, key=f"A_{drink}_pearson")
        ratings_a.append(val)

with col2:
    st.subheader("Imaginary Human")
    for drink in drinks:
        val = st.number_input(f"{drink}", min_value=0, max_value=100, value=50, key=f"B_{drink}_pearson")
        ratings_b.append(val)

if st.button("Calculate Pearson Match"):
    corr, _ = pearsonr(ratings_a, ratings_b)
    match_score = round((corr + 1) / 2 * 100, 2)
    st.success(f"**Pearson Correlation:** Match Score: {match_score}%")

st.markdown("---")
st.header("🥇 Spearman Match Score (Rank-based)")

st.markdown("Rank each drink (1 = most preferred, 3 = least preferred).")

col3, col4 = st.columns(2)
ranks_a, ranks_b = [], []

with col3:
    st.subheader("My Ranks")
    for drink in drinks:
        val = st.selectbox(f"{drink}", [1, 2, 3], key=f"A_{drink}_spearman")
        ranks_a.append(val)

with col4:
    st.subheader("Imaginary Human Ranks")
    for drink in drinks:
        val = st.selectbox(f"{drink}", [1, 2, 3], key=f"B_{drink}_spearman")
        ranks_b.append(val)

if st.button("Calculate Spearman Match"):
    corr, _ = spearmanr(ranks_a, ranks_b)
    match_score = round((corr + 1) / 2 * 100, 2)
    st.success(f"**Spearman Correlation:** Match Score: {match_score}%")

st.markdown("---")
st.caption("Made due to curiosity by @JenisaSheth 💡")
