from aiogram.utils.i18n import gettext


# i18n function
def _(text: str):
    def getargstranslation(**kwargs):
        return gettext(text).format(**kwargs)

    return getargstranslation


def get_text_by_locale(text: str, locale: str, **kwargs):
    return gettext(text, locale=locale).format(**kwargs)
