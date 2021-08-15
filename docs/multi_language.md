# Multi languages support

### Translation files:

Can be configure via environment variable: TRANSLATION_PATH, or default at: `./app/translations/` 

Directory structure:

``` bash
translations
├── en.yml
└── vi.yml
```

File content

``` yaml
hi: Hello world !
# zero, one, few, many are keyword for plural switch
example_plural:
  zero: There is %{count} person of %{field}. Please add more
  one: Congrats, you have one person in your network
  few: Congrats, you have several person in your network
  many: Congrats, there are many people in your network
validation:
  error:
    invalid_password: Password is not valid
    missing_field: Please provide field %{field}
    missing_policy: Policy is not accepted!
```

### How to use

#### 1. Using
``` python
from app.extensions.i18n import i18n, lazy_translate

# use directly
i18n.t("validation.error.invalid_password")
# use with parameter
i18n.t("validation.error.missing_field", field="password")
# option for plural
i18n.t("example_plural", count=0 ,field="network")
# -> output: There is 0 person in network. Please add more
i18n.t("example_plural", count=100 ,field="network")
# -> Congrats, there are many people in your network

# use lazy translate to make sure the configuration have been affected
# and the translation will be evaludated at runtime
lazy_translate("validation.error.missing_field", field="password")
```

#### 2. Configure

- These are already hooked to the before request, and default to read query parameter: `language`.
- We can expand to use user setting for browser preference language to setting the language

```
from app.extensions.i18n import configure_i18n

configure_i18n(BaseConfig.TRANSLATION_PATH, locate=language)
```

API call:

- ENGLISH: `api/v1/sample/register?language=en`
- VIETNAMESE: `api/v1/sample/register?language=vi`

#### To add more language:

- add new file under TRANSLATION_PATH, named: `<locale>.yml`. Example: `es.yml`
