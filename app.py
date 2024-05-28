import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Title of App
st.title("To-Do App")

# Function to add new task
def add_task():
    if st.session_state.new_task:
        st.session_state.tasks.append({"task": st.session_state.new_task, "done": False})
        st.session_state.new_task = ''

# Function to toggle status of task
def toggle_task(index):
    st.session_state.tasks[index]['done'] = not st.session_state.tasks[index]['done']

# Function to remove task
def remove_task(index):
    st.session_state.tasks.pop(index)

# Input field to add new tasks
col1, col2 = st.columns([0.9, 0.05])
with col1:
    st.text_input("Add a new task:", key='new_task', on_change=add_task)
with col2:
    st.write("")  # Placeholder to maintain alignment

# Display with checkbox and remove button
for i, task in enumerate(st.session_state.tasks):
    if 'done' not in task:
        task['done'] = False  # Ensure each task has a 'done' key

    col1, col2 = st.columns([0.8, 0.19])
    with col1:
        task_text = f"~~{task['task']}~~" if task['done'] else task['task']
        st.checkbox(task_text, value=task['done'], key=f"task_{i}", on_change=toggle_task, args=(i,))
    with col2:
        st.button("Remove", key=f"remove_{i}", on_click=remove_task, args=(i,))

# HTML target to remove unnecessary streamlit buttons
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
