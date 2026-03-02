# SEO Local

Plugin para Claude Code que convierte a Claude en un **auditor senior de SEO Local**. Ejecuta auditorías profundas basadas en evidencia real — sin consejos genéricos, sin datos inventados.

---

## Comandos disponibles

| Comando | Descripción |
|---------|-------------|
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
│   └── seo-local/
│       └── SKILL.md         # Lógica y flujos de auditoría
└── SKILL.md                 # Versión standalone
```

---

## Licencia

MIT
