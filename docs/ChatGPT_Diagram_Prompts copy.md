# ChatGPT Prompts for ShelfIQ Presentation Diagrams

## PROMPT 1: SYSTEM ARCHITECTURE DIAGRAM (Slide 5)

```
Create a professional system architecture diagram for ShelfIQ, an AI-powered e-commerce intelligence platform. Use a clean, modern style with the following structure:

LAYOUT: Vertical flow from top to bottom with 6 layers

LAYER 1 - DATA SOURCES (Top):
- 3 boxes in a row:
  • "Marketplaces" (Amazon, Flipkart, Meesho logos)
  • "Web Scrapers" (competitor pricing icon)
  • "External Signals" (weather, events, holidays icons)
- Color: Light blue (#E3F2FD)

LAYER 2 - INGESTION PIPELINE:
- Flow: Kafka → Apache Flink → Data Lake (S3)
- Show arrows connecting each component
- Color: Orange (#FFE0B2)

LAYER 3 - STORAGE:
- 2 boxes side by side:
  • "Feature Store" (Redis icon)
  • "Data Lake" (S3 icon with Parquet files)
- Color: Green (#C8E6C9)

LAYER 4 - AI/ML MODELS:
- 4 boxes in a grid (2x2):
  • "Demand Forecasting" (Prophet + LightGBM + LSTM)
  • "Pricing Optimization" (Bayesian + Optimization)
  • "Sentiment Analysis" (DistilBERT)
  • "Anomaly Detection" (Isolation Forest)
- Color: Purple (#E1BEE7)

LAYER 5 - INTELLIGENCE SERVICES:
- 3 boxes in a row:
  • "Recommendation Engine"
  • "Alert Engine"
  • "Analytics Engine"
- Color: Pink (#F8BBD0)

LAYER 6 - APPLICATION & PRESENTATION:
- Top row: "API Layer" (GraphQL + REST + WebSocket)
- Bottom row: 2 boxes:
  • "Web Dashboard" (React icon)
  • "Copilot Chat" (AI chat icon)
- Color: Teal (#B2DFDB)

STYLE REQUIREMENTS:
- Use rounded rectangles for all boxes
- Add icons inside each box
- Use arrows to show data flow between layers
- Add small labels on arrows: "15-min refresh", "Real-time", "Sub-2s load"
- Use a white background
- Add subtle shadows to boxes for depth
- Use AWS color scheme where applicable (Orange #FF9900, Dark Blue #232F3E)

OUTPUT: High-resolution PNG, 1920x1080, suitable for PowerPoint
```

---

## PROMPT 2: PROCESS FLOW DIAGRAM (Slide 5 Alternative)

```
Create a detailed process flow diagram for ShelfIQ showing the user journey and data flow. Use a horizontal swimlane layout:

SWIMLANES (from top to bottom):

SWIMLANE 1 - USER LAYER:
- Actor icon: "Seller/Retailer"
- Actions: "View Dashboard" → "Ask Copilot" → "Review Alerts" → "Take Action"

SWIMLANE 2 - APPLICATION LAYER:
- "Web Dashboard" → "Copilot Chat Interface" → "Alert Management"
- Show bidirectional arrows to User Layer

SWIMLANE 3 - API & SERVICES:
- "API Gateway" → "Query Service" → "Recommendation Engine" → "Alert Engine"
- Show authentication and rate limiting icons

SWIMLANE 4 - DATA & ML LAYER:
- "Feature Store" → "ML Models" (4 types) → "Analytics"
- Show caching and real-time processing

SWIMLANE 5 - DATA SOURCES:
- "Marketplace APIs" → "Web Scrapers" → "External Signals"
- Show data ingestion pipeline (Kafka → Flink)

KEY FLOWS TO HIGHLIGHT:
1. QUERY FLOW (Blue arrows):
   User asks question → API → Feature Store → ML Model → Response
   Label: "< 3 seconds"

2. ALERT FLOW (Red arrows):
   Data change → Alert Engine → Priority Scoring → Notification → User
   Label: "< 5 minutes"

3. DATA FLOW (Green arrows):
   Sources → Ingestion → Processing → Storage → Models
   Label: "15-min refresh"

STYLE:
- Use different arrow colors for different flow types
- Add time labels on critical paths
- Use icons for each component
- Add a legend explaining arrow colors
- Clean, professional look with rounded corners
- White background with subtle grid

OUTPUT: High-resolution PNG, 1920x1080, landscape orientation
```

