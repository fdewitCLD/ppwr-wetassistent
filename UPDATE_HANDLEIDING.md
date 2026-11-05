# Update naar PPWR-vraag-en-antwoordassistent

Deze versie beantwoordt concrete vragen in begrijpelijke taal en toont de oorspronkelijke gevonden passages. De enige kennisbron voor juridische inhoud is de meegeleverde PPWR-PDF. Let op: een taalmodel kan de wet verkeerd interpreteren. De code controleert of aangehaalde bron-ID's bestaan, maar kan niet volledig bewijzen dat elke zin door de bron wordt ondersteund.

## Bestaande Streamlit-app bijwerken
1. Pak de ZIP uit.
2. Open je GitHub-repository. Kies **Add file → Upload files**.
3. Upload **app.py** en **requirements.txt** uit deze ZIP en bevestig **Commit changes**. De bestaande bestanden `passages.json` en `ppwr.pdf` hoeven niet opnieuw te worden geüpload.
4. Open de bestaande app in Streamlit Community Cloud. Ga naar **Manage app → Settings → Secrets**.
5. Voeg de volgende regel toe, met je eigen API-sleutel tussen de aanhalingstekens:
   OPENAI_API_KEY = "sk-..."
6. Sla de secrets op. De app start meestal vanzelf opnieuw; gebruik zo nodig **Reboot app**.

## API-sleutel
Je maakt de sleutel aan via https://platform.openai.com/api-keys . De OpenAI API heeft eigen gebruikskosten, los van een ChatGPT-abonnement. Controleer of gebruik door leerlingen past bij het beleid van je school en de privacyvoorwaarden. De sleutel mag NOOIT in GitHub, de app-code of Google Classroom worden geplaatst. Alleen in Streamlit Secrets.

## Testvragen
- Wat zegt de PPWR over composteerbare verpakkingen?
- Aan welke eisen moet een verpakking in 2030 voldoen om recyclebaar te zijn?
- Wat is volgens deze wet het goedkoopste verpakkingsmateriaal? (Moet aangeven dat dit niet uit de wet kan worden vastgesteld.)

## Grenzen
De assistent doorzoekt geselecteerde tekstpassages; relevante uitzonderingen elders in de wet kunnen gemist worden. De bron-ID's worden technisch gevalideerd, maar de inhoudelijke juistheid van de uitleg niet volledig. Controleer antwoorden voor klassikaal gebruik.
