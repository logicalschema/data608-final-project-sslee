import pandas as pd


df = pd.read_csv("combined_final.csv",
                   dtype={"zip": str, "percentage": float,
                          "tobacco": int, "alcohol": int,
                          "B02001_001E": int, "B02008_001E": int,
                          "B02009_001E": int, "B02010_001E": int,
                          "B02011_001E": int, "B02012_001E": int,
                          "B02013_001E": int, "B03001_002E": int,
                          "B03001_003E": int
                })


column = df["percentage"]




tobaccoLabels = ['A', 'B', "C"]
df['tobacco_classification'] = pd.qcut(df['tobacco'], 3, labels = tobaccoLabels)

alcoholLabels = ['1', '2', '3']
df['alcohol_classification'] = pd.qcut(df['alcohol'], 3, labels = alcoholLabels)

df['class'] = df['tobacco_classification'].astype(str) + df['alcohol_classification'].astype(str)

# Classes and color
# A3: #be64ac B3: #8c62aa	C3: #3b4994
# A2: #dfb0d6 B2: #a5add3	C2: #5698b9
# A1: #e8e8e8	B1: #ace4e4	C1: #5ac8c8

'''


print(df)