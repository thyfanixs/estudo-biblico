"""Gera dados/estudos.json a partir dos PDFs em estudos/<livro>/.

Regras:
- A pasta diz o livro: estudos/genesis, estudos/exodo, estudos/1-samuel, estudos/joao, estudos/jo (Jó)...
- O nome do arquivo termina com o capítulo ou o intervalo: gn-37.pdf, gn-37-38.pdf, 37.pdf.
- Com --comprimir, PDFs acima de 5 MB passam pelo Ghostscript (se ele estiver instalado).
"""
import json, os, re, shutil, subprocess, sys, unicodedata

LIVROS = ["Gênesis","Êxodo","Levítico","Números","Deuteronômio","Josué","Juízes","Rute","1 Samuel","2 Samuel","1 Reis","2 Reis",
  "1 Crônicas","2 Crônicas","Esdras","Neemias","Ester","Jó","Salmos","Provérbios","Eclesiastes","Cânticos","Isaías","Jeremias",
  "Lamentações","Ezequiel","Daniel","Oseias","Joel","Amós","Obadias","Jonas","Miqueias","Naum","Habacuque","Sofonias","Ageu",
  "Zacarias","Malaquias","Mateus","Marcos","Lucas","João","Atos","Romanos","1 Coríntios","2 Coríntios","Gálatas","Efésios",
  "Filipenses","Colossenses","1 Tessalonicenses","2 Tessalonicenses","1 Timóteo","2 Timóteo","Tito","Filemom","Hebreus","Tiago",
  "1 Pedro","2 Pedro","1 João","2 João","3 João","Judas","Apocalipse"]

def slug(nome):
    s = unicodedata.normalize("NFD", nome)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

POR_PASTA = {slug(n): n for n in LIVROS}
POR_PASTA.update({"canticos-dos-canticos": "Cânticos", "cantares": "Cânticos", "oseias": "Oseias", "miqueias": "Miqueias"})
CAP = re.compile(r"(\d+)(?:\s*-\s*(\d+))?\.pdf$", re.I)

def comprimir(caminho):
    gs = shutil.which("gs")
    if not gs or os.path.getsize(caminho) < 5 * 1024 * 1024:
        return
    tmp = caminho + ".tmp.pdf"
    subprocess.run([gs, "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.5", "-dPDFSETTINGS=/ebook",
                    "-dNOPAUSE", "-dBATCH", "-dQUIET", f"-sOutputFile={tmp}", caminho], check=True)
    if os.path.getsize(tmp) < os.path.getsize(caminho) * 0.9:
        os.replace(tmp, caminho)
        print("comprimido:", caminho)
    else:
        os.remove(tmp)

def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base = os.path.join(raiz, "estudos")
    estudos, avisos = [], []
    for pasta in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        livro = POR_PASTA.get(pasta)
        dirpath = os.path.join(base, pasta)
        if not os.path.isdir(dirpath):
            continue
        if not livro:
            avisos.append(f"pasta sem livro conhecido: estudos/{pasta}")
            continue
        for nome in os.listdir(dirpath):
            m = CAP.search(nome)
            if not nome.lower().endswith(".pdf"):
                continue
            if not m:
                avisos.append(f"não achei o capítulo no nome: estudos/{pasta}/{nome}")
                continue
            if "--comprimir" in sys.argv:
                comprimir(os.path.join(dirpath, nome))
            de, ate = int(m.group(1)), int(m.group(2) or m.group(1))
            estudos.append({"livro": livro, "de": min(de, ate), "ate": max(de, ate), "arquivo": f"estudos/{pasta}/{nome}"})
    estudos.sort(key=lambda e: (LIVROS.index(e["livro"]), e["de"], e["ate"]))
    with open(os.path.join(raiz, "dados", "estudos.json"), "w", encoding="utf-8") as f:
        json.dump({"estudos": estudos}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(len(estudos), "estudos")
    for a in avisos:
        print("aviso:", a)

if __name__ == "__main__":
    main()
