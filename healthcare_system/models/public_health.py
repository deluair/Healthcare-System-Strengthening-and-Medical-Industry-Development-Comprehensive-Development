"""
Models for public health and preventive services in the healthcare system.
"""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

class DiseaseSurveillance(BaseModel):
    """Represents disease surveillance data."""
    id: str
    disease_name: str
    location_id: str
    cases_reported: int
    cases_confirmed: int
    cases_recovered: int
    cases_fatal: int
    date_reported: datetime
    risk_level: str  # low, moderate, high, critical
    transmission_rate: float
    preventive_measures: List[str]
    vaccination_coverage: Optional[float]

class VaccinationProgram(BaseModel):
    """Represents a vaccination program."""
    id: str
    name: str
    target_disease: str
    target_population: str  # age_group, risk_group, etc.
    start_date: datetime
    end_date: datetime
    coverage_target: float
    current_coverage: float
    facilities_involved: List[str]
    resources_allocated: Dict[str, float]
    status: str  # planned, active, completed
    outcomes: Optional[Dict[str, float]]

class HealthCampaign(BaseModel):
    """Represents a public health campaign."""
    id: str
    title: str
    objective: str
    target_audience: str
    start_date: datetime
    end_date: datetime
    location_id: str
    activities: List[Dict[str, Any]]  # activity_type, description, resources_needed
    budget: float
    resources_allocated: Dict[str, float]
    status: str  # planned, active, completed
    outcomes: Optional[Dict[str, Any]]

class PreventiveService(BaseModel):
    """Represents a preventive healthcare service."""
    id: str
    name: str
    type: str  # screening, vaccination, health_education
    target_population: str
    facility_id: str
    schedule: Dict[str, Any]  # frequency, timing, duration
    capacity: int
    current_utilization: float
    cost: float
    effectiveness_score: float = Field(ge=0, le=1)
    status: str  # active, suspended, discontinued
    outcomes: Optional[Dict[str, float]] 