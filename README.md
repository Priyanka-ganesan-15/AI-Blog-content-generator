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
