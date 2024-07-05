import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_names(value):
    pattern = r'^[A-Za-z\s]*$'
    if not re.match(pattern, value):
        raise ValidationError(
            gettext_lazy('Solo se aceptan letras en este campo'),
            code='invalid_name'
        )