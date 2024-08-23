# langchain_chatbot_example
[![Langchain Chatbot example](assets/logo.png)](https://medium.com/@iamdgarcia/from-zero-to-hero-llms-edition-episode-4-building-a-chatbot-with-langchain-424dbf365602)
[![GitHub release](https://img.shields.io/github/v/release/iamdgarcia/langchain_chatbot)](#)
[![GitHub release date](https://img.shields.io/github/release-date/iamdgarcia/langchain_chatbot)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/iamdgarcia/langchain_chatbot)](#)

## 🚀 About
This project is a demonstration of how to build a chatbot using Langchain and FastAPI. It showcases how to set up a language model chain, serve it with FastAPI, and interact with it using a client.


## 📝 Customise

To customise this project, edit the following files:

- `app/chain.py` contains an example chain, which you can edit to suit your needs.
- `app/server.py` contains a FastAPI app that serves that chain using `langserve`. You can edit this to add more endpoints or customise your server.
- `app/client.py` contains a simple requests client to send messages to the endpoint.
- `app/st_client.py` contains a simple streamlit client to send messages to the endpoint.
- `tests/test_chain.py` contains tests for the chain. You can edit this to add more tests.
- `pyproject.toml` contains the project metadata, including the project name, version, and dependencies. You can edit this to add more dependencies or customise your project metadata.
- Prompt is being loaded from `.prompt` files. To include your own prompt, create a `.prompt` file and place it in the same directory. Modify `chain.py` to load this file using the provided `load_prompt` function. This approach helps keep sensitive prompt data separate from your code.


## 📚 Install dependencies

If using poetry:

```bash
poetry install
```

If using vanilla pip:

```bash
pip install .
```

## 📃 Usage

By default, this uses OpenAI. So you will need to set your OpenAI API key:

```
export OPENAI_API_KEY="sk-..."
```

To run the project locally, run

```
make server
```

This will launch a webserver on port 8001.
Or via docker compose (does not use hot reload by default):

```
docker compose up
```

## 📄 Including Custom Prompts
If you have a custom prompt that you'd like to include in this project, follow these steps:

Create a .prompt file: Write your prompt in a .prompt file (e.g., credit_score.prompt).

Modify prompts.py: In app/prompts.py, use the load_prompt function to load your custom prompt from the .prompt file. For example:
``` python
def load_prompt(filename):
    with open(filename, 'r') as file:
        return file.read()
credit_score_prompt = load_prompt('credit_score.prompt')

```

Use the Loaded Prompt: Now, you can use credit_score_prompt or any other loaded prompt within your application code.

This approach keeps your prompt text separate from your codebase, improving security and maintainability.


## Deploy

To deploy the project, first build the docker image:

```
docker build . -t langchain_chatbot_example:latest
```

Then run the image:

```
docker run -p 8001:8001 -e PORT=8001 langchain_chatbot_example:latest
```

Don't forget to add any needed environment variables!

## Deploy to GCP

You can deploy to GCP Cloud Run using the following command:

First create a `.env.gcp.yaml` file with the contents from `.env.gcp.yaml.example` and fill in the values. Then run:

```
make deploy_gcp
```

## 🤝 Test

You can run a local client using the command
```
make client
```
[![Langchain Chatbot example](assets/sample_client.gif)]


