<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=SEO%20Local&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Plugin%20para%20Claude%20Code&descAlignY=60&descSize=20" width="100%"/>

<br/>

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-orange?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-8%20comandos-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](https://github.com/soyalonsoai/seo-local)
[![Google Maps](https://img.shields.io/badge/Google%20Maps-Compatible-red?style=for-the-badge&logo=google-maps&logoColor=white)](https://github.com/soyalonsoai/seo-local)

<br/>

### 🔍 Convierte a Claude en tu **auditor senior de SEO Local**
### Auditorías profundas basadas en evidencia real — sin consejos genéricos, sin datos inventados.

<br/>

</div>

---

## ¿Qué hace este plugin?

Con un solo comando, Claude analiza tu negocio en Google, audita tu sitio web, estudia a tus competidores y genera un **roadmap completo en PDF** listo para entregar al cliente.

- ✅ Auditoría de Google Business Profile
- ✅ Análisis de competidores en Google Maps
- ✅ On-page SEO + Schema Markup
- ✅ Test de rankability vs top 3
- ✅ Roadmap priorizado con plan 30/60/90 días
- ✅ Reporte profesional exportado en PDF

---

## Instalación

### Desde el marketplace de Soyalonso.ai

```bash
/plugin marketplace add https://github.com/soyalonsoai/seo-local
/plugin install seo-local@soyalonsoai
```

### Manual (plugin-dir)

```bash
git clone https://github.com/soyalonsoai/seo-local.git
claude --plugin-dir ./seo-local
```

---

## Comandos disponibles

| Comando | Descripción |
|---------|-------------|
| `/seo-local:seo-local-audit` | ⚡ **Full audit en un comando** — 4 sub-agentes en paralelo + roadmap en PDF |
| `/seo-local:seo-roadmap` | 📋 Consolida auditorías previas en roadmap + PDF |
| `/seo-local:seo-plan` | 🗺️ Guía de inicio — flujos recomendados según tu objetivo |
| `/seo-local:gbp-audit` | 🏢 Audita TU propia ficha de Google Business Profile |
| `/seo-local:gbm-audit` | 🗺️ Auditoría de competidores en Google Maps + ranking levers |
| `/seo-local:onpage-audit` | 📄 Auditoría on-page completa de una URL |
| `/seo-local:schema-audit` | 🏷️ Auditoría de structured data / schema markup |
| `/seo-local:rankability-test` | 📊 Test de rankability vs top 3 resultados orgánicos |

---

## Uso

### ⚡ `/seo-local:seo-local-audit` — Full SEO Local Audit *(recomendado)*

Ejecuta todos los audits en paralelo con **un solo comando** usando sub-agentes especializados, luego genera un roadmap consolidado en PDF listo para entregar al cliente.

**Input:** URL + keyword objetivo + link de Google Business Profile

**Output:**
- 4 sub-agentes corren en paralelo: on-page + schema, rankability, GBP propio, competidores
- Resumen ejecutivo con hallazgos de todas las auditorías
- Roadmap priorizado con matriz impacto/esfuerzo
- Plan de acción 30/60/90 días
- Reporte HTML + PDF profesional

---

### 📋 `/seo-local:seo-roadmap` — Roadmap consolidado

Toma los resultados de auditorías previas y los convierte en un plan de acción priorizado exportado como PDF.

**Input:** Resultados de una o más auditorías (gbp-audit, gbm-audit, onpage-audit, schema-audit, rankability-test)

**Output:**
- Tabla maestra de todos los hallazgos consolidados
- Matriz de priorización (4 cuadrantes: Quick Wins, Proyectos, Fill-ins, Reconsiderar)
- Plan de acción 30/60/90 días con tareas concretas y responsables
- Reporte HTML + PDF profesional listo para cliente

---

### 🗺️ `/seo-local:seo-plan` — Guía de inicio

Explica qué hace el plugin, todos los comandos disponibles y el proceso recomendado según tu objetivo.

**Input:** Ninguno requerido

**Output:**
- Tabla de comandos disponibles
- Flujo recomendado para rankear en Maps
- Flujo recomendado para rankear orgánicamente
- Flujo de auditoría completa

---

### 🏢 `/seo-local:gbp-audit` — Auditoría de tu propia ficha

Audita en profundidad TU propia ficha de Google Business Profile e identifica qué te está frenando en el ranking.

**Input:** Nombre del negocio + ciudad, o link directo al perfil en Google Maps

**Output:**
- Tabla completa de datos de la ficha (identidad, NAP, reseñas, completitud, fotos, actividad)
- Score de completitud / 100
- Top 3 fortalezas y top 3 problemas críticos
- Tabla de action items ordenados por impacto
- Recomendación del siguiente paso

---

### 🗺️ `/seo-local:gbm-audit` — Auditoría de competidores en Maps

Analiza los top 5 competidores orgánicos en Google Maps para una keyword y extrae los **7 ranking levers** que Google está premiando.

**Input:** Keyword (ej. "dentistas en monterrey")

**Output:**
- Lista de top 5 orgánicos
- Tabla de datos por competidor (reseñas, fotos, categorías, descripción, posts, etc.)
- Reconocimiento de patrones del top 3
- Tabla de ranking levers ordenados por impacto

---

### 📄 `/seo-local:onpage-audit` — Auditoría On-Page

Auditoría completa de 10 pasos para una URL con keyword objetivo.

**Input:** URL + keyword primaria

**Output:**
- Resumen de victorias y problemas
- Tabla de findings con estado y prioridad
- Tabla de action steps con recomendaciones exactas (incluye texto de reemplazo listo para copiar)

---

### 🏷️ `/seo-local:schema-audit` — Auditoría de Schema Markup

Evalúa el structured data de una página y genera los JSON-LD faltantes.

**Input:** URL + tipo de negocio + ciudad

**Output:**
- Tabla de schema existente con veredicto
- Tabla de schema faltante con prioridad
- Ejemplos JSON-LD listos para implementar (con placeholders)

---

### 📊 `/seo-local:rankability-test` — Test de Rankability

Compara una página vs los top 3 orgánicos para una keyword y da un veredicto directo.

**Input:** URL + keyword + ciudad

**Output:**
- Veredicto: Merece rankear más alto / Neutral / Merece rankear más bajo
- Una razón principal
- Una mejora específica
- Tabla de 5 action items

---

## Estructura del proyecto

```
seo-local/
├── .claude-plugin/
│   └── plugin.json              # Manifiesto del plugin
├── skills/
│   ├── seo-local-audit/
│   │   └── SKILL.md             # Master: lanza todos los audits + genera PDF
│   ├── seo-roadmap/
│   │   └── SKILL.md             # Consolida hallazgos en roadmap + PDF
│   ├── seo-plan/
│   │   └── SKILL.md             # Guía de inicio y flujos recomendados
│   ├── gbp-audit/
│   │   └── SKILL.md             # Auditoría de tu propia ficha GBP
│   ├── gbm-audit/
│   │   └── SKILL.md             # Auditoría de competidores en Maps
│   ├── onpage-audit/
│   │   └── SKILL.md             # Auditoría on-page
│   ├── schema-audit/
│   │   └── SKILL.md             # Auditoría de schema markup
│   └── rankability-test/
│       └── SKILL.md             # Test vs top 3 orgánicos
└── README.md
```

---

## Requisitos

- [Claude Code](https://claude.ai/code) instalado
- Conector **Claude in Chrome** (para los comandos que navegan Google Maps)
- Acceso a internet desde Claude Code

---

## Contribuciones

¿Encontraste un bug o tienes una idea? Abre un [issue](https://github.com/soyalonsoai/seo-local/issues) o manda un PR. La comunidad de Claude Code crece cuando compartimos.

---

<div align="center">

Hecho con ❤️ por [Soyalonso.ai](https://github.com/soyalonsoai) + Claude

[![GitHub](https://img.shields.io/badge/GitHub-soyalonsoai-181717?style=for-the-badge&logo=github)](https://github.com/soyalonsoai)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
