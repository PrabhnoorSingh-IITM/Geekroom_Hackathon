# How to Use the E-Commerce Intelligence Agent

A step-by-step guide for non-technical users.

---

##  Getting Started

### What You'll See When You Open the Page

1. **Engaging Hero Section** – "E-Commerce Intelligence Agent" with a brief description
2. **3-Step Onboarding Tour** – Visual cards explaining:
   - Step 1: Tell us your goal
   - Step 2: Choose your data
   - Step 3: Get smart insights
3. **"Start Your Analysis" Button** – Click here to jump to the interactive dashboard

---

##  The Three-Panel Dashboard

Once you click "Start Your Analysis", you'll see three panels:

### **Left Panel: Analysis Setup**
This is where you define what you want to analyze.

**Fields:**
- **Mode**: Choose between:
  - **Quick** (faster, ~2 minutes) – Get fast answers
  - **Deep** (thorough, ~10 minutes) – Get comprehensive strategy
  
- **Business Goal**: What matters most to you?
  - Growth – Expand your market presence
  - Retention – Keep existing customers happy
  - Profitability – Maximize margins
  - Market Expansion – Enter new markets

- **Scope Type**: Are you analyzing a specific product or category?
  - **SKU** – A single product (e.g., "SKU-472")
  - **Category** – A group of products (e.g., "Bluetooth Earbuds")

- **Scope Value**: Enter your product/category name

- **Marketplace**: Where are you selling?
  - (e.g., "Amazon", "Flipkart", "Your Store")

- **Region**: Geographic focus
  - (e.g., "India", "US", "Europe")

- **Timeframe**: Time period for analysis
  - (e.g., "Last 30 days", "Last quarter")

**Buttons:**
- **"Run Analysis"** – Submit your query and get results
- **"Load Demo Values"** – Instantly fill with sample data to see how it works

---

### **Center Panel: Data Sources**
Choose where to get your data from.

