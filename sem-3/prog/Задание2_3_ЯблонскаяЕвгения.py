import pandas as pd

headings = ["Heading1", "Heading2", "Heading3"]
data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

df = pd.DataFrame(data, columns=headings)
print(df)