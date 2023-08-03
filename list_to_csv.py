import pandas as pd

def get_dataframe(books):
    df = pd.DataFrame(books)
    return df

def save_to_csv(books, path = 'books.csv', index = False):
    df = get_dataframe(books)
    df.to_csv(path, index = index)

def test():
    books = [{'book': 'No longer human', 'price':'50$'},{'book': 'Three body problem', 'price':'30$'}]
    try:
        save_to_csv(books)
    except Exception as e:
        raise e

if __name__ == "__main__":
    test()
