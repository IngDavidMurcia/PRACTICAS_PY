import numpy as np

import pandas as pd


datos =pd.DataFrame({
    'edad' : [25, 30, 35, 40, 45],
    'ingresos' : [30000, 40000, 50000, 60000, 70000]
})
print("Datos del DataFrame:",datos.describe())