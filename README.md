# SEO Local

Plugin para Claude Code que convierte a Claude en un **auditor senior de SEO Local**. Ejecuta auditorías profundas basadas en evidencia real — sin consejos genéricos, sin datos inventados.

---

## Comandos disponibles

| Comando | Descripción |
|---------|-------------|
| `/seo-local:seo-local-audit` | **Full audit en un comando** — ejecuta todo en paralelo y genera roadmap en PDF |
| `/seo-local:seo-roadmap` | Consolida resultados de auditorías previas en un roadmap + PDF |
| `/seo-local:seo-plan` | Guía de inicio — explica el proceso completo y por dónde empezar |
| `/seo-local:gbp-audit` | Audita TU propia ficha de Google Business Profile |
| `/seo-local:gbm-audit` | Auditoría de competidores en Google Maps + ranking levers |
| `/seo-local:onpage-audit` | Auditoría on-page completa de una URL |
| `/seo-local:schema-audit` | Auditoría de structured data / schema markup |
| `/seo-local:rankability-test` | Test de rankability vs top 3 resultados orgánicos |

---

## Instalación

### Desde el marketplace de Somos Escala

```
/plugin marketplace add https://github.com/somosescala/my-marketplace
/plugin install seo-local@somosescala
```

### Manual

```bash
claude --plugin-dir ./seo-local
```

---

## Uso

### `/seo-local-audit` — Full SEO Local Audit (recomendado)

Ejecuta todos los audits en paralelo con **un solo comando** usando sub-agentes especializados, luego genera un roadmap consolidado en PDF listo para entregar al cliente.

**Input:** URL + keyword objetivo + link de Google Business Profile

**Output:**
- 4 sub-agentes corren en paralelo: on-page + schema, rankability, GBP propio, competidores
- Resumen ejecutivo con hallazgos de todas las auditorías
- Roadmap priorizado con matriz impacto/esfuerzo
- Plan de acción 30/60/90 días
- Reporte HTML + PDF profesional

---

### `/seo-roadmap` — Roadmap consolidado

Toma los resultados de auditorías previas y los convierte en un plan de acción priorizado exportado como PDF. Útil cuando ya corriste los audits individuales y quieres el plan final.

**Input:** Resultados de una o más auditorías (gbp-audit, gbm-audit, onpage-audit, schema-audit, rankability-test)

**Output:**
- Tabla maestra de todos los hallazgos consolidados
- Matriz de priorización (4 cuadrantes: Quick Wins, Proyectos, Fill-ins, Reconsiderar)
- Plan de acción 30/60/90 días con tareas concretas y responsables
- Reporte HTML + PDF profesional listo para cliente

---

### `/seo-plan` — Guía de inicio

Explica qué hace el plugin, todos los comandos disponibles y el proceso recomendado según tu objetivo.

**Input:** Ninguno requerido

**Output:**
- Tabla de comandos disponibles
- Flujo recomendado para rankear en Maps
- Flujo recomendado para rankear orgánicamente
- Flujo de auditoría completa

---

### `/gbp-audit` — Auditoría de tu propia ficha

Audita en profundidad TU propia ficha de Google Business Profile e identifica qué te está frenando en el ranking.

**Input:** Nombre del negocio + ciudad, o link directo al perfil en Google Maps

**Output:**
- Tabla completa de datos de la ficha (identidad, NAP, reseñas, completitud, fotos, actividad)
- Score de completitud / 100
- Top 3 fortalezas y top 3 problemas críticos
- Tabla de action items ordenados por impacto
- Recomendación del siguiente paso

---

### `/gbm-audit` — Auditoría Google Business Profile

Analiza los top 5 competidores orgánicos en Google Maps para una keyword y extrae los **7 ranking levers** que Google está premiando.

**Input:** Keyword (ej. "dentistas en monterrey")

**Output:**
- Lista de top 5 orgánicos
- Tabla de datos por competidor (reseñas, fotos, categorías, descripción, posts, etc.)
- Reconocimiento de patrones del top 3
- Tabla de ranking levers ordenados por impacto

---

### `/onpage-audit` — Auditoría On-Page

Auditoría completa de 10 pasos para una URL con keyword objetivo.

**Input:** URL + keyword primaria

**Output:**
- Resumen de victorias y problemas
- Tabla de findings con estado y prioridad
- Tabla de action steps con recomendaciones exactas (incluye texto de reemplazo listo para copiar)

---

### `/schema-audit` — Auditoría de Schema Markup

Evalúa el structured data de una página y genera los JSON-LD faltantes.

**Input:** URL + tipo de negocio + ciudad

**Output:**
- Tabla de schema existente con veredicto
- Tabla de schema faltante con prioridad
- Ejemplos JSON-LD listos para implementar (con placeholders)

---

### `/rankability-test` — Test de Rankability

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
│   └── plugin.json          # Manifiesto del plugin
├── skills/
│   ├── seo-local-audit/
│   │   └── SKILL.md         # Master: lanza todos los audits + genera PDF
│   ├── seo-roadmap/
│   │   └── SKILL.md         # Consolida hallazgos en roadmap + PDF
│   ├── seo-plan/
│   │   └── SKILL.md         # Guía de inicio y flujos recomendados
│   ├── gbp-audit/
│   │   └── SKILL.md         # Auditoría de tu propia ficha GBP
│   ├── gbm-audit/
│   │   └── SKILL.md         # Auditoría de competidores en Maps
│   ├── onpage-audit/
│   │   └── SKILL.md         # Auditoría on-page
│   ├── schema-audit/
│   │   └── SKILL.md         # Auditoría de schema markup
│   └── rankability-test/
│       └── SKILL.md         # Test vs top 3 orgánicos
└── README.md
```

---

## Licencia

MIT
