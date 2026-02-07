def calculate_net_yield(purchase_price, annual_rent, service_charge_sqft, area_sqft, dld_fee_pct=4):
    """
    Calculate Net Rental Yield for a Dubai Property.
    
    Args:
        purchase_price (float): Total cost of property (AED)
        annual_rent (float): Yearly rental income (AED)
        service_charge_sqft (float): Service charge per sqft (AED)
        area_sqft (float): Total area in sqft
        dld_fee_pct (float): Dubai Land Department fee (default 4%)
        
    Returns:
        float: Net Yield Percentage rounded to 2 decimals
    """
    
    # One-time costs
    dld_fee = purchase_price * (dld_fee_pct / 100)
    trustee_fee = 4200 # Standard approx
    total_acquisition_cost = purchase_price + dld_fee + trustee_fee
    
    # Recurring annual costs
    annual_service_charge = service_charge_sqft * area_sqft
    maintenance_reserve = annual_rent * 0.05 # 5% reserve for repairs
    
    # Net Income
    net_income = annual_rent - annual_service_charge - maintenance_reserve
    
    # Yield Calculation
    net_yield = (net_income / total_acquisition_cost) * 100
    
    return round(net_yield, 2)

if __name__ == "__main__":
    # Test Case: 1BHK in Business Bay
    price = 1_500_000
    rent = 110_000
    sc = 18
    area = 850
    
    y = calculate_net_yield(price, rent, sc, area)
    print(f"Property Price: AED {price:,}")
    print(f"Annual Rent:    AED {rent:,}")
    print(f"Net Yield:      {y}%")
