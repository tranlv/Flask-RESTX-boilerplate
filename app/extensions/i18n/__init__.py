import i18n


def configure_i18n(translation_path, locate):
    i18n.set("filename_format", "{locale}.{format}")
    i18n.set("skip_locale_root_data", True)
    i18n.set("locale", locate)
    i18n.set("fallback", "en")
    i18n.set("error_on_missing_translation", False)
    i18n.load_path.append(translation_path)


def set_locate(locate):
    i18n.set("locale", locate)


def lazy_translate(key, **kwargs):
    return lambda: i18n.t(key, **kwargs)
