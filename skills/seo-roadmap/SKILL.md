---
name: seo-roadmap
description: >
  Consolida los resultados de todos los audits SEO en un roadmap priorizado
  y lo exporta como PDF profesional. Úsalo después de correr los audits
  (gbp-audit, gbm-audit, onpage-audit, schema-audit, rankability-test)
  para obtener el plan de acción definitivo listo para entregar al cliente.
---

# SEO Roadmap — Plan de Acción Consolidado

Eres un consultor senior de SEO Local. Recibes resultados de múltiples auditorías y los conviertes en un plan de acción unificado, priorizado y exportado como PDF profesional listo para entregar al cliente.

**Inputs requeridos:**
- Resultados de al menos uno de estos audits: on-page, schema, rankability, gbp-audit, gbm-audit
- Nombre del negocio o dominio
- Keyword objetivo

Si el usuario corre este skill directamente (sin venir del skill `audit`), pídele que pegue los resultados de sus auditorías previas antes de continuar.

---

## PASO 1 — Consolidar todos los findings

Toma TODOS los action items de TODAS las auditorías recibidas. Elimina duplicados. Unifica en una sola tabla maestra:

| ID | Área | Hallazgo | Acción concreta | Impacto | Esfuerzo | Fuente |
|----|------|----------|----------------|---------|----------|--------|

- **Área:** On-Page / Schema / Rankability / GBP / Competidores
- **Impacto:** Alto / Medio / Bajo
- **Esfuerzo:** S (<1h) / M (1 día) / L (>1 día)
- **Fuente:** audit que lo detectó

---

## PASO 2 — Matriz de priorización

Clasifica todos los items en 4 cuadrantes:

| Cuadrante | Criterio | Qué hacer |
|-----------|---------|-----------|
| 🚀 Quick Wins | Alto impacto + Esfuerzo S o M | Ejecutar en las próximas 2 semanas |
| 🎯 Proyectos estratégicos | Alto impacto + Esfuerzo L | Planear con recursos y fecha |
| ⚡ Fill-ins | Bajo impacto + Esfuerzo S | Cuando haya tiempo libre |
| ❌ Reconsiderar | Bajo impacto + Esfuerzo L | Postergar o descartar |

---

## PASO 3 — Plan de acción 30 / 60 / 90 días

### Días 1-30 — Quick Wins + Correcciones Críticas
Lista todas las tareas del cuadrante "Quick Wins" más todos los items P0.
Para cada tarea: acción exacta, responsable sugerido (dueño / dev / agencia), resultado esperado.

### Días 31-60 — Proyectos Estratégicos
Items de alto impacto que requieren más tiempo o recursos.
Para cada proyecto: descripción del trabajo, dependencias, resultado esperado.

### Días 61-90 — Optimización + Medición
Items restantes + KPIs a revisar al finalizar los 90 días:
- Posición en Maps para la keyword objetivo
- Tráfico orgánico (Google Search Console)
- Score de completitud GBP
- Velocidad de página (PageSpeed mobile)

---

## PASO 4 — Generar archivo HTML

Crea un archivo llamado `seo-roadmap-[dominio]-[YYYYMMDD].html` en el directorio de trabajo actual.

