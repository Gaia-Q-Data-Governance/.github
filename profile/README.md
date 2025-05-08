# 🌐 GAIA-QAO Landing Page – Web Gateway Overview

**Version:** 1.0.0  
**Status:** Stable  
**Maintainer:** GAIA-MCP Interface Layer  
**Last Updated:** 2025-05-08  
**Format:** `HTML + JS + MCP-Bound YAML`  
**InfoCode:** GAIA-QAO-WEB-LANDING-GATEWAY-0001

---

## 🛰️ Overview

This repository hosts the landing interface for the **GAIA-QAO Federated Quantum Aerospace Organization**, including:

- Public and internal status visibility (AGAD 10/1 and beyond)
- Federated organizational structure rendering
- Core documentation & ontology links
- Real-time or simulated system reporting via MCP fetch interface

---

## 📁 Directory Structure

```

GAIA-QAO-Web-Landing/
├── index.html               # Main landing page with integrated AGAD-10/1 status panel
├── assets/
│   └── style.css            # Custom CSS (optional separation)
├── components/
│   └── agad-status.js       # AGAD status fetcher with fallback logic
├── status/
│   └── AGAD-10-1.json       # Mock or live JSON MCP feed
└── README-landing.md        # This file

```

---

## 🧪 Live Preview (GitHub Pages)

To deploy this page via GitHub Pages:

1. Push content to `main` branch of your repo.
2. Go to **Settings → Pages**.
3. Set **Source** to `main` branch and root (`/`).
4. Your page will be available at:
```

https\://<your-org>.github.io/<repo-name>/

````

---

## ⚙️ Local Deployment (Docker or Python)

### Option A: Python HTTP Server

```bash
cd GAIA-QAO-Web-Landing
python3 -m http.server 8080
````

