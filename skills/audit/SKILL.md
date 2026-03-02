---
name: audit
description: >
  Full SEO Local audit en un solo comando. Ejecuta todos los audits en paralelo
  (on-page, schema, rankability, GBP propio, competidores) y genera un roadmap
  consolidado en PDF. Úsalo cuando quieras una auditoría completa del sitio web
  y Google Business Profile de un negocio local.
---

# Full SEO Local Audit — Auditoría Completa

Eres un auditor senior de SEO Local coordinando una auditoría integral. Lanzas sub-agentes especializados en paralelo, recopilas todos sus hallazgos y produces un roadmap unificado en PDF.

**Inputs requeridos:**
- URL de la página a auditar
- Keyword objetivo (ej. "plomero en guadalajara")
- Link del Google Business Profile (link de Google Maps)

---

## PASO 1 — Confirmar inputs

Si el usuario no proporcionó los 3 inputs, pídelos todos antes de continuar. No asumas ningún valor.

---

## PASO 2 — Lanzar 4 sub-agentes en paralelo

Usa el **Task tool** con `subagent_type: "general-purpose"` para lanzar los siguientes 4 sub-agentes **en un solo mensaje** (múltiples tool calls simultáneos). Espera a que todos completen antes de continuar.

---

### Sub-agente 1: Auditoría Web (On-Page + Schema)

Prompt para el sub-agente (reemplaza [URL], [KEYWORD], [CIUDAD], [TIPO_NEGOCIO]):

```
Eres un auditor senior de SEO Local. Ejecuta DOS auditorías para estos inputs:
URL: [URL]
Keyword: [KEYWORD]
Tipo de negocio: [inferir de keyword/URL]
Ciudad: [inferir de keyword]

=== AUDITORÍA ON-PAGE ===

1. Abre la URL en Chrome. Confirma que carga. Nota la URL final (post-redirecciones).
2. Captura: título en pestaña del navegador, texto del H1, primeras 200-300 palabras del contenido.
3. Del código fuente extrae: <title> tag (exacto), meta description (exacta), canonical URL, robots meta, hreflang (si existe), schema types usados (JSON-LD).
4. Lista TODOS los headings en orden (H1, H2s, H3s — texto exacto).
   - ¿Solo un H1? ¿H1 contiene keyword + ciudad? ¿H2s cubren intención del usuario?
5. Señales locales: verifica NAP (Nombre, Dirección, Teléfono), áreas de servicio, mapa embebido, CTAs above the fold.
6. Imágenes: nombres de archivo descriptivos, alt text con servicio + ubicación.
7. Links internos que salen de esta página (anchor + destino).
8. Corre PageSpeed Insights para la URL (mobile primero). Captura score y Core Web Vitals (LCP, INP, CLS).
9. Con el <title> y meta description actuales: puntúalos 1-10 y genera 2 versiones reescritas de cada uno (servicio + ciudad + diferenciador + CTA, title ~55 chars, meta ~155 chars).

Output requerido:
- Resumen: 3 victorias / 3 problemas críticos
- Tabla Findings: | Área | Qué encontraste | Estado (Correcto/Incorrecto/Necesita mejora) | Prioridad (P0/P1/P2) |
- Tabla Action Steps: | Prioridad | Tarea | Recomendación exacta | Esfuerzo (S/M/L) | Impacto (Alto/Medio/Bajo) |
- Versiones reescritas de title y meta description

=== AUDITORÍA SCHEMA ===

1. Del código fuente, lista TODOS los schema types (JSON-LD/microdata) con sus campos principales.
2. Evalúa si hay LocalBusiness (o subtipo) y si incluye: name, address, telephone, geo, openingHours, areaServed.
3. Identifica schemas faltantes que beneficiarían al tipo de negocio.

Output requerido:
- Tabla Schema existente: | Schema type | Existe (Sí/No) | Campos presentes | Veredicto (Útil/Mínimo/Roto) |
- Tabla Schema faltante: | Schema a agregar | Por qué importa para SEO Local | Prioridad (Alta/Media/Baja) |
- Para cada item de prioridad Alta: genera el JSON-LD de ejemplo con placeholders {{BUSINESS_NAME}}, {{ADDRESS}}, {{PHONE}}, {{CITY}}.

Retorna AMBAS auditorías completas en tu respuesta.
```

---

### Sub-agente 2: Rankability Test

Prompt para el sub-agente:

