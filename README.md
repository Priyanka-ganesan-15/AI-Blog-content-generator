# Bloggy 
## Overview

This Streamlit app, named "Bloggy: Your Writing Companion", helps users generate blog posts by providing a title, keywords, and a desired word count. The app uses Google's generative AI model (Gemini) to generate the blog content.

### Key Components:

1. **API Configuration**: Setting up API keys and configuring the generative AI model.
2. **Streamlit Layout**: Creating the layout and user input fields.
3. **Blog Generation**: Sending user inputs to the AI model and displaying the generated blog content.

### Setup and Configuration:

1. **Install Required Libraries**:
   Ensure you have Streamlit and the Google Generative AI client library installed:

    ```bash
    pip install streamlit google-generativeai
    ```

2. **API Keys**:
   - Store your API keys in a file named `apikey.py`:
    ```python
    google_gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
    open_ai_api_key = "YOUR_OPENAI_API_KEY"
    ```

### Streamlit App Code:

```python
import streamlit as st 
import google.generativeai as genai
from apikey import google_gemini_api_key, open_ai_api_key
import openai as OpenAI

# Configure Google Generative AI
genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Model setup
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Streamlit page configuration
st.set_page_config(layout='wide')

# Title and subtitle
st.title("Bloggy: Your Writing Companion")
st.subheader("Trying to evade a writer's block? Try Bloggy to get started on your next blog post.")

# Sidebar for user input
with st.sidebar: 
    st.title("Tell me about your blog?")

    blog_title = st.text_input("What is your title?")
    keywords = st.text_area("Give me a comma-separated list of your keywords!")
    num_words = st.slider("Word count", min_value=250, max_value=1000, step=250)

    prompt_parts = [
        f"Generate a blog post that is both engaging and comprehensive about the blog title, \"{blog_title}\", and keywords \"{keywords}\". Make sure to incorporate these keywords. The blog should be approximately {num_words} words in length and suitable for an online audience. Ensure the content is original, informative, and cohesive, and maintain a consistent tone.",
    ]
    
    submit_button = st.button(label="Generate")

if submit_button:
    # Generate blog content using the configured model
    blog = model.generate_content(prompt_parts)
    st.write(blog.text)
```

### How to Run the App:

1. **Save the code** in a file, e.g., `app.py`.
2. **Run the Streamlit app** from the terminal:

    ```bash
    streamlit run app.py
    ```

3. **Interact with the app** in the browser:
   - Enter the blog title and keywords in the sidebar.
   - Adjust the desired word count using the slider.
   - Click the "Generate" button to generate the blog post.

This app provides a user-friendly interface for generating blog content using advanced AI models. Adjust the safety settings, model parameters, and other configurations as needed to fit your requirements.
