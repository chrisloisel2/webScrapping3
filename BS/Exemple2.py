from bs4 import BeautifulSoup
import requests

# URL of the webpage you want to scrape

html = """
<div class="table">
<apple for="Alexei" />
<bento for="Albina">
<apple />
</bento>
<bento for="Vitaly">
bonjour je suis le bento
<orange />
</bento>
<pickle />
</div>
"""

# Send a GET request to the URL

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(html, "html.parser")

apple = soup.select("bento[for='Vitaly']")[0].text
print(apple)
