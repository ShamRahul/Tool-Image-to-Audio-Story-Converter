# Tool-Image-to-Audio-Story-Converter
It'a a quick prototyping tool for AI Product Managers

This project allows you to convert images to audio stories using various machine learning models. It is designed to be user-friendly and is suitable for product managers with a basic Python background, allowing for fast prototyping with models.

How to Run

Prerequisites
Python installed on your system.
Basic knowledge of Python programming.
Visual Studio Code or any preferred IDE installed.

Setup & Installation

1. Clone the Repository
git clone <repository-url>
cd <repository-name>

2.Install Necessary Libraries
pip install streamlit transformers requests python-dotenv Pillow

3.Setup Environment Variables
Create a .env file in the project directory.
Add your API keys to the .env file.
HUGGINGFACEHUB_API_TOKEN=your-huggingface-api-token
OPENAI_API_KEY=your-openai-api-key

Running the App

1.Open a terminal in the project directory.
2.Run the Streamlit app with the following command:
streamlit run <filename>.py
3.Open the displayed link in a web browser to interact with the app.

Features
1.Image to Text: Converts uploaded images to text using the Hugging Face Transformers library.
2.Story Generation: Generates short stories based on the converted text using the OpenAI GPT-3.5 Turbo model.
3.Text to Speech: Converts the generated stories to speech using the Hugging Face API.

How to Use
1.Upload an Image: Use the file uploader to choose an image.
2.View the Uploaded Image: The uploaded image will be displayed on the app.
3.Generate and Listen to the Story: The app will automatically convert the image to text, generate a story, and convert the story to speech. You can listen to the generated audio story and view the scenario and story text in the expanders.

Acknowledgements
Special thanks to AI Jason YouTube Channel for the inspiration and knowledge sharing.

Contributing
Feel free to fork the project, make changes, and open a pull request if you think your changes should be included in the main project.
