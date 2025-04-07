import pandas as pd

df = pd.read_csv("HIV_AIDS_Diagnoses_by_Neighborhood__Sex__and_Race_Ethnicity_20250403.csv")

colsToConvert = [
    "TOTAL NUMBER OF HIV DIAGNOSES",
    "HIV DIAGNOSES PER 100,000 POPULATION",
    "TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES"
]

for col in colsToConvert:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df2013 = df[df["YEAR"] == 2013]
df2013 = df2013[
    (df2013["TOTAL NUMBER OF HIV DIAGNOSES"] > 0) &
    (df2013["TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES"] >= 0) &
    (df2013["HIV DIAGNOSES PER 100,000 POPULATION"] > 0)
]

grouped = df2013.groupby("Neighborhood (U.H.F)").agg({
    "HIV DIAGNOSES PER 100,000 POPULATION": "mean",
    "TOTAL NUMBER OF HIV DIAGNOSES": "sum",
    "TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES": "sum"
}).reset_index()

grouped["probabilityOfHIV"] = grouped["HIV DIAGNOSES PER 100,000 POPULATION"] / 100000
grouped["probabilityOfHIVtoAIDS"] = grouped["TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES"] / grouped["TOTAL NUMBER OF HIV DIAGNOSES"]

result = grouped[[
    "Neighborhood (U.H.F)",
    "probabilityOfHIV",
    "probabilityOfHIVtoAIDS"
]]

result.to_csv("hiv_probabilities_2013.csv", index=False)
