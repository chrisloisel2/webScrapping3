from bs4 import BeautifulSoup


html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple de Page Web sur la Bourse</title>
    <style>
        body { font-family: Arial, sans-serif; }
        header { background-color: #4CAF50; color: white; padding: 10px; text-align: center; }
        nav { float: left; width: 200px; background: #ccc; padding: 20px; }
        nav ul { list-style-type: none; padding: 0; }
        article { float: left; padding: 20px; width: 70%; }
        section:after { content: ""; display: table; clear: both; }
        footer { background-color: #777; color: white; text-align: center; padding: 10px; position: relative; bottom: 0; width: 100%; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
    </style>
</head>
<body>

<header>
    <h1>Bienvenue sur Mon Site Web de Bourse</h1>
</header>

<nav>
    <ul>
        <li><a href="#section1">Marchés Financiers</a></li>
        <li><a href="#section2">Actualités Boursières</a></li>
        <li><a href="#section3">Analyses et Conseils</a></li>
    </ul>
</nav>

<section>
    <article id="section1">
        <h2>Marchés Financiers</h2>
        <p>Ceci est le contenu de la première section. Elle contient un tableau avec des données boursières factices.</p>
        <table>
            <tr>
                <th>Entreprise</th>
                <th>Prix de l'Action</th>
                <th>Variation</th>
            </tr>
            <tr>
                <td>Entreprise A</td>
                <td>50 €</td>
                <td>+1.5%</td>
            </tr>
            <tr>
                <td>Entreprise B</td>
                <td>35 €</td>
                <td>-0.8%</td>
            </tr>
            <tr>
                <td>Entreprise C</td>
                <td>42 €</td>
                <td>+2.3%</td>
            </tr>
        </table>
    </article>

    <article id="section2">
        <h2>Actualités Boursières</h2>
        <p>Cette section contient une liste de liens vers des actualités fictives sur la bourse :</p>
        <ul>
            <li><a href="#">L'impact de la politique économique sur les marchés</a></li>
            <li><a href="#">Les dernières tendances des techs en bourse</a></li>
            <li><a href="#">Analyse trimestrielle du marché boursier</a></li>
        </ul>
    </article>

    <article id="section3">
        <h2>Analyses et Conseils</h2>
        <p>Dans cette section, des experts partagent leurs analyses et conseils sur les stratégies d'investissement :</p>
        <p>Contenu d'analyse et de conseil à venir...</p>
    </article>
</section>

<footer>
    <p>Ceci est le pied de page. © 2024 MonSiteWeb sur la Bourse</p>
</footer>

</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

titre = soup.title.text
print(f"Titre de la page : {titre}")

table = soup.find('table')

rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    if cols:
        data.append({
            'colonne1': cols[0].text.strip(),
            'colonne2': cols[1].text.strip(),
            'colonne2': cols[2].text.strip(),
        })

print(data)

articles = soup.find_all('article')
for article in articles:
    titre_section = article.find('h2').text
    premier_paragraphe = article.find('p').text
    print(f"Titre de la section : {titre_section}")
    print(f"Premier paragraphe : {premier_paragraphe}")


liens = soup.find('article', {'id': 'section2'}).find_all('a')

for lien in liens:
    texte = lien.text
    url = lien['href']
    print(f"Texte : {texte}, URL : {url}")

paragraphes = soup.select('article > p')
for p in paragraphes:
    print(p.text)

