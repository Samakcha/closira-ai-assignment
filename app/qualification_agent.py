QUALIFICATION_QUESTIONS = [
    "What type of business do you run?",
    "How large is your team?",
    "What tools are you currently using?"
]


def ask_qualification_questions(conversation_history):

    lead_data = {}

    print("\n--- Lead Qualification ---")

    for question in QUALIFICATION_QUESTIONS:

        print(f"\nAI: {question}")

        conversation_history.append({
            "role": "ai",
            "message": question
        })

        answer = input("Customer: ")

        conversation_history.append({
            "role": "customer",
            "message": answer
        })

        lead_data[question] = answer

    return lead_data