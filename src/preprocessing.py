import pandas as pd

def load_and_clean_data(file_path):
    print("Mengunduh dan memeriksa dataset saham BBRI...")
    df = pd.read_csv(file_path)
    # Lakukan pembersihan data di sini
    return df

if __name__ == "__main__":
    # Mengarah ke data lokal dari kaggle
    data_path = "data/BBRI.csv"
    df = load_and_clean_data(data_path)