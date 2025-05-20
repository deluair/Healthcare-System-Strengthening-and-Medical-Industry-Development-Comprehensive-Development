"""
Main script to run the healthcare system simulation.
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List
import matplotlib.pyplot as plt
import seaborn as sns
from .simulation.core import HealthcareSystemSimulation
from .data.generator import DataGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_simulation() -> HealthcareSystemSimulation:
    """Set up the initial simulation state."""
    # Create simulation instance
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)  # Simulate one year
    simulation = HealthcareSystemSimulation(start_date, end_date)
    
    # Create data generator
    generator = DataGenerator()
    
    # Generate initial data
    logger.info("Generating initial simulation data...")
    
    # Generate locations (hierarchical structure)
    districts = [generator.generate_location() for _ in range(8)]  # 8 districts
    for district in districts:
        simulation.add_location(district)
        
        # Generate upazilas for each district
        upazilas = [generator.generate_location(district.id) for _ in range(5)]
        for upazila in upazilas:
            simulation.add_location(upazila)
            
            # Generate unions for each upazila
            unions = [generator.generate_location(upazila.id) for _ in range(10)]
            for union in unions:
                simulation.add_location(union)
                
                # Generate facilities for each union
                facilities = [generator.generate_facility(union.id) for _ in range(3)]
                for facility in facilities:
                    simulation.add_facility(facility)
                    
                    # Generate healthcare workers for each facility
                    workers = [generator.generate_healthcare_worker(facility.id) 
                             for _ in range(facility.staff_count)]
                    for worker in workers:
                        simulation.add_healthcare_worker(worker)
                        
                    # Generate resources for each facility
                    resources = [generator.generate_resource(facility.id) 
                               for _ in range(5)]
                    for resource in resources:
                        simulation.add_resource(resource)
                        
                # Generate patients for each union
                patients = [generator.generate_patient(union.id) 
                          for _ in range(1000)]  # 1000 patients per union
                for patient in patients:
                    simulation.add_patient(patient)
                    
    # Generate treatments
    treatments = [generator.generate_treatment() for _ in range(50)]
    for treatment in treatments:
        simulation.add_treatment(treatment)
        
    logger.info("Initial data generation complete.")
    return simulation

def plot_metrics(metrics: Dict[str, List[tuple]]) -> None:
    """Plot simulation metrics."""
    plt.style.use('seaborn')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Plot facility utilization
    dates, values = zip(*metrics["facility_utilization"])
    ax1.plot(dates, values, label='Facility Utilization')
    ax1.set_title('Facility Utilization Over Time')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Utilization Rate')
    ax1.legend()
    
    # Plot healthcare quality
    dates, values = zip(*metrics["healthcare_quality"])
    ax2.plot(dates, values, label='Healthcare Quality')
    ax2.set_title('Healthcare Quality Over Time')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Quality Score')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('simulation_metrics.png')
    plt.close()

def main():
    """Main function to run the simulation."""
    try:
        # Set up simulation
        simulation = setup_simulation()
        
        # Run simulation
        logger.info("Starting simulation...")
        simulation.run()
        logger.info("Simulation complete.")
        
        # Plot results
        metrics = simulation.get_metrics()
        plot_metrics(metrics)
        logger.info("Results plotted to simulation_metrics.png")
        
    except Exception as e:
        logger.error(f"Error running simulation: {str(e)}")
        raise

if __name__ == "__main__":
    main() 