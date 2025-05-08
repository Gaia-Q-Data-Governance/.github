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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ICY Code Decision Flowchart - AMPEL BWB Project</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
            color: #343a40;
        }
        .container {
            max-width: 960px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 25px 35px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        h1, h2, h3, h4 {
            color: #003366; /* Dark Blue */
        }
        h1 {
            text-align: center;
            border-bottom: 2px solid #004a99;
            padding-bottom: 10px;
            margin-bottom: 30px;
            font-size: 1.8em;
        }
         h2 {
            font-size: 1.5em;
            color: #004a99; /* Medium Blue */
            border-bottom: 1px solid #ced4da;
            padding-bottom: 8px;
            margin-top: 35px;
            margin-bottom: 20px;
        }
         h3 {
            font-size: 1.25em;
            color: #0056b3; /* Lighter Blue */
            margin-top: 25px;
            margin-bottom: 10px;
        }
         h4 {
            font-size: 1.1em;
            color: #0069d9; /* Slightly brighter blue */
            margin-top: 15px;
            margin-bottom: 5px;
        }
        p {
            margin-bottom: 15px;
        }
        .disclaimer {
            background-color: #fff3cd; /* Warning yellow */
            border-left: 5px solid #ffeeba;
            padding: 15px 20px;
            margin-bottom: 30px;
            border-radius: 5px;
            color: #856404;
        }
        .disclaimer strong {
            color: #856404;
            font-weight: bold;
        }
        /* Mermaid diagram container styling */
        .mermaid-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            background-color: #fdfdfd;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            overflow-x: auto; /* Add scroll for very wide diagrams */
            margin-bottom: 25px;
        }
        /* Basic styling for lists */
        ul, ol {
            margin-left: 20px;
            margin-bottom: 15px;
        }
        li {
            margin-bottom: 8px;
        }
        ul li ul { /* Indent nested lists */
            margin-top: 8px;
            margin-left: 25px;
        }
        /* Code block styling */
        pre {
            background-color: #e9ecef;
            border: 1px solid #ced4da;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto; /* Enable horizontal scrolling for long lines */
            font-family: Consolas, 'Courier New', monospace;
            font-size: 0.9em;
            color: #212529;
            margin-bottom: 20px;
        }
        code { /* Inline code style */
            font-family: Consolas, 'Courier New', monospace;
            background-color: rgba(27, 31, 35, 0.05);
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-size: 85%;
        }
        pre code { /* Reset specific styles for code within pre */
             background-color: transparent;
             padding: 0;
             border-radius: 0;
             font-size: inherit;
        }
         strong {
             font-weight: 600;
         }

    </style>
    <!-- Include Mermaid JS library -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
    <div class="container">

        <h1>ICY Code Decision Flowchart for AMPEL BWB Project</h1>

        <div class="disclaimer">
            <strong>DISCLAIMER: GenAI Proposal Status</strong><br>
            This document was generated with AI assistance and represents a proposed decision flowchart for ICY code selection for GAIA Quantum Aerospace Organization (GAIA-QAO). The content is subject to review, modification, and approval by authorized stakeholders.
        </div>

        <h2>Introduction</h2>
        <p>Thank you for your analysis of the Expanded ICY Codes Reference Table. Based on your feedback highlighting the importance of this system for integrating revolutionary technologies, ensuring regulatory compliance, managing sustainability, and future-proofing the AMPEL BWB Quantum Embarked aircraft project, I've developed a decision flowchart to guide engineers in selecting the appropriate ICY code.</p>
        <p>This flowchart will help standardize the decision-making process across engineering teams and ensure consistent application of the expanded ICY codes system.</p>

        <h2>ICY Code Selection Flowchart</h2>
        <div class="mermaid-container">
            <pre class="mermaid">
