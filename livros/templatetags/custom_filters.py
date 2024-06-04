from django import template

register = template.Library()

@register.filter
def numeroEstrelasCheias(numeroestrelas):
    return range(int(numeroestrelas))

@register.filter
def numeroEstrelasMetade(numeroestrelas):
    numero_string = str(numeroestrelas)
    posicao_virgula = numero_string.find('.')
    primeiro_digito_apos_virgula = numero_string[posicao_virgula + 1]
    primeiro_digito_int = int(primeiro_digito_apos_virgula)
    if(primeiro_digito_int >= 5):
        return range(1)
    return range(0)

@register.filter
def numeroEstrelasVazio(numeroestrelas):

    return range(5 - round(numeroestrelas))