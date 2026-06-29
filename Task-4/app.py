import streamlit as st

from agent import run_agent
from memory import load_memory, clear_memory

st.set_page_config(
    page_title="AI Project Mentor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Project Mentor Agent")
st.write("Plan AI projects, get guidance, search the web, solve calculations, and continue previous conversations.")

st.sidebar.title("Memory")

if st.sidebar.button("Clear Memory"):
    clear_memory()
    st.sidebar.success("Memory Cleared")
    st.rerun()

memory = load_memory()

if memory:
    st.sidebar.subheader("Recent Conversations")

    for chat in reversed(memory[-5:]):
        st.sidebar.markdown(f"**You:** {chat['user']}")
        st.sidebar.markdown(f"**Agent:** {chat['assistant'][:80]}...")
        st.sidebar.markdown("---")

user_input = st.chat_input("Ask anything...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        response, tool_used, reasoning = run_agent(user_input)

    with st.chat_message("assistant"):
        st.success(f"Tool Used: {tool_used.upper()}")

    with st.expander("🧠 Agent Reasoning"):

        for step in reasoning:
            st.write("✅", step)

    st.write(response)

    st.download_button(
        "📄 Download Response",
        data=response,
        file_name="project_plan.txt",
        mime="text/plain"
    )