from pydantic import BaseModel

class TaxProfile(BaseModel):
    income: float
    deductions: float
    marital_status: str

class TaxResult(BaseModel):
    tax_owed: float
    tax_refund: float
    effective_tax_rate: float
