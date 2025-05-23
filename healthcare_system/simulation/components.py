"""
Simulation components for the healthcare system.
"""

from typing import Dict, List, Optional
import numpy as np
from healthcare_system.models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)
from ..models.quality import (
    QualityIndicator, PatientSafetyIncident,
    QualityImprovementPlan, Accreditation
)
from ..models.public_health import (
    DiseaseSurveillance, VaccinationProgram,
    HealthCampaign, PreventiveService
)
from ..models.pharmaceutical import (
    PharmaceuticalProduct, ManufacturingFacility,
    SupplyChain, ResearchProject, QualityControl
)

class HealthcareInfrastructure:
    """Manages healthcare facilities and infrastructure."""
    
    def __init__(self):
        self.facilities: Dict[str, Facility] = {}
        self.resources: Dict[str, Resource] = {}
        
    def add_facility(self, facility: Facility) -> None:
        """Add a facility to the infrastructure."""
        self.facilities[facility.id] = facility
        
    def get_facility_utilization(self, facility_id: str) -> float:
        """Calculate facility utilization rate."""
        if facility_id not in self.facilities:
            return 0.0
            
        facility = self.facilities[facility_id]
        # Simulate utilization based on capacity and staff
        base_utilization = min(facility.staff_count / (facility.capacity * 0.1), 1.0)
        # Add some random variation
        return min(base_utilization + np.random.normal(0, 0.1), 1.0)
        
    def update_facility_quality(self, facility_id: str, quality_score: float) -> None:
        """Update facility quality score."""
        if facility_id in self.facilities:
            self.facilities[facility_id].quality_score = max(0.0, min(1.0, quality_score))

class WorkforceDevelopment:
    """Manages healthcare workforce development."""
    
    def __init__(self):
        self.workers: Dict[str, HealthcareWorker] = {}
        self.training_programs: Dict[str, List[str]] = {}
        
    def add_worker(self, worker: HealthcareWorker) -> None:
        """Add a healthcare worker."""
        self.workers[worker.id] = worker
        self.training_programs[worker.id] = []
        
    def assign_training(self, worker_id: str, program: str) -> None:
        """Assign a training program to a worker."""
        if worker_id in self.workers:
            if program not in self.training_programs[worker_id]:
                self.training_programs[worker_id].append(program)
                
    def update_performance(self, worker_id: str, performance_score: float) -> None:
        """Update worker performance score."""
        if worker_id in self.workers:
            self.workers[worker_id].performance_score = max(0.0, min(1.0, performance_score))

class HealthcareFinancing:
    """Manages healthcare financing and insurance."""
    
    def __init__(self):
        self.insurance_coverage: Dict[str, float] = {}  # patient_id -> coverage rate
        self.facility_funding: Dict[str, float] = {}  # facility_id -> funding amount
        
    def set_insurance_coverage(self, patient_id: str, coverage: float) -> None:
        """Set insurance coverage for a patient."""
        self.insurance_coverage[patient_id] = max(0.0, min(1.0, coverage))
        
    def allocate_funding(self, facility_id: str, amount: float) -> None:
        """Allocate funding to a facility."""
        self.facility_funding[facility_id] = amount
        
    def calculate_coverage_rate(self) -> float:
        """Calculate overall insurance coverage rate."""
        if not self.insurance_coverage:
            return 0.0
        return sum(self.insurance_coverage.values()) / len(self.insurance_coverage)

class DigitalHealth:
    """Manages digital health systems and records."""
    
    def __init__(self):
        self.electronic_records: Dict[str, Dict] = {}  # patient_id -> health record
        self.telemedicine_sessions: Dict[str, List[str]] = {}  # patient_id -> session records
        
    def update_electronic_record(self, patient_id: str, record_data: Dict) -> None:
        """Update electronic health record for a patient."""
        if patient_id not in self.electronic_records:
            self.electronic_records[patient_id] = {}
        self.electronic_records[patient_id].update(record_data)
        
    def record_telemedicine_session(self, patient_id: str) -> None:
        """Record a telemedicine session."""
        if patient_id not in self.telemedicine_sessions:
            self.telemedicine_sessions[patient_id] = []
        self.telemedicine_sessions[patient_id].append("session_recorded")
        
    def get_patient_history(self, patient_id: str) -> Dict:
        """Get patient's electronic health record."""
        return self.electronic_records.get(patient_id, {})

