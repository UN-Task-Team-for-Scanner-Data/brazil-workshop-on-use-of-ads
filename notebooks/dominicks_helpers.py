import pandas as pd

def download_category(category_name):
    """
    Basic function to download raw UPC and movement data for a given category
    """
    url = "https://www.chicagobooth.edu/research/kilts/research-data/-/media/enterprise/centers/kilts/datasets/dominicks-dataset/"
    product_url = f"{url}upc_csv-files/upc{category_name}.csv"
    upc_url = f"{url}movement_csv-files/w{category_name}.zip"

    # Get upc data
    df = pd.read_csv(product_url, encoding='latin1')
    df.to_parquet(f"../data/raw/{category_name}_products.parquet", index=False)

    # Get movement data
    df = pd.read_csv(upc_url, encoding='latin1', compression='zip')
    df = df.drop(columns=['PRICE_HEX', 'PROFIT_HEX'])
    df.to_parquet(f"../data/raw/{category_name}_movement.parquet", index=False)
    
    print("Done! Raw data for {category_name} has been downloaded and saved to /data/raw/ as parquet files.")

def download_weeks_and_stores():
    """
    Placeholder function to download data for weeks and stores.
    In a real implementation, this would contain logic to access the relevant data source.
    """
    weeks_url = "https://raw.githubusercontent.com/eurostat/dff/master/CSV/weeks.csv"
    stores_url = "https://raw.githubusercontent.com/eurostat/dff/master/CSV/stores.csv"

    df = pd.read_csv(stores_url)
    df = pd.read_csv(stores_url, header=None, names=['STORE','CITY','PRICE_TIER','ZONE','ZIP_CODE','ADDRESS'])
    df.to_parquet(f"../data/raw/stores.parquet", index=False)

    # TO DO - do weeks


def join_data(list_categories):
    """
    Placeholder function to join the data for the given categories.
    """
    pass

if __name__ == "__main__":
    # Example of reading in a CSV file with pandas
    download_category("beverages")
