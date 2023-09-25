# Import necessary libraries and modules
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
import requests
import os
import streamlit as st

# Load environment variables from a .env file
load_dotenv(find_dotenv())
# Retrieve API tokens from environment variables
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Define a function to convert image to text
def img2text(url):
     # Initialize the image-to-text pipeline from Hugging Face Transformers
    image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")

     # Get the generated text from the image
    text = image_to_text(url)[0]["generated_text"]

    # Print and return the generated text
    print(text)
    return text

# Test the img2text function with an example image file 
img2text("IMG_6502.jpeg")



#llm using ChatGPT- Define a function to generate a story based on a scenario
def generate_story(scenario):
    # Define a template for the prompt to be used with the language model
    template = """
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 50 words;

    CONTEXT: {scenario}
    STORY;
    """

    # Create a prompt with the given template and scenario
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

     # Initialize the language model with specified parameters
    story_llm = LLMChain(llm=OpenAI(model_name= "gpt-3.5-turbo", temperature=1, max_tokens=100), prompt=prompt, verbose=True)

     # Generate and print the story based on the given scenario
    story = story_llm.predict(scenario=scenario)

    print(story)
    return story




# Define a function to convert text to speech
def text2speech(message):
     # Define the API URL for the Hugging Face model
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    # Set up the headers for the API request, including the authorization token
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    # Define the payload for the API request
    payloads={
        "inputs": message
    }

    # Make a POST request to the API and write the response content to a file
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)


# Define the main function to run the Streamlit app
def main():
    
    # Set up the Streamlit page configuration
    st.set_page_config(page_title="img 2 audio story", page_icon="")

    st.header("Turn Image to Audio Story")
    # Allow the user to upload an image file
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    # If a file is uploaded, process the file and generate the audio story
    if uploaded_file is not None:
        print(uploaded_file)
        # Write the uploaded file to the local storage
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)

         # Display the uploaded image on the Streamlit app
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=False)
        # Convert the image to text, generate a story from the text, and convert the story to speech
        scenario = img2text(uploaded_file.name)
        story = generate_story(scenario)
        text2speech(story)

        # Display the scenario and story on the Streamlit app
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)

         # Play the generated audio on the Streamlit app
        st.audio("audio.flac")

# Run the main function if the script is executed
if __name__ == '__main__':
    main()