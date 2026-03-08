# ShelfIQ Presentation Diagrams - Optimized & Clean

## Simplified diagrams that fit perfectly in PowerPoint slides

---

## SLIDE 5: PROCESS FLOW / USE CASE DIAGRAM

### OPTION A: User Journey Flow (RECOMMENDED)
**Clean, simple sequence showing seller interaction**

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'16px'}}}%%
sequenceDiagram
    participant Seller
    participant ShelfIQ
    participant AI Engine
    participant Market

    Market->>AI Engine: Price drop detected
    AI Engine->>ShelfIQ: Generate alert
    ShelfIQ->>Seller: Notify with recommendation
    Seller->>ShelfIQ: Review & apply
    ShelfIQ->>Seller: Confirm action taken
```

**Export:** mermaid.live → 1200x500px PNG

---

### OPTION B: Simple Process Flow (ALTERNATIVE)
**Horizontal flow with better spacing**

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'15px'}}}%%
graph LR
    A[Collect Data<br/>Marketplaces<br/>Competitors] --> B[Process<br/>Validate<br/>Analyze]
    B --> C[AI Models<br/>Forecast<br/>Optimize]
    C --> D[Generate<br/>Insights<br/>Alerts]
    D --> E[Deliver<br/>Dashboard<br/>Copilot]

    style A fill:#E3F2FD,stroke:#1976D2,stroke-width:3px
    style B fill:#FFE0B2,stroke:#F57C00,stroke-width:3px
    style C fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px
    style D fill:#F8BBD0,stroke:#C2185B,stroke-width:3px
    style E fill:#B2DFDB,stroke:#00796B,stroke-width:3px
```

**Export:** mermaid.live → 1400x350px PNG

---

## SLIDE 6: WIREFRAMES/MOCKUPS

### Dashboard Wireframe - Simplified ChatGPT Prompt

```
Create a clean, minimal web dashboard wireframe in landscape format (1600x700px).

LAYOUT:

TOP BAR (50px):
- "ShelfIQ" logo (left)
- Search bar (center)
- Bell icon, Profile (right)

MAIN CONTENT - TWO COLUMNS:

LEFT (65%):
- 4 KPI CARDS in one row:
  Revenue | Margin | Market Share | Alerts
  (show values with up/down arrows)

- LARGE CHART below:
  Simple line chart showing revenue trend
  Clean axes, minimal labels

RIGHT (35%):
- "Top Opportunities" panel:
  3 items with icons and brief text

- "Recent Alerts" panel:
  3 items with colored status dots

STYLE:
- Minimal, clean design
- Light gray background (#F5F5F5)
- White cards with subtle shadows
- Blue primary color (#1976D2)
- Professional SaaS look
- Readable fonts
- Plenty of white space

OUTPUT: PNG, 1600x700px, landscape
```

---

## SLIDE 7: ARCHITECTURE DIAGRAM

### Simplified System Architecture (CLEAN VERSION)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'14px'}}}%%
graph LR
    subgraph Sources[" DATA SOURCES "]
        A1[Marketplaces]
        A2[Scrapers]
        A3[Signals]
    end

    subgraph Pipeline[" PIPELINE "]
        B1[Kafka]
        B2[Flink]
    end

    subgraph Storage[" STORAGE "]
        C1[Redis]
        C2[S3]
    end

    subgraph AI[" AI/ML "]
        D1[Forecast]
        D2[Pricing]
        D3[Sentiment]
    end

    subgraph App[" APPLICATION "]
        E1[API]
        E2[Dashboard]
        E3[Copilot]
    end

    Sources --> Pipeline
    Pipeline --> Storage
    Storage --> AI
    AI --> App

    style Sources fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style Pipeline fill:#FFE0B2,stroke:#F57C00,stroke-width:2px
    style Storage fill:#C8E6C9,stroke:#388E3C,stroke-width:2px
    style AI fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style App fill:#B2DFDB,stroke:#00796B,stroke-width:2px
```

**Export:** mermaid.live → 1400x500px PNG

---

### ALTERNATIVE: Layered Architecture (VERTICAL)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'14px'}}}%%
graph TB
    subgraph UI[" USER INTERFACE LAYER "]
        U1[Dashboard]
        U2[Copilot Chat]
    end

    subgraph API[" API & SERVICES LAYER "]
        A1[GraphQL API]
        A2[REST API]
        A3[WebSocket]
    end

    subgraph Intel[" INTELLIGENCE LAYER "]
        I1[Recommendation Engine]
        I2[Alert Engine]
    end

    subgraph ML[" AI/ML LAYER "]
        M1[Demand Forecast]
        M2[Pricing Optimization]
        M3[Sentiment Analysis]
    end

    subgraph Data[" DATA LAYER "]
        D1[Feature Store]
        D2[Data Lake]
        D3[Kafka Pipeline]
    end

    subgraph Source[" DATA SOURCES "]
        S1[Marketplaces]
        S2[Competitors]
        S3[External Signals]
    end

    UI --> API
    API --> Intel
    Intel --> ML
    ML --> Data
    Data --> Source

    style UI fill:#B2DFDB,stroke:#00796B,stroke-width:2px
    style API fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style Intel fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    style ML fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style Data fill:#C8E6C9,stroke:#388E3C,stroke-width:2px
    style Source fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
```

