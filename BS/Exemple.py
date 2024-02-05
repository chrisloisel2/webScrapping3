from bs4 import BeautifulSoup
import requests

# parser l'html


response = requests.get("https://fr.wikipedia.org/wiki/CNN")

html = """
<!DOCTYPE html>
<html>
<head>
	<title>Page Title</title>
</head>
<body>
	<ul>
		<li>Item 1</li>
		<li class="yolo">Item 2</li>
		<li class="yolo">Item 3</li>
		<img/>
	</ul>
	<h1>This is a Heading</h1>
	<h1 class="yolo">This is a paragraph.</h1>
	<h1 id="yolo">This is another paragraph.</h1>
	<a href="https://www.google.com">This is a link</a>
</body>
</html>
"""

# soup = BeautifulSoup(response.content, "html.parser")
soup = BeautifulSoup(html, "html.parser")


# Recuperer la premiere balise h1
a = soup.find("a")
print(a)


# Recuperer la premiere balise h1

h1 = soup.find("h1")
print(h1)

# Recuperer toutes les balises h1

h1 = soup.find_all("h1")
print(h1)


# Recuperer une balise avec sa classe

print("-------------------------------\n")
# div = soup.find("nav", attrs={
#     "class": "vector-toc-landmark",
#     "role": "navigation",
#     "aria-label" : "Sommaire"
#     })
# print(div)



# Recuperer une balise avec sa classe

# classYolo = soup.find(attrs={"class": "yolo"})

classYolo = soup.find_all( class_="yolo")
print(classYolo)


# Recuperer une balise avec son id

# idYolo = soup.find(attrs={"id": "yolo"})
# print(idYolo)

idYolo = soup.find_all( id="yolo")
print(idYolo)
