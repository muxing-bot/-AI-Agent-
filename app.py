import streamlit as st
import json
from agents.pipeline import run_workflow

st.set_page_config(page_title="AI Office Dashboard", layout="wide")

st.title("🚀 AI 办公自动化系统（Pro版）")

# ====== 加载数据 ======
with open("data/usage.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ====== 顶部指标 ======
col1, col2, col3 = st.columns(3)

col1.metric("📊 今日Token使用", "780,000")
col2.metric("🧠 本周平均", "580,000")
col3.metric("👥 活跃用户", len(data["users"]))

st.divider()

# ====== 图表 ======
st.subheader("📈 Token 使用趋势（近7天）")
st.line_chart(data["daily_tokens"])

# ====== 历史任务 ======
st.subheader("🗂 历史任务")
st.write(data["tasks"])

st.divider()

# ====== 主功能 ======
st.subheader("🤖 执行新任务")

task = st.text_input("输入任务：", "写一份项目周报")

if st.button("执行"):
    result = run_workflow(task)
    st.success("完成！")
    st.write(result["result"])