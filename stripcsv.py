import pandas as pd

hvi = pd.read_csv("HVI_rankings.csv")
modzcta = pd.read_csv("MODZCTA.csv")
zipcodes = pd.read_csv("NYC_zipcodes.csv")

hvi["ZIP Code Tabulation Area (ZCTA) 2020"] = hvi["ZIP Code Tabulation Area (ZCTA) 2020"].astype(str)
modzcta["ZCTA"] = modzcta["ZCTA"].astype(str)
modzcta["MODZCTA"] = modzcta["MODZCTA"].astype(str)
zipcodes["ZIP Codes"] = zipcodes["ZIP Codes"].astype(str)

merged = hvi.merge(modzcta, left_on="ZIP Code Tabulation Area (ZCTA) 2020", right_on="ZCTA", how="left")
merged = merged.merge(zipcodes, left_on="MODZCTA", right_on="ZIP Codes", how="left")
'''
merged["HVI_normalized"] = (
    (merged["Heat Vulnerability Index (HVI)"] - merged["Heat Vulnerability Index (HVI)"].min())
    / (merged["Heat Vulnerability Index (HVI)"].max() - merged["Heat Vulnerability Index (HVI)"].min())
)
'''
output = merged[["Neighborhood", "Heat Vulnerability Index (HVI)"]].dropna().drop_duplicates()
output.columns = ["neighborhood", "hvi"]

output.to_csv("neighborhood_hvi_probabilities.csv", index=False)
