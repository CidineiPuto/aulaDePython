# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# Minha solução________________________________________________________________

# from datetime import datetime

# from dateutil.relativedelta import relativedelta

# start_of_loan = datetime.strptime('20/12/2020', '%d/%m/%Y')  # emprestimo
# five_years = relativedelta(years=5)
# end_of_loan = (start_of_loan + five_years)  # final do emprestimo
# twenty_day = relativedelta(day=20)

# # calcular o valor da parcela mensal
# loan_amount = 1000000
# interest_rate = 0.01  # taxa de juro,  1% de juros ao mês
# num_payments = 60  # 5 anos = 60 meses

# monthly_interest_rate = interest_rate / 12  # taxas de juro mensais
# present_value = (1 + monthly_interest_rate) ** (-num_payments)
# # valor necessário para pagar hoje e quitar toda a divida com os juros
# # acumulados

# annuity_factor = (1 - present_value) / monthly_interest_rate
# monthly_payment = loan_amount / annuity_factor

# # calcular as datas de vencimento e o valor de cada parcela
# payment_date = start_of_loan + twenty_day
# fmt = "%d/%m/%Y"

# for num in range(num_payments):

#     print(
#         f'Data de vencimento: {payment_date.strftime(fmt)}'
#         f' -- Valor da parcela: R${monthly_payment:.2f}')
#     payment_date += relativedelta(months=1)

# Professor solução____________________________________________________________
from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_empréstimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_empréstimo + delta_anos

data_parcela = data_empréstimo

data_parcelas = []
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas
fmt = ('%d/%m/%Y')

for data in data_parcelas:
    print(data.strftime(fmt), f'R${valor_parcela:,.2f}')
print()

print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)
