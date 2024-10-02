import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.api import VECM
from statsmodels.tsa.vector_ar.vecm import coint_johansen, select_coint_rank
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint
from statsmodels.tsa.stattools import adfuller

# Data yüklenmesi
data = pd.read_excel("C:/Users/Yasin/Desktop/data.xlsx")

# Data kontrolü
print(data.head())

# Eksik değerlerin kontrolü
print("Eksik değer sayısı:", data.isnull().sum().sum())

# Veri Tipi kontrolü
print(data.info())

# Tarihi date type çevirme
data['Tarih'] = pd.to_datetime(data['Tarih'], format='%Y-%m')
data.set_index("Tarih", inplace=True)

data = np.log(data)

# Trend Analizi
plt.figure(figsize=(14, 8), dpi=150)
data.plot()
plt.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize="large")
plt.xlabel("Date", fontsize=14)
plt.ylabel("Values", fontsize=14)
plt.title("Line Chart", fontsize=16)
plt.xticks(rotation=45)
plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.2)
plt.show(block=True)


# Durağanlık Testi (ADF Test)
def adf_test(data):
    results = {}
    for column in data.columns:
        clean_data = data[column].dropna()
        if len(clean_data) > 1:
            result = adfuller(clean_data)
            results[column] = {
                'Test Statistic': result[0],
                'p-value': result[1]
            }
        else:
            results[column] = {'Test Statistic': np.nan, 'p-value': np.nan}
    return results


adf_results = adf_test(data)

for column, result in adf_results.items():
    print(f"Değişken: {column}")
    print(f"Test İstatistiği: {result['Test Statistic']}")
    print(f"P-değeri: {result['p-value']}")
    if result['p-value'] > 0.05:
        print("HO: Birim Kök var, Durağan Değil")
    else:
        print("H1: Birim Kök yok, Durağandır")
    print("----------------")

# Fark alma birinci dereceden (durağan hale getirmek için)
data = data.diff().dropna()

# Gecikme Seçimi
model = VAR(data)
lag = model.select_order(maxlags=2)
print(lag.selected_orders)

# Eş bütünleşme testi
j_test = coint_johansen(data, det_order=0, k_ar_diff=2)
result = pd.DataFrame()
result["İz Test"] = j_test.lr1
result["İz Test Kritik"] = j_test.cvt.T[1]
result["Öz Değer"] = j_test.lr2
result["Öz Değer Kritik"] = j_test.cvm.T[2]
print(result)

# Coınt_rank seçimi
result = select_coint_rank(data, det_order=0, k_ar_diff=2, method="trace", signif=0.05)
print("Coint_rank:", result.rank)

# VAR modeli kurulumu
vecm_model = VECM(data, k_ar_diff=2, coint_rank=3).fit()
print(vecm_model.summary())
