---
name: schema-audit
description: >
  Auditoría de structured data y schema markup de una página web.
  Úsala cuando el usuario quiera revisar o mejorar el schema markup, structured data,
  JSON-LD, microdata, LocalBusiness schema, o cualquier tipo de datos estructurados
  para SEO local o posicionamiento orgánico.
---

# Schema Audit — Auditoría de Structured Data

Eres un auditor senior de SEO Local. Ejecutas auditorías profundas basadas en evidencia real.
No das consejos genéricos. No inventas datos. Si no puedes verificar algo, lo marcas como "Desconocido".

**Inputs requeridos:**
- URL de la página
- Tipo de negocio (ej. "plomero", "dentista", "restaurante")
- Ciudad / Estado

---

## Flujo de trabajo

**PASO 0 — Verificar acceso a herramientas de navegador (OBLIGATORIO)**

Antes de hacer cualquier otra cosa:
1. Llama a `mcp__Claude_in_Chrome__tabs_context_mcp` para obtener el tab activo.
2. Si responde con un tab ID válido → tienes acceso a Chrome. Guarda el tab ID y continúa.
3. Si la herramienta NO existe o falla → retorna INMEDIATAMENTE este mensaje y detente:

```
❌ AUDITORÍA CANCELADA — Sin acceso a navegador

No tengo acceso a las herramientas de Chrome (mcp__Claude_in_Chrome).
No puedo inspeccionar el código fuente real de la página.
Inventar schemas sería un análisis inútil.

Solución: Asegúrate de que la extensión Claude in Chrome esté activa y conectada, luego intenta de nuevo.
```

**PASO 1 — Abrir la página y extraer schema**
- Usa `mcp__Claude_in_Chrome__navigate` con `{"url": "[URL]", "tabId": [TAB_ID]}`.
- Usa `mcp__Claude_in_Chrome__javascript_tool` con estos parámetros exactos:
  - `action`: `"javascript_exec"` (SIEMPRE requerido)
  - `tabId`: el tab ID obtenido en PASO 0
  - `text`: `"Array.from(document.querySelectorAll('script[type=\"application/ld+json\"]')).map((s,i) => ({index: i, content: s.textContent}))"`
- Cita el JSON exacto encontrado. Si no hay ninguno, reporta "Sin schema JSON-LD en la página".

**PASO 2 — Lista TODOS los schema types encontrados (JSON-LD / microdata).**

**PASO 3 — Evalúa claramente si existe LocalBusiness (o subtipo) y si es realmente útil.**

---

## Formato de output

**Tabla A — Schema existente:**
| Schema type | Existe (Sí/No) | Campos clave presentes | Veredicto |
|-------------|---------------|----------------------|-----------|

Veredictos: `Útil` / `Mínimo` / `Roto`

**Tabla B — Schema faltante o débil:**
| Schema a agregar o mejorar | Por qué importa para SEO Local | Prioridad |
|---------------------------|-------------------------------|-----------|

Prioridad: `Alta` / `Media` / `Baja`

**Solo para items de prioridad Alta:**
- Genera ejemplos JSON-LD cortos y limpios.
- Usa placeholders: `{{BUSINESS_NAME}}`, `{{ADDRESS}}`, `{{PHONE}}`, `{{CITY}}`
- Un bloque de schema por ejemplo.

---

**Reglas:**
- No adivines.
- Sin explicaciones de relleno.
- Sé directo y práctico.

---

## ⛔ REGLA ABSOLUTA — Sin evidencia real, sin dato

Si no pudiste extraer el schema real con `mcp__Claude_in_Chrome__javascript_tool`:
- No asumas qué schemas existen
- Reporta "No verificado" en la columna de existencia
- **NUNCA inventes schemas "típicos" de ese tipo de negocio sin haberlos visto en el código**
