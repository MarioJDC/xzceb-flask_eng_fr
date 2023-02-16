"""
Translator of french to english text.
@Author: Mario Afonso
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

class Translator:
    def __init__(self):
        authenticator = IAMAuthenticator(APIKEY)
        self.language_translator = LanguageTranslatorV3(
            version='2022-02-01',
            authenticator=authenticator
        )
        self.language_translator.set_service_url(URL)

    def __translate(self,text,languagepair):
        response = self.language_translator.translate(text=text, model_id=languagepair)
        return response.get_result()['translations'][0]['translation']

    def english_to_french(self,english_text):
        try:
            return self.__translate(english_text,'en-fr')
        except ApiException as exception:
            print("Api failed with error: " +str(exception.code) + ": " + exception.message +"\n")
            return ""

    def french_to_english(self,french_text):
        try:
            return self.__translate(french_text,'fr-en')
        except ApiException as exception:
            print("Api failed with error: " +str(exception.code) + ": " + exception.message + "\n")
            return ""