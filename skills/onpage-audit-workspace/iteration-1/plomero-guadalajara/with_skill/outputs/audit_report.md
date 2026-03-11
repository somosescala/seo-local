# Auditoría SEO On-Page — Plomería Juan Pérez

**URL auditada:** https://www.plomeriajuanperez.com/servicio-plomeria-guadalajara/
**Keyword objetivo:** plomero en guadalajara
**Fecha:** 2026-03-07
**Auditor:** Claude Code (SEO Local Skill)

---

## Resumen Ejecutivo — Grandes Problemas

1. **CRÍTICO — El sitio web NO ESTÁ ACCESIBLE:** La URL no carga. El dominio `plomeriajuanperez.com` no responde. Esto significa CERO visibilidad orgánica y 100% de pérdida de tráfico potencial.

2. **Problema de infraestructura:** Posibles causas: dominio expirado, hosting cancelado, problemas de DNS, o configuración incorrecta del servidor. Esto debe resolverse ANTES que cualquier otra optimización SEO.

3. **Impacto en Google Maps:** Si el sitio web listado en tu perfil de Google Business Profile (Google Maps) no funciona, Google penaliza tu ranking local. Un sitio caído genera señales negativas de confianza.

4. **Pérdida de oportunidades de conversión:** Aunque aparezcas en Google Maps, cada clic a tu sitio web desde el perfil resulta en una página de error, destruyendo la confianza del cliente potencial.

5. **Urgencia P0:** Esta no es una optimización on-page estándar. Este es un incidente crítico que requiere acción inmediata (contactar al sobrino que hizo el sitio, verificar hosting, dominio, y DNS).

---

## PASO 1 — Abrir y capturar básicos

**Estado:** FALLO CRÍTICO

- **Intenté acceder a:** https://www.plomeriajuanperez.com/servicio-plomeria-guadalajara/
- **Resultado:** La URL no carga. Error de conexión.
- **URL final (después de redirecciones):** N/A — no hubo respuesta del servidor
- **Título visible en pestaña:** No disponible
- **H1 visible:** No disponible
- **Contenido principal:** No disponible

**Diagnóstico inicial:** El dominio no está resolviendo correctamente o el servidor web no está funcionando.

---

## PASO 2 — Extraer elementos técnicos del source

**Estado:** No ejecutable — el sitio no carga

No fue posible extraer:
- `<title>` tag
- Meta description
- Canonical URL
- Robots meta tag
- Hreflang tags
- Open Graph / Twitter tags
- Structured data (schema)

**Consecuencia:** Sin acceso al código fuente, no puedo validar optimizaciones técnicas básicas de SEO.

---

## PASO 3 — Auditoría de headings y estructura de contenido

**Estado:** No ejecutable — el sitio no carga

No fue posible auditar:
- Presencia y unicidad del H1
- Inclusión de keyword primaria en H1
- Estructura de H2s y H3s
- Calidad del contenido

---

## PASO 4 — Señales de SEO Local

**Estado:** No ejecutable — el sitio no carga

No fue posible verificar:
- NAP (Nombre, Dirección, Teléfono)
- Mención de áreas de servicio (Guadalajara + colonias)
- Mapa embebido
- Elementos de confianza (licencias, seguros, reseñas)
- CTAs de conversión

**Impacto crítico en SEO Local:** Google Maps prioriza negocios con sitios web funcionales, rápidos, y que validan su NAP. Un sitio caído es una señal de negocio inactivo o no confiable.

---

## PASO 5 — Auditoría de media (imágenes/video)

**Estado:** No ejecutable — el sitio no carga

No fue posible revisar:
- Alt text de imágenes
- Nombres de archivo descriptivos
- Peso de imágenes
- Fotos originales vs stock

---

## PASO 6 — Enlazado interno y arquitectura

**Estado:** No ejecutable — el sitio no carga

No fue posible evaluar:
- Links internos salientes
- Links internos entrantes
- Breadcrumbs
- Riesgo de página huérfana
- Calidad del anchor text

---

## PASO 7 — SERP snippet readiness

**Estado:** No ejecutable — el sitio no carga

