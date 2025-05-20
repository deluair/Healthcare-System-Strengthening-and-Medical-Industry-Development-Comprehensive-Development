"""
Main script to run the healthcare system simulation.
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from healthcare_system.simulation.engine import SimulationEngine
from healthcare_system.models.base import (
    Location, Facility, HealthcareWorker, Patient,
    Treatment, Resource
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_sample_data():
    """Create sample data for the simulation."""
    # Create locations
    locations = {
        "dhaka": Location(
            id="dhaka",
            name="Dhaka",
            type="city",
            population=20000000,
            coordinates={"latitude": 23.7, "longitude": 90.4}
        ),
        "chittagong": Location(
            id="chittagong",
            name="Chittagong",
            type="city",
            population=5000000,
            coordinates={"latitude": 22.3, "longitude": 91.8}
        )
    }
    
    # Create facilities
    facilities = {
        "dhaka_hospital": Facility(
            id="dhaka_hospital",
            name="Dhaka Medical College Hospital",
            type="hospital",
            location_id="dhaka",
            capacity=2000,
            staff_count=500,
            equipment={"xray": 10, "mri": 2, "ct": 3},
            services=["general", "emergency", "specialized"],
            quality_score=0.85
        ),
        "chittagong_hospital": Facility(
            id="chittagong_hospital",
            name="Chittagong Medical College Hospital",
            type="hospital",
            location_id="chittagong",
            capacity=1000,
            staff_count=300,
            equipment={"xray": 5, "mri": 1, "ct": 2},
            services=["general", "emergency"],
            quality_score=0.75
        )
    }
    
    # Create healthcare workers
    workers = {
        "dr_ahmed": HealthcareWorker(
            id="dr_ahmed",
            name="Dr. Ahmed",
            type="doctor",
            specialization="general",
            facility_id="dhaka_hospital",
            experience_years=10,
            qualifications=["MBBS", "MD"],
            skills=["diagnosis", "treatment", "surgery"],
            performance_score=0.9
        ),
        "dr_rahman": HealthcareWorker(
            id="dr_rahman",
            name="Dr. Rahman",
            type="doctor",
            specialization="emergency",
            facility_id="chittagong_hospital",
            experience_years=8,
            qualifications=["MBBS", "FCPS"],
            skills=["emergency_care", "trauma"],
            performance_score=0.85
        )
    }
    
    # Create patients
    patients = {
        "patient1": Patient(
            id="patient1",
            name="John Smith",
            age=45,
            gender="male",
            location_id="dhaka",
            insurance_status="insured",
            medical_history=["hypertension"],
            current_conditions=["fever", "cough"],
            socioeconomic_status="middle"
        ),
        "patient2": Patient(
            id="patient2",
            name="Sarah Johnson",
            age=32,
            gender="female",
            location_id="chittagong",
            insurance_status="uninsured",
            medical_history=[],
            current_conditions=["pregnancy"],
            socioeconomic_status="low"
        )
    }
    
    return locations, facilities, workers, patients

def analyze_results(engine):
    """Analyze simulation results and generate insights."""
    metrics = engine.get_metrics()

    # Assume all metrics have the same dates (since they are updated together)
    metric_names = list(metrics.keys())
    if not metric_names:
        return pd.DataFrame(), {}
    dates, _ = zip(*metrics[metric_names[0]])
    data = {'date': dates}
    for metric_name, values in metrics.items():
        _, scores = zip(*values)
        data[metric_name] = scores
    df_metrics = pd.DataFrame(data)

    # Calculate statistics
    stats = df_metrics.describe()

    # Generate insights
    insights = {
        "facility_utilization": {
            "mean": stats["facility_utilization"]["mean"],
            "std": stats["facility_utilization"]["std"],
            "min": stats["facility_utilization"]["min"],
            "max": stats["facility_utilization"]["max"],
            "trend": "increasing" if df_metrics["facility_utilization"].iloc[-1] > df_metrics["facility_utilization"].iloc[0] else "decreasing"
        },
        "healthcare_quality": {
            "mean": stats["healthcare_quality"]["mean"],
            "std": stats["healthcare_quality"]["std"],
            "min": stats["healthcare_quality"]["min"],
            "max": stats["healthcare_quality"]["max"],
            "trend": "improving" if df_metrics["healthcare_quality"].iloc[-1] > df_metrics["healthcare_quality"].iloc[0] else "declining"
        }
    }

    return df_metrics, insights

def generate_report(df_metrics, insights):
    """Generate a formatted report of the simulation results."""
    report = []
    report.append("Healthcare System Simulation Report")
    report.append("=" * 40)
    report.append("\nFacility Utilization:")
    report.append(f"Mean: {insights['facility_utilization']['mean']:.2f}")
    report.append(f"Standard Deviation: {insights['facility_utilization']['std']:.2f}")
    report.append(f"Range: {insights['facility_utilization']['min']:.2f} - {insights['facility_utilization']['max']:.2f}")
    report.append(f"Trend: {insights['facility_utilization']['trend']}")
    
    report.append("\nHealthcare Quality:")
    report.append(f"Mean: {insights['healthcare_quality']['mean']:.2f}")
    report.append(f"Standard Deviation: {insights['healthcare_quality']['std']:.2f}")
    report.append(f"Range: {insights['healthcare_quality']['min']:.2f} - {insights['healthcare_quality']['max']:.2f}")
    report.append(f"Trend: {insights['healthcare_quality']['trend']}")
    
    return "\n".join(report)

def plot_results(df_metrics):
    """Generate plots of the simulation results."""
    plt.figure(figsize=(12, 6))
    
    # Plot facility utilization
    plt.subplot(1, 2, 1)
    sns.lineplot(data=df_metrics, x='date', y='facility_utilization')
    plt.title('Facility Utilization Over Time')
    plt.xticks(rotation=45)
    
    # Plot healthcare quality
    plt.subplot(1, 2, 2)
    sns.lineplot(data=df_metrics, x='date', y='healthcare_quality')
    plt.title('Healthcare Quality Over Time')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('simulation_results.png')
    plt.close()

def main():
    """Main function to run the simulation."""
    try:
        # Set up simulation parameters
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)  # One year simulation
        
        # Create simulation engine
        logger.info("Initializing simulation engine...")
        engine = SimulationEngine(start_date, end_date)
        
        # Create and add sample data
        logger.info("Creating sample data...")
        locations, facilities, workers, patients = create_sample_data()
        
        # Add data to simulation
        logger.info("Adding data to simulation...")
        for location in locations.values():
            engine.add_location(location)
        for facility in facilities.values():
            engine.add_facility(facility)
        for worker in workers.values():
            engine.add_healthcare_worker(worker)
        for patient in patients.values():
            engine.add_patient(patient)
        
        # Run simulation
        logger.info("Running simulation...")
        engine.run()
        
        # Analyze results
        logger.info("Analyzing results...")
        df_metrics, insights = analyze_results(engine)
        
        # Generate report
        logger.info("Generating report...")
        report = generate_report(df_metrics, insights)
        print("\n" + report)
        
        # Plot results
        logger.info("Generating plots...")
        plot_results(df_metrics)
        
        logger.info("Simulation completed successfully!")
        
    except Exception as e:
        logger.error(f"Error running simulation: {str(e)}")
        raise

if __name__ == "__main__":
    main() 