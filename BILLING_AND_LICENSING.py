"""
================================================================================
ARLREG BILLING & LICENSING SYSTEM
Subsription, Enterprise, and Revenue Management
================================================================================
"""

import json
from datetime import datetime, timedelta
from enum import Enum


class LicenseType(Enum):
    FREE = "free"
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    ACADEMIC = "academic"


class BillingManager:
    """
    Manages all subscription, licensing, and revenue operations for ARLREG
    """
    
    def __init__(self):
        self.pricing_tiers = {
            LicenseType.FREE: {
                "name": "Free Tier",
                "monthly_cost": 0,
                "api_requests": 1_000,
                "support": "Community",
                "features": [
                    "Core ARLREG validation",
                    "Red Letter protocol access",
                    "GitHub community support"
                ]
            },
            LicenseType.STARTER: {
                "name": "Starter",
                "monthly_cost": 99,
                "api_requests": 100_000,
                "support": "Email (24-48hr response)",
                "features": [
                    "All Free features",
                    "100K API requests/month",
                    "Priority email support",
                    "Slack integration",
                    "Usage analytics dashboard"
                ]
            },
            LicenseType.PROFESSIONAL: {
                "name": "Professional",
                "monthly_cost": 499,
                "api_requests": 10_000_000,
                "support": "Priority (4-hour response)",
                "features": [
                    "All Starter features",
                    "10M API requests/month",
                    "Phone & chat support",
                    "Custom rules development",
                    "API rate limiting: 10K/min",
                    "99.9% SLA",
                    "Advanced analytics",
                    "Monthly strategy consultation"
                ]
            },
            LicenseType.ENTERPRISE: {
                "name": "Enterprise",
                "monthly_cost": "Custom",
                "api_requests": "Unlimited",
                "support": "24/7 Dedicated Account Manager",
                "features": [
                    "All Professional features",
                    "Unlimited API requests",
                    "Dedicated 24/7 support",
                    "Custom SLA (99.99%+)",
                    "On-premise deployment option",
                    "Quarterly business reviews",
                    "Custom integration",
                    "Compliance & audit reports",
                    "White-label options",
                    "Priority feature requests"
                ]
            },
            LicenseType.ACADEMIC: {
                "name": "Academic (Free)",
                "monthly_cost": 0,
                "api_requests": 1_000_000,
                "support": "Community + Academic support",
                "features": [
                    "All Free features",
                    "1M API requests/month",
                    "Academic support channel",
                    "Research collaboration",
                    "Published research usage"
                ]
            }
        }

    def get_pricing_table(self):
        """Return complete pricing structure"""
        pricing = {}
        for license_type, details in self.pricing_tiers.items():
            pricing[license_type.value] = details
        return pricing

    def calculate_monthly_revenue(self, subscribers):
        """
        Calculate projected monthly revenue
        
        Args:
            subscribers: Dict of {license_type: count}
        """
        total = 0
        breakdown = {}
        
        for license_type, count in subscribers.items():
            price = self.pricing_tiers[license_type]["monthly_cost"]
            if isinstance(price, int):
                tier_revenue = price * count
                total += tier_revenue
                breakdown[license_type.value] = tier_revenue
            else:
                breakdown[license_type.value] = "Custom"
        
        return {"total": total, "breakdown": breakdown}

    def generate_invoice(self, customer_id, license_type, period_start, period_end):
        """Generate subscription invoice"""
        tier = self.pricing_tiers[license_type]
        cost = tier["monthly_cost"]
        
        return {
            "invoice_id": f"INV-{customer_id}-{datetime.now().timestamp()}",
            "customer_id": customer_id,
            "license_type": license_type.value,
            "period": f"{period_start} to {period_end}",
            "amount": cost,
            "features": tier["features"],
            "api_limit": tier["api_requests"],
            "support_tier": tier["support"],
            "due_date": (datetime.now() + timedelta(days=30)).isoformat(),
            "status": "issued",
            "timestamp": datetime.now().isoformat()
        }


