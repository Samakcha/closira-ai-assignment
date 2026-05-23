from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_conversation_summary(
    conversation_history,
    lead_data,
    escalation_reason
):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are generating a structured customer support conversation summary.

                Return the summary under these exact headings:

                1. Customer Intent
                2. Key Details Collected
                3. Escalation Status
                4. SOP Gaps Identified
                5. Recommended Next Action

                Keep it concise, structured, and professional.
                """
                            },
                            {
                                "role": "user",
                                "content": f"""
                Conversation History:
                {conversation_history}

                Lead Data:
                {lead_data}

                Escalation Reason:
                {escalation_reason if escalation_reason else "No escalation"}
            """
            }
        ]
    )

    return response.choices[0].message.content