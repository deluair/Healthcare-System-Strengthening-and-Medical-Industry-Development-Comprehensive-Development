"""
Test cases for the healthcare system simulation components.
"""

import pytest
from datetime import datetime
from ..simulation.components import (
    HealthcareInfrastructure, WorkforceDevelopment,
    HealthcareFinancing, DigitalHealth, MedicalTourism
)
from ..models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)

@pytest.fixture
def infrastructure():
    """Create a healthcare infrastructure instance for testing."""
    return HealthcareInfrastructure()

@pytest.fixture
def workforce():
    """Create a workforce development instance for testing."""
    return WorkforceDevelopment()

@pytest.fixture
def financing():
    """Create a healthcare financing instance for testing."""
    return HealthcareFinancing()

@pytest.fixture
def digital_health():
    """Create a digital health instance for testing."""
    return DigitalHealth()

@pytest.fixture
def medical_tourism():
    """Create a medical tourism instance for testing."""
    return MedicalTourism()

@pytest.fixture
def sample_facility():
    """Create a sample facility for testing."""
    return Facility(
        id="test_facility",
        name="Test Hospital",
        type="hospital",
        location_id="test_location",
        capacity=100,
        staff_count=20,
        equipment={"xray": 2, "mri": 1},
        services=["general", "emergency"],
        quality_score=0.8
    )

@pytest.fixture
def sample_worker():
    """Create a sample healthcare worker for testing."""
    return HealthcareWorker(
        id="test_worker",
        name="Dr. Test",
        type="doctor",
        specialization="general",
        facility_id="test_facility",
        experience_years=5,
        qualifications=["MBBS", "MD"],
        skills=["diagnosis", "treatment"],
        performance_score=0.9
    )

@pytest.fixture
def sample_patient():
    """Create a sample patient for testing."""
    return Patient(
        id="test_patient",
        name="John Doe",
        age=30,
        gender="male",
        location_id="test_location",
        insurance_status="insured",
        medical_history=[],
        current_conditions=["fever"],
        socioeconomic_status="middle"
    )

def test_healthcare_infrastructure(infrastructure, sample_facility):
    """Test healthcare infrastructure functionality."""
    infrastructure.add_facility(sample_facility)
    assert sample_facility.id in infrastructure.facilities
    assert sample_facility.id in infrastructure.maintenance_schedule
    
    utilization = infrastructure.get_facility_utilization(sample_facility.id)
    assert 0 <= utilization <= 1

def test_workforce_development(workforce, sample_worker):
    """Test workforce development functionality."""
    workforce.add_worker(sample_worker)
    assert sample_worker.id in workforce.workers
    
    workforce.assign_training(sample_worker.id, "advanced_care")
    qualifications = workforce.get_worker_qualifications(sample_worker.id)
    assert "advanced_care" in qualifications

def test_healthcare_financing(financing, sample_patient):
    """Test healthcare financing functionality."""
    financing.set_insurance_coverage(sample_patient.id, 0.8)
    assert financing.insurance_coverage[sample_patient.id] == 0.8
    
    financing.allocate_funding("test_facility", 1000000)
    assert financing.facility_funding["test_facility"] == 1000000
    
    cost = financing.calculate_patient_cost(sample_patient.id, 1000)
    assert cost == 200  # 20% of original cost

def test_digital_health(digital_health, sample_patient):
    """Test digital health functionality."""
    digital_health.record_telemedicine_session(sample_patient.id)
    assert len(digital_health.telemedicine_sessions[sample_patient.id]) == 1
    
    record = {"diagnosis": "fever", "treatment": "rest"}
    digital_health.update_electronic_record(sample_patient.id, record)
    history = digital_health.get_patient_history(sample_patient.id)
    assert history["diagnosis"] == "fever"

def test_medical_tourism(medical_tourism, sample_patient):
    """Test medical tourism functionality."""
    medical_tourism.register_international_patient(sample_patient)
    assert sample_patient.id in medical_tourism.international_patients
    
    medical_tourism.add_export_service("test_facility", "cardiac_surgery")
    services = medical_tourism.get_available_services("test_facility")
    assert "cardiac_surgery" in services 