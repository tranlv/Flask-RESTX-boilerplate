## Convention for define and validate the payload data

1. Each endpoint which require the data inuput from user must define a schema

``` python
from app.extensions.schema import HoovadaSchema

class EmailRegistrationSchema(HoovadaSchema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": messages.ERR_PLEASE_PROVIDE.format('email')
        },
        metadata={"description": "The email used for registration"}
    )
    password = fields.Str(
        required=True,
        validate=validate_password,
        error_messages={
            "required": messages.ERR_PLEASE_PROVIDE.format('password')
        }
    )
    password_confirm = fields.Str(
        required=True,
        validate=validate_password,
        error_messages={
            "required": messages.ERR_PLEASE_PROVIDE.format('password_confirm')
        }
    )
    display_name = fields.Str(
        required=True,
        validate=validate_display_name,
        error_messages={
            "required": messages.ERR_PLEASE_PROVIDE.format('display_name')
        }
    )
    is_policy_accepted = fields.Bool(
        required=True,
        error_messages={
            "required": messages.ERR_NO_POLICY_ACCEPTED
        }
    )
```

2. Add to swagger doc

View in endpoint need to pass the schema conversion to the `@api.expect()` to be automatically include in the swagger docs

```python
@api.route('/register', methods=['POST'])
class Register(Resource):
    # this is for swagger doc, no other meaning
    @api.expect(EmailRegistrationSchema().to_flask_restx_model(api))
    def post(self):
        return SampleController().register(api.payload)
```

3. Add validate decorator before the controller methods to validate data

``` python
from .decorator import validate_payload

class SampleController(Controller):

    @validate_payload(EmailRegistrationSchema)
    def register(self, data):
        # data here is clean and successfully validated
        return data
```

If there are error on the validation the response data will look like this:

``` json
{
  "status": false,
  "code": 400,
  "message": {
    "password": [
      "The password is invalid!"
    ],
    "email": [
      "Not a valid email address."
    ],
    "password_confirm": [
      "The password is invalid!"
    ]
  },
  "data": null
}
```

To run the example, go to `http://localhost:5000/api/v1/openapi` and try the example register

