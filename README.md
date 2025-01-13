
# Fitness and Diet Planner - AI-Powered Personalized Plans

This project is an AI-powered Fitness and Diet Planner that generates customized workout and diet plans based on user inputs. The application uses the **llama-3.3-70b-versatile model** hosted on **Groq Cloud** to create personalized plans and features an interactive chat interface to engage users and refine their plans.

## Features

- **Personalized Plans**: Generate customized workout and diet plans based on your inputs such as current weight, target weight, workout type, and more.
- **Interactive Chat**: Ask questions about your generated plan and get helpful responses from the AI assistant.
- **User-Friendly Interface**: Built with **Streamlit**, this application allows you to enter your details in an easy-to-use form and view your personalized plans.

## Getting Started

Follow these steps to run the application on your local machine:

### Prerequisites

- Python 3.x
- Streamlit
- LangChain
- Groq API Key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vikrambhat2/AIFitnessPlanner.git
   cd AIFitnessPlanner
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your **Groq API Key**:

   ```
   GROQ_API_KEY=your_groq_api_key
   ```

4. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

### Usage

- Enter your fitness and diet details, such as workout type, diet type, current weight, target weight, and other information.
- Click "Generate Plans" to receive personalized diet and workout plans.
- Use the interactive chat interface to ask questions and refine your plans further.

## Code Explanation

- **Streamlit UI**: The front-end of the app is created using Streamlit, which allows for easy deployment and a clean user interface.
- **LangChain**: We use LangChain to interface with the **llama-3.3-70b-versatile model** hosted on **Groq Cloud** to generate customized plans.
- **Chat Interface**: Users can ask the system questions about their plans, and the system provides real-time answers based on the generated plan.


## Contributing

Feel free to open issues or submit pull requests to improve this project. Contributions are welcome!



💡 **Created by Vikram Bhat**


