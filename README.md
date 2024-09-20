# Data Transformation Code Generator
This Streamlit app, powered by Toolhouse AI and OpenAI's LLM, generates Python code to transform data from one JSON format to another. It provides a description of the transformation function and verifies its correctness through automated unit testing.

# Features
- Automatically generates Python transformation functions based on input and output JSON examples.
- Provides detailed descriptions of how the function works.
- Verifies the generated code by running unit tests.
- Built with Streamlit for an easy-to-use interface.

## Getting Started

You can run the Data Transformation Code Generator app locally or use optional setups like VS Code devcontainer or GitHub Codespaces.

### Prerequisites

- Toolhouse API Key (get it from https://app.toolhouse.ai/settings/api-keys)
- OpenAI API Key (get it from https://platform.openai.com)

### Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Boburmirzo/ai-data-transformation-code-generator.git
cd ai-data-transformation-code-generator
```

2. Create a .env file in your project directory with the API Keys:

```bash
TOOLHOUSE_API_KEY=(key from https://app.toolhouse.ai/settings/api-keys)
OPENAI_API_KEY=(key from https://platform.openai.com)
```

3. Install virtual environment (Preferred)

```bash
python3 -m venv env
source env/bin/activate
```
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Open your browser and go to http://localhost:8501 to interact with the app.

### Open in GitHub Codespaces
Click here to open in GitHub Codespaces

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=lightgrey&logo=github)](https://codespaces.new/Boburmirzo/ai-data-transformation-code-generator)

### Open in Dev Container

Click here to open in Dev Container

[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Container&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Boburmirzo/ai-data-transformation-code-generator)