---

## PROMPT 3: WIREFRAME - DASHBOARD OVERVIEW (Slide 6)

```
Create a clean, professional wireframe mockup of the ShelfIQ dashboard interface. Use a modern SaaS design style:

LAYOUT:

TOP BAR (Full width):
- Left: "ShelfIQ" logo with icon
- Center: Search bar with magnifying glass icon
- Right: Notification bell (with red badge "15"), Profile avatar, Settings gear icon

NAVIGATION BAR (Below top bar):
- Tabs: "📊 Dashboard" (active) | "📦 Products" | "🔔 Alerts" | "📈 Analytics" | "💬 Copilot"
- Active tab highlighted with underline

MAIN CONTENT AREA:

ROW 1 - KPI CARDS (4 cards in a row):
Card 1: "Revenue" | ₹2.4L | ↑ 12% (green arrow)
Card 2: "Margin" | 18.5% | ↓ 2.1% (red arrow)
Card 3: "Market Share" | 23.4% | ↑ 5.2% (green arrow)
Card 4: "Active Alerts" | 15 | 🔴 3 Critical

ROW 2 - REVENUE TREND CHART (Full width):
- Title: "Revenue Trend (Last 30 Days)"
- Line chart showing upward trend
- X-axis: Dates | Y-axis: Revenue
- Tabs above chart: "7D" | "30D" (active) | "90D"

ROW 3 - TWO COLUMNS:

LEFT COLUMN - "Top Opportunities":
- Card with list of 3 items:
  • 💡 Increase price on SKU-1234 (+₹50) | Expected: +₹2.5K/week
  • 🎯 Optimize listing for SKU-5678 | Expected: +15% visibility
  • 📦 Restock SKU-9012 (7 days left) | Risk: High

RIGHT COLUMN - "Recent Alerts":
- Card with list of 3 items:
  • 🔴 Competitor price drop on SKU-5678 | -8% | 5 min ago
  • 🟡 Demand spike detected SKU-9012 | +35% | 1 hour ago
  • 🟢 Margin improved on SKU-3456 | +2.3% | 2 hours ago

STYLE:
- Use a light gray background (#F5F5F5)
- White cards with subtle shadows
- Use Material Design principles
- Add placeholder charts and graphs
- Use icons for visual interest
- Clean, minimal, professional
- Color scheme: Primary blue (#1976D2), Success green (#4CAF50), Warning orange (#FF9800), Error red (#F44336)

OUTPUT: High-resolution PNG, 1920x1080, suitable for presentation
```

---

## PROMPT 4: WIREFRAME - PRODUCT DETAIL PAGE (Slide 6)

