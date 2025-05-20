"""
Simulation engine for the healthcare system.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from healthcare_system.models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)
from healthcare_system.simulation.components import (
    HealthcareInfrastructure, WorkforceDevelopment,
    HealthcareFinancing, DigitalHealth
)

class SimulationEngine:
    """Main simulation engine that coordinates all components."""
    
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = start_date
        
        # Initialize components
        self.infrastructure = HealthcareInfrastructure()
        self.workforce = WorkforceDevelopment()
        self.financing = HealthcareFinancing()
        self.digital_health = DigitalHealth()
        
        # Simulation state
        self.locations: Dict[str, Location] = {}
        self.metrics: Dict[str, List[Tuple[datetime, float]]] = {
            "facility_utilization": [],
            "healthcare_quality": [],
            "insurance_coverage": [],
            "digital_health_adoption": []
        }
        
    def add_location(self, location: Location) -> None:
        """Add a location to the simulation."""
        self.locations[location.id] = location
        
    def add_facility(self, facility: Facility) -> None:
        """Add a healthcare facility to the simulation."""
        self.infrastructure.add_facility(facility)
        # Initialize facility funding
        self.financing.allocate_funding(facility.id, 1000000)  # Default funding
        
    def add_healthcare_worker(self, worker: HealthcareWorker) -> None:
        """Add a healthcare worker to the simulation."""
        self.workforce.add_worker(worker)
        # Assign initial training
        self.workforce.assign_training(worker.id, "basic_healthcare")
        
    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the simulation."""
        # Set default insurance coverage
        coverage = 0.7 if patient.insurance_status == "insured" else 0.0
        self.financing.set_insurance_coverage(patient.id, coverage)
        
        # Initialize electronic health record
        self.digital_health.update_electronic_record(
            patient.id,
            {
                "patient_info": {
                    "name": patient.name,
                    "age": patient.age,
                    "gender": patient.gender
                },
                "medical_history": patient.medical_history,
                "current_conditions": patient.current_conditions
            }
        )
        
    def simulate_facility_operations(self) -> None:
        """Simulate daily facility operations (aggregate for all facilities)."""
        utilizations = []
        qualities = []
        for facility_id in self.infrastructure.facilities:
            # Update facility utilization
            utilization = self.infrastructure.get_facility_utilization(facility_id)
            utilizations.append(utilization)
            # Update healthcare quality based on workforce
            workers = [w for w in self.workforce.workers.values() 
                      if w.facility_id == facility_id]
            if workers:
                quality = np.mean([w.performance_score for w in workers])
            else:
                quality = 0.5
            qualities.append(quality)
        # Store the average for the day
        if utilizations:
            avg_utilization = float(np.mean(utilizations))
        else:
            avg_utilization = 0.0
        if qualities:
            avg_quality = float(np.mean(qualities))
        else:
            avg_quality = 0.0
        self.metrics["facility_utilization"].append(
            (self.current_date, avg_utilization)
        )
        self.metrics["healthcare_quality"].append(
            (self.current_date, avg_quality)
        )
        
    def simulate_patient_care(self) -> None:
        """Simulate patient care activities."""
        for patient_id in self.financing.insurance_coverage:
            # Simulate patient visits (10% chance per day)
            if np.random.random() < 0.1:
                # Record telemedicine session
                self.digital_health.record_telemedicine_session(patient_id)
                
                # Update electronic health record
                self.digital_health.update_electronic_record(
                    patient_id,
                    {"last_visit": self.current_date.isoformat()}
                )
                
    def simulate_workforce_development(self) -> None:
        """Simulate workforce development activities."""
        for worker_id in self.workforce.workers:
            # Simulate training completion (5% chance per day)
            if np.random.random() < 0.05:
                # Assign new training
                training_programs = [
                    "advanced_care", "specialized_treatment",
                    "emergency_response", "quality_improvement"
                ]
                new_training = np.random.choice(training_programs)
                self.workforce.assign_training(worker_id, new_training)
                
    def calculate_metrics(self) -> None:
        """Calculate and update system-wide metrics."""
        # Calculate insurance coverage
        coverage = np.mean(list(self.financing.insurance_coverage.values()))
        self.metrics["insurance_coverage"].append(
            (self.current_date, coverage)
        )
        
        # Calculate digital health adoption
        adoption = len(self.digital_health.electronic_records) / len(self.financing.insurance_coverage)
        self.metrics["digital_health_adoption"].append(
            (self.current_date, adoption)
        )
        
    def step(self) -> None:
        """Advance the simulation by one time step."""
        if self.current_date >= self.end_date:
            raise StopIteration("Simulation has reached end date")
            
        # Run daily simulations
        self.simulate_facility_operations()
        self.simulate_patient_care()
        self.simulate_workforce_development()
        self.calculate_metrics()
        
        # Advance time
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
        
    def get_facility_summary(self, facility_id: str) -> Dict[str, float]:
        """Get a summary of facility performance."""
        return {
            "utilization": self.infrastructure.get_facility_utilization(facility_id),
            "quality": np.mean([w.performance_score for w in self.workforce.workers.values() 
                              if w.facility_id == facility_id]),
            "funding": self.financing.facility_funding.get(facility_id, 0.0)
        }
        
    def get_patient_summary(self, patient_id: str) -> Dict[str, Any]:
        """Get a summary of patient care."""
        return {
            "insurance_coverage": self.financing.insurance_coverage.get(patient_id, 0.0),
            "telemedicine_sessions": len(self.digital_health.telemedicine_sessions.get(patient_id, [])),
            "health_record": self.digital_health.get_patient_history(patient_id)
        } 