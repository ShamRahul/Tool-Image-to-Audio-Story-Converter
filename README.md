# LLM-Tool-Image-to-Audio-Story-Converter

Quick Prototyping Tool for AI Product Managers. Enabling the conversion of images to audio stories through various machine learning models. It is crafted to be user-friendly, specifically catering to product managers with a foundational understanding of Python, facilitating swift and efficient prototyping with models.

🚀 How to Run

🛠️ Prerequisites

1. Python installed on your system. Note: Make sure you install python 3.8 and not 3.11, else you would face challenges installing other libraries.
2. Basic knowledge of Python programming.
3. Visual Studio Code or any preferred IDE installed.

🛠️ Setup & Installation

1. Clone the Repository
2. git clone : repository-url
3. cd : repository-name

Install Necessary Libraries

1. pip install streamlit transformers requests python-dotenv Pillow

Setup Environment Variables

1. Create a .env file in the project directory.
2. Add your API keys to the .env file.
3. HUGGINGFACEHUB_API_TOKEN=your-huggingface-api-token
4. OPENAI_API_KEY=your-openai-api-key

🚀 Running the App

1. Open a terminal in the project directory.
2. Run the Streamlit app with the following command:
3. streamlit run <filename>.py
4. Open the displayed link in a web browser to interact with the app.

🌟 Features

1. Image to Text: Converts uploaded images to text using the Hugging Face Transformers library.
2. Story Generation: Generates short stories based on the converted text using the OpenAI GPT-3.5 Turbo model.
3. Text to Speech: Converts the generated stories to speech using the Hugging Face API.

📘 How to Use

1. Upload an Image: Use the file uploader to choose an image.
2. View the Uploaded Image: The uploaded image will be displayed on the app.
3. Generate and Listen to the Story: The app will automatically convert the image to text, generate a story, and convert the story to speech. You can listen to the generated audio story and view the scenario and story text in the expanders.

🙏 Acknowledgements

Special thanks to AI Jason YouTube Channel for the inspiration and knowledge sharing.

🤝 Contributing

Feel free to fork the project, make changes, and open a pull request if you think your changes should be included in the main project.


