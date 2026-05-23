ESCALATION_KEYWORDS = {
    "angry": [
        "terrible",
        "bad service",
        "disappointed",
        "angry",
        "frustrated",
        "complaint"
    ],

    "human_request": [
        "human",
        "real person",
        "agent",
        "manager"
    ],

    "medical_question": [
        "pregnant",
        "side effects",
        "medical",
        "safe",
        "allergy"
    ],

    "pricing_negotiation": [
        "discount",
        "cheaper",
        "lower price",
        "negotiate"
    ]
}

def detect_escalation(user_message):
    message = user_message.lower()
    for category, keywords in ESCALATION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in message:
                return {
                    "escalate": True,
                    "reason": category
                }
    
    return {
        "escalate": False,
        "reason": None
    }
            