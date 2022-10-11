from django.core.exceptions import ValidationError

def validar_distrito(value):
    if value > 16:
        raise ValidationError(
            '%(value)s no es Distrito existente en Cochabamba',
            params={'value': value}
        )

def validar_subdistrito(value):
    if value > 25:
        raise ValidationError(
            '%(value)s no es un SubDistrito existente en Cochabamba',
            params={'value': value}
        )

def validar_codcat(value):
    if len(value) > 15:
        raise ValidationError(
            '%(value)s no es codigo catastral valido',
            params={'value': value}
        )
