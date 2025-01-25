from aiogram.utils.i18n import gettext


# i18n function
def _(text: str):
    def getargstranslation(**kwargs):
        return gettext(text).format(**kwargs)

    return getargstranslation


def get_text_by_locale(text: str, locale: str, **kwargs):
    return gettext(text, locale=locale).format(**kwargs)


# New text templates for the GIF search feature
GIF_SEARCH_RESULTS = _("Here are the GIFs matching your search:")
NO_GIFS_FOUND = _("No GIFs found for the given tags.")
NO_TAGS_PROVIDED = _("Please provide tags to search for GIFs.")
