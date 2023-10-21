from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, text, language_code='ru'):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    tg_answer = response.query_result.fulfillment_text
    vk_answer = None
    if not response.query_result.intent.is_fallback:
        vk_answer = tg_answer
    return tg_answer, vk_answer