graph TD
    A[Start ICY Code Selection] --> B{What is the technology domain?};
    B -- Conventional Systems --> C{Are parts fully interchangeable?};
    B -- Quantum Systems --> D{What is the quantum relationship?};
    B -- Sustainable Systems --> E{What is the sustainability aspect?};

    C -- Yes --> F(100: Fully interchangeable);
    C -- No --> G{Are there any conditions?};
    C -- Partially --> H{What is the limitation type?};

    G -- Yes --> I{What are the conditions?};
    G -- No --> J(600-699: Not interchangeable<br/>codes);

    I -- Inspection required --> K(110: Interchangeable after<br/>inspection);
    I -- Documentation update --> L(120: Interchangeable with<br/>documentation update);
    I -- Software/firmware update --> M(130: Interchangeable with<br/>software/firmware update);
    I -- Other conditions --> N(140-190: Other conditional<br/>interchangeability);

    H -- Functional limitations --> O(400-499: Partial interchangeability<br/>codes);
    H -- Assembly considerations --> P(500-599: Assembly<br/>interchangeability codes);

    C -- "One-way" --> Q{Is there one-way compatibility?};
    Q -- Yes --> R(300-399: One-way<br/>interchangeable codes);
    Q -- No --> J; % Back to non-interchangeable if not one-way

    D -- Quantum-Classical --> S{What is the compatibility direction?};
    D -- Quantum Hardware --> T(720-739: Quantum hardware<br/>interchangeability codes);
    D -- Quantum Software --> U(740-759: Quantum software<br/>interchangeability codes);
    D -- Quantum-Quantum --> V(760-779: Quantum-quantum<br/>interchangeability codes);
    D -- Quantum Integration --> W(780-799: Quantum integration<br/>interchangeability codes);

    S -- Bidirectional --> X(700: Quantum-classical<br/>interchangeable);
    S -- Classical to Quantum only --> Y(701: Classical-to-quantum one-way<br/>interchangeable);
    S -- With adaptation --> Z(702-708: Quantum-classical with<br/>adaptation codes);
    S -- Not compatible --> AA(709: Quantum-classical not<br/>interchangeable);

    E -- Materials --> BB(800-819: Sustainable materials<br/>interchangeability codes);
    E -- Energy Systems --> CC(820-839: Energy systems<br/>interchangeability codes);
    E -- Propulsion --> DD(840-859: Propulsion systems<br/>interchangeability codes);
    E -- Circular Economy --> EE(860-879: Circular economy<br/>interchangeability codes);
    E -- Operations --> FF(880-899: Sustainable operations<br/>interchangeability codes);

    F --> GG(Document ICY Code Decision);
    K --> GG; L --> GG; M --> GG; N --> GG;
    J --> GG;
    O --> GG; P --> GG;
    R --> GG;
    T --> GG; U --> GG; V --> GG; W --> GG;
    X --> GG; Y --> GG; Z --> GG; AA --> GG;
    BB --> GG; CC --> GG; DD --> GG; EE --> GG; FF --> GG;

    GG --> HH[Complete ICY Documentation];

    %% Styling (Optional - Mermaid handles defaults)
    % classDef decision fill:#f9f,stroke:#333,stroke-width:2px;
    % classDef process fill:#ccf,stroke:#333,stroke-width:2px;
    % classDef output fill:#cfc,stroke:#333,stroke-width:2px;
    %
    % class A,HH process;
    % class B,C,D,E,G,H,I,Q,S decision;
    % class F,J,K,L,M,N,O,P,R,T,U,V,W,X,Y,Z,AA,BB,CC,DD,EE,FF,GG output;
            </pre>
        </div>

        <h2>Detailed Decision Process</h2>

        <h3>Step 1: Identify Technology Domain</h3>
        <p>Begin by determining which of the three primary technology domains the components belong to:</p>
        <ul>
            <li><strong>Conventional Systems (100-699)</strong>: Traditional aerospace components and systems</li>
            <li><strong>Quantum Systems (700-799)</strong>: Quantum computing, sensing, or communication components</li>
            <li><strong>Sustainable Systems (800-899)</strong>: Sustainable materials, energy systems, or circular economy components</li>
        </ul>

        <h3>Step 2: Determine Interchangeability Relationship</h3>
        <p>Based on the technology domain, assess the specific interchangeability relationship:</p>
        <h4>For Conventional Systems:</h4>
        <ul>
            <li>Is the component fully interchangeable with the original part?</li>
            <li>Is there conditional interchangeability?</li>
            <li>Is there one-way compatibility?</li>
            <li>Is there partial interchangeability?</li>
            <li>Is there assembly-level interchangeability?</li>
            <li>Is there no interchangeability?</li>
        </ul>
        <h4>For Quantum Systems:</h4>
        <ul>
            <li>Is this a quantum-classical interchangeability scenario?</li>
            <li>Is this a quantum hardware interchangeability scenario?</li>
            <li>Is this a quantum software interchangeability scenario?</li>
            <li>Is this a quantum-quantum interchangeability scenario?</li>
            <li>Is this a quantum integration interchangeability scenario?</li>
        </ul>
        <h4>For Sustainable Systems:</h4>
        <ul>
            <li>Is this a sustainable materials interchangeability scenario?</li>
            <li>Is this an energy systems interchangeability scenario?</li>
            <li>Is this a propulsion systems interchangeability scenario?</li>
            <li>Is this a circular economy interchangeability scenario?</li>
            <li>Is this a sustainable operations interchangeability scenario?</li>
        </ul>

        <h3>Step 3: Identify Specific Conditions</h3>
        <p>For each interchangeability relationship, determine the specific conditions or limitations:</p>
        <ul>
            <li>Are there physical modifications required?</li>
            <li>Are there software/firmware updates needed?</li>
            <li>Are there performance limitations?</li>
            <li>Are there documentation changes required?</li>
            <li>Are there certification implications?</li>
            <li>Are there testing requirements?</li>
            <li>Are there training requirements?</li>
        </ul>

        <h3>Step 4: Select the Appropriate ICY Code</h3>
        <p>Based on the technology domain, interchangeability relationship, and specific conditions, select the most appropriate three-digit ICY code from the reference table.</p>

        <h3>Step 5: Document the ICY Code Decision</h3>
        <p>Complete the ICY code documentation using the standardized template, including:</p>
        <ol>
            <li>Primary ICY Code</li>
            <li>Part Numbers</li>
            <li>Conditions</li>
            <li>Implementation Requirements</li>
            <li>Verification Method</li>
            <li>Approval Authority</li>
            <li>Documentation References</li>
        </ol>

        <h2>ICY Code Documentation Template</h2>
        <pre><code># ICY Code Documentation

