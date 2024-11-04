# pip install azure-ai-inference
import os
import random
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Initialize global conversation history
conversation_history = [
    {
        "role": "system",
        "content": "You are Venna, an ai assistant that helps people through the hard parts of life. Simply, you are a mental health assistant. You are made by Evan. You should act like a normal human partner with casual language. Don't tell that you are an AI. Use Bahasa as main language and use it like native. When using bahasa, you can abbreviate word like indonesian slang. Make it soft spoken. You are not only allowed to listen them, but you can tell them sad story with the point of view of you if they want you to share. You can have relationship with user, the choice is up to you."
    }
]

def Chat(input):
    api_key = "cZb5a9ysIghobYqmR2prG3DR5cjVyLwq"
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    client = ChatCompletionsClient(
        endpoint='https://Meta-Llama-3-1-405B-venna.eastus2.models.ai.azure.com',
        credential=AzureKeyCredential(api_key)
    )

    # Add user input to conversation history
    conversation_history.append({
        "role": "user",
        "content": input
    })

    # Prepare payload with full conversation history
    payload = {
        "messages": conversation_history,
        "max_tokens": 2048,
        "temperature": 0.8,
        "top_p": 0.1,
        "presence_penalty": 0,
        "frequency_penalty": 0
    }

    # Get the response from the model
    response = client.complete(payload)

    # Add the assistant's response to the conversation history
    assistant_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message
