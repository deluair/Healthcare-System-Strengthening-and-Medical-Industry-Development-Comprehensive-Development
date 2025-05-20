"""
Core simulation module for the healthcare system.
"""

import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from ..models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)
from .components import (
    HealthcareInfrastructure, WorkforceDevelopment,
    HealthcareFinancing, DigitalHealth, MedicalTourism
)

class HealthcareSystemSimulation:
    """Main simulation class for the healthcare system."""
    
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = start_date
        self.locations: Dict[str, Location] = {}
        
        # Initialize components
        self.infrastructure = HealthcareInfrastructure()
        self.workforce = WorkforceDevelopment()
        self.financing = HealthcareFinancing()
        self.digital_health = DigitalHealth()
        self.medical_tourism = MedicalTourism()
        
        self.metrics: Dict[str, List[Tuple[datetime, float]]] = {}
        
    def add_location(self, location: Location) -> None:
        """Add a location to the simulation."""
        self.locations[location.id] = location
        
    def add_facility(self, facility: Facility) -> None:
        """Add a healthcare facility to the simulation."""
        self.infrastructure.add_facility(facility)
        
    def add_healthcare_worker(self, worker: HealthcareWorker) -> None:
        """Add a healthcare worker to the simulation."""
        self.workforce.add_worker(worker)
        
    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the simulation."""
        # Set default insurance coverage
        self.financing.set_insurance_coverage(patient.id, 0.7)
        
    def add_treatment(self, treatment: Treatment) -> None:
        """Add a treatment to the simulation."""
        # Store treatment in infrastructure
        self.infrastructure.resources[treatment.id] = Resource(
            id=treatment.id,
            name=treatment.name,
            type="treatment",
            quantity=1,
            unit_cost=treatment.cost,
            facility_id="",  # Treatments are not facility-specific
            status="available"
        )
        
    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the simulation."""
        self.infrastructure.add_resource(resource)
        
    def calculate_facility_utilization(self, facility_id: str) -> float:
        """Calculate the utilization rate of a facility."""
        return self.infrastructure.get_facility_utilization(facility_id)
        
    def calculate_healthcare_quality(self, facility_id: str) -> float:
        """Calculate the quality score of a facility."""
        facility = self.infrastructure.facilities[facility_id]
        workers = [w for w in self.workforce.workers.values() 
                  if w.facility_id == facility_id]
        
        if not workers:
            return facility.quality_score
            
        worker_scores = [w.performance_score for w in workers]
        equipment_quality = sum(facility.equipment.values()) / len(facility.equipment) if facility.equipment else 0.5
        
        return (np.mean(worker_scores) * 0.6 + equipment_quality * 0.4)
        
    def simulate_patient_flow(self) -> None:
        """Simulate patient flow through the healthcare system."""
        for patient_id in self.financing.insurance_coverage.keys():
            # Determine if patient needs care
            if np.random.random() < 0.1:  # 10% chance of needing care
                # Record telemedicine session
                self.digital_health.record_telemedicine_session(patient_id)
                
                # Update electronic health record
                self.digital_health.update_electronic_record(
                    patient_id,
                    {"last_visit": self.current_date.isoformat()}
                )
                
    def update_metrics(self) -> None:
        """Update system-wide metrics."""
        # Calculate and store various metrics
        facility_utilizations = [
            self.calculate_facility_utilization(f.id)
            for f in self.infrastructure.facilities.values()
        ]
        
        healthcare_qualities = [
            self.calculate_healthcare_quality(f.id)
            for f in self.infrastructure.facilities.values()
        ]
        
        self.metrics["facility_utilization"] = [
            (self.current_date, np.mean(facility_utilizations))
        ]
        
        self.metrics["healthcare_quality"] = [
            (self.current_date, np.mean(healthcare_qualities))
        ]
        
    def step(self) -> None:
        """Advance the simulation by one time step."""
        if self.current_date >= self.end_date:
            raise StopIteration("Simulation has reached end date")
            
        self.simulate_patient_flow()
        self.update_metrics()
        self.current_date += timedelta(days=1)
        
    def run(self) -> None:
        """Run the complete simulation."""
        while self.current_date < self.end_date:
            try:
                self.step()
            except StopIteration:
                break
                
    def get_metrics(self) -> Dict[str, List[Tuple[datetime, float]]]:
        """Get the current simulation metrics."""
        return self.metrics 