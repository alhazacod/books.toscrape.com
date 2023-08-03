from pandas import read_csv
from books_scrapper import get_books_from_all_pages, print_books
import sys
import argparse
from list_to_csv import save_to_csv

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Programa para obtener todos los libros de la pagina books.toscrape.com y guardarlos como un csv')

    # Argumentos
    parser.add_argument('start', nargs='?', default=1, help = 'Starting page. If no argument starting page is 1.')
    parser.add_argument('end', nargs='?', default=sys.maxsize-1, help = 'End page. If no argument it will end when there\'s no books or the page didn\'t load.')
    parser.add_argument('step', nargs='?', default=1,help = 'Step in pages. If no argument step is 1')
    
    # Opciones
    parser.add_argument('-p', '--print_books', action='store_true', help = 'Imprimir todos los libros con sus precios.')

    args = parser.parse_args()
    books = get_books_from_all_pages('http://books.toscrape.com/catalogue/page-{}.html',start_page=int(args.start),end_page=int(args.end),step=int(args.step))
    save_to_csv(books)

    print('Data have been saved in books.csv')

    if args.print_books:
        print_books(books)

if __name__ == "__main__":
    main()
