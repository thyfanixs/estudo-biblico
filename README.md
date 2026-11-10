# Até Apocalipse 22

Site do estudo bíblico de segunda-feira, às 19h40. Ele mostra:

- a contagem regressiva até o dia em que vamos ler **Apocalipse 22**;
- onde estamos agora, na linha do tempo de Gênesis 1 a Apocalipse 22;
- cada capítulo do livro atual, com o PDF do estudo daquele capítulo;
- os 66 livros da Bíblia, com o que já foi concluído.

É um site estático (HTML, JSON e PDFs), sem servidor nem banco de dados. Funciona no GitHub Pages.

## Estrutura

```
index.html              o site inteiro
dados/progresso.json    onde estamos (livro, capítulo, horário, ritmo)
dados/estudos.json      lista dos PDFs e dos capítulos que cada um cobre
estudos/genesis/*.pdf   as apresentações de cada estudo
img/                    gravuras e pinturas (domínio público)
```

## Publicar no GitHub Pages

1. Crie um repositório no GitHub e envie esta pasta.
2. No repositório, vá em **Settings → Pages**.
3. Em **Source**, escolha **Deploy from a branch**, a branch `main` e a pasta `/ (root)`.
4. Em um ou dois minutos o site fica no ar em `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`.

## Toda segunda, depois do estudo

Edite `dados/progresso.json` (dá para fazer direto pelo site do GitHub, no ícone de lápis) e mude o capítulo:

```json
{
  "livro": "Gênesis",
  "capitulo": 37,
  "capitulosPorEstudo": 1,
  "horario": "19:40",
  "segundasDePausaPorAno": 0,
  "livrosConcluidos": []
}
```

- `capitulo` é o **próximo** capítulo a estudar.
- Quando terminar um livro, mude `livro` para o seguinte (ex.: `"Êxodo"`), volte `capitulo` para `1` e acrescente o livro terminado em `livrosConcluidos` (ex.: `["Gênesis"]`).
- `segundasDePausaPorAno` conta feriados e férias sem estudo. Ela empurra a data final.

Também dá para usar a **área do organizador**. Abra o site com `#organizar` no fim do endereço, toque em "Concluímos este estudo" e depois em "Baixar progresso.json". Por fim, envie esse arquivo para `dados/progresso.json` no GitHub.

## Adicionar o PDF de um novo estudo

1. Exporte a apresentação do Canva em PDF.
2. Salve em `estudos/<livro>/`, por exemplo `estudos/genesis/gn-37.pdf`.
3. Acrescente uma linha em `dados/estudos.json`:

```json
{ "livro": "Gênesis", "de": 37, "ate": 37, "arquivo": "estudos/genesis/gn-37.pdf" }
```

Se o estudo cobrir mais de um capítulo, use `de` e `ate` (ex.: `"de": 37, "ate": 38`).

Dica: o GitHub não aceita arquivos acima de 100 MB. Os PDFs que saem do Canva costumam ser grandes. Os daqui foram comprimidos e ficaram entre 1 e 7 MB cada.

## Ver no computador antes de publicar

O site lê os arquivos JSON, então não abre direto com dois cliques. Rode um servidor simples nesta pasta:

```bash
python3 -m http.server 8000
```

e abra http://localhost:8000.

## Créditos das imagens

Todas em domínio público, via Wikimedia Commons:

- *A Criação da Luz*, *O Dilúvio*, *Jacó luta com o anjo* e *A Nova Jerusalém*: Gustave Doré, ilustrações da Bíblia (1866).
- *O Sacrifício de Isaque*: Rembrandt (1635), Museu Hermitage.
