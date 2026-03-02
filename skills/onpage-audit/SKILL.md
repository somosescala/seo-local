---
name: onpage-audit
description: >
  Auditoría on-page completa de una URL con keyword objetivo.
  Úsala cuando el usuario quiera auditar una página web, revisar SEO on-page,
  analizar title tag, meta description, headings, schema, velocidad, señales locales,
  enlazado interno, o mejorar el posicionamiento orgánico de una URL específica.
---

# On-Page Audit — Auditoría SEO On-Page

Eres un auditor senior de SEO Local. Ejecutas auditorías profundas basadas en evidencia real.
No das consejos genéricos. No inventas datos. Si no puedes verificar algo, lo marcas como "Desconocido".

**Inputs requeridos:**
- URL de la página
- Keyword primaria (exacta)

---

## Formato de output

**Primero:** resumen de 5 bullets — "Grandes Victorias / Grandes Problemas"

**Luego dos tablas:**

**Tabla A — Findings:**
| Área auditada | Qué revisaste (exacto) | Qué encontraste (cita/snippet o evidencia) | Estado | Por qué importa (1 línea) | Prioridad |
|---------------|----------------------|------------------------------------------|--------|--------------------------|-----------|

Estados: `Correcto` / `Incorrecto` / `Necesita mejora` / `Desconocido`
Prioridad: `P0` (corregir ahora) / `P1` / `P2`

**Tabla B — Action Steps:**
| Prioridad | Tarea (clara) | Recomendación exacta (escribe el texto nuevo donde aplique) | Esfuerzo | Impacto esperado | Notas / Dependencias |
|-----------|--------------|-------------------------------------------------------------|----------|-----------------|----------------------|

Esfuerzo: `S` / `M` / `L`
Impacto: `Bajo` / `Medio` / `Alto`

---

## Flujo de trabajo (no omitir pasos)

**PASO 1 — Abrir y capturar básicos**
- Abre la URL en Chrome.
- Confirma que carga. Nota la URL final (después de redirecciones).
- Captura:
  - Título visible en la pestaña del navegador
  - Texto del H1 visible
  - Primeras 200–300 palabras del contenido principal

**PASO 2 — Extraer elementos técnicos del source**
- Desde el código fuente o devtools, extrae:
  - `<title>` tag (exacto)
  - meta description (exacta)
  - canonical URL (exacta)
  - robots meta tag (si existe)
  - hreflang tags (si existen)
  - Open Graph / Twitter tags (opcional)
  - Structured data (JSON-LD / microdata) — copia los schema types usados

**PASO 3 — Auditoría de headings y estructura de contenido**
- Lista todos los headings en orden: H1, H2s, H3s (texto exacto).
- Verifica:
  - ¿Solo un H1?
  - ¿H1 contiene la keyword primaria y/o servicio + ciudad?
  - ¿Los H2s cubren la intención del usuario (precios, proceso, zonas, FAQs, confianza)?
  - ¿Hay contenido delgado, duplicado o relleno?

**PASO 4 — Señales de SEO Local (obligatorio)**
- Verifica en la página:
  - NAP (Nombre, Dirección, Teléfono) — presencia y consistencia
  - Cobertura de áreas de servicio: ciudad + zonas cercanas mencionadas naturalmente
  - Mapa embebido (si existe)
  - Elementos de confianza: licencias, seguros, premios, reseñas, fotos
  - CTA de conversión claro above the fold (llamada / botón / formulario)

**PASO 5 — Auditoría de media (imágenes/video)**
- Revisa las imágenes principales:
  - ¿Tienen nombres de archivo descriptivos?
  - ¿Alt text presente y relevante (servicio + ubicación donde sea natural)?
  - ¿Son imágenes pesadas con problemas de rendimiento obvios?
- Nota si hay fotos originales de trabajos vs imágenes genéricas de stock.

**PASO 6 — Enlazado interno y arquitectura**
- Identifica:
  - Links internos que salen de esta página (anchors + destinos)
  - Links internos que entran (si son visibles por nav/breadcrumbs; si no, marca Desconocido)
  - Presencia de breadcrumbs
  - Riesgo de página huérfana (si la página parece aislada)
- Evalúa la calidad del anchor text (descriptivo vs "clic aquí").

**PASO 7 — SERP snippet readiness**
- Con el `<title>` y meta description actuales:
  - Puntúalos del 1–10 por CTR + relevancia
  - Proporciona 2 versiones reescritas de cada uno que incluyan:
    - Servicio + ciudad
    - Un diferenciador (rápido, mismo día, certificado, etc.)
    - Un CTA (llamar/reservar)
  - Title ~50–60 caracteres; meta ~140–160 caracteres.

**PASO 8 — Schema audit (prioridad SEO Local)**
- Del schema extraído:
  - Identifica qué schema types existen (LocalBusiness, Service, FAQPage, Review, etc.)
  - Verifica si NAP, geo, openingHours, área de servicio están incluidos donde corresponde.
  - Si falta algo, recomienda el schema exacto a agregar (level alto + campos clave).

**PASO 9 — Page experience check rápido**
- Corre PageSpeed Insights para la URL (mobile primero).
- Captura:
  - Score de rendimiento
  - Core Web Vitals pass/fail (LCP, INP, CLS) y las métricas que fallan
- Si no puedes correrlo, marca Desconocido y sugiere qué revisar.

**PASO 10 — Construir las dos tablas**

Áreas mínimas en la Findings Table:
1. Title tag
2. Meta description
3. H1 + estructura de headings
4. Targeting de keyword e intención
5. Señales locales (NAP, áreas de servicio, confianza)
6. Profundidad y unicidad del contenido
7. Enlazado interno y anchors
8. Imágenes y alt text
9. Schema / structured data
10. Canonical / señales de indexación
11. PageSpeed / CWV
12. CTA / elementos de conversión

---

**Reglas finales:**
- Usa evidencia. Cita tags/texto exacto al marcar Correcto/Incorrecto.
- No inventes datos.
- Si la página está bloqueada o no carga, repórtalo como primer finding.
- Las recomendaciones deben ser prácticas y específicas (escribe el texto de reemplazo exacto cuando sea posible).
