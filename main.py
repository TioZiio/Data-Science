import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import plotly.express as px


arquivo = 'credit_risk_dataset.csv'

df = pd.read_csv(arquivo)

"""
Columns:
person_age - Idade
person_income - Renda anual
person_home_ownership - Propriedade da casa (Aluguel, Hipoteca, Dono)
person_emp_length - Tempo do emprego
loan_intent - Intenção do emprestimo (Educação, Médico, Quitar dividas, Empreendimento)
loan_grade - Grau do emprestimo
loan_amnt - Valor do emprestimo
loan_int_rate - Taxa de juros
loan_status - Status do emprestimo (1 inadimplente, 0 não)
loan_percent_income - Renda percentual
cb_person_default_on_file - Inadimplencia historica
cb_person_cred_hist_length - Duração do histórico de crédito
 """

un = np.unique(df['cb_person_default_on_file'], return_counts=True)

print(df['person_income'])

# plt.hist(x=df['person_income'])

gra =  px.scatter_matrix(df, dimensions=['person_age', 'person_income'])
gra.show()
