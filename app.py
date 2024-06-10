import streamlit as st 
import google.generativeai as genai
from apikey import google_gemini_api_key, open_ai_api_key
import openai as OpenAI

# client = OpenAI.Client(api_key=open_ai_api_key)
genai.configure(api_key= google_gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#model set-up
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)




st.set_page_config(layout='wide')

#TITLE
st.title("Bloggy : Your Writing Companion")
st.subheader('Trying to evade a writer\'s block? Try Bloggy to get started on your next blog post.')

#sidebar
with st.sidebar: 
    st.title("Tell me about your blog?")

    blog_title = st.text_input("What is your title?")

    Keywords = st.text_area("give me a comma-seperated list of you keywords!")

    num_words = st.slider("Word count", min_value=250, max_value=1000, step= 250 )

    # num_images = st.number_input("How many images would you like?", min_value= 1, max_value= 5, step =1)

    prompt_parts = [
        f"Generate a blog post that is both engaging and comprehensive about the blog title, \"{blog_title}\", and keywords \"{Keywords}\". Make sure to incorporate these keywords. The blog should be aproximately {num_words} words in length and suitable for an online audience. Ensure the content is original, informative and cohesive, and maintain a consistent tone",
    ]
    
    submit_button = st.button(label="Generate")

if submit_button:

    blog = model.generate_content(prompt_parts)

    # images = client.images.generate(
    # model="dall-e-3",
    # prompt="a white siamese cat",
    # size="1024x1024",
    # quality="standard",
    # n=1,
    # )
    # image_url = images.data[0].url

    # st.image(image_url, caption= "generated image")
    st.write(blog.text)