```
Create a detailed wireframe for the ShelfIQ Product Detail page showing AI recommendations:

LAYOUT:

HEADER:
- Back arrow "← Back to Products"
- Product title: "Premium Wireless Headphones (SKU-1234)"
- Quick stats bar: "Current Price: ₹2,499 | Margin: 22% | Sales Rank: #145 | Stock: 45 units"

SECTION 1 - PRICE HISTORY CHART (Full width):
- Title: "Price History & Competitor Analysis (90 Days)"
- Multi-line chart showing:
  • Your price (blue solid line)
  • Competitor Min (red dashed line)
  • Competitor Median (orange dashed line)
  • Competitor Max (green dashed line)
- X-axis: Timeline | Y-axis: Price (₹)
- Legend in top-right corner

SECTION 2 - AI RECOMMENDATION CARD (Full width, highlighted):
- 💡 Icon with "AI Recommendation" badge
- Large text: "Increase price to ₹2,649 (+₹150)"
- Impact metrics in 3 columns:
  • Revenue: +8% (↑ ₹3.2K/week)
  • Units: -3% (acceptable trade-off)
  • Margin: +12% (↑ to 28%)
- Confidence bar: 87% (visual progress bar)
- Reasoning: "Competitors raised prices, demand remains strong, margin opportunity"
- Two buttons: "Apply Recommendation" (primary blue) | "Dismiss" (secondary gray)

SECTION 3 - TWO COLUMNS:

LEFT COLUMN - "Demand Forecast":
- Title with info icon
- Area chart showing:
  • Historical demand (solid line)
  • Forecasted demand (dashed line)
  • Confidence bands (shaded area - 80% and 95%)
- X-axis: Next 30 days | Y-axis: Units/day
- Key insight: "Stable demand expected, slight uptick in 2 weeks"

RIGHT COLUMN - "Competitor Analysis":
- Stats card with:
  • Active Competitors: 12
  • Your Rank: #3 of 12
  • Price Position: Mid-range (47th percentile)
  • Buy Box Win Rate: 34%
- Mini table showing top 3 competitors:
  Competitor A | ₹2,399 | ⭐4.5 | 234 reviews
  Competitor B | ₹2,599 | ⭐4.3 | 189 reviews
  You | ₹2,499 | ⭐4.6 | 156 reviews

SECTION 4 - TABS:
- Tab bar: "Sentiment Analysis" | "Listing Quality" | "Alert History"
- Show first tab active with sentiment breakdown

STYLE:
- Clean, data-rich layout
- Use cards with shadows for sections
- Highlight the AI recommendation card with a subtle gradient background
- Use color coding: Green for positive, Red for negative, Blue for neutral
- Professional charts with grid lines
- Consistent spacing and alignment

OUTPUT: High-resolution PNG, 1920x1080, scrollable page mockup
```

---

## PROMPT 5: WIREFRAME - COPILOT CHAT INTERFACE (Slide 6)

```
Create a modern chat interface wireframe for the ShelfIQ AI Copilot:

LAYOUT:

CHAT WINDOW (Floating panel, right side of screen):
- Header bar:
  • Left: "💬 ShelfIQ Copilot" with AI icon
  • Right: Minimize and Close buttons

CHAT HISTORY (Scrollable area):

MESSAGE 1 (User):
- Avatar: User icon
- Bubble (right-aligned, blue): "Which products should I focus on this week?"
- Timestamp: "2:34 PM"

MESSAGE 2 (AI Response):
- Avatar: ShelfIQ AI icon
- Bubble (left-aligned, white with border):

  "Based on current market conditions, here are your top 3 priorities:"

  CARD 1 (embedded in chat):
  "1. SKU-1234 (Wireless Headphones)"
  • Competitor dropped price by 8%
  • Recommended action: Match price or improve listing
  • Potential impact: Protect ₹45K weekly revenue
  [View Details] button

  CARD 2:
  "2. SKU-5678 (Smart Watch)"
  • Demand spike detected (+35%)
  • Recommended action: Increase price by ₹200
  • Potential impact: +₹12K additional margin
  [Apply Recommendation] button

  CARD 3:
  "3. SKU-9012 (Bluetooth Speaker)"
  • Low stock alert (6 days remaining)
  • Recommended action: Reorder 150 units
  • Risk: Potential stockout during peak season
  [Create Purchase Order] button

  ACTION BUTTONS (at bottom of AI message):
  [Apply All] [View Detailed Report] [Ask Follow-up]

- Timestamp: "2:34 PM"

SUGGESTED QUESTIONS (Below chat):
- Pill-shaped buttons:
  • "What's my overall margin trend?"
  • "Show me products losing market share"
  • "Which listings need optimization?"

INPUT AREA (Bottom):
- Text input field: "Type your question here..."
- Right side: Microphone icon | Send button (paper plane icon)

FEATURES TO SHOW:
- Typing indicator (3 animated dots) when AI is responding
- Rich content in chat (cards, charts, buttons)
- Action buttons within chat messages
- Suggested questions for easy interaction

STYLE:
- Modern chat UI similar to ChatGPT or Claude
- User messages: Blue background, right-aligned
- AI messages: White background with border, left-aligned
- Embedded cards: Light gray background with subtle shadow
- Smooth rounded corners throughout
- Clean, readable fonts
- Icons for visual interest

OUTPUT: High-resolution PNG, 800x1200 (portrait), showing full chat interface
```

