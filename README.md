# Real Estate Insights & Analytics 🏢📊

A collection of data structures, ROI calculators, and market analysis tools for the UAE (Dubai) and Indian real estate markets.

## 🚀 Features

- **ROI Calculator (Dubai):** Compute Net Rental Yields factoring in Service Charges and DLD fees.
- **Market Data Structures:** JSON schemas for tracking off-plan launches across Emaar, Damac, DLF, etc.
- **Payment Plan Analyzer:** Compare 60/40 vs 50/50 vs Post-Handover plans.

## 📂 Project Structure

- `calculators/` - Python scripts for yield and mortgage calculations.
- `data/` - JSON/CSV datasets for market tracking.
- `docs/` - Analysis of micro-markets (Business Bay, Downtown, Gurgaon).

## 🛠️ Usage

```python
from calculators.roi import calculate_net_yield

# Example: calculate yield for a 1BHK in Business Bay
yield_pct = calculate_net_yield(
    purchase_price=1500000,  # AED
    annual_rent=120000,      # AED
    service_charge_sqft=18,  # AED/sqft
    area_sqft=800
)
print(f"Net Yield: {yield_pct}%")
```

## 👨‍💻 Author

**Abhijeet Pandey**
*Tech & Real Estate Enthusiast*
