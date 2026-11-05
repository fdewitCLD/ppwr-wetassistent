import json,re
from pathlib import Path
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ROOT=Path(__file__).parent
st.set_page_config(page_title='PPWR | Wettekstassistent',page_icon='📘',layout='centered')

@st.cache_resource(show_spinner=False)
def load_index():
    passages=json.loads((ROOT/'passages.json').read_text(encoding='utf-8'))
    texts=[x['text'] for x in passages]
    word=TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True,strip_accents='unicode',max_features=120000)
    char=TfidfVectorizer(analyzer='char_wb',ngram_range=(3,5),sublinear_tf=True,max_features=160000)
    return passages,word,char,word.fit_transform(texts),char.fit_transform(texts)

passages,word,char,W,C=load_index()
st.title('📘 PPWR-wetassistent')
st.caption('O&O • Alleen de aangeleverde Verordening (EU) 2025/40 • Geen AI-verzonnen antwoorden')
st.info('Deze assistent zoekt **letterlijke passages** uit de wettekst. Een gevonden passage is niet automatisch het volledige juridische antwoord. Controleer ook de uitzonderingen en de rest van het artikel.')
question=st.text_input('Wat wil je weten over de PPWR?',placeholder='Bijvoorbeeld: Welke regels gelden voor composteerbare verpakkingen?')
with st.expander('Voorbeelden van vragen'):
    st.write('Wat staat er over recyclebaarheid vanaf 2030?')
    st.write('Welke eisen zijn er voor verpakkingen die in contact komen met levensmiddelen?')
    st.write('Wat staat er over composteerbare verpakkingen?')

if question.strip():
    if len(question)>400:
        st.warning('Stel een kortere vraag (maximaal 400 tekens).')
    else:
        qw=word.transform([question]);qc=char.transform([question])
        scores=0.65*linear_kernel(qw,W).ravel()+0.35*linear_kernel(qc,C).ravel()
        order=scores.argsort()[::-1]
        # Diversity: avoid showing multiple nearly identical chunks on the same page.
        chosen=[]; pagecounts={}
        for i in order:
            p=passages[int(i)]['page']
            if pagecounts.get(p,0)>=2:continue
            if scores[i]<0.035:break
            chosen.append(int(i));pagecounts[p]=pagecounts.get(p,0)+1
            if len(chosen)==6:break
        st.subheader('Gevonden passages')
        if not chosen:
            st.warning('Ik kan geen voldoende passende passage vinden in deze wettekst. Probeer een concretere vraag of zoekterm. Ik geef daarom geen inhoudelijk antwoord.')
        else:
            st.caption('Gesorteerd op tekstuele overeenkomst met je vraag; niet op juridische relevantie of volledigheid.')
            for n,i in enumerate(chosen,1):
                p=passages[i]
                with st.container(border=True):
                    st.markdown(f'**{n}. {p["section"]} — pagina {p["page"]} van 124**')
                    st.write(p['text'])
            st.warning('Let op: deze passages kunnen onvolledig zijn. Lees bij twijfel het volledige artikel in de PDF. De sectie-aanduiding is automatisch herkend; controleer deze in het origineel.')

with st.expander('Bekijk de volledige oorspronkelijke wettekst'):
    st.download_button('Download PPWR (PDF)',(ROOT/'ppwr.pdf').read_bytes(),file_name='PPWR_Verordening_EU_2025_40_NL.pdf',mime='application/pdf')
st.divider()
st.caption('Bron: geüploade Nederlandse PPWR, Verordening (EU) 2025/40, Publicatieblad 22 januari 2025. Geen internetzoekfunctie, geen externe kennisbronnen en geen generatieve AI. De vragen worden in deze applicatie niet opgeslagen.')
