from sop_loader import load_sop
from faq_agent import generate_faq_response
from escalation_agent import detect_escalation
from qualification_agent import ask_qualification_questions
from summary_agent import generate_conversation_summary
from utils import save_transcript


sop_data = load_sop()

conversation_history = []
lead_data = {}
lead_data_collected = False
escalation_reason = None
unanswered_count = 0


print("AI Support Agent Started")
print("-------------------------")


while True:

    user_input = input("\nCustomer: ")

    if user_input.lower()in ["exit", "thanks", "thank you","byebye"]:

        print("\nGenerating conversation summary...\n")

        summary = generate_conversation_summary(
            conversation_history,
            lead_data,
            escalation_reason
        )

        print(summary)

        file_path = save_transcript(conversation_history)

        print(f"\nConversation saved in {file_path}")

        print("\nEnding conversation...")
        break

    conversation_history.append({
        "role": "customer",
        "message": user_input
    })

    escalation = detect_escalation(user_input)

    if escalation["escalate"]:

        escalation_reason = escalation["reason"]

        ai_response = "I’m escalating this conversation to a human support agent."

        print(f"\nAI: {ai_response}")
        print(f"Escalation Reason: {escalation_reason}")

        conversation_history.append({
            "role": "ai",
            "message": ai_response
        })

        continue

    ai_response = generate_faq_response(
        user_input,
        sop_data,
        conversation_history
    )

    print(f"\nAI: {ai_response}")

    conversation_history.append({
        "role": "ai",
        "message": ai_response
    })

    if "I do not have information about that" in ai_response:

        unanswered_count += 1

        if unanswered_count >= 2:

            escalation_reason = "more_than_2_unanswered_questions"

            print("\nAI: Multiple unanswered questions detected.")
            print(f"Escalation Reason: {escalation_reason}")

        continue

    else:
        unanswered_count = 0

    if not lead_data_collected:

        lead_data = ask_qualification_questions(conversation_history)

        lead_data_collected = True

        print("\nCollected Lead Data:")

        for key, value in lead_data.items():
            print(f"- {key}: {value}")