#### Option 1: Use Sample Data (Recommended for First-Time Users)
- Select **"Sample datasets"** radio button
- Our pre-loaded datasets include:
  - Catalog (product info)
  - Reviews (customer feedback)
  - Pricing (your & competitors' prices)
  - Competitors (competitive landscape)
  - Performance (sales & conversion data)
- Click "Run Analysis" – that's it!

#### Option 2: Upload Your Own CSVs
- Select **"Upload CSVs"** radio button
- Click the upload area or drag and drop CSV files
- **Supported columns** (our system auto-detects):
  - **Catalog**: sku, category, price, stock
  - **Reviews**: sku, rating, text
  - **Pricing**: sku, our_price, competitor_price
  - **Competitors**: competitor, sku, features
  - **Performance**: sku, views, conversions

- The system will:
  - Parse your files automatically
  - Show you if any required columns are missing
  - Map your data to the right categories

---

### **Right Panel: Research Output**
Your insights and recommendations appear here.

**What You'll See:**

1. **Two Key Metrics**
   - **Confidence Score** (0-100%)
     - Green (75%+) = High confidence in findings
     - Yellow (50-74%) = Medium confidence
     - Red (<50%) = Low confidence (more data needed)
   - **Completeness** (0-100%)
     - Shows if you have enough data to make decisions
     - Higher is better

2. **Risk Flags**
   - Common issues flagged:
     - Missing price data for competitors
     - Low review volume
     - Incomplete sales data
     - Seasonal trends not accounted for
   - Use these to understand data limitations

3. **Strategic Recommendations**
   - Actionable insights specific to your goal
   - Prioritized by impact and evidence
   - Examples:
     - "Reduce price by 5% to match Category leader"
     - "Increase reviews by highlighting positive feedback"
     - "Target premium buyers with feature education"

4. **Full Report**
   - Detailed markdown report with:
     - Executive summary
     - Detailed findings
     - Competitive analysis
     - Risk assessment
     - Implementation steps
   - Scroll down to read the complete analysis

---

##  Real-World Example

### Scenario: You Sell Wireless Earbuds on Amazon

**Your Setup:**
- Mode: **Quick** (you need fast answers)
- Business Goal: **Profitability** (reduce costs, improve margins)
- Scope Type: **Category**
- Scope Value: **Wireless Earbuds**
- Marketplace: **Amazon**
- Region: **India**
- Timeframe: **Last 30 days**
- Data: **Sample datasets** (quick start)

**Click "Run Analysis"** → Wait 30-60 seconds

**You Get:**
```
Confidence: 82% (High) 
Completeness: 78% (Good)

 Risk Flags:
- Competitor pricing updated recently (monitor daily)
- Limited review volume for budget models
- Seasonal demand variance in Q4

 Strategic Recommendations:
1. Price positioning: Drop price to ₹3,499 (match competitor XYZ)
2. Review generation: Incentivize 5-star reviews (currently 4.1 avg)
3. Feature focus: Highlight 6-hour battery (vs 4-hour average)
4. Margin optimization: Source new supplier for 15% cost savings

Full Report: [Detailed 3-page analysis...]
```

---

##  Quick Tips

### For Fastest Results
- Use **Quick Mode** + **Sample Data**
- Takes ~30 seconds total
- Great for testing and demos

### For Best Insights
- Use **Deep Mode** with **Your Own Data**
- Takes ~10 minutes but much more accurate
- Personalized to your market

### Understanding Confidence Scores
| Confidence | Meaning | Action |
|-----------|---------|--------|
| 75-100% | High | Trust the recommendations |
| 50-74% | Medium | Recommendations are directional; verify key assumptions |
| <50% | Low | Need more/better data before deciding |

### Common Issues & Solutions

**"Confidence is too low (30%)"**
- You don't have enough data
- Solution: Upload more datasets or use a longer timeframe

**"My risk flags seem random"**
- The agent is flagging missing data
- Solution: Upload complete datasets with all columns

**"The recommendations don't make sense"**
- The agent may be finding patterns in incomplete data
- Solution: Verify your data quality; use deep mode for more context

---

##  Typical Workflows

### Workflow 1: Quick Competitive Check (5 minutes)
1. Load demo data
2. Set mode to "Quick"
3. Change goal to your current focus
4. Read recommendations
5. Done!

### Workflow 2: Deep Strategic Analysis (30 minutes)
1. Export your product, review, and pricing data
2. Open data sources tab
3. Upload CSVs
4. Set mode to "Deep"
5. Run analysis
6. Read full report
7. Export insights for team discussion

### Workflow 3: Ongoing Monitoring (weekly)
1. Export last week's data
2. Upload to analysis panel
3. Monitor confidence and completeness trends
4. Track how recommendations perform

---

##  Privacy & Data

- **No API key needed** – Direct connection to your local API
- **Data stays local** – No cloud uploads unless you choose
- **Processing** – Runs in-browser and in your backend
- **Storage** – Results cached locally for future comparisons

---

##  Support Tips

### Before Asking for Help
1. Check your data columns match expected names
2. Try demo data first to confirm system works
3. Note the confidence score and risk flags

### What to Include When Reporting Issues
1. What you were trying to do
2. Which mode (Quick/Deep) and goal (Growth/Retention/etc)
3. Sample data or data structure
4. Error message (if any)
5. Confidence score of the failing analysis

---

##  Understanding the Science Behind the Agent

**How the Agent Works:**

1. **Metric Computation** – Calculates ratings, price gaps, conversions
2. **Gap Analysis** – Compares your product to competitors
3. **Risk Detection** – Flags missing data and outliers
4. **Confidence Scoring** – Rates how trustworthy findings are
5. **Recommendation Generation** – Produces 3-5 actionable items
6. **Memory** – Learns from your history over time

**Why Some Data is Required:**
- **Catalog** – Understand what you're selling
- **Reviews** – Understand customer sentiment
- **Pricing** – Competitive positioning
- **Performance** – Validate recommendations with real metrics

**Quality Improves When You Add:**
- Longer timeframes (1 month → 6 months)
- More detailed product data
- Customer demographic info
- Inventory and stockout data
- Return and churn rates

---

##  Advanced: Using the Demo

Click **"Load Demo Values"** to automatically fill in an example about Bluetooth Earbuds. This is perfect for:
- Testing the system before uploading your data
- Understanding what good outputs look like
- Training team members
- Quick demos to stakeholders

The demo uses pre-loaded sample data that represents a realistic e-commerce scenario.

---

**Ready to get started?** Click "Start Your Analysis" above and choose your analysis parameters. The agent will handle the rest! 
