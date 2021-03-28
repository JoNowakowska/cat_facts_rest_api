"""This module connects to the external API (Google Cloud Translation API) to translate texts."""

from google.cloud import storage

import os

credential_path = "service_account.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# Explicitly use service account credentials by specifying the private key file.
storage_client = storage.Client.from_service_account_json('service_account.json')

# Make an authenticated API request
buckets = list(storage_client.list_buckets())


def translate_text(target, text):
    """Get response from the Google Cloud Translation API and return a list of translated strings."""
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.

    result = translate_client.translate(text, target_language=target)

    translated_list = [i.get("translatedText") for i in result]

    return translated_list