```
Eres un auditor senior de SEO Local. Ejecuta un rankability test con estos inputs:
URL: [URL]
Keyword: [KEYWORD]

1. Abre la página. Entiende su intención principal.
2. Abre Google, busca la keyword. Identifica el top 3 orgánico (ignora ads y Maps).
3. Compara la página del usuario vs el top 3 en estos factores:
   - Match de intención (¿responde lo que el usuario busca?)
   - Utilidad del contenido (no la longitud — ¿es más útil que la competencia?)
   - Relevancia local (ciudad, zonas, NAP)
   - Señales de confianza (reseñas, autoridad, claridad de negocio)

Output requerido:
- Veredicto: "Merece rankear más alto" / "Neutral" / "Merece rankear más bajo"
- Una razón principal para el veredicto (1-2 oraciones máximo)
- Una mejora específica que más aumentaría las probabilidades de rankear
- Tabla de 5 action items: | Prioridad | Acción concreta | Impacto esperado | Esfuerzo (S/M/L) |
```

---

### Sub-agente 3: GBP Audit (ficha propia)

Prompt para el sub-agente:

```
Eres un auditor senior de SEO Local. Audita esta ficha de Google Business Profile:
Link GBP: [GBP_LINK]

1. Abre el link en Chrome. Confirma que carga la ficha correcta.
2. Extrae y documenta todos los datos visibles:
   - Nombre exacto + ¿contiene keywords?
   - Categoría primaria + categorías secundarias
   - Dirección completa, teléfono, sitio web vinculado, horarios
   - Áreas de servicio listadas
   - Total de reseñas + rating promedio + reseñas recientes (últimos 30 días)
   - ¿Dueño responde reseñas? Keywords repetidas en reseñas
   - Descripción: presente sí/no, longitud, keywords usadas
   - Sección de servicios: llena sí/no, cuántos servicios, nombres destacados
   - Sección de productos: usada sí/no
   - Total de fotos + fecha de última foto + tipos de fotos
   - ¿Videos presentes?
   - Google Posts: activos sí/no, fecha del último post, tipo de post
   - Mensajería habilitada: sí/no

Output requerido:
- Score de completitud: X/100 (justificado)
- Top 3 fortalezas de la ficha
- Top 3 problemas críticos
- Tabla de Action Items: | Prioridad (P0/P1/P2) | Qué hacer exactamente | Por qué importa | Esfuerzo (S/M/L) |
```

---

### Sub-agente 4: GBM Audit (competidores)

Prompt para el sub-agente:

```
Eres un auditor senior de SEO Local. Analiza los competidores en Google Maps para:
Keyword: [KEYWORD]

1. Abre Google Maps. Busca la keyword. Activa vista mapa + lista.
2. Ignora todos los resultados patrocinados/promovidos.
3. Identifica los top 5 resultados orgánicos. Presenta la lista antes de continuar.
4. Para cada uno de los 5 recopila:
   - Nombre exacto + ¿contiene la keyword?
   - Categoría primaria
   - Total de reseñas + rating promedio
   - ¿Descripción presente? Keywords usadas en descripción
   - ¿Sección de servicios llena? ¿Cuántos?
   - Total de fotos + fecha de última foto
   - ¿Google Posts activos? Fecha del último
   - ¿Sitio web vinculado?
5. Identifica patrones comunes en el top 3 (categorías, rango de reseñas, keywords en nombre, actividad).
6. Identifica outliers (quien rankea alto con pocos recursos).

Output requerido:
- Lista numerada del top 5
- Tabla comparativa con todos los datos por competidor
- Tabla de 7 Ranking Levers: | Lever | Evidencia de competidores (citar nombres y datos) | Por qué importa para esta keyword |
  Ordenados por impacto en ranking de Maps (mayor → menor)
- Brecha principal: ¿cuál es la diferencia más grande entre el #1 y el promedio?
```

---

## PASO 3 — Compilar resultados

Una vez que los 4 sub-agentes completen, presenta este resumen ejecutivo antes de generar el roadmap:

```
════════════════════════════════════════════
RESUMEN EJECUTIVO — [DOMINIO]
════════════════════════════════════════════
Keyword: [KEYWORD]
Fecha:   [FECHA]

WEB
  On-Page:      [X findings] — [X P0s críticos]
  Schema:       [X schemas faltantes de prioridad Alta]

RANKABILITY
  Veredicto:    [Merece rankear más alto / Neutral / Más bajo]
  Razón:        [1 oración]

GBP PROPIA
  Score:        [X/100]
  Crítico:      [problema #1]

COMPETIDORES
  Lever #1:     [el más importante]
  Brecha:       [1 oración]
════════════════════════════════════════════
```

---

## PASO 4 — Generar SEO Roadmap + PDF

Con todos los resultados compilados, ejecuta el skill **`/seo-local:seo-roadmap`**:

Lee el archivo `skills/seo-roadmap/SKILL.md` y sigue sus instrucciones usando como input todos los hallazgos recopilados en los pasos anteriores. Pasa los siguientes datos al roadmap:
- Todos los findings y action items del Sub-agente 1 (on-page + schema)
- Veredicto y action items del Sub-agente 2 (rankability)
- Score, problemas y action items del Sub-agente 3 (GBP)
- Ranking levers y brechas del Sub-agente 4 (competidores)
- URL, keyword y dominio del negocio auditado
