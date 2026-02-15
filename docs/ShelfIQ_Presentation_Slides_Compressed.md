# ShelfIQ - AWS AI for Bharat Hackathon
## Compressed Presentation Slides

---

## SLIDE 1: TITLE
**ShelfIQ - AI Commerce Intelligence Copilot**

Empowering Indian Retailers & Marketplace Sellers with AI

Team: OG404
AWS AI for Bharat Hackathon 2024

---

## SLIDE 2: THE PROBLEM & SOLUTION

**The Challenge:**
• 70% of Indian sellers struggle with pricing decisions
• Manual competitor tracking across 100s of products impossible
• Demand forecasting errors = ₹1000s Cr lost revenue annually
• Limited access to actionable market intelligence

**Our Solution: ShelfIQ**
AI-powered copilot providing:
• Real-time competitor pricing intelligence
• AI-driven demand forecasting
• Automated pricing recommendations
• Listing optimization & margin protection

**Impact:** 15% pricing accuracy ↑ | 20% stockouts ↓ | 10% revenue ↑

---

## SLIDE 3: WHY SHELFIQ IS DIFFERENT

**Competitive Advantages:**

1. **AI Copilot vs Static Dashboards**
   → Conversational AI with actionable recommendations

2. **India-First Design**
   → Built for Amazon.in, Flipkart, Meesho
   → Festival demand prediction | Vernacular languages

3. **Affordable for SMBs**
   → ₹2,999/month vs ₹50K-2L/month (competitors)

4. **Real-Time Intelligence**
   → 15-minute competitor price updates
   → Instant alerts on market changes

**USP:** Only AI copilot for Indian e-commerce with multi-marketplace support

---

## SLIDE 4: CORE FEATURES

**Intelligence Layer:**
• Competitor Price Monitoring (real-time, 90-day history)
• AI Pricing Recommendations (demand elasticity-based)
• Demand Forecasting (7/14/30/90-day predictions)
• Review Sentiment Analysis (aspect-based)

**Action Layer:**
• Listing Optimization (SEO, keywords, images)
• Smart Alerts (price wars, stockouts, margin risks)
• Growth Actions (prioritized opportunities with ROI)

**Interface:**
• Copilot Chat (natural language queries)
• Multi-Marketplace Dashboard (unified view)
• Real-time Notifications (email, SMS, webhook)

---

## SLIDE 5: SYSTEM ARCHITECTURE

```
DATA SOURCES
↓
Marketplaces (Amazon, Flipkart) | Web Scrapers | External Signals
↓
INGESTION PIPELINE (Kafka → Flink → Data Lake)
↓
FEATURE STORE (Redis + S3)
↓
AI/ML MODELS
• Demand Forecasting (Prophet + LightGBM + LSTM)
• Pricing Optimization (Bayesian + Constrained Optimization)
• Sentiment Analysis (DistilBERT)
• Anomaly Detection (Isolation Forest)
↓
INTELLIGENCE SERVICES
Recommendation Engine | Alert Engine | Analytics
↓
API LAYER (GraphQL + REST + WebSocket)
↓
USER INTERFACE (React Dashboard + Copilot Chat)
```

**Data Flow:** 15-min refresh | Real-time alerts | Sub-2s dashboard load

---

## SLIDE 6: USER INTERFACE

**Dashboard Overview:**
• KPI Cards: Revenue, Margin, Market Share, Alerts
• Revenue Trend Chart (7/30/90-day views)
• Top Opportunities Widget
• Recent Alerts Feed

**Product Detail Page:**
• Price History vs Competitors (90-day chart)
• AI Recommendation Card with Impact Prediction
• Demand Forecast with Confidence Bands
• Competitor Analysis Table

**Copilot Chat:**
• Natural language queries
• Rich responses (charts, tables, actions)
• One-click action execution
• Suggested follow-up questions

---

## SLIDE 7: USE CASES

**Use Case 1: Price War Protection**
Scenario: Competitor drops price 12%
→ Alert + AI analysis + Recommendation
→ Result: Protected ₹45K weekly revenue, maintained 18% margin

