"""
Script to automatically grade assertions for onpage-audit benchmark.
Checks objective, verifiable criteria from the eval outputs.
"""

import json
import re
from pathlib import Path

def grade_audit_report(report_path, assertions):
    """Grade a single audit report against assertions."""

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    results = []

    for assertion in assertions:
        name = assertion['name']
        passed = False
        evidence = ""

        # Check each assertion type
        if "Resumen inicial de 5 bullets" in name:
            # Look for 5 numbered points near the start
            summary_section = content[:2000]  # First 2000 chars
            numbered_points = re.findall(r'^\d+\.\s+\*\*', summary_section, re.MULTILINE)
            bullet_points = re.findall(r'^[•\-\*]\s+', summary_section, re.MULTILINE)
            passed = len(numbered_points) >= 5 or len(bullet_points) >= 5
            evidence = f"Found {len(numbered_points)} numbered points and {len(bullet_points)} bullet points in first 2000 chars"

        elif "Tabla de Findings existe" in name:
            passed = "Tabla A" in content or "## Findings" in content or ("Área auditada" in content and "Prioridad" in content)
            evidence = "Found Findings table markers" if passed else "No Findings table markers found"

        elif "Cobertura mínima" in name:
            required_areas = ['title', 'meta description', 'H1', 'heading', 'local', 'NAP',
                            'contenido', 'enlace', 'imagen', 'schema', 'canonical', 'PageSpeed', 'CTA']
            found_areas = sum(1 for area in required_areas if area.lower() in content.lower())
            passed = found_areas >= 10
            evidence = f"Found {found_areas}/13 required audit areas mentioned"

        elif "Tabla de Action Steps" in name:
            passed = "Tabla B" in content or "## Action" in content or ("Prioridad" in content and "Esfuerzo" in content and "Impacto" in content)
            evidence = "Found Action Steps table markers" if passed else "No Action Steps table markers found"

        elif "Estados correctos" in name:
            # Check if using correct states
            valid_states = ['Correcto', 'Incorrecto', 'Necesita mejora', 'Desconocido']
            has_valid = any(state in content for state in valid_states)
            # Check for invalid states (this is a heuristic)
            passed = has_valid
            evidence = "Uses valid status terms" if passed else "No valid status terms found"

        elif "Priorización P0/P1/P2" in name:
            p0_count = content.count('P0')
            p1_count = content.count('P1')
            p2_count = content.count('P2')
            passed = (p0_count + p1_count + p2_count) >= 5
            evidence = f"Found P0: {p0_count}, P1: {p1_count}, P2: {p2_count} priority markers"

        elif "Esfuerzo e impacto" in name:
            # Check for S/M/L effort and Bajo/Medio/Alto impact
            effort_pattern = r'\b[SML]\b'
            impact_pattern = r'Bajo|Medio|Alto'
            effort_count = len(re.findall(effort_pattern, content))
            impact_count = len(re.findall(impact_pattern, content))
            passed = effort_count >= 3 and impact_count >= 3
            evidence = f"Found {effort_count} effort markers (S/M/L) and {impact_count} impact markers"

        elif "Evidencia específica" in name:
            # Look for quoted snippets, code blocks, or specific data
            quotes = len(re.findall(r'[""""].*?[""""]', content))
            code_blocks = len(re.findall(r'```', content))
            specific_data = len(re.findall(r'\d+\s*(caracteres|pixels|ms|segundos|%)', content))
            passed = (quotes + code_blocks + specific_data) >= 10
            evidence = f"Found {quotes} quotes, {code_blocks//2} code blocks, {specific_data} specific metrics"

        elif "Recomendaciones accionables" in name:
            # Look for code blocks, exact text examples
            code_blocks = len(re.findall(r'```', content)) // 2
            passed = code_blocks >= 2
            evidence = f"Found {code_blocks} code blocks with specific recommendations"

        elif "Desconocido" in name:
            desconocido_count = content.count('Desconocido')
            no_disponible = content.count('No disponible') + content.count('no disponible')
            passed = (desconocido_count + no_disponible) >= 1 or "no carga" in content.lower()
            evidence = f"Found {desconocido_count} 'Desconocido' + {no_disponible} 'No disponible' markers, indicating honest reporting of limitations"

        results.append({
            "text": name,
            "passed": passed,
            "evidence": evidence
        })

    return results

def main():
    iteration_dir = Path(__file__).parent

    # Grade all eval runs
    eval_dirs = ['plomero-guadalajara', 'dentista-monterrey', 'restaurante-queretaro']
    configs = ['with_skill', 'without_skill']

    for eval_name in eval_dirs:
        eval_dir = iteration_dir / eval_name

        # Load metadata with assertions
        with open(eval_dir / 'eval_metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        assertions = metadata['assertions']

        for config in configs:
            report_path = eval_dir / config / 'outputs' / 'audit_report.md'

            if not report_path.exists():
                print(f"[WARN] Report not found: {report_path}")
                continue

            # Grade the report
            results = grade_audit_report(report_path, assertions)

            # Calculate pass rate
            passed = sum(1 for r in results if r['passed'])
            total = len(results)
            pass_rate = passed / total if total > 0 else 0

            # Save grading results
            grading_data = {
                "eval_name": eval_name,
                "configuration": config,
                "pass_rate": pass_rate,
                "passed": passed,
                "total": total,
                "expectations": results
            }

            grading_path = eval_dir / config / 'grading.json'
            with open(grading_path, 'w', encoding='utf-8') as f:
                json.dump(grading_data, f, indent=2, ensure_ascii=False)

            print(f"[OK] {eval_name}/{config}: {passed}/{total} assertions passed ({pass_rate:.1%})")

if __name__ == '__main__':
    main()
