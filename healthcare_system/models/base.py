"""
Base models for the healthcare system simulation.
"""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Location(BaseModel):
    """Represents a geographical location in the healthcare system."""
    id: str
    name: str
    type: str  # district, upazila, union, ward
    population: int
    coordinates: Dict[str, float]  # latitude, longitude
    parent_id: Optional[str] = None

class Facility(BaseModel):
    """Represents a healthcare facility."""
    id: str
    name: str
    type: str  # hospital, clinic, diagnostic center, etc.
    location_id: str
    capacity: int
    staff_count: int
    equipment: Dict[str, int]  # equipment type -> count
    services: List[str]
    quality_score: float = Field(ge=0, le=1)
    operational_status: str = "active"
    last_updated: datetime = Field(default_factory=datetime.now)

class HealthcareWorker(BaseModel):
    """Represents a healthcare worker."""
    id: str
    name: str
    type: str  # doctor, nurse, technician, etc.
    specialization: Optional[str]
    facility_id: str
    experience_years: int
    qualifications: List[str]
    skills: List[str]
    performance_score: float = Field(ge=0, le=1)
    status: str = "active"

class Patient(BaseModel):
    """Represents a patient in the system."""
    id: str
    name: str
    age: int
    gender: str
    location_id: str
    insurance_status: str
    medical_history: List[Dict[str, Any]]
    current_conditions: List[str]
    socioeconomic_status: str
    last_visit: Optional[datetime]

class Treatment(BaseModel):
    """Represents a medical treatment or procedure."""
    id: str
    name: str
    type: str
    cost: float
    duration_minutes: int
    required_equipment: List[str]
    required_staff: List[str]
    success_rate: float = Field(ge=0, le=1)
    complications_rate: float = Field(ge=0, le=1)

class Resource(BaseModel):
    """Represents a healthcare resource (equipment, supplies, etc.)."""
    id: str
    name: str
    type: str
    quantity: int
    unit_cost: float
    facility_id: str
    status: str
    maintenance_schedule: Optional[Dict[str, Any]]
    last_maintenance: Optional[datetime] 