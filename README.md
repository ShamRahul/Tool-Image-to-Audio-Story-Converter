# Tool-Image-to-Audio-Story-Converter

Quick Prototyping Tool for AI Product Managers
This project serves as a quick prototyping tool, enabling the conversion of images to audio stories through various machine learning models. It is crafted to be user-friendly, specifically catering to product managers with a foundational understanding of Python, facilitating swift and efficient prototyping with models.

🚀 How to Run

🛠️ Prerequisites
Python installed on your system.
Basic knowledge of Python programming.
Visual Studio Code or any preferred IDE installed.

🛠️ Setup & Installation
Clone the Repository
git clone <repository-url>
cd <repository-name>

Install Necessary Libraries
pip install streamlit transformers requests python-dotenv Pillow

Setup Environment Variables
Create a .env file in the project directory.
Add your API keys to the .env file.
HUGGINGFACEHUB_API_TOKEN=your-huggingface-api-token
OPENAI_API_KEY=your-openai-api-key

🚀 Running the App
Open a terminal in the project directory.
Run the Streamlit app with the following command:
streamlit run <filename>.py
Open the displayed link in a web browser to interact with the app.

🌟 Features
Image to Text: Converts uploaded images to text using the Hugging Face Transformers library.
Story Generation: Generates short stories based on the converted text using the OpenAI GPT-3.5 Turbo model.
Text to Speech: Converts the generated stories to speech using the Hugging Face API.

📘 How to Use
Upload an Image: Use the file uploader to choose an image.
View the Uploaded Image: The uploaded image will be displayed on the app.
Generate and Listen to the Story: The app will automatically convert the image to text, generate a story, and convert the story to speech. You can listen to the generated audio story and view the scenario and story text in the expanders.

🙏 Acknowledgements
Special thanks to AI Jason YouTube Channel for the inspiration and knowledge sharing.

🤝 Contributing
Feel free to fork the project, make changes, and open a pull request if you think your changes should be included in the main project.


