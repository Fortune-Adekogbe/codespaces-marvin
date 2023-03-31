from marvin import ai_fn

@ai_fn
def translator_pidgin_to_english(pidgin_text: str)-> list:
    """
    Given a Nigerian Pidgin sentence, this function returns a list of 2 english translations and the model's confidence in the translation.
    """

print(translator_pidgin_to_english("Progress Chukwuyem na di winner of Nigerian Idol Season 7."))
print(translator_pidgin_to_english("All di local and world tori wey you suppose know in 60 seconds!"))