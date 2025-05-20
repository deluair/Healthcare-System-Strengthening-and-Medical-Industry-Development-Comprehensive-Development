"""
Models for the pharmaceutical industry in the healthcare system.
"""

from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class PharmaceuticalProduct(BaseModel):
    """Represents a pharmaceutical product."""
    id: str
    name: str
    type: str  # drug, vaccine, medical_device
    manufacturer: str
    registration_number: str
    approval_date: datetime
    expiry_date: Optional[datetime]
    ingredients: List[str]
    dosage_form: str
    strength: str
    storage_conditions: Dict[str, Any]
    price: float
    status: str  # approved, pending, suspended
    market_availability: float = Field(ge=0, le=1)

class ManufacturingFacility(BaseModel):
    """Represents a pharmaceutical manufacturing facility."""
    id: str
    name: str
    location_id: str
    type: str  # API, formulation, packaging
    capacity: Dict[str, float]  # product_type -> production_capacity
    current_utilization: float
    certifications: List[str]  # GMP, ISO, etc.
    quality_control_labs: int
    production_lines: int
    status: str  # active, maintenance, suspended
    compliance_score: float = Field(ge=0, le=1)

class SupplyChain(BaseModel):
    """Represents pharmaceutical supply chain information."""
    id: str
    product_id: str
    manufacturer_id: str
    distribution_centers: List[str]
    inventory_levels: Dict[str, int]  # location_id -> quantity
    lead_time: int  # days
    reorder_point: int
    safety_stock: int
    status: str  # normal, disrupted, critical
    last_updated: datetime = Field(default_factory=datetime.now)

class ResearchProject(BaseModel):
    """Represents a pharmaceutical research project."""
    id: str
    title: str
    type: str  # drug_development, clinical_trial, etc.
    start_date: datetime
    end_date: Optional[datetime]
    budget: float
    current_expenditure: float
    team_size: int
    objectives: List[str]
    milestones: List[Dict[str, Any]]  # description, target_date, status
    status: str  # planning, active, completed
    outcomes: Optional[Dict[str, Any]]

class QualityControl(BaseModel):
    """Represents quality control testing for pharmaceutical products."""
    id: str
    product_id: str
    facility_id: str
    test_type: str  # stability, potency, purity, etc.
    test_date: datetime
    parameters: Dict[str, float]  # parameter -> value
    specifications: Dict[str, float]  # parameter -> acceptable_range
    results: Dict[str, Any]  # parameter -> {value, status}
    status: str  # passed, failed, pending
    reviewer: str
    review_date: Optional[datetime] 