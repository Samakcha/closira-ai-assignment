import os


def save_transcript(conversation_history):

    folder_name = "test_transcripts"

    os.makedirs(folder_name, exist_ok=True)

    existing_files = [
        file for file in os.listdir(folder_name)
        if file.startswith("session_transcript_") and file.endswith(".md")
    ]

    session_number = len(existing_files) + 1

    file_path = f"{folder_name}/session_transcript_{session_number}.md"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for message in conversation_history:

            role = message["role"].capitalize()
            content = message["message"]

            file.write(f"{role}: {content}\n\n")

    return file_path