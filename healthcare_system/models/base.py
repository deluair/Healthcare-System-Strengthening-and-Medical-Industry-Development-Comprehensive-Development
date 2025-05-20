"""
Base models for the healthcare system simulation.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass
class Location:
    """Represents a geographical location in the healthcare system."""
    id: str
    name: str
    type: str  # city, district, etc.
    population: int
    coordinates: Dict[str, float]  # latitude, longitude

@dataclass
class Facility:
    """Represents a healthcare facility."""
    id: str
    name: str
    type: str  # hospital, clinic, etc.
    location_id: str
    capacity: int
    staff_count: int
    equipment: Dict[str, int]  # equipment type -> count
    services: List[str]
    quality_score: float  # 0.0 to 1.0

@dataclass
class HealthcareWorker:
    """Represents a healthcare worker."""
    id: str
    name: str
    type: str  # doctor, nurse, etc.
    specialization: str
    facility_id: str
    experience_years: int
    qualifications: List[str]
    skills: List[str]
    performance_score: float  # 0.0 to 1.0

@dataclass
class Patient:
    """Represents a patient in the healthcare system."""
    id: str
    name: str
    age: int
    gender: str
    location_id: str
    insurance_status: str  # insured, uninsured
    medical_history: List[str]
    current_conditions: List[str]
    socioeconomic_status: str  # low, middle, high

@dataclass
class Treatment:
    """Represents a medical treatment."""
    id: str
    name: str
    type: str
    cost: float
    duration: int  # in days
    success_rate: float  # 0.0 to 1.0
    required_equipment: List[str]
    required_skills: List[str]

@dataclass
class Resource:
    """Represents a healthcare resource."""
    id: str
    name: str
    type: str  # medicine, equipment, etc.
    quantity: int
    cost: float
    facility_id: str
    expiry_date: Optional[str] = None  # for medicines 