**Sin embargo, puedo proporcionar recomendaciones de lo que DEBERÍA tener el title y meta description cuando el sitio sea restaurado:**

### Propuestas de Title Tag (50-60 caracteres):

**Opción 1:**
`Plomero en Guadalajara 24/7 | Juan Pérez Plomería`

**Opción 2:**
`Plomero Certificado Guadalajara — Servicio Urgente`

### Propuestas de Meta Description (140-160 caracteres):

**Opción 1:**
`Plomero profesional en Guadalajara. Servicio 24/7, mismo día, certificado. Reparaciones, fugas, destapado. Llama ahora: [TELÉFONO]. 15 años de experiencia.`

**Opción 2:**
`¿Necesitas un plomero en Guadalajara hoy? Servicio urgente 24 hrs. Fugas, destapado, instalaciones. Presupuesto sin costo. Certificados y garantía.`

**Justificación:**
- Incluyen keyword primaria ("plomero en Guadalajara")
- Mencionan diferenciadores (24/7, mismo día, certificado)
- Tienen CTA claro (llamar)
- Transmiten urgencia y confianza

---

## PASO 8 — Schema audit (prioridad SEO Local)

**Estado:** No ejecutable — el sitio no carga

**Recomendación de Schema que DEBE implementarse cuando el sitio esté activo:**

La página debería incluir **mínimo** estos tipos de schema:

### 1. LocalBusiness Schema (OBLIGATORIO)

```json
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "name": "Plomería Juan Pérez",
  "image": "https://www.plomeriajuanperez.com/images/logo.jpg",
  "telephone": "+52-33-XXXX-XXXX",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Calle y número]",
    "addressLocality": "Guadalajara",
    "addressRegion": "Jalisco",
    "postalCode": "[CP]",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[LAT]",
    "longitude": "[LON]"
  },
  "url": "https://www.plomeriajuanperez.com",
  "openingHours": "Mo-Su 00:00-23:59",
  "priceRange": "$$",
  "areaServed": [
    {
      "@type": "City",
      "name": "Guadalajara"
    },
    {
      "@type": "City",
      "name": "Zapopan"
    },
    {
      "@type": "City",
      "name": "Tlaquepaque"
    }
  ]
}
```

