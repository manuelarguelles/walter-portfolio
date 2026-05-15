# Walter Castañeda · Portafolio interactivo (3 versiones)

Portafolio web interactivo construido a partir del PDF original de **Walter Alejandro Castañeda Torres** — Diseñador UI/UX en el Gobierno Regional de San Martín (Perú). Cada versión es un sitio estático autocontenido (HTML + CSS + JS vanilla, sin build step).

## 🚀 Versiones publicadas (Vercel)

| Versión | Concepto | Stack visual | URL en vivo |
|---------|---------|--------------|-------------|
| **A — Claude design puro** | Look editorial calmado tipo revista. Paleta crema-terracota, tipografía Fraunces italic, mucho whitespace. | Inter + Fraunces (opsz 144) | <https://walter-portfolio-a.vercel.app> |
| **B — Branding Walter refinado ★** | Mantiene el branding turquesa/azul del PDF original, con principios de Claude design (espaciado, tipografía, jerarquía). | Inter + Fraunces · paleta gov | <https://walter-portfolio-b.vercel.app> |
| **C — Showcase agresivo** | B + dark mode toggle, parallax en hero, tilt 3D en cards, marquee de skills, timeline scroll-driven, easter egg Konami. | B + animaciones avanzadas | <https://walter-portfolio-c.vercel.app> |

📦 **Repositorio**: <https://github.com/manuelarguelles/walter-portfolio>

> La versión **B** es la recomendada para uso principal: respeta el branding existente de Walter y comunica criterio (no reemplaza ciegamente la identidad). **A** es para audiencias que valoren estética editorial/Anthropic. **C** suma para entrevistas técnicas donde demostrar interacción premium.

## 📂 Estructura

```
walter-portfolio/
├── README.md           ← este archivo
├── assets/             ← PNGs originales (referencia, 15 páginas del PDF + crops)
├── version-a/
│   ├── index.html      ← single-file autocontenido
│   └── assets/         ← copia de assets para deploy independiente
├── version-b/
│   ├── index.html
│   └── assets/
└── version-c/
    ├── index.html
    └── assets/
```

## 🎯 Contenido del portafolio (común a las 3 versiones)

- **10 Prototipos** (Makinfo, Siscomtur, SIRID, Mesa de Partes web/móvil, GSCConvocatorias, GSCombustible, Visita San Martín, Presupuesto, GSTramite)
- **1 Case Study UI/UX** (Siscomtur — 6 fases: Discover → User flow → Wireframes → Prototype → Agile → Impact)
- **2 Diagramas de flujo BPMN** (BIM-GORESAM, TUPA)
- **6 Dashboards Power BI** (Infra, Finanzas, Educación, Salud, Tránsito, Mortalidad)
- **Galería**: imágenes, iconos, logos, manuales, videos
- **3 reconocimientos**: SERVIR (UX), DIRCETUR, Sello de Accesibilidad Digital AA

## ⚙️ Características técnicas

- Single-file HTML por versión (cero build, cero deps JS)
- Tipografía via Google Fonts (Inter + Fraunces)
- Filtros animados, lightbox con teclado, tabs, scroll reveal
- Mobile-first responsive (breakpoint ~880px)
- Accesibilidad: focus rings, alt text, aria-labels, `prefers-reduced-motion`
- Versión C: dark mode con `localStorage`, `prefers-color-scheme`

## 🛠 Stack & herramientas detectadas

Figma · Adobe CC (Photoshop, Illustrator, InDesign) · Power BI · Bizagi · HTML · SQL · Scrum

## 👤 Contacto Walter

- 💬 WhatsApp: **+51 921 363 347**
- ✉ Email: **waltercastanedat@gmail.com**
- 💼 LinkedIn: [Walter Castañeda Torres](https://www.linkedin.com/in/walter-casta%C3%B1eda-torres/)

## 📝 Desarrollo

Construido por **Manuel Argüelles** (con Claude Code) a partir del PDF original `Portafolio_sinVirus.pdf` entregado por Walter el 14 de mayo de 2026.

Para correr localmente:

```bash
cd version-b/   # o version-a / version-c
python3 -m http.server 8000
open http://localhost:8000
```

## 📄 Licencia

Contenido visual, textos, capturas y reconocimientos pertenecen a **Walter Alejandro Castañeda Torres** y al Gobierno Regional de San Martín. Código base del scaffolding HTML/CSS/JS: libre de uso para referencia.
