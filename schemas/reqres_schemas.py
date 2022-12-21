from voluptuous import Schema, PREVENT_EXTRA, Required, Optional, ALLOW_EXTRA

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

put_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

login_user_schema = Schema(
    {
        "token": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

