# PPWR-wetassistent — voor O&O-leerlingen

Dit is een brongebonden **zoekassistent** voor de Nederlandstalige Verordening (EU) 2025/40 (PPWR). Hij geeft uitsluitend **letterlijke passages** uit de aangeleverde PDF terug. Hij genereert geen eigen antwoorden. Dit is bewust: daardoor kan hij geen juridische informatie uit andere bronnen toevoegen.

## Online zetten — zo weinig mogelijk stappen

1. Maak een account op https://github.com (of gebruik je bestaande account). Maak een **nieuwe repository**, bijvoorbeeld `ppwr-wetassistent`. Kies **Public** voor de eenvoudigste gratis publicatieroute. Bedenk: de code en PDF zijn dan publiek zichtbaar.
2. Upload **alle bestanden uit deze map** naar de hoofdmap van de repository: `app.py`, `passages.json`, `ppwr.pdf`, `requirements.txt` en eventueel `build_index.py` en `README.md`. Gebruik in GitHub `Add file` > `Upload files` > `Commit changes`.
3. Ga naar https://share.streamlit.io, meld je aan via GitHub en kies `Create app` / `Deploy an app`.
4. Selecteer je repository en branch `main`, en geef als hoofdscript `app.py` op. Klik op **Deploy**.
5. Open de gegenereerde website, test de vragen hieronder en deel de URL via Google Classroom.

Streamlit Community Cloud is een dienst van een externe partij. De precieze menu's, limieten en voorwaarden kunnen wijzigen. Als GitHub of Streamlit op school geblokkeerd is, overleg met ICT over een andere hostingomgeving.

## Testvragen

- Welke eisen stelt de PPWR aan recyclebaarheid vanaf 2030?
- Wat staat er over composteerbare verpakkingen?
- Wat staat er over PFAS in voedselverpakkingen?
- Wie won het WK voetbal in 2010? (moet geen voetbalantwoord geven)

## Belangrijke beperkingen

- **Geen AI-chat:** dit is een zoekassistent die relevante wettekst toont. Dat is de meest robuuste manier om uitsluitend broninformatie te laten zien zonder externe feiten te verzinnen.
- De zoekfunctie gebruikt tekstovereenkomst. Een passage kan relevant lijken maar toch niet het juiste of volledige juridische antwoord geven. Leerlingen moeten uitzonderingen en andere leden controleren.
- Automatische artikelherkenning kan onjuist zijn bij doorlopende pagina's. Het paginanummer is afkomstig uit de originele PDF; controleer artikel en lid in de PDF.
- Dit is de geüploade tekst uit januari 2025. Latere wijzigingen, uitvoeringshandelingen en andere wetgeving worden **niet** automatisch verwerkt.
- Geen accounts of chatgeschiedenis. De applicatie bewaart de vragen niet zelf. Hostingproviders kunnen wel technische logs verwerken. Vermijd leerlingnamen en persoonsgegevens in vragen; bespreek externe hosting met de school.
- De PDF wordt openbaar aangeboden bij een publieke repository en als download in de app. Het gaat om een publiek EU-document.

## Lokaal draaien (optioneel)

Installeer Python en voer uit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Bij een nieuwe PDF

Vervang `ppwr.pdf`, voer `python build_index.py` uit en upload de nieuwe `passages.json` en PDF. Controleer dan opnieuw de paginering en de sectieherkenning.