class MedicalTourism:
    """Manages medical tourism and export services."""
    
    def __init__(self):
        self.international_patients: Dict[str, Patient] = {}
        self.export_services: Dict[str, List[str]] = {}
        
    def register_international_patient(self, patient: Patient) -> None:
        """Register an international patient."""
        self.international_patients[patient.id] = patient
        
    def add_export_service(self, facility_id: str, service: str) -> None:
        """Add an export service to a facility."""
        if facility_id not in self.export_services:
            self.export_services[facility_id] = []
        self.export_services[facility_id].append(service)
        
    def get_available_services(self, facility_id: str) -> List[str]:
        """Get available export services for a facility."""
        return self.export_services.get(facility_id, [])

class QualityImprovement:
    """Manages quality improvement and patient safety."""
    
    def __init__(self):
        self.indicators: Dict[str, QualityIndicator] = {}
        self.incidents: Dict[str, PatientSafetyIncident] = {}
        self.improvement_plans: Dict[str, QualityImprovementPlan] = {}
        self.accreditations: Dict[str, Accreditation] = {}
        
    def add_indicator(self, indicator: QualityIndicator) -> None:
        """Add a quality indicator."""
        self.indicators[indicator.id] = indicator
        
    def record_incident(self, incident: PatientSafetyIncident) -> None:
        """Record a patient safety incident."""
        self.incidents[incident.id] = incident
        
    def create_improvement_plan(self, plan: QualityImprovementPlan) -> None:
        """Create a quality improvement plan."""
        self.improvement_plans[plan.id] = plan
        
    def update_accreditation(self, accreditation: Accreditation) -> None:
        """Update facility accreditation."""
        self.accreditations[accreditation.id] = accreditation
        
    def get_facility_quality_score(self, facility_id: str) -> float:
        """Calculate overall quality score for a facility."""
        facility_indicators = [
            ind for ind in self.indicators.values()
            if ind.id in self.improvement_plans.get(facility_id, {}).indicators
        ]
        if not facility_indicators:
            return 0.0
        return sum(ind.current_value for ind in facility_indicators) / len(facility_indicators)

class PublicHealth:
    """Manages public health and preventive services."""
    
    def __init__(self):
        self.disease_surveillance: Dict[str, DiseaseSurveillance] = {}
        self.vaccination_programs: Dict[str, VaccinationProgram] = {}
        self.health_campaigns: Dict[str, HealthCampaign] = {}
        self.preventive_services: Dict[str, PreventiveService] = {}
        
    def add_disease_surveillance(self, surveillance: DiseaseSurveillance) -> None:
        """Add disease surveillance data."""
        self.disease_surveillance[surveillance.id] = surveillance
        
    def create_vaccination_program(self, program: VaccinationProgram) -> None:
        """Create a vaccination program."""
        self.vaccination_programs[program.id] = program
        
    def launch_health_campaign(self, campaign: HealthCampaign) -> None:
        """Launch a health campaign."""
        self.health_campaigns[campaign.id] = campaign
        
    def add_preventive_service(self, service: PreventiveService) -> None:
        """Add a preventive service."""
        self.preventive_services[service.id] = service
        
    def get_disease_risk_level(self, location_id: str) -> str:
        """Get current disease risk level for a location."""
        location_surveillance = [
            s for s in self.disease_surveillance.values()
            if s.location_id == location_id
        ]
        if not location_surveillance:
            return "low"
        return max(s.risk_level for s in location_surveillance)

class PharmaceuticalIndustry:
    """Manages pharmaceutical industry development."""
    
    def __init__(self):
        self.products: Dict[str, PharmaceuticalProduct] = {}
        self.manufacturing_facilities: Dict[str, ManufacturingFacility] = {}
        self.supply_chains: Dict[str, SupplyChain] = {}
        self.research_projects: Dict[str, ResearchProject] = {}
        self.quality_controls: Dict[str, QualityControl] = {}
        
    def add_product(self, product: PharmaceuticalProduct) -> None:
        """Add a pharmaceutical product."""
        self.products[product.id] = product
        
    def add_manufacturing_facility(self, facility: ManufacturingFacility) -> None:
        """Add a manufacturing facility."""
        self.manufacturing_facilities[facility.id] = facility
        
    def create_supply_chain(self, supply_chain: SupplyChain) -> None:
        """Create a supply chain."""
        self.supply_chains[supply_chain.id] = supply_chain
        
    def add_research_project(self, project: ResearchProject) -> None:
        """Add a research project."""
        self.research_projects[project.id] = project
        
    def add_quality_control(self, quality_control: QualityControl) -> None:
        """Add quality control testing."""
        self.quality_controls[quality_control.id] = quality_control
        
    def get_product_availability(self, product_id: str) -> float:
        """Calculate product availability across supply chain."""
        supply_chains = [
            sc for sc in self.supply_chains.values()
            if sc.product_id == product_id
        ]
        if not supply_chains:
            return 0.0
        return sum(sc.status == "normal" for sc in supply_chains) / len(supply_chains) 