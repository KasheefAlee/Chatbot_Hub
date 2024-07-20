
# Chatbot Hub

Welcome to Kashif Ali Azim's Chatbot Hub! This project is a web application that hosts multiple AI-powered chatbots and a sentiment analysis tool. The application is built using Flask and integrates various AI models to provide different functionalities.

## Project Structure

```
project/
│
├── static/
│   ├── background.jpeg
│   └── style.css
│
├── templates/
│   ├── chatbot.html
│   ├── main.html
│   └── sentiment.html
│
├── app.py
└── README.md
```

- `static/`: Contains static files such as images and CSS.
- `templates/`: Contains HTML templates for different pages.
- `app.py`: The main Flask application file.
- `README.md`: This readme file.

## Setup

### Prerequisites

- Python 3.7 or higher
- Flask

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/chatbot-hub.git
   cd chatbot-hub
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On MacOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask application:**

   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

## Features

### Main Page

The main page welcomes users and provides links to the different chatbots and sentiment analysis tool.

### Chatbots

- **Friendly Chatbot:** An AI chatbot designed to have friendly and engaging conversations.
- **PDF Q&A Chatbot:** An AI chatbot capable of answering questions from an uploaded PDF file.

### Sentiment Analysis

A tool that uses an AI model to analyze the sentiment of user-provided text.

## File Descriptions

- **`app.py`**: Contains the main Flask application code.
- **`templates/main.html`**: The HTML template for the main page.
- **`templates/chatbot.html`**: The HTML template for the chatbot page.
- **`templates/sentiment.html`**: The HTML template for the sentiment analysis page.
- **`static/background.jpeg`**: The background image used in the application.
- **`static/style.css`**: Custom CSS styles for the application.

## Configuration

Ensure the Flask app is configured to serve static files correctly. You can place your static files in the `static` directory and use them in your HTML templates.

## Troubleshooting

If you encounter issues with the background image not displaying, ensure the following:
- The image file `background.jpeg` is located in the `static` directory.
- The HTML template references the image correctly using `{{ url_for('static', filename='background.jpeg') }}`.
- Clear your browser cache and perform a hard refresh.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
