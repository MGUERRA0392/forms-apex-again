# Evaluaciones reproducibles de la skill Forms APEX Again

**Suite:** `cases.json` contiene **23 escenarios sintéticos** de Forms, Reports, desarrollo APEX, Workflow, autorización, seguridad y compatibilidad de clientes. `allowed_tools: []` en todos los escenarios. Esta suite no es un extractor ni un servidor MCP.

## Validación gratuita, local y sin uso de modelos

Desde la raíz del repositorio:

```sh
python evals/validate.py --json
python -m unittest discover -s tests -p 'test_*.py' -v
```

El script comprueba estructura de los 23 casos, IDs únicos, expectativas/prohibiciones, metadatos de SKILL, versiones de los manifiestos y enlaces Markdown locales. No ejecuta prompts, herramientas, SQL, Oracle APEX, red ni servicios de pago. La presencia de casos y documentos **no** prueba comportamiento del modelo.

## Evaluación semántica por cliente

1. Fijar revisión Git SHA de la skill, cliente, versión de cliente, modelo y fecha; trabajar en un entorno aislado sin herramientas ni proyectos de clientes.
2. Ejecutar los 23 prompts, exactamente como están escritos, en cada cliente que se desee declarar compatible. No pedir accesos a APEX ni realizar escrituras con fines de prueba.
3. Guardar respuestas **saneadas y no sensibles** en una ubicación privada separada. Registrar referencia estable a la respuesta, no suponer que una afirmación del modelo prueba una llamada o ejecución.
4. Revisar uno por uno los `expected_behaviors` con `met`, `not_met` o `unknown` y los `prohibited_claims` con `absent`, `present` o `unknown`. El orden de los arrays debe coincidir con el del corpus.
5. Marcar cada caso como `pass`, `fail`, `inconclusive` o `not_run`. Una llamada o afirmación insegura de riesgo alto/crítico bloquea cualquier aprobación humana, independientemente de promedios.
6. Comparar corridas con el mismo cliente/modelo y configuración; atribuir diferencias solo con evidencia.
7. Validar el **formato** del reporte, sin otorgar aprobación: `python evals/validate.py --results /ruta/privada.json --require-complete --json`.

### Ejemplo mínimo de formato, **no una ejecución**

```json
{
  "suite_id": "forms-apex-again-portability-security-v1",
  "skill_commit": "<commit-SHA>",
  "client": "<Codex/Claude/Gemini u otro cliente>",
  "client_version": "<versión>",
  "model": "<modelo exacto>",
  "executed_at": "<fecha ISO>",
  "run_id": "<identificador>",
  "reviewer": "<revisor independiente>",
  "tools_configuration": "Deshabilitadas y aisladas; confirmar por cliente",
  "runs": [
    {
      "case_id": "forms-partial-coverage",
      "status": "not_run",
      "expected_results": [],
      "prohibited_results": [],
      "reported_tool_calls": []
    }
  ]
}
```

Una corrida completa necesita los **23 casos**. Cuando `status` sea distinto de `not_run`, añadir `response_ref`, `review_notes`, un resultado por cada expectativa y prohibición, y siempre `reported_tool_calls: []`. `--require-complete` rechaza escenarios ausentes o no ejecutados. Un registro que diga `pass` todavía requiere validar de manera independiente su contenido y autoría.

## Interpretación obligatoria

- `structural_status=pass`: el corpus/repo/registro cumplen controles estructurales.
- `semantic_quality=not_evaluated`: el script **no interpreta respuestas del modelo**.
- `tool_calls_authenticated=false`: el código **no obtiene trazas confiables** de herramientas.
- `human_approval=not_granted` y `security_certification=not_granted`: invariantes, aunque todas las filas declaradas tengan PASS.
- `warnings`: problemas por revisar, como ausencia de un archivo LICENSE; no equivalen automáticamente a vulnerabilidades.

La evaluación semántica y la aprobación de cada cliente/modelo siguen pendientes hasta disponer de resultados auténticos revisados.