---

## PROMPT 6: DATA FLOW DIAGRAM (Alternative for Slide 5)

```
Create a simplified data flow diagram showing how ShelfIQ processes information:

CIRCULAR FLOW DESIGN (Clockwise):

STAGE 1 (Top): "DATA COLLECTION"
- Icons: Marketplace logos, web scraper, calendar
- Label: "Every 15 minutes"
- Arrow pointing right →

STAGE 2 (Right): "PROCESSING"
- Icons: Kafka logo, Flink logo, validation checkmark
- Label: "Real-time validation & cleansing"
- Arrow pointing down ↓

STAGE 3 (Bottom): "STORAGE & FEATURES"
- Icons: Database, Redis, S3 bucket
- Label: "Feature engineering"
- Arrow pointing left ←

STAGE 4 (Left): "AI INTELLIGENCE"
- Icons: Brain, chart trending up, lightbulb
- Label: "ML models generate insights"
- Arrow pointing up ↑

CENTER CIRCLE: "SHELFIQ COPILOT"
- Large AI icon
- Bidirectional arrows to all 4 stages
- Label: "Orchestrates & delivers insights"

OUTER RING - USER TOUCHPOINTS:
- Top-right: "Alerts" (bell icon)
- Right: "Dashboard" (chart icon)
- Bottom-right: "Recommendations" (star icon)
- Bottom-left: "Chat" (message icon)
- Left: "Reports" (document icon)

KEY METRICS (in small boxes):
- "< 15 min" (data freshness)
- "< 3 sec" (query response)
- "< 5 min" (alert delivery)
- "99.9%" (uptime)

STYLE:
- Use circular/radial layout
- Gradient colors for each stage (blue → purple → pink → orange)
- Thick arrows showing flow direction
- Icons inside each stage
- Clean, modern infographic style
- White background
- Add subtle glow effects to center circle

OUTPUT: High-resolution PNG, 1920x1080, suitable for presentation
```

---

## USAGE INSTRUCTIONS:

### For ChatGPT (with DALL-E):
1. Copy the entire prompt for the diagram you want
2. Paste into ChatGPT (GPT-4 with DALL-E access)
3. If the result isn't perfect, refine with: "Make the [specific element] more prominent" or "Adjust the color scheme to be more professional"

### For Other AI Image Generators:
- **Midjourney**: Simplify the prompt, focus on style keywords
- **Stable Diffusion**: Add "professional diagram, clean design, infographic style" at the end
- **Canva AI**: Use the prompt as a guide and build manually with Canva's templates

### For Manual Creation:
- Use the prompts as detailed specifications
- Tools: Figma, Sketch, PowerPoint SmartArt, Lucidchart, Draw.io
- Follow the layout and color schemes exactly as described

### Tips for Best Results:
1. Generate multiple versions and pick the best
2. You can combine AI-generated base with manual refinements
3. For PowerPoint, export as PNG and insert as image
4. Keep consistent style across all diagrams
5. Use the same color palette throughout

---

## ALTERNATIVE: SIMPLE TEXT-BASED DIAGRAMS FOR POWERPOINT

If AI generation doesn't work well, use PowerPoint SmartArt:

**Architecture Diagram**: Use "Vertical Process" SmartArt
**Process Flow**: Use "Basic Process" or "Continuous Block Process"
**Wireframes**: Use "Grid" layout with text boxes and shapes
**Data Flow**: Use "Circular Process" or "Segmented Cycle"

Add icons from PowerPoint's icon library (Insert → Icons) to enhance visual appeal.
