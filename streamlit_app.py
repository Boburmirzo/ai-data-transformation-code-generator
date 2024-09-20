import os
import json
import streamlit as st
from openai import OpenAI
from toolhouse import Toolhouse, Provider

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TOOLHOUSE_API_KEY = os.getenv("TOOLHOUSE_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
th = Toolhouse(access_token=TOOLHOUSE_API_KEY, provider=Provider.OPENAI)

# Set timezone for the AI Agent
th.set_metadata("timezone", "-7")

# Define the OpenAI model
MODEL = "gpt-4o"


def header_container():
    with st.container():
        st.title("Data Transformation Code Generator")
        st.write(
            "Generate Python transformation functions using LLM that can run with Toolhouse"
        )


def generate_code(description: str, input_json: str, output_json: str):
    data = {
        "description": description,
        "input_json": json.loads(input_json),
        "output_json": json.loads(output_json),
    }
    messages = [
        {
            "role": "system",
            "content": """You are a senior data engineer in Python to implement data transformation functions.
                Use this Python code structure always for other transformation function examples with mandatory handler function:
                ```python
                import json
                def handler(data):
                    # code need to here and you can add other functions which called from this function
                    return data
                ```""",
        },
        {
            "role": "user",
            "content": f"Generate data transformation code in Python given the following input data: {data}."
            f"Run unit tests for data transformation code to verify if it is working for given input and output",
        },
    ]
    with st.status("Generating code..", expanded=True) as status:
        st.write("Please wait while we generate the code..")
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        # Passes Code Execution as a tool
        tools=th.get_tools(bundle="data-transformation-code-generator"),
    )

    code_content = response.choices[0].message.content
    st.code(code_content, language="markdown")

    return response, messages


def validate_code(response, messages):
    with st.status("Validating code..", expanded=True) as status:
        st.write(
            "Please wait while we validate the code with the given input and output .."
        )
        # Runs the Code Execution tool, gets the unit test result,
        # and appends it to the context
        messages += th.run_tools(response)

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=th.get_tools(),
        )
        # Prints the response with the unit test result
        status.update(label="Code Validated.", state="complete")
        st.success(response.choices[0].message.content, icon="✅")


def main():
    header_container()
    with st.form("transformation_form"):
        description = st.text_input(
            label="Write a description of the transformation. What does it do?",
            value="Generate a nickname based on the users name and the year of birth",
        )
        input_json = st.text_input(
            label="Input JSON example", value='{"age": 33, "name": "john"}'
        )
        output_json = st.text_input(
            label="Output JSON example", value='{"nickname": "john1991"}'
        )

        submitted = st.form_submit_button("Generate")

        if submitted:
            response, messages = generate_code(description, input_json, output_json)
            validate_code(response, messages)


if __name__ == "__main__":
    st.set_page_config(
        page_title="Toolhouse Data Transformation Generator",
    )
    main()
