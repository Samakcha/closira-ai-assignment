from openai import OpenAI
from dotenv import load_dotenv
import os

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_faq_response(
    user_message,
    sop_data,
    conversation_history
):

    recent_history = conversation_history[-6:]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                SOP DATA:
                {sop_data}

                RECENT CONVERSATION HISTORY:
                {recent_history}

                CUSTOMER MESSAGE:
                {user_message}

                Answer strictly from SOP only.

                If answer does not exist in SOP:
                reply exactly:
                "I do not have information about that in the SOP. I recommend escalating this to a human support agent."
                """
            }
        ]
    )

    return response.choices[0].message.content