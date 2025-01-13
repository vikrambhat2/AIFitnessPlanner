import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the LLM
langchain_llm = ChatGroq(api_key=groq_api_key, model="llama-3.3-70b-versatile")

# Define the prompt template for plan generation
plan_prompt_template = """
You are a fitness and diet planner. Using the following inputs, create two detailed plans:
1. A **diet plan** table listing day-to-day food intake for {number_of_weeks} weeks.
2. A **workout plan** table listing day-to-day exercises for {number_of_weeks} weeks.

Inputs:
- **Workout type**: {workout_type}
- **Diet type**: {diet_type}
- **Current body weight**: {current_weight} kg
- **Target weight**: {target_weight} kg
- **Specific dietary restrictions**: {dietary_restrictions}
- **Health conditions**: {health_conditions}
- **Age**: {age}
- **Gender**: {gender}
- **Other instructions**: {comments}

Return the plans in a neat, structured format with tables and include any relevant key notes.
"""

plan_prompt = PromptTemplate(
    input_variables=[
        "workout_type",
        "diet_type",
        "current_weight",
        "target_weight",
        "dietary_restrictions",
        "health_conditions",
        "age",
        "gender",
        "number_of_weeks",
        "comments",
    ],
    template=plan_prompt_template,
)

# Define the prompt template for chat interactions
chat_prompt_template = """
You are a fitness and diet expert. Answer the following user question based on the given plan:

Plan: {plan}

Question: {question}

Provide a clear and helpful response.
"""

chat_prompt = PromptTemplate(
    input_variables=["plan", "question"],
    template=chat_prompt_template,
)

# Set up the chains
plan_chain = LLMChain(llm=langchain_llm, prompt=plan_prompt)
chat_chain = LLMChain(llm=langchain_llm, prompt=chat_prompt)


st.set_page_config(page_title="🧘‍♀️ Fitness and Diet Planner", layout="wide")
# Streamlit App
st.title("🧘‍♀️ Fitness and Diet Planner")

# Creating a two-column layout
col1, col2 = st.columns(2)

# Column 1: User Inputs
with col1:
    st.header("Enter your details:")
    workout_type = st.text_input("Workout Type (e.g., Weight Loss, Muscle Gain)")
    diet_type = st.text_input("Diet Type (e.g., Indian, Mediterranean)")
    current_weight = st.number_input("Current Body Weight (kg)", min_value=30.0, max_value=200.0, value=75.0, step=1.0)
    target_weight = st.number_input("Target Weight (kg)", min_value=30.0, max_value=200.0, value=68.0, step=1.0)
    dietary_restrictions = st.text_input("Dietary Restrictions (e.g., No dairy, Low sugar)")
    health_conditions = st.text_input("Any Health Conditions?", "")
    age = st.number_input("Age", min_value=10, max_value=100, value=30, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    number_of_weeks = st.slider("Number of Weeks", min_value=1, max_value=12, value=4)
    comments = st.text_area("Additional Comments")

    if st.button("Generate Plans"):
        # Clear conversation history but retain the plan
        st.session_state["messages"] = []  # Reset conversation history

        with st.spinner("Generating personalized fitness and diet plans..."):
            try:
                # Generate and store the new plan
                response = plan_chain.run({
                    "workout_type": workout_type,
                    "diet_type": diet_type,
                    "current_weight": current_weight,
                    "target_weight": target_weight,
                    "dietary_restrictions": dietary_restrictions,
                    "health_conditions": health_conditions,
                    "age": age,
                    "gender": gender,
                    "number_of_weeks": number_of_weeks,
                    "comments": comments,
                })
                st.session_state.plan = response  # Store the new plan
                st.success("Plans generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Column 2: Display Plan
with col2:
    if "plan" in st.session_state and st.session_state.plan:
        st.header("Your Plans:")
        #st.markdown(st.session_state.plan)

        st.markdown(f'<div class="scrollable-response">{st.session_state.plan}</div>', unsafe_allow_html=True)

# Chatbox Section
if "plan" in st.session_state and st.session_state.plan:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Converse with your plan")

    # Initialize chat history if not already present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Ask question input field at the bottom
    if prompt := st.chat_input("Ask a question about your plan"):
        # Append user question to chat history (after it is submitted)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get the assistant's response
        try:
            answer = chat_chain.run({"plan": st.session_state.plan, "question": prompt})
        except Exception as e:
            answer = f"An error occurred: {e}"

        # Append assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("user").write(prompt)
        # Display the assistant's response in chat
        st.chat_message("assistant").write(answer)

# Footer
st.markdown("---")
st.caption("💡 Vikram Bhat")