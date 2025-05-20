"""
Configuration settings for the healthcare system simulation.
"""

from typing import Dict, List

# Simulation Parameters
SIMULATION_START_DATE = "2023-01-01"
SIMULATION_END_DATE = "2023-12-31"
SIMULATION_STEP_DAYS = 1

# Location Parameters
DISTRICT_COUNT = 8
UPAZILA_PER_DISTRICT = 5
UNION_PER_UPAZILA = 10
PATIENTS_PER_UNION = 1000

# Facility Parameters
FACILITIES_PER_UNION = 3
STAFF_TO_CAPACITY_RATIO = 0.5
RESOURCES_PER_FACILITY = 5

# Treatment Parameters
TREATMENT_COUNT = 50

# Quality Parameters
MIN_QUALITY_SCORE = 0.5
MAX_QUALITY_SCORE = 1.0
MIN_PERFORMANCE_SCORE = 0.6
MAX_PERFORMANCE_SCORE = 1.0

# Facility Types and Their Characteristics
FACILITY_TYPES: Dict[str, Dict] = {
    "tertiary_hospital": {
        "min_capacity": 500,
        "max_capacity": 1000,
        "required_equipment": [
            "mri_scanner", "ct_scanner", "xray_machine",
            "ultrasound_machine", "ventilator", "defibrillator"
        ],
        "required_staff": [
            "specialist_doctor", "general_doctor", "nurse",
            "technician", "pharmacist", "administrator"
        ]
    },
    "secondary_hospital": {
        "min_capacity": 200,
        "max_capacity": 500,
        "required_equipment": [
            "xray_machine", "ultrasound_machine",
            "ventilator", "defibrillator"
        ],
        "required_staff": [
            "general_doctor", "nurse", "technician",
            "pharmacist", "administrator"
        ]
    },
    "primary_hospital": {
        "min_capacity": 50,
        "max_capacity": 200,
        "required_equipment": [
            "xray_machine", "basic_laboratory_equipment"
        ],
        "required_staff": [
            "general_doctor", "nurse", "pharmacist"
        ]
    },
    "clinic": {
        "min_capacity": 10,
        "max_capacity": 50,
        "required_equipment": [
            "basic_medical_equipment"
        ],
        "required_staff": [
            "general_doctor", "nurse"
        ]
    },
    "diagnostic_center": {
        "min_capacity": 20,
        "max_capacity": 100,
        "required_equipment": [
            "xray_machine", "ultrasound_machine",
            "laboratory_equipment"
        ],
        "required_staff": [
            "technician", "radiologist", "laboratory_technician"
        ]
    },
    "specialized_center": {
        "min_capacity": 30,
        "max_capacity": 150,
        "required_equipment": [
            "specialized_equipment"
        ],
        "required_staff": [
            "specialist_doctor", "nurse", "technician"
        ]
    }
}

# Worker Types and Their Characteristics
WORKER_TYPES: Dict[str, Dict] = {
    "doctor": {
        "min_experience": 0,
        "max_experience": 40,
        "qualifications": ["MBBS", "MD", "PhD"],
        "specializations": [
            "cardiology", "neurology", "pediatrics",
            "surgery", "gynecology", "orthopedics"
        ]
    },
    "nurse": {
        "min_experience": 0,
        "max_experience": 35,
        "qualifications": ["BSc Nursing", "MSc Nursing"],
        "specializations": [
            "critical_care", "pediatric", "emergency",
            "surgical", "community_health"
        ]
    },
    "technician": {
        "min_experience": 0,
        "max_experience": 30,
        "qualifications": ["Diploma", "BSc", "Certification"],
        "specializations": [
            "radiology", "laboratory", "biomedical",
            "pharmacy", "maintenance"
        ]
    },
    "pharmacist": {
        "min_experience": 0,
        "max_experience": 30,
        "qualifications": ["BPharm", "MPharm"],
        "specializations": [
            "clinical", "hospital", "research",
            "retail", "industrial"
        ]
    },
    "administrator": {
        "min_experience": 0,
        "max_experience": 35,
        "qualifications": ["MBA", "MHA", "BBA"],
        "specializations": [
            "hospital", "clinical", "healthcare",
            "operations", "finance"
        ]
    },
    "support_staff": {
        "min_experience": 0,
        "max_experience": 25,
        "qualifications": ["High School", "Vocational Training"],
        "specializations": [
            "maintenance", "logistics", "security",
            "housekeeping", "transportation"
        ]
    }
}

# Treatment Types and Their Characteristics
TREATMENT_TYPES: Dict[str, Dict] = {
    "consultation": {
        "min_cost": 100,
        "max_cost": 500,
        "min_duration": 15,
        "max_duration": 60,
        "required_equipment": ["basic_medical_equipment"],
        "required_staff": ["doctor"]
    },
    "surgery": {
        "min_cost": 5000,
        "max_cost": 100000,
        "min_duration": 60,
        "max_duration": 480,
        "required_equipment": [
            "surgical_instruments", "anesthesia_machine",
            "monitoring_equipment"
        ],
        "required_staff": [
            "surgeon", "anesthesiologist", "nurse",
            "technician"
        ]
    },
    "diagnostic_test": {
        "min_cost": 200,
        "max_cost": 2000,
        "min_duration": 30,
        "max_duration": 120,
        "required_equipment": [
            "xray_machine", "ultrasound", "laboratory_equipment"
        ],
        "required_staff": ["technician", "radiologist"]
    },
    "therapy": {
        "min_cost": 300,
        "max_cost": 1000,
        "min_duration": 45,
        "max_duration": 90,
        "required_equipment": [
            "therapy_equipment", "exercise_equipment"
        ],
        "required_staff": ["therapist", "nurse"]
    },
    "emergency_care": {
        "min_cost": 1000,
        "max_cost": 5000,
        "min_duration": 30,
        "max_duration": 180,
        "required_equipment": [
            "defibrillator", "ventilator", "monitoring_equipment"
        ],
        "required_staff": [
            "emergency_physician", "nurse", "paramedic"
        ]
    },
    "preventive_care": {
        "min_cost": 50,
        "max_cost": 300,
        "min_duration": 15,
        "max_duration": 60,
        "required_equipment": [
            "vaccination_equipment", "screening_tools"
        ],
        "required_staff": ["general_physician", "nurse"]
    }
}

# Resource Types and Their Characteristics
RESOURCE_TYPES: Dict[str, Dict] = {
    "medical_equipment": {
        "min_quantity": 1,
        "max_quantity": 10,
        "min_unit_cost": 1000,
        "max_unit_cost": 100000,
        "maintenance_frequency_days": 90
    },
    "pharmaceuticals": {
        "min_quantity": 100,
        "max_quantity": 1000,
        "min_unit_cost": 10,
        "max_unit_cost": 1000,
        "maintenance_frequency_days": 30
    },
    "supplies": {
        "min_quantity": 1000,
        "max_quantity": 10000,
        "min_unit_cost": 1,
        "max_unit_cost": 100,
        "maintenance_frequency_days": 7
    },
    "technology": {
        "min_quantity": 1,
        "max_quantity": 5,
        "min_unit_cost": 500,
        "max_unit_cost": 5000,
        "maintenance_frequency_days": 60
    },
    "furniture": {
        "min_quantity": 10,
        "max_quantity": 100,
        "min_unit_cost": 100,
        "max_unit_cost": 1000,
        "maintenance_frequency_days": 180
    }
} 