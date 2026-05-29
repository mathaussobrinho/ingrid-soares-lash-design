# Ingrid Soares Lash Design — Landing Page

Landing page estática (HTML + CSS + JavaScript puro), elegante e responsiva, para a Ingrid Soares Lash Design. Sem dependências e sem build: é só abrir o `index.html`.

## Estrutura

```
Ingrid/
├── index.html        # Conteúdo e seções da página
├── styles.css        # Tema, cores e layout responsivo
├── script.js         # Menu mobile, scroll e animações
├── assets/           # Imagens (foto da Ingrid, etc.)
└── README.md
```

## Como visualizar

- Forma rápida: dê dois cliques em `index.html` para abrir no navegador.
- Recomendado (servidor local), para o mapa e fontes carregarem perfeitamente:

```bash
# Com Python instalado
python -m http.server 8000
# Depois acesse http://localhost:8000
```

## Como editar o essencial

- **Foto da Ingrid**: veja as instruções em `assets/LEIA-ME.txt`. Resumo: salve a foto como `assets/ingrid.jpg` e troque o bloco `.photo-placeholder` por `<img src="assets/ingrid.jpg" alt="Ingrid Soares" />` na seção "Sobre".
- **Textos**: tudo fica em `index.html`, organizado por seção (Hero, Sobre, Serviços, Diferenciais, Localização, CTA, Footer).
- **WhatsApp**: o número está nos links `https://wa.me/5531983596974`. Para trocar, use Localizar/Substituir por todo o `index.html`.
- **Instagram**: `https://www.instagram.com/ingridsoareslashdesign/`.
- **Cores**: ajuste as variáveis no topo do `styles.css` (`:root`): `--lilac`, `--purple`, `--pink`, `--gold`, etc.

## Paleta

| Cor        | Hex       |
|------------|-----------|
| Lilás      | `#C9A6E0` |
| Roxo       | `#7B5EA7` |
| Roxo fundo | `#4F3A6E` |
| Rosa bebê  | `#FBE4EC` |
| Dourado    | `#C9A24B` |

## Publicar (grátis)

Por ser um site estático, funciona em qualquer hospedagem de arquivos:

- **Netlify / Vercel**: arraste a pasta ou conecte o repositório.
- **GitHub Pages**: suba os arquivos no repositório e ative o Pages.

Basta garantir que `index.html`, `styles.css`, `script.js` e a pasta `assets/` estejam juntos.
