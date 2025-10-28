# 🥤 Drink Matcher Playground

A fun Streamlit app to explore **Pearson** vs **Spearman** correlation — see how two users' drink preferences compare!

🚀 **[👉 Try it live on Streamlit!](https://drinkmatcher.streamlit.app/)**

---

### 🧠 Understanding the Correlations

**🔹 Pearson Correlation** — Measures the _linear relationship_ between two sets of numerical ratings.

> If both users’ drink **ratings** increase or decrease together at a constant rate, they’ll have a high Pearson correlation.

**🔸 Spearman Correlation** — Measures the _rank-based relationship_ between two sets of preferences.

> If both users **rank** drinks in a similar order, even if their exact scores differ, they’ll have a high Spearman correlation.

🧃 _In short:_

- Pearson cares about **how much** users like each drink.
- Spearman cares about **the order** in which they like them.

---

## 🚀 Run locally

```bash
pip install -r requirements.txt
streamlit run drink_matcher.py
```