## Basic Information
- **ICY Code**: [Three-digit code]
- **Original Part Number**: [Part number]
- **Replacement Part Number**: [Part number]
- **System**: [System name]
- **Aircraft Effectivity**: [Aircraft models]
- **Date**: [Documentation date]
- **Prepared By**: [Engineer name]

## Interchangeability Assessment
- **Interchangeability Category**: [Category description]
- **Specific Conditions**: [Detailed conditions]
- **Limitations**: [Any limitations]
- **Rationale**: [Engineering rationale for the ICY code assignment]

## Implementation Requirements
- **Physical Modifications**: [Required modifications]
- **Software/Firmware Updates**: [Required updates]
- **Documentation Updates**: [Required documentation changes]
- **Training Requirements**: [Required training]
- **Tools/Equipment**: [Special tools or equipment needed]

## Verification Method
- **Inspection Requirements**: [Required inspections]
- **Test Procedures**: [Required tests]
- **Acceptance Criteria**: [Criteria for successful implementation]
- **Test Documentation**: [Required test documentation]

## Approval
- **Engineering Approval**: [Name, signature, date]
- **Quality Approval**: [Name, signature, date]
- **Certification Approval**: [Name, signature, date]
- **Configuration Management Approval**: [Name, signature, date]

## References
- **Engineering Drawings**: [Drawing numbers]
- **Technical Documents**: [Document numbers]
- **Test Procedures**: [Procedure numbers]
- **Certification Documents**: [Document numbers]
</code></pre>

        <h2>Implementation Guidelines</h2>
        <ol>
            <li><strong>Training</strong>: Provide training to all engineering and maintenance personnel on the expanded ICY codes system and decision flowchart.</li>
            <li><strong>Integration with Tools</strong>: Integrate the decision flowchart into the Equipment Impact Analysis tool to guide users through the code selection process.</li>
            <li><strong>Validation Process</strong>: Establish a validation process for ICY code assignments, including peer review and approval by appropriate authorities.</li>
            <li><strong>Documentation Control</strong>: Ensure all ICY code documentation is stored in a centralized system with appropriate version control.</li>
            <li><strong>Periodic Review</strong>: Schedule periodic reviews of ICY code assignments to ensure consistency and identify any patterns requiring system updates.</li>
            <li><strong>Feedback Loop</strong>: Establish a feedback mechanism for engineers to suggest improvements to the ICY codes system and decision flowchart.</li>
        </ol>

        <h2>Conclusion</h2>
        <p>This decision flowchart provides a structured approach to selecting the appropriate ICY code for the AMPEL BWB Quantum Embarked aircraft project. By standardizing the decision-making process, it will help ensure consistent application of the expanded ICY codes system across all technology domains, supporting the project's goals of integrating revolutionary technologies while maintaining safety, efficiency, and regulatory compliance.</p>

    </div>

    <!-- Initialize Mermaid -->
    <script>
        mermaid.initialize({ startOnLoad: true });
    </script>
</body>
</html>
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
