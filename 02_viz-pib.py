from frictionless import Package
import pandas as pd
import matplotlib.pyplot as plt

dp = Package('datapackage.json')
pib_mg = dp.get_resource('pib_mg').to_pandas()

# indice temporal
pib_mg.index = pd.date_range(start = '01/01/2002', periods = pib_mg.shape[0], freq = 'Q')
pib_mg.index = pib_mg.index.to_period('Q').strftime('Q%q-%Y')

# removendo coluna período
pib_mg.drop('Período (1)', axis = 1, inplace = True)

pib_mg['PIB'].plot()

plt.show()