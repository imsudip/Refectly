# REFLECTLY - Reflective Journaling AI

REFLECTLY is a Reflective Journaling AI designed to assist users in exploring their thoughts and feelings, serving as a catalyst for self-discovery and personal growth. This command-line application is built using Python and leverages Chroma DB and OpenAI APIs (LFMs) for its functionality.

## Features

1. **Reflective Journaling**: REFLECTLY provides users with a platform to engage in reflective journaling. Users can express their thoughts, emotions, and experiences through text input.

2. **Knowledge Base Storage**: The AI utilizes Chroma DB as a vector database to store embeddings of the knowledge base (KB). These embeddings are created during conversations with the AI and serve as long-term memory for the system, allowing it to retain critical user information.

3. **Personalized AI Interaction**: REFLECTLY employs OpenAI APIs to facilitate natural language processing and generation. The AI engages in conversations with users, offering empathetic responses and meaningful insights based on the user's input.

4. **Self-Discovery and Personal Growth**: By providing a safe and non-judgmental space for users to reflect and express themselves, REFLECTLY aims to support users on their journey of self-discovery and personal growth. The AI's responses and prompts encourage introspection and help users gain insights into their emotions and experiences.

## Technologies Used

The project utilizes the following technologies:

- **(LFMs) OpenAI APIs**: OpenAI APIs are leveraged for natural language processing and generation. These APIs enable the AI to engage in conversations with users and provide meaningful responses based on the input received.
- **Python**: The application is developed using the Python programming language, which provides a robust and versatile framework for building AI-driven applications.

- **Chroma DB**: Chroma DB is used as a vector database for storing embeddings of the knowledge base. It allows efficient retrieval and storage of data, enabling the AI to maintain and recall user information effectively.


## Setup

To use REFLECTLY, follow these steps:

1. Clone the repository:
2. Install the required packages: `pip install -r requirements.txt`
3. Update `user_profile.txt` file with your initial information
```
- Name: UPDATE WITH YOUR NAME
- Profession: UPDATE WITH YOUR JORB
- Interests: UPDATE WITH YOUR HORBIES
- Beliefs: WHAT DO YOU BELIEVE?
- Plans: WHAT ARE YOUR GOALS?
- Preference: HOW DO YOU PREFER TO COMMUNICATE?
```
4. Update `key_openai.txt` with your OpenAI API key

## Usage

- Main chat client: `python chat.py`
- Take a look in your KB: `python chromadb_peek.py`

## Code Explanation

This Python script serves as the implementation of a chatbot that leverages the OpenAI's GPT-4 model. It additionally integrates the chatbot with a persistent knowledge base using the ChromaDB library. Here's an overview of how the different parts of the script function:

1. **Utility Functions**: The script starts with several utility functions to handle file operations and to interact with OpenAI's API. These include functions for saving and opening files, and a function to run the chatbot, managing retries in case of exceptions.
2. **Main Application**: The script's main operation is contained within a continuous loop (`while True:`), enabling continuous interaction with the user. This loop does the following:
   - **Instantiates the ChromaDB client** for persistent storage and knowledge base management.
   - **Initiates the chatbot** by loading OpenAI's API key and preparing a conversation list.
   - **Captures user input** and adds it to the conversation list. The input is also logged in a separate file for record-keeping.
   - **Searches the knowledge base** for relevant content based on the current conversation and updates the chatbot's default system message accordingly.
   - **Generates a response** from the chatbot based on the conversation so far, which includes the updated default system message and the user's input.
   - **Updates the user profile** based on the user's recent messages, using the chatbot's response as the updated profile.
   - **Updates the knowledge base** with the most recent conversation, either adding a new entry or updating an existing entry. If an existing entry becomes too long, it's split into two separate entries.

The script logs all interactions with the OpenAI API and updates to the knowledge base, providing a record of the chatbot's operations and aiding in debugging and optimization efforts. The use of the ChromaDB library allows for scalable storage and retrieval of the chatbot's knowledge base, accommodating a growing number of conversations and data points.

But seriously just look at the code, it's pretty straight forward. 

## Future Enhancements

The REFLECTLY project has the potential for future enhancements, including:

- Developing a graphical user interface (GUI) for a more user-friendly and visually appealing experience.
- Using `langchain` to optimize the code.


## Contribution

Contributions to the project are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request describing the changes you have made.


## Credits

- [OpenAI](https://openai.com/) for their amazing API
- Inspiration from a repo of [David Sappiro]() which which gives the idea of knowledge base.
- I've used `gpt-3-turbo-32k` and ChromaDB and added multi threading to make it faster. also made the prompts better.