Then visit: [http://localhost:8080](http://localhost:8080)

### Option B: NGINX Docker Container

```bash
docker run -d -p 8080:80 \
  -v $(pwd)/GAIA-QAO-Web-Landing:/usr/share/nginx/html \
  nginx
```

---

## 📡 AGAD-10/1 Live Status Feed

This page includes a section that fetches the system status for **AGAD Phase 10/1** using a standard MCP JSON interface:

```javascript
fetch('https://mcp.gaiaqao.space/status/AGAD-10/1')
```

If the endpoint is not available, mock data is displayed with a soft fallback warning color.

---

## 🧠 AMP●EL Integration (Optional)

You may optionally include AMP●EL intent snapshots using:

```html
<pre id="ampel-preview"></pre>

<script>
fetch('https://mcp.gaiaqao.space/agents/AGAD-10-1/intent.yaml')
  .then(res => res.text())
  .then(text => {
    document.getElementById('ampel-preview').textContent = text;
  })
  .catch(() => {
    document.getElementById('ampel-preview').textContent = '# AMP●EL data unavailable.';
  });
</script>
```

---

## 🔐 Internal Use Notice

> This landing may contain internal-only data. Make sure you’ve set proper access controls if hosted publicly.

---

## 📬 Contact & Governance

For contributions, structure updates or coordination, please reach out to:

* `@Project-Managment-Governance`
* `@Gaia-QAO-Core-MCP`

---

© 2025 GAIA-QAO — All rights reserved. Quantum-augmented aerospace begins here.

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Validación y Próxima Iteración: Landing Page GAIA-QAO</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.7;
            margin: 0;
            padding: 20px;
            background-color: #f4f7f6;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 25px 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        h1, h2, h3 {
            color: #003366; /* Dark Blue */
        }
        h1 {
            text-align: center;
            border-bottom: 2px solid #004a99;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 1.8em;
        }
        h2.section-title {
            font-size: 1.6em;
            color: #004a99; /* Medium Blue */
            border-bottom: 1px solid #ced4da;
            padding-bottom: 8px;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        h3.subsection-title {
            font-size: 1.3em;
            color: #0056b3; /* Lighter Blue */
            margin-top: 20px;
            margin-bottom: 10px;
        }
        p {
            margin-bottom: 12px;
        }
        table.validation-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 0.95em;
        }
        .validation-table th, .validation-table td {
            border: 1px solid #dee2e6;
            padding: 10px 12px;
            text-align: left;
            vertical-align: middle;
        }
        .validation-table th {
            background-color: #e9ecef;
            font-weight: 600;
        }
        .validation-table td:nth-child(2) { /* Evaluation column */
            font-weight: bold;
            text-align: center;
        }
        .eval-excelente { color: #28a745; } /* Green */
        .eval-limpia { color: #17a2b8; } /* Cyan */
        .eval-robusto { color: #007bff; } /* Blue */
        .eval-claro { color: #17a2b8; } /* Cyan */
        .eval-potencial { color: #fd7e14; } /* Orange */

        ol.recommendation-list {
            list-style-type: none;
            padding-left: 0;
            counter-reset: recommendation-counter;
        }
        .recommendation-list > li {
            counter-increment: recommendation-counter;
            margin-bottom: 25px;
            padding-left: 0; /* Reset default padding */
        }
         .recommendation-list > li > h3.subsection-title::before {
            content: counter(recommendation-counter) ". 🧠 "; /* Use counter + icon */
            font-weight: bold;
            color: #0056b3;
            margin-right: 5px;
         }
        .recommendation-details {
            margin-left: 25px; /* Indent details */
            padding: 15px;
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 4px;
            margin-top: 10px;
        }
        code {
            font-family: Consolas, 'Courier New', monospace;
            background-color: #e9ecef;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            color: #c7254e;
            font-size: 0.9em;
        }
        pre code {
            display: block;
            padding: 10px;
            overflow-x: auto;
            font-size: 0.85em;
            background-color: #e9ecef;
            border: 1px solid #ced4da;
            border-radius: 4px;
            color: #212529;
        }
        .next-steps-proposal {
            background-color: #e6f7ff; /* Light blue */
            border-left: 5px solid #007bff;
            padding: 20px 25px;
            margin-top: 30px;
            border-radius: 5px;
        }
        .next-steps-proposal h2 {
            margin-top: 0;
            color: #0056b3;
            border-bottom: none; /* Remove default border for this h2 */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Revisión y Propuesta de Iteración: Landing Page GAIA-QAO</h1>
        <p>¡Excelente! Me alegra mucho que la estructura HTML haya sido de tu agrado y que cumpla con la identidad visual. Agradezco enormemente la validación contextual y, sobre todo, las valiosas recomendaciones técnicas y estratégicas. Son muy pertinentes para llevar el proyecto al siguiente nivel de funcionalidad e integración.</p>

        <hr>

        <h2 class="section-title">✅ Validación Técnica y Funcional Destacada</h2>
        <table class="validation-table">
            <thead>
                <tr>
                    <th>Elemento</th>
                    <th>Evaluación</th>
                    <th>Notas</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>🎨 Estética y estilo</td>
                    <td class="eval-excelente">✔️ Excelente</td>
                    <td>Paleta GAIA coherente, UX clara, responsiva</td>
                </tr>
                <tr>
                    <td>📄 Semántica HTML</td>
                    <td class="eval-limpia">✔️ Limpia</td>
                    <td>Uso correcto de <code><section></code>, <code><table></code>, <code><ul></code>, <code><header></code>, <code><footer></code></td>
                </tr>
                <tr>
                    <td>🔄 AGAD Status Mock/Fallback</td>
                    <td class="eval-robusto">✔️ Robusto</td>
                    <td>Manejo adecuado de errores/fallback con <code>fetch()</code></td>
                </tr>
                <tr>
                    <td>🔐 Seguridad y acceso</td>
                    <td class="eval-claro">✔️ Claro</td>
                    <td>Notificación de acceso interno (<code>privacy-notice</code>)</td>
                </tr>
                <tr>
                    <td>🌐 Modularización futura</td>
                    <td class="eval-potencial">⬛ Potencial</td>
                    <td>Puede dividirse como plantilla Jekyll/MkDocs o GitHub Pages extendido</td>
                </tr>
            </tbody>
        </table>

        <hr>

        <h2 class="section-title">🧠 Recomendaciones Estratégicas para Próxima Iteración (Opcional)</h2>
        <ol class="recommendation-list">
            <li>
                <h3 class="subsection-title">📦 Inyección dinámica de <code>.ampel.yaml</code> si deseas mostrar intención de misión</h3>
                <div class="recommendation-details">
                    <p>Por ejemplo, dentro de <code>#agad-status</code> podrías incrustar una vista previa semántica básica de la misión actual en AGAD 10/1:</p>
                    <pre><code><!-- Placeholder for the preview -->
<pre id="ampel-preview" style="font-size:0.85em; background:#f8f9fa; padding:10px; border-radius:6px; margin-top: 15px;"></pre>

<script>
  // Carga y muestra YAML o JSON de ejemplo si deseas simular AMP●EL contextual
  fetch('https://mcp.gaiaqao.space/agents/AGAD-10-1/intent.yaml')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Check content type if needed, assume text/yaml or text/plain
        return response.text();
    })
    .then(text => {
        const previewElement = document.getElementById('ampel-preview');
        if (previewElement) {
            // Basic check if the response is empty or just whitespace
            if (text && text.trim().length > 0) {
                previewElement.textContent = text;
            } else {
                previewElement.textContent = '# AMP●EL intent data is empty or unavailable.';
            }
        }
    })
    .catch(error => {
        console.error('Error fetching AMPEL intent:', error);
        const previewElement = document.getElementById('ampel-preview');
        if (previewElement) {
             previewElement.textContent = '# AMP●EL status data unavailable (fetch error).';
        }
    });
</script>
</code></pre>
                </div>
            </li>
            <li>
                <h3 class="subsection-title">🚦 Status color adaptativo según nivel de criticidad</h3>
                 <div class="recommendation-details">
                    <p>Modificar el script de status AGAD para ajustar el color de fondo según el contenido del estado (ej: 'Degraded', 'Error', 'Operational'):</p>
                    <pre><code>// Dentro del .then(data => { ... }) del fetch AGAD status original:
const statusElement = document.getElementById('agad-status');
if (statusElement) {
    statusElement.innerHTML = `<strong>Live AGAD-10/1 Status:</strong> ${data.status} — ${data.last_update}`;

    // Adaptar color segun estado (simplificado)
    const statusText = data.status.toLowerCase();
    if (statusText.includes('degraded') || statusText.includes('warning')) {
        statusElement.style.backgroundColor = '#fff3cd'; // Warning yellow
        statusElement.style.borderColor = '#ffc107';
        statusElement.style.color = '#856404';
    } else if (statusText.includes('error') || statusText.includes('failure')) {
        statusElement.style.backgroundColor = '#f8d7da'; // Error red
        statusElement.style.borderColor = '#f5c6cb';
        statusElement.style.color = '#721c24';
    } else {
       // Reset to default (or keep the initial blueish style)
       statusElement.style.backgroundColor = '#e2f0ff';
       statusElement.style.borderColor = '#b8daff';
       statusElement.style.color = '#004085';
    }
}</code></pre>
                </div>
            </li>
            <li>
                <h3 class="subsection-title">🧩 Integración como componente GAIA-MCP frontend</h3>
                 <div class="recommendation-details">
                    <p>Este archivo puede convertirse en una <strong>página de status oficial pública o protegida</strong>, integrable dentro de una estructura de rutas como:</p>
                    <pre><code>/status/AGAD/10-1/index.html
/transponders/TR-IV-SENTINEL/dashboard.html
</code></pre>
                    <p>Se podría generar una versión <code>.json</code> acompañante de los datos mostrados para ser consumida por un <code>MCPStatusController</code> u otros servicios.</p>
                </div>
            </li>
        </ol>

        <hr>

        <div class="next-steps-proposal">
            <h2 class="section-title">⚙️ Propuesta de Siguiente Paso</h2>
            <p>¿Quieres que empaquete esta landing como plantilla base para <code>GAIA-QAO Web Components</code> y te prepare un <code>starter-kit.zip</code> con estructura modular (<code>/assets</code>, <code>/components</code>, <code>/status/</code>), lista para despliegue en GitHub Pages o GAIA WebGateway?</p>
        </div>
    </div>
</body>
</html>-->