class EnterpriseContractTemplate:
    """
    Generate custom enterprise contracts with specific terms
    """
    
    @staticmethod
    def create_contract(company_name, annual_value, deployment_type, support_level):
        """Generate enterprise contract"""
        return {
            "contract_type": "Enterprise Service Agreement (ESA)",
            "company": company_name,
            "annual_value": annual_value,
            "term_months": 12,
            "deployment": deployment_type,  # cloud, on-premise, hybrid
            "support": support_level,  # standard, premium, vip
            "features": {
                "api_requests": "Unlimited",
                "concurrent_validations": "Unlimited",
                "custom_rules": "Yes",
                "sso_integration": "Yes",
                "audit_logging": "Yes",
                "compliance_reporting": "Yes",
                "dedicated_infrastructure": deployment_type == "on-premise",
                "data_residency": "Customizable"
            },
            "support_terms": {
                "response_time": "1 hour" if support_level == "vip" else "4 hours",
                "availability": "24/7" if support_level in ["premium", "vip"] else "Business hours",
                "dedicated_account_manager": support_level in ["premium", "vip"],
                "quarterly_reviews": True
            },
            "sla": {
                "uptime": "99.99%",
                "credit_multiplier": 5 if support_level == "vip" else 3,
                "incident_response": "30 minutes"
            },
            "payment_terms": {
                "frequency": "Annual",
                "due_on_signing": True,
                "volume_discounts": "Available"
            },
            "renewal_terms": {
                "auto_renewal": True,
                "renewal_notice": "90 days",
                "price_adjustment": "CPI + 3% max"
            }
        }


class RevenueForecast:
    """
    Project revenue and growth metrics
    """
    
    @staticmethod
    def project_24_months():
        """Return 24-month revenue forecast"""
        return {
            "month_1_3": {
                "period": "Months 1-3: Foundation",
                "free_users": 500,
                "paid_subscribers": 5,
                "monthly_revenue": 2_000,
                "quarterly_total": 6_000
            },
            "month_4_6": {
                "period": "Months 4-6: Early Adoption",
                "free_users": 2_000,
                "paid_subscribers": 25,
                "monthly_revenue": 20_000,
                "quarterly_total": 60_000
            },
            "month_7_9": {
                "period": "Months 7-9: Growth Phase",
                "free_users": 5_000,
                "paid_subscribers": 100,
                "monthly_revenue": 75_000,
                "quarterly_total": 225_000
            },
            "month_10_12": {
                "period": "Months 10-12: Acceleration",
                "free_users": 10_000,
                "paid_subscribers": 200,
                "monthly_revenue": 200_000,
                "quarterly_total": 600_000,
                "annual_total": 891_000
            },
            "month_13_18": {
                "period": "Months 13-18: Scale",
                "free_users": 50_000,
                "paid_subscribers": 500,
                "monthly_revenue": 500_000,
                "six_month_total": 3_000_000
            },
            "month_19_24": {
                "period": "Months 19-24: Maturity",
                "free_users": 100_000,
                "paid_subscribers": 1_000,
                "enterprise_contracts": 20,
                "monthly_revenue": 1_500_000,
                "six_month_total": 9_000_000,
                "two_year_total": 12_891_000
            }
        }


# EXPORT
if __name__ == "__main__":
    billing = BillingManager()
    
    print("\n=== ARLREG PRICING TIERS ===")
    print(json.dumps(billing.get_pricing_table(), indent=2, default=str))
    
    print("\n=== 24-MONTH REVENUE FORECAST ===")
    print(json.dumps(RevenueForecast.project_24_months(), indent=2))
    
    print("\n=== ENTERPRISE CONTRACT EXAMPLE ===")
    contract = EnterpriseContractTemplate.create_contract(
        company_name="TechCorp Inc",
        annual_value=500_000,
        deployment_type="on-premise",
        support_level="vip"
    )
    print(json.dumps(contract, indent=2))
