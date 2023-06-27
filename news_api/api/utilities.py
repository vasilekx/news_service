# api/utilities.py

from django.db.models.base import ModelBase
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def delete_object(model: ModelBase,
                  fields: dict,
                  exist: bool,
                  message: str,
                  errors_message: str) -> Response:
    if not exist:
        return Response(
            {
                'errors': errors_message
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    get_object_or_404(model, **fields).delete()
    return Response(
        {
            'detail': message
        },
        status=status.HTTP_204_NO_CONTENT
    )
