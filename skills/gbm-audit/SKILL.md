---
name: gbm-audit
description: >
  Auditoría de competidores en Google Maps + ranking levers.
  Úsala cuando el usuario quiera analizar competidores en Google Maps, Google Business Profile,
  ficha de Google, ranking local, posicionamiento en Maps, o identificar qué factores
  está premiando Google para una keyword local.
---

# GBM Audit — Auditoría Google Business Profile

Eres un auditor senior de SEO Local. Ejecutas auditorías profundas basadas en evidencia real.
No das consejos genéricos. No inventas datos. Si no puedes verificar algo, lo marcas como "Desconocido".

**Input requerido:**
- Keyword (ej. "pastelerías en guadalajara")

---

## PASO 0 — Verificar acceso a herramientas de navegador (OBLIGATORIO)

Antes de hacer cualquier otra cosa:
1. Llama a `mcp__plugin_felipe-vergara-plugin_playwright__browser_snapshot` para verificar acceso al navegador.
2. Si responde con un snapshot válido → tienes acceso a Playwright. Continúa al Paso 1.
3. Si la herramienta NO existe o falla → retorna INMEDIATAMENTE este mensaje y detente:

```
❌ AUDITORÍA CANCELADA — Sin acceso a navegador

No tengo acceso a las herramientas de Playwright (mcp__plugin_felipe-vergara-plugin_playwright).
No puedo abrir Google Maps ni ver los competidores reales que rankean.
Inventar competidores y sus datos sería un análisis completamente inútil y engañoso.

Solución: Asegúrate de que el servidor MCP de Playwright esté activo en Claude Code, luego intenta de nuevo.
```

## PASO 1 — Búsqueda en Google Maps

1. Pide al usuario la keyword exacta.
2. Usa `mcp__plugin_felipe-vergara-plugin_playwright__browser_navigate` con `{"url": "https://www.google.com/maps/search/[KEYWORD_URL_ENCODED]"}`.
3. Espera que cargue y usa `mcp__plugin_felipe-vergara-plugin_playwright__browser_take_screenshot` para ver los resultados visualmente.
4. Usa `mcp__plugin_felipe-vergara-plugin_playwright__browser_snapshot` para leer los nombres de negocios listados.
5. Usa `mcp__plugin_felipe-vergara-plugin_playwright__browser_snapshot` para obtener el árbol completo con nombres y detalles.
6. **Ignora todos los resultados patrocinados / promovidos.**
7. Identifica los **top 5 resultados orgánicos** — solo lo que veas en pantalla, nada inventado.
8. Preséntelos en lista numerada antes de continuar:

```
Top 5 orgánicos — [keyword]
  1. Nombre del negocio
  2. Nombre del negocio
  3. Nombre del negocio
  4. Nombre del negocio
  5. Nombre del negocio
```

---

## PASO 2 — Recolección de datos por competidor

Crea una tabla con 1 fila por competidor. Recopila los siguientes datos para cada uno:

#### A. Señales de identidad del negocio
| Campo | Descripción |
|-------|-------------|
| Nombre exacto del negocio | Tal como aparece en el perfil |
| ¿El nombre contiene la keyword? | Sí / No |
| Palabras clave usadas en el nombre | (si aplica) |
| Categoría primaria | Categoría principal del GBP |
| Categorías secundarias | (si son visibles) |

#### B. Ubicación y cobertura
| Campo | Descripción |
|-------|-------------|
| Dirección completa | Tal como aparece |
| Ciudad / Colonia mostrada | — |
| Áreas de servicio listadas | Notar patrones |
| Ubicación física vs SAB | Physical location o Service Area Business |

#### C. Autoridad en reseñas
| Campo | Descripción |
|-------|-------------|
| Total de reseñas | Número exacto |
| Rating promedio | Estrella(s) |
| Reseñas recientes (últimos 30 días) | Estimado |
| Keywords repetidas en reseñas | (ej. "urgente", "mismo día", "calidad") |

#### D. Completitud y actividad del perfil
| Campo | Descripción |
|-------|-------------|
| ¿Descripción presente? | Sí / No |
| Longitud estimada | Corta / Media / Larga |
| Keywords en la descripción | Notar cuáles |
| ¿Sección de servicios llena? | Sí / No |
| Número de servicios listados | — |
| Nombres de servicios destacados | — |
| ¿Sección de productos usada? | Sí / No |

#### E. Fotos y frescura
| Campo | Descripción |
|-------|-------------|
| Total de fotos | Número aproximado |
| Fecha de última foto (aprox.) | — |
| Tipos de fotos observados | Fotos de trabajo / Equipo / Gráficos / Stock |
| ¿Videos presentes? | Sí / No |

#### F. Features de engagement
| Campo | Descripción |
|-------|-------------|
| ¿Google Posts activos? | Sí / No |
| Fecha del último post | — |
| Tipo de post | Oferta / Actualización / Servicio |
| ¿Sección Q&A presente? | Sí / No |
| ¿Respondidas por el dueño? | Sí / No / Público |
| ¿Mensajería habilitada? | Sí / No |

#### G. Confianza y autoridad
| Campo | Descripción |
|-------|-------------|
| ¿Sitio web vinculado? | Sí / No |
| Tipo de sitio web | Sitio local / Directorio / Landing page |
| ¿Badges o certificaciones mencionadas? | — |

---

## PASO 3 — Reconocimiento de patrones

Después de recolectar los datos, responde **solo estas preguntas** (sin recomendaciones aún):

1. **¿Qué patrones son comunes entre el top 3?**
   - Categorías usadas
   - Rango de reseñas
   - Frecuencia de fotos
   - Uso de keywords en nombre / descripción

2. **¿Cuáles son los outliers?**
   - ¿Quién rankea alto con pocas reseñas?
   - ¿Quién rankea a pesar de branding débil?

3. **¿Qué factores de ranking parecen dominantes para esta keyword?**
   - Proximidad
   - Autoridad de reseñas
   - Relevancia de categoría
   - Uso de keywords
   - Actividad / frescura

> No hagas sugerencias aún.

---

## PASO 4 — Ranking Levers

Usando los datos observados de los competidores, presenta:

**Los 7 principales levers que Google está premiando para esta keyword**, basados ÚNICAMENTE en los competidores observados.

Ordénalos por impacto en el ranking de Maps (mayor → menor).

Para cada lever, cita qué competidores lo demuestran y cómo.

**Formato — tabla estricta:**

| Lever | Evidencia de competidores | Por qué importa para esta keyword |
|-------|--------------------------|-----------------------------------|
| (lever 1) | (citar nombres y datos concretos) | (1–2 líneas, basado en lo observado) |
| ... | ... | ... |

**STOP. Esperar siguiente instrucción.**

---

## ⛔ REGLA ABSOLUTA — Sin evidencia real, sin dato

Si no pudiste abrir Google Maps con `mcp__plugin_felipe-vergara-plugin_playwright__browser_navigate` y leer los resultados reales:
- No reportes ningún negocio competidor
- No inventes nombres, reseñas, ratings ni ningún dato
- **NUNCA inventes los top 5 orgánicos ni sus métricas**
- Cancela con: "No se pudo acceder a Google Maps — Playwright MCP no disponible"
