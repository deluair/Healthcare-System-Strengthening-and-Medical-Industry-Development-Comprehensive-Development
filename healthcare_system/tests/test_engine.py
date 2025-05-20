"""
Test cases for the healthcare system simulation engine.
"""

import pytest
from datetime import datetime, timedelta
from ..simulation.engine import SimulationEngine
from ..models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)

@pytest.fixture
def engine():
    """Create a simulation engine instance for testing."""
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)  # One day simulation for testing
    return SimulationEngine(start_date, end_date)

@pytest.fixture
def sample_location():
    """Create a sample location for testing."""
    return Location(
        id="test_location",
        name="Test District",
        type="district",
        population=100000,
        coordinates={"latitude": 23.7, "longitude": 90.4}
    )

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

def test_engine_initialization(engine):
    """Test simulation engine initialization."""
    assert engine.start_date == datetime(2023, 1, 1)
    assert engine.end_date == datetime(2023, 1, 2)
    assert engine.current_date == datetime(2023, 1, 1)
    assert isinstance(engine.metrics, dict)
    assert "facility_utilization" in engine.metrics
    assert "healthcare_quality" in engine.metrics
    assert "insurance_coverage" in engine.metrics
    assert "digital_health_adoption" in engine.metrics

def test_add_location(engine, sample_location):
    """Test adding a location to the simulation."""
    engine.add_location(sample_location)
    assert sample_location.id in engine.locations
    assert engine.locations[sample_location.id] == sample_location

def test_add_facility(engine, sample_facility):
    """Test adding a facility to the simulation."""
    engine.add_facility(sample_facility)
    assert sample_facility.id in engine.infrastructure.facilities
    assert engine.financing.facility_funding[sample_facility.id] == 1000000

def test_add_healthcare_worker(engine, sample_worker):
    """Test adding a healthcare worker to the simulation."""
    engine.add_healthcare_worker(sample_worker)
    assert sample_worker.id in engine.workforce.workers
    assert "basic_healthcare" in engine.workforce.training_programs[sample_worker.id]

def test_add_patient(engine, sample_patient):
    """Test adding a patient to the simulation."""
    engine.add_patient(sample_patient)
    assert sample_patient.id in engine.financing.insurance_coverage
    assert engine.financing.insurance_coverage[sample_patient.id] == 0.7
    assert sample_patient.id in engine.digital_health.electronic_records

def test_simulate_facility_operations(engine, sample_facility, sample_worker):
    """Test facility operations simulation."""
    engine.add_facility(sample_facility)
    engine.add_healthcare_worker(sample_worker)
    engine.simulate_facility_operations()
    
    assert len(engine.metrics["facility_utilization"]) > 0
    assert len(engine.metrics["healthcare_quality"]) > 0

def test_simulate_patient_care(engine, sample_patient):
    """Test patient care simulation."""
    engine.add_patient(sample_patient)
    engine.simulate_patient_care()
    
    # Check if telemedicine session was recorded
    assert sample_patient.id in engine.digital_health.telemedicine_sessions

def test_simulate_workforce_development(engine, sample_worker):
    """Test workforce development simulation."""
    engine.add_healthcare_worker(sample_worker)
    engine.simulate_workforce_development()
    
    # Check if additional training was assigned
    assert len(engine.workforce.training_programs[sample_worker.id]) >= 1

def test_calculate_metrics(engine, sample_patient):
    """Test metrics calculation."""
    engine.add_patient(sample_patient)
    engine.calculate_metrics()
    
    assert len(engine.metrics["insurance_coverage"]) > 0
    assert len(engine.metrics["digital_health_adoption"]) > 0

def test_simulation_step(engine, sample_facility, sample_worker, sample_patient):
    """Test simulation step."""
    engine.add_facility(sample_facility)
    engine.add_healthcare_worker(sample_worker)
    engine.add_patient(sample_patient)
    
    initial_date = engine.current_date
    engine.step()
    
    assert engine.current_date == initial_date + timedelta(days=1)
    assert len(engine.metrics["facility_utilization"]) > 0
    assert len(engine.metrics["healthcare_quality"]) > 0
    assert len(engine.metrics["insurance_coverage"]) > 0
    assert len(engine.metrics["digital_health_adoption"]) > 0

def test_get_facility_summary(engine, sample_facility, sample_worker):
    """Test facility summary generation."""
    engine.add_facility(sample_facility)
    engine.add_healthcare_worker(sample_worker)
    
    summary = engine.get_facility_summary(sample_facility.id)
    assert "utilization" in summary
    assert "quality" in summary
    assert "funding" in summary

def test_get_patient_summary(engine, sample_patient):
    """Test patient summary generation."""
    engine.add_patient(sample_patient)
    
    summary = engine.get_patient_summary(sample_patient.id)
    assert "insurance_coverage" in summary
    assert "telemedicine_sessions" in summary
    assert "health_record" in summary 