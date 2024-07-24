import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from LLaMA 2 Model
def get_llama_response(topic, count, platform):
    # Load the LLaMA 2 model (Updated import)
    llm = CTransformers(
        model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 512, "temperature": 0.5},  # Increased max tokens, adjusted temperature for more creative output
    )

    # Prompt Template
    template = """
    You are an expert in software testing. Generate {count} detailed test cases for the topic of '{topic}' in a {platform}.
    For each test case, include:

    - Test Case ID
    - Test Case Description
    - Preconditions
    - Input Data
    - Steps to be Executed
    - Expected Output
    - Actual Output (to be filled during testing)
    - Status (Pass/Fail - to be filled during testing)

    Ensure the test cases are practical, cover various scenarios (positive, negative, edge cases), and follow a clear format.
    """

    prompt = PromptTemplate(
        input_variables=["platform", "topic", "count"], template=template
    )

    # Generate the response (Using invoke)
    response = llm.invoke(prompt.format(platform=platform, topic=topic, count=count))
    return response

# --- Streamlit UI ---

st.set_page_config(
    page_title="Generate Test Cases",
    page_icon="🤖",
    layout="centered"
)

st.header("Generate Test Cases 🤖")

topic = st.text_input("Enter the topic to generate test cases for:")

col1,col2 = st.columns([5,5])

with col1:
    count = st.number_input("Number of test cases:", min_value=1, value=1)

with col2:
    platform = st.selectbox(
        "Platform of your application:",
        ("Android Application", "Website", "Software", "Web Application"),
        index=0,
    )

if st.button("Generate Test Cases"):
    with st.spinner("Generating test cases..."):
        response = get_llama_response(topic, count, platform)
        st.subheader("Generated Test Cases:")
        st.code(response)  # Display the response as formatted code
