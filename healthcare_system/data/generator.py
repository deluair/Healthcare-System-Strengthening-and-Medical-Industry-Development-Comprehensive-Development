"""
Data generation module for creating realistic simulation data.
"""

import uuid
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from ..models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)

class DataGenerator:
    """Generates realistic simulation data for the healthcare system."""
    
    def __init__(self):
        self.location_types = ["district", "upazila", "union", "ward"]
        self.facility_types = [
            "tertiary_hospital", "secondary_hospital", "primary_hospital",
            "clinic", "diagnostic_center", "specialized_center"
        ]
        self.worker_types = [
            "doctor", "nurse", "technician", "pharmacist",
            "administrator", "support_staff"
        ]
        self.treatment_types = [
            "consultation", "surgery", "diagnostic_test",
            "therapy", "emergency_care", "preventive_care"
        ]
        self.resource_types = [
            "medical_equipment", "pharmaceuticals", "supplies",
            "technology", "furniture"
        ]
        
    def generate_location(self, parent_id: str = None) -> Location:
        """Generate a realistic location."""
        location_type = random.choice(self.location_types)
        population = random.randint(1000, 1000000)
        
        return Location(
            id=str(uuid.uuid4()),
            name=f"{location_type.capitalize()}_{random.randint(1, 100)}",
            type=location_type,
            population=population,
            coordinates={
                "latitude": random.uniform(20.0, 26.0),  # Bangladesh coordinates
                "longitude": random.uniform(88.0, 92.0)
            },
            parent_id=parent_id
        )
        
    def generate_facility(self, location_id: str) -> Facility:
        """Generate a realistic healthcare facility."""
        facility_type = random.choice(self.facility_types)
        capacity = random.randint(10, 1000)
        staff_count = random.randint(5, capacity // 2)
        
        return Facility(
            id=str(uuid.uuid4()),
            name=f"{facility_type.replace('_', ' ').title()} {random.randint(1, 100)}",
            type=facility_type,
            location_id=location_id,
            capacity=capacity,
            staff_count=staff_count,
            equipment=self._generate_equipment(),
            services=self._generate_services(facility_type),
            quality_score=random.uniform(0.5, 1.0),
            operational_status="active"
        )
        
    def generate_healthcare_worker(self, facility_id: str) -> HealthcareWorker:
        """Generate a realistic healthcare worker."""
        worker_type = random.choice(self.worker_types)
        
        return HealthcareWorker(
            id=str(uuid.uuid4()),
            name=f"Worker_{random.randint(1, 1000)}",
            type=worker_type,
            specialization=self._generate_specialization(worker_type),
            facility_id=facility_id,
            experience_years=random.randint(0, 40),
            qualifications=self._generate_qualifications(worker_type),
            skills=self._generate_skills(worker_type),
            performance_score=random.uniform(0.6, 1.0)
        )
        
    def generate_patient(self, location_id: str) -> Patient:
        """Generate a realistic patient."""
        return Patient(
            id=str(uuid.uuid4()),
            name=f"Patient_{random.randint(1, 1000)}",
            age=random.randint(0, 100),
            gender=random.choice(["male", "female"]),
            location_id=location_id,
            insurance_status=random.choice(["insured", "uninsured", "partial"]),
            medical_history=self._generate_medical_history(),
            current_conditions=self._generate_conditions(),
            socioeconomic_status=random.choice(["low", "middle", "high"])
        )
        
    def generate_treatment(self) -> Treatment:
        """Generate a realistic treatment."""
        treatment_type = random.choice(self.treatment_types)
        
        return Treatment(
            id=str(uuid.uuid4()),
            name=f"{treatment_type.replace('_', ' ').title()} {random.randint(1, 100)}",
            type=treatment_type,
            cost=random.uniform(100, 10000),
            duration_minutes=random.randint(15, 480),
            required_equipment=self._generate_required_equipment(treatment_type),
            required_staff=self._generate_required_staff(treatment_type),
            success_rate=random.uniform(0.7, 0.99),
            complications_rate=random.uniform(0.01, 0.3)
        )
        
    def generate_resource(self, facility_id: str) -> Resource:
        """Generate a realistic resource."""
        resource_type = random.choice(self.resource_types)
        
        return Resource(
            id=str(uuid.uuid4()),
            name=f"{resource_type.replace('_', ' ').title()} {random.randint(1, 100)}",
            type=resource_type,
            quantity=random.randint(1, 100),
            unit_cost=random.uniform(10, 1000),
            facility_id=facility_id,
            status=random.choice(["active", "maintenance", "retired"]),
            maintenance_schedule=self._generate_maintenance_schedule(),
            last_maintenance=datetime.now() - timedelta(days=random.randint(0, 365))
        )
        
    def _generate_equipment(self) -> Dict[str, int]:
        """Generate realistic equipment for a facility."""
        equipment_types = [
            "xray_machines", "mri_scanners", "ct_scanners",
            "ultrasound_machines", "ventilators", "defibrillators"
        ]
        return {
            equipment: random.randint(0, 5)
            for equipment in equipment_types
        }
        
    def _generate_services(self, facility_type: str) -> List[str]:
        """Generate realistic services based on facility type."""
        base_services = ["general_consultation", "emergency_care"]
        specialized_services = {
            "tertiary_hospital": ["specialized_surgery", "cancer_treatment", "cardiac_care"],
            "secondary_hospital": ["basic_surgery", "maternity_care", "pediatric_care"],
            "primary_hospital": ["basic_healthcare", "vaccination", "family_planning"],
            "clinic": ["outpatient_care", "basic_diagnostics", "pharmacy"],
            "diagnostic_center": ["laboratory_tests", "imaging", "specialized_diagnostics"],
            "specialized_center": ["specialized_treatment", "rehabilitation", "research"]
        }
        return base_services + specialized_services.get(facility_type, [])
        
    def _generate_specialization(self, worker_type: str) -> str:
        """Generate realistic specialization based on worker type."""
        specializations = {
            "doctor": ["cardiology", "neurology", "pediatrics", "surgery"],
            "nurse": ["critical_care", "pediatric", "emergency", "surgical"],
            "technician": ["radiology", "laboratory", "biomedical", "pharmacy"],
            "pharmacist": ["clinical", "hospital", "research", "retail"],
            "administrator": ["hospital", "clinical", "healthcare", "operations"],
            "support_staff": ["maintenance", "logistics", "security", "housekeeping"]
        }
        return random.choice(specializations.get(worker_type, ["general"]))
        
    def _generate_qualifications(self, worker_type: str) -> List[str]:
        """Generate realistic qualifications based on worker type."""
        base_qualifications = {
            "doctor": ["MBBS", "MD", "PhD"],
            "nurse": ["BSc Nursing", "MSc Nursing"],
            "technician": ["Diploma", "BSc", "Certification"],
            "pharmacist": ["BPharm", "MPharm"],
            "administrator": ["MBA", "MHA", "BBA"],
            "support_staff": ["High School", "Vocational Training"]
        }
        return random.sample(base_qualifications.get(worker_type, ["Basic"]), 
                           random.randint(1, 3))
        
    def _generate_skills(self, worker_type: str) -> List[str]:
        """Generate realistic skills based on worker type."""
        base_skills = {
            "doctor": ["diagnosis", "treatment_planning", "surgery", "patient_care"],
            "nurse": ["patient_care", "medication_administration", "emergency_care"],
            "technician": ["equipment_operation", "maintenance", "quality_control"],
            "pharmacist": ["medication_dispensing", "inventory_management", "patient_counseling"],
            "administrator": ["management", "planning", "coordination"],
            "support_staff": ["maintenance", "logistics", "customer_service"]
        }
        return random.sample(base_skills.get(worker_type, ["general"]), 
                           random.randint(2, 4))
        
    def _generate_medical_history(self) -> List[Dict[str, Any]]:
        """Generate realistic medical history."""
        conditions = [
            "hypertension", "diabetes", "asthma", "heart_disease",
            "arthritis", "cancer", "thyroid_disorder"
        ]
        return [
            {
                "condition": random.choice(conditions),
                "diagnosis_date": (datetime.now() - timedelta(days=random.randint(0, 3650))).isoformat(),
                "treatment": random.choice(["medication", "surgery", "therapy"]),
                "status": random.choice(["active", "resolved", "chronic"])
            }
            for _ in range(random.randint(0, 3))
        ]
        
    def _generate_conditions(self) -> List[str]:
        """Generate realistic current conditions."""
        conditions = [
            "fever", "cough", "headache", "back_pain",
            "joint_pain", "fatigue", "anxiety", "depression"
        ]
        return random.sample(conditions, random.randint(0, 2))
        
    def _generate_required_equipment(self, treatment_type: str) -> List[str]:
        """Generate realistic required equipment for treatment."""
        equipment_map = {
            "surgery": ["surgical_instruments", "anesthesia_machine", "monitoring_equipment"],
            "diagnostic_test": ["xray_machine", "ultrasound", "laboratory_equipment"],
            "therapy": ["therapy_equipment", "exercise_equipment"],
            "emergency_care": ["defibrillator", "ventilator", "monitoring_equipment"],
            "preventive_care": ["vaccination_equipment", "screening_tools"]
        }
        return equipment_map.get(treatment_type, ["basic_equipment"])
        
    def _generate_required_staff(self, treatment_type: str) -> List[str]:
        """Generate realistic required staff for treatment."""
        staff_map = {
            "surgery": ["surgeon", "anesthesiologist", "nurse", "technician"],
            "diagnostic_test": ["technician", "radiologist"],
            "therapy": ["therapist", "nurse"],
            "emergency_care": ["emergency_physician", "nurse", "paramedic"],
            "preventive_care": ["general_physician", "nurse"]
        }
        return staff_map.get(treatment_type, ["general_physician"])
        
    def _generate_maintenance_schedule(self) -> Dict[str, Any]:
        """Generate realistic maintenance schedule."""
        return {
            "frequency_days": random.randint(30, 365),
            "last_maintenance": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            "next_maintenance": (datetime.now() + timedelta(days=random.randint(30, 365))).isoformat(),
            "maintenance_type": random.choice(["preventive", "corrective", "predictive"])
        } 