**Export:** mermaid.live → 1000x800px PNG

---

## SLIDE 8: TECHNOLOGIES USED

### Tech Stack - Compact Version

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'14px'}}}%%
graph TB
    subgraph Frontend[" FRONTEND "]
        F1[React + TypeScript]
        F2[Material-UI]
    end

    subgraph Backend[" BACKEND "]
        B1[GraphQL]
        B2[FastAPI]
        B3[Node.js]
    end

    subgraph ML[" AI/ML "]
        M1[Prophet]
        M2[LightGBM]
        M3[DistilBERT]
        M4[GPT-4]
    end

    subgraph Data[" DATA "]
        D1[Kafka]
        D2[Flink]
        D3[Redis]
        D4[PostgreSQL]
    end

    subgraph AWS[" AWS CLOUD "]
        A1[EKS]
        A2[SageMaker]
        A3[Bedrock]
        A4[S3]
    end

    Frontend --> Backend
    Backend --> ML
    Backend --> Data
    ML --> AWS
    Data --> AWS

    style Frontend fill:#B2DFDB,stroke:#00796B,stroke-width:2px
    style Backend fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style ML fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    style Data fill:#C8E6C9,stroke:#388E3C,stroke-width:2px
    style AWS fill:#FFE0B2,stroke:#FF9900,stroke-width:3px
```

**Export:** mermaid.live → 1200x700px PNG

---

## SLIDE 9: ESTIMATED IMPLEMENTATION COST

### Cost Breakdown - Visual Representation (NO NUMBERS)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'14px'}}}%%
graph TB
    subgraph Cost[" IMPLEMENTATION COST COMPONENTS "]

        subgraph Team[" TEAM COSTS "]
            T1[Development Team<br/>Full-stack & ML Engineers]
            T2[DevOps & Infrastructure]
            T3[Design & Product]
        end

        subgraph Infra[" INFRASTRUCTURE "]
            I1[AWS Cloud Services<br/>EKS, SageMaker, S3]
            I2[Database & Storage<br/>RDS, Redis, ElastiCache]
            I3[Networking & CDN<br/>CloudFront, API Gateway]
        end

        subgraph Services[" THIRD-PARTY SERVICES "]
            S1[AI/ML APIs<br/>OpenAI, Bedrock]
            S2[Data Collection<br/>Marketplace APIs, Proxies]
            S3[Monitoring & Tools<br/>Observability Stack]
        end

        subgraph Other[" OTHER COSTS "]
            O1[Security & Compliance<br/>Audits, Certifications]
            O2[Legal & Operations]
            O3[Marketing & Acquisition]
        end
    end

    style Team fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style Infra fill:#FFE0B2,stroke:#F57C00,stroke-width:2px
    style Services fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style Other fill:#C8E6C9,stroke:#388E3C,stroke-width:2px
```

**Export:** mermaid.live → 1400x700px PNG

---

### ALTERNATIVE: Cost Categories (Simpler)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'15px'}}}%%
graph LR
    A[Implementation<br/>Cost] --> B[Personnel<br/>Development Team<br/>DevOps<br/>Design]
    A --> C[Infrastructure<br/>AWS Services<br/>Databases<br/>Storage]
    A --> D[Services<br/>AI APIs<br/>Data Sources<br/>Monitoring]
    A --> E[Operations<br/>Security<br/>Legal<br/>Marketing]

    style A fill:#1976D2,stroke:#0D47A1,stroke-width:3px,color:#fff
    style B fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style C fill:#FFE0B2,stroke:#F57C00,stroke-width:2px
    style D fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px
    style E fill:#C8E6C9,stroke:#388E3C,stroke-width:2px
