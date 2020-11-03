from django.core.exceptions import ValidationError

def validate_location(container):
    """
    Validation function used to validate the location field of FacadeForm.
    This function force the correctly use of commas between city, state and country.
    It doesn't allow inputs like: 'city,, state country' or 'city,    ,'
    """

    locations = container.replace(' ', '')
    locations = locations.split(',')


    if '' in locations:
        raise ValidationError('Por favor, utilize a separação por vírgulas corretamente.')

    if len(locations) != 3:
        raise ValidationError('Por favor, preencha utlizando o nome da cidade, estado e país, respectivamente.')

    if len(locations) > 3:
        raise ValidationError('Por favor, coloque a entrada de forma correta. Informações de como adicionar a cidade estão na aba "ajuda".')

    return container
