"""
Test cases for the healthcare system simulation.
"""

import pytest
from datetime import datetime, timedelta
from ..simulation.core import HealthcareSystemSimulation
from ..data.generator import DataGenerator
from ..models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)

@pytest.fixture
def simulation():
    """Create a simulation instance for testing."""
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)  # One day simulation for testing
    return HealthcareSystemSimulation(start_date, end_date)

@pytest.fixture
def generator():
    """Create a data generator instance for testing."""
    return DataGenerator()

def test_simulation_initialization(simulation):
    """Test simulation initialization."""
    assert simulation.start_date == datetime(2023, 1, 1)
    assert simulation.end_date == datetime(2023, 1, 2)
    assert simulation.current_date == datetime(2023, 1, 1)
    assert isinstance(simulation.locations, dict)
    assert isinstance(simulation.facilities, dict)
    assert isinstance(simulation.healthcare_workers, dict)
    assert isinstance(simulation.patients, dict)
    assert isinstance(simulation.treatments, dict)
    assert isinstance(simulation.resources, dict)
    assert isinstance(simulation.metrics, dict)

def test_add_location(simulation, generator):
    """Test adding a location to the simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    assert location.id in simulation.locations
    assert simulation.locations[location.id] == location

def test_add_facility(simulation, generator):
    """Test adding a facility to the simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    assert facility.id in simulation.facilities
    assert simulation.facilities[facility.id] == facility

def test_add_healthcare_worker(simulation, generator):
    """Test adding a healthcare worker to the simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    worker = generator.generate_healthcare_worker(facility.id)
    simulation.add_healthcare_worker(worker)
    assert worker.id in simulation.healthcare_workers
    assert simulation.healthcare_workers[worker.id] == worker

def test_add_patient(simulation, generator):
    """Test adding a patient to the simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    patient = generator.generate_patient(location.id)
    simulation.add_patient(patient)
    assert patient.id in simulation.patients
    assert simulation.patients[patient.id] == patient

def test_add_treatment(simulation, generator):
    """Test adding a treatment to the simulation."""
    treatment = generator.generate_treatment()
    simulation.add_treatment(treatment)
    assert treatment.id in simulation.treatments
    assert simulation.treatments[treatment.id] == treatment

def test_add_resource(simulation, generator):
    """Test adding a resource to the simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    resource = generator.generate_resource(facility.id)
    simulation.add_resource(resource)
    assert resource.id in simulation.resources
    assert simulation.resources[resource.id] == resource

def test_calculate_facility_utilization(simulation, generator):
    """Test facility utilization calculation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    utilization = simulation.calculate_facility_utilization(facility.id)
    assert 0.3 <= utilization <= 0.9

def test_calculate_healthcare_quality(simulation, generator):
    """Test healthcare quality calculation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    worker = generator.generate_healthcare_worker(facility.id)
    simulation.add_healthcare_worker(worker)
    quality = simulation.calculate_healthcare_quality(facility.id)
    assert 0 <= quality <= 1

def test_simulate_patient_flow(simulation, generator):
    """Test patient flow simulation."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    patient = generator.generate_patient(location.id)
    simulation.add_patient(patient)
    simulation.simulate_patient_flow()
    # Patient's last_visit should be updated if they needed care
    assert patient.last_visit is not None

def test_update_metrics(simulation, generator):
    """Test metrics update."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    simulation.update_metrics()
    assert "facility_utilization" in simulation.metrics
    assert "healthcare_quality" in simulation.metrics

def test_simulation_step(simulation, generator):
    """Test simulation step."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    patient = generator.generate_patient(location.id)
    simulation.add_patient(patient)
    initial_date = simulation.current_date
    simulation.step()
    assert simulation.current_date == initial_date + timedelta(days=1)

def test_simulation_run(simulation, generator):
    """Test complete simulation run."""
    location = generator.generate_location()
    simulation.add_location(location)
    facility = generator.generate_facility(location.id)
    simulation.add_facility(facility)
    patient = generator.generate_patient(location.id)
    simulation.add_patient(patient)
    simulation.run()
    assert simulation.current_date == simulation.end_date
    assert len(simulation.metrics["facility_utilization"]) > 0
    assert len(simulation.metrics["healthcare_quality"]) > 0 