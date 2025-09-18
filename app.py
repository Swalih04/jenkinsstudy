import requests
import pandas as pd
import numpy as np

def main():
    print("✅ Python Application Running...")

    # Use requests
    response = requests.get("https://httpbin.org/get")
    print("Response Status:", response.status_code)

    # Use numpy
    arr = np.array([1, 2, 3, 4, 5])
    print("Numpy Array Sum:", np.sum(arr))

    # Use pandas
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
    print("Pandas DataFrame:\n", df)

    if response.status_code == 200:
        exit(0)   # success → Jenkins interprets as success
    else:
        exit(1)   # failure → Jenkins interprets as failure

if __name__ == "__main__":
    main()
