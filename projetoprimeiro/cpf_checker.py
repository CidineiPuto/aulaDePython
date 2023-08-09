import os


def cpf_checker(cpf):
    cpf_enviado_usuario = cpf
    cpf_novo = ""

    for digito in cpf_enviado_usuario:
        if digito == "." or digito == "-" or digito == " ":
            cpf_novo += ""
        else:
            cpf_novo += digito

    entrada_e_sequencial = cpf_novo == cpf_novo[0] * len(cpf_novo)
    if entrada_e_sequencial:
        os.system("cls")
        raise ValueError

    nove_digitos = cpf_novo[:9]
    contador_regressivo = 10

    resultado_dig_1 = 0

    for digito in nove_digitos:
        try:
            resultado_dig_1 += int(digito) * contador_regressivo
            contador_regressivo -= 1
        except ValueError:
            resultado_dig_1 = 0
            break

    if not resultado_dig_1:
        os.system("cls")
        raise ValueError

    digito1 = (resultado_dig_1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo2 = 11
    resultado_dig_2 = 0

    for digito in dez_digitos:
        resultado_dig_2 += int(digito) * contador_regressivo2
        contador_regressivo2 -= 1

    digito_2 = (resultado_dig_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_feito_pelo_calculo = f"{nove_digitos}{digito1}{digito_2}"

    os.system("cls")

    if cpf_novo != cpf_feito_pelo_calculo:
        return False
    return True
