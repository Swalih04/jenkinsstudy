import pandas as pd
import requests

def main():
    # Create a simple DataFrame
    data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
    df = pd.DataFrame(data)
    print("DataFrame created:")
    print(df)

    # Make a simple GET request
    response = requests.get("https://httpbin.org/get")
    if response.status_code == 200:
        print("API call successful:", response.json()["url"])
        return 0  # success
    else:
        print("API call failed with status:", response.status_code)
        return 1  # failure

if __name__ == "__main__":
    exit(main())
