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

Abra a área do organizador: o endereço do site com `#organizar` no fim (https://thyfanixs.github.io/estudo-biblico/#organizar). Ela não aparece para os visitantes. Lá, em **Adicionar o PDF de um estudo**, escolha o livro e o site mostra o nome certo do arquivo e o botão que abre a pasta do livro no GitHub. Só a sua conta do GitHub pode enviar arquivos. O caminho é este:

1. No Canva: **Compartilhar → Baixar → PDF padrão**, com **Compactar arquivo** marcado. Pelo navegador, o GitHub aceita até 25 MB.
2. Dê ao arquivo o nome do capítulo, como `gn-37.pdf`. Se o estudo cobrir mais de um capítulo, use o intervalo, como `gn-37-38.pdf`.
3. Envie o arquivo para a pasta do livro, como `estudos/genesis/` ou `estudos/exodo/` (no GitHub: **Add file → Upload files**).

Pronto. A automação em `.github/workflows/estudos.yml` comprime o PDF se ele passar de 5 MB, refaz `dados/estudos.json` e publica o site de novo. Leva uns três minutos.

O nome da pasta é o nome do livro sem acentos e com hífen: `genesis`, `exodo`, `1-samuel`, `joao`, `jo` (Jó), `apocalipse`. Para rodar a mesma atualização no computador: `python3 scripts/atualizar_estudos.py`.

## Bíblia online

Cada capítulo sem PDF abre o texto na [Bíblia Online](https://www.bibliaonline.com.br/acf), que é gratuita e não pede cadastro (Almeida Corrigida Fiel). Assim, quem não tem Bíblia pode acompanhar o estudo.

## Pinturas

`dados/pinturas.json` diz quais são as três imagens de cada livro. Os arquivos ficam em `img/livros/`. A galeria muda quando outro livro é escolhido em "Ver o livro".

## Ver no computador antes de publicar

O site lê os arquivos JSON, então não abre direto com dois cliques. Rode um servidor simples nesta pasta:

```bash
python3 -m http.server 8000
```

e abra http://localhost:8000.

## Créditos das imagens

Todas em domínio público, via Wikimedia Commons. O autor e o ano de cada obra aparecem na legenda da galeria e em `dados/pinturas.json`, junto com o link da página original no Commons.