**Use Case 2: Festival Demand Spike**
Scenario: Diwali approaching
→ 35% demand spike forecast + Price increase recommendation
→ Result: 22% revenue increase, zero stockouts

**Use Case 3: Listing Optimization**
Scenario: New seller, low visibility
→ SEO analysis + Competitor benchmarking + A/B test suggestions
→ Result: 45% visibility ↑, 18% conversion rate ↑

---

## SLIDE 8: TECHNOLOGY STACK

**Frontend:** React 18 + TypeScript | Material-UI | Recharts | Socket.io

**Backend:** FastAPI (Python) | Node.js | GraphQL (Apollo) | Kong Gateway

**AI/ML:**
• Forecasting: Prophet + LightGBM + LSTM
• Pricing: Bayesian Regression + Optimization
• NLP: DistilBERT | GPT-4 (Copilot)
• Serving: TensorFlow Serving | MLflow

**Data:** Kafka | Flink | Airflow | Feast (Feature Store) | S3 Data Lake

**AWS Services:**
• Compute: EKS (Kubernetes)
• Database: RDS PostgreSQL | ElastiCache Redis
• ML: SageMaker | Bedrock
• Storage: S3 | Monitoring: CloudWatch

**DevOps:** Docker | Terraform | GitHub Actions | ArgoCD | Prometheus

---

## SLIDE 9: IMPLEMENTATION COST

**Phase 1: MVP (3 Months) - ₹35 Lakhs**
• Team: 5 engineers + PM + Designer = ₹27L
• Infrastructure (AWS): ₹1.5L
• Third-party APIs: ₹2.25L
• Other (testing, legal): ₹3.6L

**Phase 2-4: Scale (9 Months) - ₹2.76 Crores**
• Expanded team (12 members): ₹2.08Cr
• Scaled infrastructure: ₹16.65L
• APIs & services: ₹18L
• Security, compliance, marketing: ₹33L

**Total Year 1: ₹3.1 Crores**

**Cost Optimization:**
• AWS startup credits: ₹10-15L savings
• Open-source tools (Feast, MLflow)
• Spot instances: 30-50% compute savings

**Revenue Target:** ₹60L ARR by month 12 (100 customers @ ₹5K/month)

---

## SLIDE 10: AWS & BHARAT ALIGNMENT

**AWS Services Used:**
• SageMaker (ML training & deployment)
• Bedrock (LLM for copilot)
• EKS (container orchestration)
• RDS + ElastiCache (databases)
• S3 + Glue (data lake & ETL)
• CloudWatch + X-Ray (monitoring)

**Bharat-Specific Features:**
• Multi-language: Hindi, Tamil, Telugu, Bengali, Marathi
• Festival Intelligence: Diwali, Holi, Eid demand prediction
• Indian Marketplaces: Flipkart, Meesho, Amazon.in
• Tier 2/3 Focus: Affordable pricing, low-bandwidth UI
• GST Compliance: Indian tax integration

**Social Impact:**
• Target: 10,000+ MSMEs empowered in Year 1
• Economic Impact: ₹50+ Cr additional revenue for sellers
• Job Creation: Enable 500+ new e-commerce businesses

**Innovation:** First conversational AI copilot for Indian e-commerce

---

## SLIDE 11: COMPETITIVE LANDSCAPE

| Feature | ShelfIQ | Helium 10 | Unicommerce |
|---------|---------|-----------|-------------|
| AI Copilot | ✅ | ❌ | ❌ |
| Indian Marketplaces | ✅ | ❌ | ✅ |
| Real-time Pricing | ✅ | Partial | ❌ |
| AI Forecasting | ✅ | Basic | Basic |
| Vernacular Support | ✅ | ❌ | ❌ |
| Pricing | ₹2,999+ | ₹8,000+ | ₹15,000+ |
| Festival Intelligence | ✅ | ❌ | ❌ |

