import json
import argparse
from environs import Env
from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(
        description='Программа загружает вопросы, ответы и создает intent для бота в DialogFlow'
    )
    parser.add_argument(
        'mypath',
        help='Путь к файлу с вопросами-ответами в *.json формате'
    )
    args = parser.parse_args()

    load_dotenv()
    with open(args.path, "r") as file:
        questions = file.read()

    questions = json.loads(questions)

    for intent_name in questions.keys():
        intent = questions[intent_name]
        create_intent(
            env.str("PROJECT_ID"),
            intent_name,
            intent['questions'],
            [intent['answer']],
        )


if __name__ == '__main__':
    main()
