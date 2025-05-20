"""
Models for quality improvement and patient safety in the healthcare system.
"""

from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class QualityIndicator(BaseModel):
    """Represents a quality indicator for healthcare facilities."""
    id: str
    name: str
    category: str  # clinical, operational, patient_satisfaction
    target_value: float
    current_value: float
    unit: str  # percentage, count, score
    last_updated: datetime = Field(default_factory=datetime.now)

class PatientSafetyIncident(BaseModel):
    """Represents a patient safety incident."""
    id: str
    facility_id: str
    incident_type: str  # medication_error, infection, fall, etc.
    severity: str  # minor, moderate, severe, critical
    description: str
    date_occurred: datetime
    date_reported: datetime
    status: str  # reported, under_investigation, resolved
    resolution: Optional[str]
    preventive_measures: List[str]

class QualityImprovementPlan(BaseModel):
    """Represents a quality improvement plan."""
    id: str
    facility_id: str
    title: str
    objectives: List[str]
    indicators: List[str]  # quality indicator IDs
    start_date: datetime
    end_date: datetime
    status: str  # planned, active, completed
    progress: float = Field(ge=0, le=1)
    resources_allocated: Dict[str, float]  # resource_type -> amount
    outcomes: Optional[Dict[str, float]]  # indicator_id -> achieved_value

class Accreditation(BaseModel):
    """Represents facility accreditation status."""
    id: str
    facility_id: str
    standard: str  # JCI, ISO, national_standard
    level: str  # basic, intermediate, advanced
    valid_from: datetime
    valid_until: datetime
    status: str  # active, expired, suspended
    requirements_met: List[str]
    pending_requirements: List[str]
    audit_history: List[Dict[str, Any]]  # audit_date, findings, recommendations 