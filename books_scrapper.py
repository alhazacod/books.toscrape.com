import requests # Para conectarnos a la pagina y descargar el html
from bs4 import BeautifulSoup # Para manejar el html

def print_books(books): # Imprimir una lista de libros
    print('-------------------------------')
    for index,book in enumerate(books,1):
        title = book['title']
        price = book['price']
        print(f'{index}. Titulo: {title},  Precio: {price}')
        print('-------------------------------')

def get_books_from_page(response):
    html_content = response.text # Descargamos el codigo html de la pagina
    soup = BeautifulSoup(html_content, 'html.parser') # 'html.parser' es el analizador que se utilizará para interpretar el contenido html

    # En esta pagina los libros están expuestos utilizando <article> y ademas tienen la clase 'product_pod'
    books = soup.find_all('article', class_='product_pod')

    books_list = []
    
    # Verificamos si hay libros en la pagina
    if not books:
        return False

    # Imprimimos todos los libros
    for book in books:
        title = book.h3.a.attrs['title'] # Obtenemos el atributo 'title' de h3>a
        price = book.find('p', class_='price_color').text # encontramos la el <p> que tenga la clase 'price_color' y lo convertimos a texto
        books_list.append({'title': title, 'price': price})
        # El siguiente es un ejemplo del codigo html de un libro:
        #<article class="product_pod">
        # <div class="image_container">
        #   <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
        # </div>
        # <p class="star-rating Three">
        #   <i class="icon-star"></i>
        #   <i class="icon-star"></i>
        #   <i class="icon-star"></i>
        #   <i class="icon-star"></i>
        #   <i class="icon-star"></i>
        # </p>
        # <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
        # <div class="product_price">
        #   <p class="price_color">£51.77</p>
        #   <p class="instock availability">
        #   <i class="icon-ok"></i>
        #   In stock
        #   </p>
        #   <form>
        #     <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
        #   </form>
        # </div>
        #</article>       
    return books_list

# base_url debe tener la siguiente forma: 'http://books.toscrape.com/catalogue/page-{}.html' con el espacio el formato
def get_books_from_all_pages(base_url,start_page = 1,end_page = 1111111111111, step = 1): 
    books = []
    for page_number in range(start_page,end_page+1,step):
        url = base_url.format(page_number) # Damos formato a la url con el numero de la pagina
        response = requests.get(url) # Cargamos la pagina

        if response.status_code == 200: # Si la conexion fue valida
            new_books = get_books_from_page(response) # Obtenemos los libros que hay en la pagina
            if new_books != False: # Si hay libros los agregamos
                books.extend(new_books) # Agregamos los libros de la pagina a la lista total de libros
            else: # Si no hay libros salimos del bucle
                break
        else:
            print(f'Connection error at page {page_number}: {response.status_code}')
            break
        print(f'Page {page_number} done!', end = "\r")
    print(f'Scrapping done!')
    return books
