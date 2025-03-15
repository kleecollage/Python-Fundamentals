import bs4, requests

# result = requests.get("https://escueladirecta-blog.blogspot.com/")
# print(type(result))
# print(result.text)

# soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
# print(len(soup.select('a')))
# print(soup.select('title')[0].get_text())

# special_title = soup.select('h3')[3].get_text()
# print(special_title)

# posts = soup.select('.post .post-title .snippet-container')
# for post in posts:
#     print(post.get_text())



result = requests.get("https://www.escueladirecta.com/l/products")
soup = bs4.BeautifulSoup(result.text, "lxml")
images = soup.select('.object-cover')[0]['src']
print(images)
# for i in images:
#     print(i)
images_product_1 = requests.get(images)
# print(images_product_1.content)
file = open('my_image.jgp', 'wb')
file.write(images_product_1.content)
file.close()










