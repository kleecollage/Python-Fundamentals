import requests, bs4

# URL WITHOUT PAGE NUMBER
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# ITERATE OVER PAGES
# for i in range(1, 11):
#     print(base_url.format(i))

# SEARCHING FOR THE DATA WE WANT
# req = requests.get(base_url.format('1'))
# soup = bs4.BeautifulSoup(req.text, "lxml")
# books = soup.select('.product_pod') --> IN HERE!
# # GET STARS
# book_stars = books[0].select('.star-rating.Three')  --> GOT IT!
# print(book_stars)
# # GET TITLE
# book_title = books[0].select('a')[1]['title']  --> GOT IT!
# print(book_title)


# GLOBAL VARIABLES
high_rating_books = []

# ITERATE OVER PAGES
for page in range(1, 51):
    # CREATE SOUP FOREACH PAGE
    url_page = base_url.format(page)
    req = requests.get(url_page)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    # SELECT DATA FROM BOOKS
    books = soup.select(".product_pod")
    # ITERATE OVER BOOKS
    for book in books:
        # CHECK 4> STARS
        if len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five")) != 0:
            # SAVE TITLE
            book_title = book.select("a")[1]["title"]
            # ADD BOOK TO OUR LIST
            high_rating_books.append(book_title)

# RESULT IN CONSOLE
for i in high_rating_books:
    print(i)