```

**Export:** mermaid.live → 1400x400px PNG

---

### Cost Information - Text Content for Slide

**SLIDE 9 CONTENT (No specific numbers):**

### Implementation Cost Structure

**Development Phase:**
- Core development team (full-stack, ML, DevOps engineers)
- UI/UX design and product management
- Quality assurance and testing

**Infrastructure:**
- AWS cloud services (compute, storage, ML)
- Database and caching infrastructure
- Content delivery and networking

**Third-Party Services:**
- AI/ML API access (GPT-4, foundation models)
- Marketplace API integrations
- Data collection and proxy services
- Monitoring and observability tools

**Operational Costs:**
- Security audits and compliance certifications
- Legal and administrative
- Customer acquisition and marketing

**Cost Optimization Strategies:**
- AWS startup credits program
- Open-source alternatives where feasible
- Spot instances for non-critical workloads
- Reserved instances for production
- Gradual team scaling based on milestones

**Funding Approach:**
- Seed funding for initial development
- Revenue-based scaling post-launch
- Break-even target within operational timeline

---

## SLIDE 10: AWS SERVICES / HACKATHON REQUIREMENTS

### AWS Services Integration - Clean Version

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#FF9900','fontSize':'14px'}}}%%
graph TB
    subgraph AWS[" AWS CLOUD PLATFORM "]

        subgraph Compute[" COMPUTE "]
            C1[Amazon EKS<br/>Kubernetes]
            C2[AWS Lambda<br/>Serverless]
        end

        subgraph AI[" AI/ML "]
            A1[Amazon SageMaker<br/>Model Training]
            A2[Amazon Bedrock<br/>Foundation Models]
        end

        subgraph Data[" DATA & STORAGE "]
            D1[Amazon S3<br/>Data Lake]
            D2[Amazon RDS<br/>PostgreSQL]
            D3[ElastiCache<br/>Redis]
        end

        subgraph Network[" NETWORKING "]
            N1[API Gateway]
            N2[CloudFront CDN]
            N3[Route 53]
        end

        subgraph Monitor[" MONITORING "]
            M1[CloudWatch]
            M2[X-Ray]
        end
    end

    Compute --> AI
    AI --> Data
    Compute --> Data
    Network --> Compute
    Monitor --> Compute
    Monitor --> AI

    style AWS fill:#232F3E,stroke:#FF9900,stroke-width:4px,color:#fff
    style Compute fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style AI fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style Data fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style Network fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style Monitor fill:#FF9900,stroke:#232F3E,stroke-width:2px
```

**Export:** mermaid.live → 1400x700px PNG

---

### ALTERNATIVE: AWS Services Flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'fontSize':'14px'}}}%%
graph LR
    A[User Request] --> B[CloudFront<br/>CDN]
    B --> C[API Gateway]
    C --> D[EKS<br/>Application]
    D --> E[SageMaker<br/>ML Models]
    D --> F[Bedrock<br/>LLM]
    D --> G[RDS<br/>Database]
    D --> H[ElastiCache<br/>Cache]
    E --> I[S3<br/>Data Lake]

    style A fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style B fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style C fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style D fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style E fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style F fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style G fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style H fill:#FF9900,stroke:#232F3E,stroke-width:2px
    style I fill:#FF9900,stroke:#232F3E,stroke-width:2px
```

**Export:** mermaid.live → 1400x400px PNG

---

## EXPORT SETTINGS FOR ALL DIAGRAMS

### Mermaid Live Editor Settings:
1. Go to https://mermaid.live
2. Paste code
3. Click "Actions" → "PNG"
4. Set appropriate width (specified for each diagram)
5. Choose transparent background
6. Download

### Recommended Dimensions:
- **Horizontal flow diagrams:** 1400x400-500px
- **Vertical/layered diagrams:** 1000-1200x700-800px
- **Complex diagrams:** 1400x700px
- **Simple flows:** 1200-1400x350-500px

### PowerPoint Tips:
1. Insert PNG into slide
2. Position below title (leave ~100px for title)
3. Center align horizontally
4. Maintain aspect ratio when resizing
5. Ensure text is readable from distance

---

## FINAL RECOMMENDATIONS BY SLIDE

| Slide | Recommended Diagram | Dimensions | Tool |
|-------|-------------------|------------|------|
| 5 | User Journey Flow (Option A) | 1200x500 | Mermaid |
| 6 | Dashboard Wireframe | 1600x700 | ChatGPT |
| 7 | Simplified Architecture (Horizontal) | 1400x500 | Mermaid |
| 8 | Tech Stack Compact | 1200x700 | Mermaid |
| 9 | Cost Categories (Simpler) | 1400x400 | Mermaid |
| 10 | AWS Services Integration | 1400x700 | Mermaid |

---

## QUICK GENERATION CHECKLIST

- [ ] Slide 5: Copy User Journey Flow → mermaid.live → Export 1200x500px
- [ ] Slide 6: Copy Dashboard prompt → ChatGPT → Generate → Download
- [ ] Slide 7: Copy Simplified Architecture → mermaid.live → Export 1400x500px
- [ ] Slide 8: Copy Tech Stack → mermaid.live → Export 1200x700px
- [ ] Slide 9: Copy Cost Categories → mermaid.live → Export 1400x400px
- [ ] Slide 10: Copy AWS Services → mermaid.live → Export 1400x700px

**Total Time: ~45 minutes for all 6 diagrams**

All diagrams are now optimized for PowerPoint with better spacing and cleaner layouts!

