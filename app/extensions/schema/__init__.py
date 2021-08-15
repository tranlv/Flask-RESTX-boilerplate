from flask_restx import fields as restx_fields
from marshmallow import Schema, fields


class HoovadaSchema(Schema):
    TYPE_MAPPING = {
        fields.String: restx_fields.String,
        fields.URL: restx_fields.Url,
        fields.DateTime: restx_fields.DateTime,
        fields.Date: restx_fields.Date,
        fields.Boolean: restx_fields.Boolean,
        fields.Integer: restx_fields.Integer,
        fields.Float: restx_fields.Float
    }

    def to_flask_restx_model(self, api):
        # this conversion to make sure this can be use to render
        # swagger docs
        restfx_model = dict()
        for key, value in self.fields.items():
            restx_equivalent_field = self.TYPE_MAPPING.get(
                type(value), restx_fields.String
            )
            kwargs = {}
            if value.required is True:
                kwargs["required"] = True
            if value.metadata.get("description") is not None:
                kwargs["description"] = value.metadata.get("description")
            if bool(kwargs) is True:
                restfx_model[key] = restx_equivalent_field(**kwargs)
            else:
                restfx_model[key] = restx_equivalent_field(**kwargs)

        return api.model(self.__class__.__name__, restfx_model)