**Our Edge:** Only affordable AI copilot built specifically for Indian sellers

---

## SLIDE 12: GO-TO-MARKET

**Launch Phases:**
• Months 1-3: Beta (50 users, free)
• Months 4-6: Soft Launch (200 customers @ ₹2,999)
• Months 7-12: Scale (1,000 customers @ ₹4,999)

**Acquisition Channels:**
• Content Marketing (SEO, YouTube tutorials)
• Seller Communities (Facebook groups, forums)
• Webinars & Workshops
• Referral Program (₹1,000 credit)
• Marketplace Partnerships

**Pricing Tiers:**
• Starter: ₹2,999/mo (100 SKUs)
• Growth: ₹9,999/mo (1,000 SKUs)
• Pro: ₹24,999/mo (10,000 SKUs)
• Enterprise: Custom (unlimited)

---

## SLIDE 13: EXECUTION ROADMAP

**Q1 (Months 1-3): MVP**
Core pipeline | Basic forecasting | Dashboard | Beta launch (50 users)

**Q2 (Months 4-6): Enhanced**
Multi-marketplace | Advanced ML | Copilot chat | 200 customers

**Q3 (Months 7-9): Scale**
Feature store | Real-time processing | Mobile-responsive | 500 customers

**Q4 (Months 10-12): Enterprise**
SSO/MFA | Custom reports | API integrations | 1,000 customers

**Team:** 5 → 12 members (Full-stack, ML, DevOps, Design, PM, QA)

---

## SLIDE 14: SUCCESS METRICS

**Product KPIs:**
• Forecast accuracy: MAPE <15%
• Recommendation acceptance: >60%
• Dashboard load: <2 seconds
• System uptime: 99.9%

**Business KPIs:**
• Customers: 1,000 in Year 1
• MRR: ₹50L by Month 12
• Retention: >90%
• NPS: >50
• Customer ROI: >5x

**Impact KPIs:**
• Revenue increase: 15%+
• Stockout reduction: 20%+
• Time saved: 10 hrs/week
• Margin improvement: 3-5%

---

## SLIDE 15: CALL TO ACTION

**Vision:**
Make AI-powered commerce intelligence accessible to every Indian seller

**The Ask:**
• Funding: ₹2 Cr seed round (12-month runway)
• Partnerships: Collaboration with Indian marketplaces
• Pilot: 50 beta users for validation
• Mentorship: E-commerce & AI experts

**Contact:**
📧 team@shelfiq.in
🌐 www.shelfiq.in
💻 github.com/Jeejo-Joy/shelfiq-commerce-intelligence

**Next Steps:**
MVP (3 months) → Beta (50 sellers) → Launch (200 customers) → Scale (1,000)

**"Empowering Indian sellers with AI, one smart decision at a time."**

---

## BONUS SLIDE: DEMO HIGHLIGHTS

**Live Demo Flow:**
1. Dashboard: Real-time KPIs and alerts
2. Copilot Chat: "Which products need attention today?"
3. Pricing Recommendation: Impact prediction with confidence score
4. Alert System: Real-time competitor price drop notification
5. Multi-Marketplace View: Unified analytics across platforms

**Key Differentiators to Show:**
✓ Natural language interaction
✓ Real-time data (15-min refresh)
✓ Actionable recommendations (not just data)
✓ One-click action execution
✓ Indian marketplace focus

---

## PRESENTATION TIPS

**Timing (15 minutes):**
• Slides 1-2: 2 min (Problem)
• Slides 3-4: 3 min (Solution)
• Slides 5-7: 4 min (How it works)
• Slides 8-10: 3 min (Tech & AWS)
• Slides 11-15: 3 min (Market & Ask)

**Key Messages:**
1. AI democratization for Indian MSMEs
2. Real-time intelligence (15-min updates)
3. Affordable (₹2,999 vs ₹50,000)
4. India-first (festivals, languages)
5. Proven impact (15% revenue ↑)

**Storytelling:**
Seller pain → ShelfIQ solution → Demo → Impact → Call to action