El HTML debe tener esta estructura y estilos exactos:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SEO Roadmap — [NEGOCIO]</title>
<style>
  /* Reset y base */
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', system-ui, -apple-system, sans-serif; background: #F8FAFC; color: #0F172A; font-size: 14px; line-height: 1.6; }

  /* Header */
  .header { background: #0F172A; color: white; padding: 40px 48px; }
  .header h1 { font-size: 28px; font-weight: 700; margin-bottom: 4px; }
  .header .meta { color: #94A3B8; font-size: 13px; }
  .header .keyword { display: inline-block; background: #2563EB; color: white; padding: 3px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-top: 8px; }

  /* Contenedor principal */
  .container { max-width: 1100px; margin: 0 auto; padding: 40px 48px; }

  /* Sección */
  .section { margin-bottom: 48px; }
  .section-title { font-size: 18px; font-weight: 700; color: #0F172A; border-left: 4px solid #2563EB; padding-left: 12px; margin-bottom: 20px; }

  /* Tarjetas de resumen ejecutivo */
  .summary-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
  .summary-card { background: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 20px; }
  .summary-card .label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: #64748B; letter-spacing: 0.5px; margin-bottom: 6px; }
  .summary-card .value { font-size: 24px; font-weight: 700; color: #0F172A; }
  .summary-card .sub { font-size: 12px; color: #64748B; margin-top: 4px; }

  /* Tablas */
  table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; border: 1px solid #E2E8F0; margin-bottom: 24px; }
  th { background: #F1F5F9; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #475569; padding: 12px 16px; text-align: left; }
  td { padding: 12px 16px; border-top: 1px solid #F1F5F9; vertical-align: top; }
  tr:nth-child(even) td { background: #FAFAFA; }

  /* Badges de prioridad */
  .badge { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
  .p0 { background: #FEE2E2; color: #DC2626; }
  .p1 { background: #FEF3C7; color: #D97706; }
  .p2 { background: #E0F2FE; color: #0284C7; }

  /* Badges de impacto */
  .alto { background: #D1FAE5; color: #059669; }
  .medio { background: #DBEAFE; color: #2563EB; }
  .bajo { background: #F1F5F9; color: #64748B; }

  /* Cuadrantes de matriz */
  .matrix-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .quadrant { background: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 20px; }
  .quadrant h3 { font-size: 14px; font-weight: 700; margin-bottom: 12px; }
  .quadrant ul { list-style: none; }
  .quadrant li { padding: 4px 0; font-size: 13px; color: #334155; border-bottom: 1px solid #F8FAFC; }
  .quadrant li:last-child { border-bottom: none; }
  .q-quickwins { border-top: 4px solid #10B981; }
  .q-strategic { border-top: 4px solid #2563EB; }
  .q-fillin { border-top: 4px solid #F59E0B; }
  .q-reconsider { border-top: 4px solid #94A3B8; }

  /* Plan 30/60/90 */
  .plan-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }
  .plan-col { background: white; border: 1px solid #E2E8F0; border-radius: 10px; overflow: hidden; }
  .plan-col-header { padding: 16px 20px; font-weight: 700; font-size: 14px; color: white; }
  .plan-col-header.d30 { background: #2563EB; }
  .plan-col-header.d60 { background: #7C3AED; }
  .plan-col-header.d90 { background: #0891B2; }
  .plan-col-body { padding: 16px 20px; }
  .plan-item { padding: 10px 0; border-bottom: 1px solid #F1F5F9; }
  .plan-item:last-child { border-bottom: none; }
  .plan-item .task { font-weight: 600; font-size: 13px; color: #0F172A; margin-bottom: 3px; }
  .plan-item .result { font-size: 12px; color: #64748B; }

  /* Footer */
  .footer { background: #0F172A; color: #64748B; text-align: center; padding: 24px; font-size: 12px; margin-top: 60px; }
  .footer span { color: #2563EB; font-weight: 600; }

  /* Print */
  @media print {
    body { background: white; }
    .header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .plan-col-header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  }
</style>
</head>
<body>

<div class="header">
  <h1>[NOMBRE DEL NEGOCIO]</h1>
  <div class="meta">SEO Local Roadmap — Generado el [FECHA]</div>
  <div class="keyword">[KEYWORD]</div>
</div>

<div class="container">

  <!-- Resumen Ejecutivo -->
  <div class="section">
    <div class="section-title">Resumen Ejecutivo</div>
    <div class="summary-grid">
      <div class="summary-card">
        <div class="label">Score GBP</div>
        <div class="value">[X]/100</div>
        <div class="sub">Google Business Profile</div>
      </div>
      <div class="summary-card">
        <div class="label">Rankability</div>
        <div class="value">[VEREDICTO CORTO]</div>
        <div class="sub">[keyword]</div>
      </div>
      <div class="summary-card">
        <div class="label">Issues Críticos (P0)</div>
        <div class="value">[X]</div>
        <div class="sub">Requieren acción inmediata</div>
      </div>
      <div class="summary-card">
        <div class="label">Quick Wins</div>
        <div class="value">[X]</div>
        <div class="sub">Alto impacto, bajo esfuerzo</div>
      </div>
    </div>
  </div>

  <!-- Tabla maestra de findings -->
  <div class="section">
    <div class="section-title">Todos los Hallazgos</div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Área</th>
          <th>Hallazgo</th>
          <th>Acción concreta</th>
          <th>Impacto</th>
          <th>Esfuerzo</th>
        </tr>
      </thead>
      <tbody>
        <!-- [INSERTAR FILAS GENERADAS DINÁMICAMENTE] -->
        <!-- Ejemplo de fila:
        <tr>
          <td>#1</td>
          <td>On-Page</td>
          <td>Title tag no contiene ciudad</td>
          <td>Reescribir title: "Plomero en Guadalajara | Servicio 24h | García"</td>
          <td><span class="badge alto">Alto</span></td>
          <td>S</td>
        </tr>
        -->
      </tbody>
    </table>
  </div>

  <!-- Matriz de priorización -->
  <div class="section">
    <div class="section-title">Matriz de Priorización</div>
    <div class="matrix-grid">
      <div class="quadrant q-quickwins">
        <h3>🚀 Quick Wins — Hacer ahora</h3>
        <ul>
          <!-- [INSERTAR ITEMS DEL CUADRANTE] -->
        </ul>
      </div>
      <div class="quadrant q-strategic">
        <h3>🎯 Proyectos Estratégicos — Planear</h3>
        <ul>
          <!-- [INSERTAR ITEMS DEL CUADRANTE] -->
        </ul>
      </div>
      <div class="quadrant q-fillin">
        <h3>⚡ Fill-ins — Cuando haya tiempo</h3>
        <ul>
          <!-- [INSERTAR ITEMS DEL CUADRANTE] -->
        </ul>
      </div>
      <div class="quadrant q-reconsider">
        <h3>❌ Reconsiderar — Postergar</h3>
        <ul>
          <!-- [INSERTAR ITEMS DEL CUADRANTE] -->
        </ul>
      </div>
    </div>
  </div>

  <!-- Plan 30/60/90 -->
  <div class="section">
    <div class="section-title">Plan de Acción 30 / 60 / 90 Días</div>
    <div class="plan-grid">
      <div class="plan-col">
        <div class="plan-col-header d30">Días 1–30 · Quick Wins</div>
        <div class="plan-col-body">
          <!-- [INSERTAR TAREAS DEL PRIMER MES] -->
        </div>
      </div>
      <div class="plan-col">
        <div class="plan-col-header d60">Días 31–60 · Proyectos</div>
        <div class="plan-col-body">
          <!-- [INSERTAR TAREAS DEL SEGUNDO MES] -->
        </div>
      </div>
      <div class="plan-col">
        <div class="plan-col-header d90">Días 61–90 · Optimización</div>
        <div class="plan-col-body">
          <!-- [INSERTAR TAREAS DEL TERCER MES + KPIs] -->
        </div>
      </div>
    </div>
  </div>

</div>

<div class="footer">
  Generado por <span>SEO Local Audit</span> · [FECHA] · Para uso interno y de cliente
</div>

</body>
</html>
```

**Instrucción:** Completa el HTML reemplazando TODOS los placeholders con los datos reales de las auditorías. Inserta las filas de tabla, los items de los cuadrantes y las tareas del plan 30/60/90 con el contenido real. Guarda el archivo.

---

## PASO 5 — Convertir HTML a PDF

Ejecuta el siguiente script Python para convertir el HTML a PDF. Guarda el script como `generate_pdf.py` y ejecútalo:

```python
import subprocess
import sys
import os

html_file = "seo-roadmap-[dominio]-[fecha].html"  # Usa el nombre real del archivo generado
pdf_file = html_file.replace(".html", ".pdf")
html_path = os.path.abspath(html_file)
pdf_path = os.path.abspath(pdf_file)

print(f"Convirtiendo {html_file} a PDF...")

# Método 1: Chrome headless (más confiable en Windows/Mac/Linux)
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Users\{}\AppData\Local\Google\Chrome\Application\chrome.exe".format(os.environ.get("USERNAME", "")),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/usr/bin/chromium",
]

chrome_found = False
for chrome_path in chrome_paths:
    if os.path.exists(chrome_path):
        try:
            result = subprocess.run([
                chrome_path,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                f"--print-to-pdf={pdf_path}",
                f"file:///{html_path}"
            ], capture_output=True, timeout=30)
            if result.returncode == 0 and os.path.exists(pdf_path):
                print(f"✅ PDF generado con Chrome: {pdf_path}")
                chrome_found = True
                break
        except Exception as e:
            continue

if not chrome_found:
    # Método 2: weasyprint
    try:
        import weasyprint
        weasyprint.HTML(filename=html_path).write_pdf(pdf_path)
        print(f"✅ PDF generado con weasyprint: {pdf_path}")
    except ImportError:
        print("Instalando weasyprint...")
        subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint"], check=True)
        import weasyprint
        weasyprint.HTML(filename=html_path).write_pdf(pdf_path)
        print(f"✅ PDF generado con weasyprint: {pdf_path}")
    except Exception as e:
        # Método 3: abrir en navegador para impresión manual
        print(f"⚠️  No se pudo generar el PDF automáticamente.")
        print(f"Abre este archivo en Chrome y usa Ctrl+P → Guardar como PDF:")
        print(f"  {html_path}")
        try:
            os.startfile(html_path)  # Windows
        except:
            subprocess.run(["open", html_path])  # Mac
```

Una vez que el PDF se genere exitosamente, reporta al usuario:

```
✅ SEO Roadmap listo.

📄 HTML: seo-roadmap-[dominio]-[fecha].html
📋 PDF:  seo-roadmap-[dominio]-[fecha].pdf

El roadmap incluye:
- [X] hallazgos consolidados de [N] auditorías
- [X] quick wins para ejecutar en los primeros 30 días
- Plan de acción completo para 90 días
```

Si el PDF falla pero el HTML está listo, indícale al usuario que abra el HTML en Chrome y use Ctrl+P → "Guardar como PDF".

---

**Reglas:**
- No omitas ningún finding de las auditorías recibidas.
- Cada tarea en el roadmap debe ser accionable y específica — nada vago.
- Prioriza por impacto real en ranking, no por facilidad.
- El PDF es un entregable profesional para el cliente — cuida la presentación.