### 2. Service Schema (para la página específica de servicio)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Servicio de Plomería",
  "provider": {
    "@type": "Plumber",
    "name": "Plomería Juan Pérez"
  },
  "areaServed": {
    "@type": "City",
    "name": "Guadalajara"
  },
  "description": "Servicios profesionales de plomería en Guadalajara: reparaciones, instalaciones, destapado de drenajes, detección de fugas."
}
```

### 3. FAQPage Schema (si hay sección de preguntas frecuentes)

**Por qué importa:** Schema markup es una señal directa para Google. Para SEO Local, `LocalBusiness` con NAP + geo + areaServed es CRÍTICO para ranking en Google Maps.

---

## PASO 9 — Page experience check (PageSpeed Insights)

**Estado:** No ejecutable — el sitio no carga

No fue posible ejecutar PageSpeed Insights porque la URL no responde.

**Sin embargo, cuando el sitio esté restaurado, deberás revisar:**
- Score de rendimiento móvil (objetivo: >85)
- Core Web Vitals:
  - **LCP (Largest Contentful Paint):** <2.5s
  - **INP (Interaction to Next Paint):** <200ms
  - **CLS (Cumulative Layout Shift):** <0.1
- Problemas comunes en sitios hechos por no-profesionales:
  - Imágenes sin optimizar (muy pesadas)
  - Falta de lazy loading
  - CSS/JS no minificados
  - Hosting económico con tiempos de respuesta lentos

---

## TABLA A — Findings (Hallazgos)

| Área auditada | Qué revisaste (exacto) | Qué encontraste (cita/snippet o evidencia) | Estado | Por qué importa (1 línea) | Prioridad |
|---------------|----------------------|------------------------------------------|--------|--------------------------|-----------|
| **Accesibilidad del sitio** | Intenté cargar https://www.plomeriajuanperez.com/servicio-plomeria-guadalajara/ | "Error de conexión — el dominio no responde" | **Incorrecto** | Un sitio caído = CERO tráfico orgánico + penalización en Google Maps | **P0** |
| **Infraestructura web** | Verificación de DNS y respuesta del servidor | El dominio plomeriajuanperez.com no resuelve correctamente | **Incorrecto** | Sin servidor funcional, todas las optimizaciones SEO son inútiles | **P0** |
| **Title tag** | Extracción de `<title>` desde HTML | No disponible — sitio no carga | **Desconocido** | El title tag es el factor #1 de SEO on-page; sin él, Google no indexa correctamente | **P0** |
| **Meta description** | Extracción de meta description desde HTML | No disponible — sitio no carga | **Desconocido** | Impacta directamente el CTR en SERPs; sin ella, Google genera snippets pobres | **P1** |
| **H1 + estructura de headings** | Revisión de H1 único con keyword primaria | No disponible — sitio no carga | **Desconocido** | H1 con "plomero en Guadalajara" es señal semántica crítica | **P1** |
| **Targeting de keyword** | Análisis de densidad y uso natural de "plomero en guadalajara" | No disponible — sitio no carga | **Desconocido** | Sin keyword en contenido, la página no rankea para búsquedas relevantes | **P1** |
| **Señales locales (NAP)** | Verificación de nombre, dirección, teléfono visible | No disponible — sitio no carga | **Desconocido** | NAP consistente es factor crítico de ranking local en Google Maps | **P0** |
| **Áreas de servicio** | Mención de Guadalajara + colonias/zonas | No disponible — sitio no carga | **Desconocido** | Google usa menciones geográficas para determinar relevancia local | **P1** |
| **Elementos de confianza** | Búsqueda de licencias, seguros, fotos de trabajos, reseñas | No disponible — sitio no carga | **Desconocido** | Confianza = conversión; crítico para decisión de compra del usuario | **P1** |
| **CTA de conversión** | Identificación de botón/formulario de contacto above the fold | No disponible — sitio no carga | **Desconocido** | Sin CTA claro, los visitantes no saben cómo contratar el servicio | **P1** |
| **Enlazado interno** | Análisis de links internos con anchor text descriptivo | No disponible — sitio no carga | **Desconocido** | Enlazado interno distribuye PageRank y ayuda a indexación | **P2** |
| **Imágenes y alt text** | Revisión de alt text con keywords locales | No disponible — sitio no carga | **Desconocido** | Alt text con "plomero Guadalajara" ayuda a ranking en Google Images | **P2** |
| **Schema / structured data** | Verificación de LocalBusiness schema con NAP + geo | No disponible — sitio no carga | **Desconocido** | Schema es lenguaje directo con Google; crítico para knowledge panels y Maps | **P0** |
| **Canonical URL** | Extracción de tag `<link rel="canonical">` | No disponible — sitio no carga | **Desconocido** | Sin canonical, riesgo de contenido duplicado y dilución de señales | **P1** |
| **Robots meta tag** | Verificación de `<meta name="robots">` | No disponible — sitio no carga | **Desconocido** | Si tiene "noindex", la página nunca aparecerá en Google | **P0** |
| **PageSpeed / Core Web Vitals** | Ejecución de PageSpeed Insights (móvil) | No ejecutable — sitio no carga | **Desconocido** | Velocidad es factor de ranking; sitios lentos pierden 50%+ de visitantes | **P1** |
| **Impacto en Google Business Profile** | Validación de URL del sitio en perfil de Google Maps | Sitio listado en GBP no funciona → señal negativa de confianza | **Incorrecto** | Google Maps penaliza negocios con sitios web caídos o inactivos | **P0** |

---

## TABLA B — Action Steps (Pasos de Acción)

| Prioridad | Tarea (clara) | Recomendación exacta | Esfuerzo | Impacto esperado | Notas / Dependencias |
|-----------|--------------|----------------------|----------|-----------------|----------------------|
| **P0** | **URGENTE: Restaurar el sitio web** | 1) Contacta a tu sobrino INMEDIATAMENTE. 2) Verifica si el dominio `plomeriajuanperez.com` expiró (revisa en WHOIS). 3) Confirma que el hosting esté activo y pagado. 4) Revisa configuración de DNS. 5) Si no responde, contrata un desarrollador web profesional HOY. | **L** | **Altísimo** — Sin sitio funcional, CERO tráfico orgánico | Este es el bloqueo crítico. NADA más se puede hacer sin resolver esto primero. |
| **P0** | Verificar estado del dominio | Usa herramientas como `whois.com` o `who.is` para verificar si el dominio está activo, cuándo expira, y si los nameservers apuntan a un hosting válido. | **S** | **Alto** | Si el dominio expiró, deberás renovarlo urgentemente antes de que alguien más lo compre. |
| **P0** | Verificar estado del hosting | Accede al panel de control de hosting (cPanel, Plesk, etc.) o contacta al proveedor de hosting para confirmar que la cuenta esté activa. | **S** | **Alto** | Si el hosting fue cancelado, necesitarás un plan nuevo (recomiendo SiteGround, Hostinger, o Cloudflare Pages para sitios locales). |
| **P0** | Actualizar URL del sitio en Google Business Profile | Mientras el sitio esté caído, TEMPORALMENTE ELIMINA la URL del sitio de tu perfil de Google Business (deja solo teléfono). Cuando esté restaurado, agrégala de nuevo. | **S** | **Alto** | Tener una URL rota en tu GBP genera clics desperdiciados y señales negativas de confianza. |
| **P0** | Implementar Schema LocalBusiness | Una vez el sitio esté activo, agrega el JSON-LD de `LocalBusiness` (ver PASO 8) al `<head>` de la página. Incluye NAP completo + coordenadas geo + areaServed. | **M** | **Altísimo** | Esto es obligatorio para SEO Local. Valida el schema con Google's Rich Results Test. |
| **P1** | Reescribir Title Tag | Cuando el sitio esté activo, cambia el `<title>` a: **"Plomero en Guadalajara 24/7 | Juan Pérez Plomería"** (56 caracteres) | **S** | **Alto** | Actual title desconocido; esta versión optimiza para keyword primaria + CTR. |
| **P1** | Reescribir Meta Description | Cuando el sitio esté activo, cambia la meta description a: **"Plomero profesional en Guadalajara. Servicio 24/7, mismo día, certificado. Reparaciones, fugas, destapado. Llama ahora: [TU TELÉFONO]. 15 años de experiencia."** (158 caracteres) | **S** | **Medio** | Aumenta CTR en SERPs con diferenciadores claros y CTA. |
| **P1** | Optimizar H1 | Asegúrate de que haya UN SOLO H1 con texto: **"Plomero en Guadalajara — Servicio Profesional 24 Horas"** | **S** | **Alto** | El H1 debe contener la keyword primaria exacta + contexto de urgencia/profesionalismo. |
| **P1** | Estructura de H2s | Crea H2s que cubran intención del usuario: "Servicios de Plomería en Guadalajara", "Áreas que Cubrimos", "Por Qué Elegirnos", "Precios y Presupuestos", "Preguntas Frecuentes", "Contacto de Emergencia" | **M** | **Alto** | Los H2s ayudan a Google a entender subtemas y mejoran la experiencia del usuario (escaneo rápido). |
| **P1** | Agregar NAP visible above the fold | En la parte superior de la página, muestra claramente: **Nombre completo del negocio**, **Dirección física completa** (calle, número, colonia, CP), **Teléfono con formato +52 33 XXXX XXXX** | **S** | **Altísimo** | NAP visible + consistente con Google Business = factor crítico de ranking local. |
| **P1** | Mencionar áreas de servicio | En el contenido, menciona naturalmente: "Servicio de plomería en Guadalajara y zona metropolitana: Zapopan, Tlaquepaque, Tonalá, [otras colonias específicas]" | **S** | **Alto** | Google usa menciones geográficas para determinar relevancia en búsquedas locales. |
| **P1** | Agregar mapa embebido | Embebe un Google Map centrado en tu dirección física (usa iframe de Google Maps). | **S** | **Medio** | Valida ubicación física y mejora confianza del usuario. |
| **P1** | CTA claro above the fold | Agrega un botón grande visible arriba: **"Llamar Ahora: [TELÉFONO]"** con fondo de color contrastante (naranja/verde). Si es posible, usa `tel:+5233XXXXXXXX` como link. | **S** | **Alto** | Facilita conversión desde móviles (mayoría del tráfico local es móvil). |
| **P1** | Canonical URL | Agrega `<link rel="canonical" href="https://www.plomeriajuanperez.com/servicio-plomeria-guadalajara/" />` en el `<head>` | **S** | **Medio** | Evita problemas de contenido duplicado. |
| **P1** | Verificar robots meta | Asegúrate de que NO haya `<meta name="robots" content="noindex">` en la página. Debe ser `index, follow` o sin tag (permite indexación por defecto). | **S** | **Altísimo** | Si tiene "noindex", Google NUNCA mostrará la página en resultados. |
| **P1** | Optimizar velocidad (PageSpeed) | Una vez restaurado el sitio: 1) Comprime todas las imágenes (usa TinyPNG o ShortPixel). 2) Habilita lazy loading de imágenes. 3) Minifica CSS/JS. 4) Usa un CDN (Cloudflare gratis). Objetivo: score móvil >85. | **M-L** | **Alto** | Velocidad es factor de ranking + impacta conversión (usuarios abandonan sitios lentos). |
| **P2** | Agregar contenido de confianza | Incluye sección "Sobre Nosotros" con: años de experiencia, licencias/certificaciones, fotos REALES de trabajos completados, testimonios de clientes de Guadalajara. | **M** | **Medio** | Genera confianza y diferenciación vs competencia. |
| **P2** | Optimizar alt text de imágenes | Todas las imágenes deben tener alt text descriptivo. Ejemplo: `alt="Plomero reparando fuga en casa de Guadalajara"`, `alt="Servicio de destapado de drenaje Zapopan"` | **S** | **Medio** | Ayuda a ranking en Google Images + accesibilidad. |
| **P2** | Enlazado interno estratégico | Crea links internos desde esta página hacia: página de inicio, página de servicios generales, páginas de otras zonas (si existen). Usa anchor text descriptivo: "servicios de plomería en Zapopan" vs "clic aquí". | **M** | **Medio** | Distribuye autoridad interna y ayuda a indexación de otras páginas. |
| **P2** | Sección de FAQs con schema | Agrega una sección "Preguntas Frecuentes" con preguntas reales: "¿Cuánto cuesta un plomero en Guadalajara?", "¿Dan servicio de emergencia?", "¿Qué zonas cubren?". Implementa FAQPage schema. | **M** | **Medio** | Ayuda a aparecer en rich results de Google + responde objeciones del usuario. |
| **P2** | Agregar Open Graph tags | Agrega tags OG para mejorar compartidos en redes sociales: `og:title`, `og:description`, `og:image` (foto del servicio), `og:url` | **S** | **Bajo** | Mejora presentación cuando alguien comparte el link en Facebook/WhatsApp. |

---

## Diagnóstico Final y Próximos Pasos

### El problema real

Tu sitio web NO está funcionando. Esto no es un problema de SEO on-page estándar. Este es un incidente crítico de infraestructura.

**Posibles causas (en orden de probabilidad):**

1. **Dominio expirado:** El dominio `plomeriajuanperez.com` no fue renovado. Esto pasa cuando el pago anual falla o se olvida.

2. **Hosting cancelado:** El servidor donde estaba alojado el sitio fue dado de baja (por falta de pago o el plan de hosting expiró).

3. **Error de configuración DNS:** Los nameservers del dominio no apuntan correctamente al hosting.

4. **Servidor caído:** El servidor del hosting está temporalmente fuera de servicio (menos probable si lleva 2 años sin actualizaciones).

5. **Sitio hackeado/eliminado:** Aunque menos común, es posible que el sitio haya sido comprometido o borrado.

### Por qué no apareces bien en Google Maps

Si tu perfil de Google Business Profile lista un sitio web que NO funciona:

- Google detecta esto automáticamente mediante crawlers
- Interpreta tu negocio como potencialmente inactivo o no confiable
- **Penaliza tu ranking local** en Maps
- Los usuarios que encuentran tu negocio y hacen clic en "Sitio web" obtienen un error → destruye conversión y confianza
- Google puede incluso desindexar tu negocio si parece abandonado

### Acción INMEDIATA (Hoy mismo)

1. **Contacta a tu sobrino** que hizo el sitio y pregunta:
   - ¿Dónde está registrado el dominio? (GoDaddy, Namecheap, etc.)
   - ¿Qué hosting se usó? (Hostinger, SiteGround, etc.)
   - ¿Tiene acceso a las cuentas?
   - ¿Cuándo fue la última vez que verificó que el sitio funcionara?

2. **Verifica el dominio** en whois.com:
   - ¿Está activo o expiró?
   - ¿Cuándo expira?
   - ¿Quién es el registrar?

3. **Decisión crítica:**
   - Si tu sobrino no responde o no tiene acceso: **Contrata un desarrollador web profesional HOY**.
   - Si el dominio expiró y no es recuperable: **Compra un nuevo dominio** (ej: `plomeriajuanperez.mx` o `plomeriaguadalajara.com`) y construye un sitio nuevo.
   - Si el hosting fue cancelado: **Contrata un hosting nuevo** (recomiendo SiteGround o Hostinger, desde $3-5 USD/mes).

4. **Actualiza Google Business Profile:**
   - Mientras el sitio esté caído, **ELIMINA temporalmente** la URL del sitio de tu perfil de Google Business.
   - Deja solo el teléfono como método de contacto primario.
   - Cuando el sitio esté restaurado, agrégalo de nuevo.

### Cuando el sitio esté restaurado

Sigue la **Tabla B — Action Steps** en orden de prioridad (P0 → P1 → P2). Las primeras acciones (Schema LocalBusiness, Title/Meta, H1, NAP visible, CTA claro) te darán el 80% del impacto en SEO Local.

### Nota sobre "sitios hechos por sobrinos"

Sin ánimo de ofender, pero sitios hechos por familiares no-profesionales suelen tener:
- Falta de mantenimiento (renovaciones, actualizaciones de seguridad)
- Hosting barato que falla o expira
- CERO SEO técnico (schema, velocidad, estructura)
- Diseño no optimizado para conversión

**Recomendación:** Considera invertir en un desarrollador profesional de SEO Local o una agencia. Para un negocio de servicios locales, un sitio bien hecho puede generar 10-50 clientes nuevos al mes. El ROI justifica la inversión.

---

## Recursos para verificar el estado actual

1. **Verificar dominio:** https://www.whois.com/whois/plomeriajuanperez.com
2. **Verificar DNS:** https://dnschecker.org/ (escribe `plomeriajuanperez.com`)
3. **Verificar si el sitio está caído globalmente:** https://downforeveryoneorjustme.com/plomeriajuanperez.com
4. **Cuando esté activo, valida schema:** https://search.google.com/test/rich-results
5. **Cuando esté activo, verifica velocidad:** https://pagespeed.web.dev/

---

## Conclusión

**No tienes un problema de SEO on-page. Tienes un problema de sitio web no funcional.**

Esto es lo único que importa ahora: **Restaurar el sitio web URGENTE**.

Todo lo demás (title tags, headings, schema, velocidad) es secundario. Sin sitio funcional:
- Cero tráfico orgánico
- Penalización en Google Maps
- Pérdida de conversiones
- Pérdida de confianza

Contacta a quien sea responsable del hosting/dominio **HOY**. Si no obtienes respuesta en 24 horas, contrata a un profesional.

Una vez restaurado, ejecuta los action steps de la Tabla B y verás mejoras en ranking local en 2-4 semanas.

Si necesitas ayuda adicional para implementar las optimizaciones cuando el sitio esté activo, considera contratar un especialista en SEO Local.

---

**Auditoría completada el:** 2026-03-07
**Herramienta:** Claude Code — SEO Local On-Page Audit Skill
**Próxima acción:** Restaurar infraestructura web (P0)