from bs4 import BeautifulSoup
import requests

# parser l'html


response = requests.get("https://fr.wikipedia.org/wiki/Mammif%C3%A8re")

html = """
<!DOCTYPE html>
<html>
<head>
	<title>Page Title</title>
</head>
<body>
	<ul>
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
		<img/>
	</ul>
	<h1>This is a Heading</h1>
	<h1>This is a paragraph.</h1>
	<h1>This is another paragraph.</h1>
	<a href="https://www.google.com">This is a link</a>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")


# Recuperer la premiere balise h1
h1 = soup.h1
print(h1)


# Recuperer la premiere balise h1

h1 = soup.find("h1")
print(h1)

# Recuperer toutes les balises h1

h1 = soup.find_all("h1")
print(h1)


