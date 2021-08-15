from marshmallow import fields, ValidationError, INCLUDE
from app.extensions.utils.util import (
    is_valid_password,
    is_valid_display_name
)
from app.extensions.schema import HoovadaSchema
from app.extensions.i18n import i18n, lazy_translate


def validate_password(data):
    if not is_valid_password(data):
        raise ValidationError(i18n.t("validation.error.invalid_password"))


def validate_display_name(data):
    if not is_valid_display_name(data):
        raise ValidationError(i18n.t("validation.error.invalid_display_name"))


class EmailRegistrationSchema(HoovadaSchema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": lazy_translate("validation.error.missing_field", field="email")
        },
        metadata={"description": "The email used for registration"}
    )
    password = fields.Str(
        required=True,
        validate=validate_password,
        error_messages={
            "required": lazy_translate("validation.error.missing_field", field="password")
        }
    )
    password_confirm = fields.Str(
        required=True,
        validate=validate_password,
        error_messages={
            "required": lazy_translate("validation.error.missing_field", field="password_confirm")
        }
    )
    display_name = fields.Str(
        required=True,
        validate=validate_display_name,
        error_messages={
            "required": lazy_translate("validation.error.missing_field", field="display_name")
        }
    )
    is_policy_accepted = fields.Bool(
        required=True,
        error_messages={
            "required": lazy_translate("validation.error.missing_policy")
        }
    )

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE
