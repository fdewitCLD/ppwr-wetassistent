import json,re,fitz
from pathlib import Path
root=Path(__file__).parent
pdf=root/'ppwr.pdf'
doc=fitz.open(pdf)
chunks=[]; current='Overwegingen / inleiding'
for pi,page in enumerate(doc):
    raw=page.get_text(sort=True)
    raw=re.sub(r'(?m)^\s*(?:NL\s+PB L van 22\.1\.2025|PB L van 22\.1\.2025\s+NL|\d+/124\s+.*|ELI:.*|Publicatieblad.*|van de Europese Unie.*)\s*$','',raw)
    raw=re.sub(r'(?m)^\s*\f?\s*$','\n',raw)
    lines=[re.sub(r'\s+',' ',l).strip() for l in raw.splitlines()]
    lines=[l for l in lines if l and not re.fullmatch(r'\d+/124|\d{1,3}',l)]
    # Heading labels occur alone; keep most recent heading for citations, but page may span headings.
    buf=[]; size=0
    def flush():
        global chunks
        if buf:
            t=' '.join(buf).strip()
            if len(t)>55: chunks.append({'page':pi+1,'section':current,'text':t})
    for line in lines:
        m=re.fullmatch(r'Artikel\s+(\d+[a-z]?)',line,re.I)
        b=re.fullmatch(r'BIJLAGE\s+([IVX]+)',line,re.I)
        if m or b:
            flush();buf=[];size=0
            current=('Artikel '+m.group(1)) if m else ('Bijlage '+b.group(1))
            continue
        if size+len(line)>900 and buf:
            flush();buf=buf[-2:];size=sum(map(len,buf))
        buf.append(line);size+=len(line)
    flush()
(root/'passages.json').write_text(json.dumps(chunks,ensure_ascii=False,indent=0),encoding='utf-8')
print(len(chunks),'passages',len(doc),'pages')
