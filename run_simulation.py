"""
Script to run the healthcare system simulation and analyze results.
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from healthcare_system.main import setup_simulation, plot_metrics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def analyze_results(simulation):
    """Analyze simulation results and generate insights."""
    metrics = simulation.get_metrics()
    
    # Convert metrics to pandas DataFrame for analysis
    utilization_df = pd.DataFrame(
        metrics["facility_utilization"],
        columns=["date", "utilization"]
    )
    quality_df = pd.DataFrame(
        metrics["healthcare_quality"],
        columns=["date", "quality"]
    )
    
    # Calculate statistics
    utilization_stats = utilization_df["utilization"].describe()
    quality_stats = quality_df["quality"].describe()
    
    # Generate insights
    insights = {
        "facility_utilization": {
            "mean": utilization_stats["mean"],
            "std": utilization_stats["std"],
            "min": utilization_stats["min"],
            "max": utilization_stats["max"],
            "trend": "increasing" if utilization_df["utilization"].iloc[-1] > utilization_df["utilization"].iloc[0] else "decreasing"
        },
        "healthcare_quality": {
            "mean": quality_stats["mean"],
            "std": quality_stats["std"],
            "min": quality_stats["min"],
            "max": quality_stats["max"],
            "trend": "increasing" if quality_df["quality"].iloc[-1] > quality_df["quality"].iloc[0] else "decreasing"
        }
    }
    
    return insights

def generate_report(insights):
    """Generate a comprehensive report of simulation results."""
    report = f"""
Healthcare System Simulation Report
=================================
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Facility Utilization Analysis
---------------------------
Mean Utilization: {insights['facility_utilization']['mean']:.2%}
Standard Deviation: {insights['facility_utilization']['std']:.2%}
Minimum Utilization: {insights['facility_utilization']['min']:.2%}
Maximum Utilization: {insights['facility_utilization']['max']:.2%}
Trend: {insights['facility_utilization']['trend']}

Healthcare Quality Analysis
-------------------------
Mean Quality Score: {insights['healthcare_quality']['mean']:.2%}
Standard Deviation: {insights['healthcare_quality']['std']:.2%}
Minimum Quality Score: {insights['healthcare_quality']['min']:.2%}
Maximum Quality Score: {insights['healthcare_quality']['max']:.2%}
Trend: {insights['healthcare_quality']['trend']}

Recommendations
--------------
1. Facility Utilization:
   - {'Increase capacity' if insights['facility_utilization']['mean'] > 0.8 else 'Optimize resource allocation'}
   - {'Implement load balancing' if insights['facility_utilization']['std'] > 0.2 else 'Maintain current distribution'}

2. Healthcare Quality:
   - {'Focus on quality improvement initiatives' if insights['healthcare_quality']['mean'] < 0.7 else 'Maintain quality standards'}
   - {'Address quality variations' if insights['healthcare_quality']['std'] > 0.15 else 'Continue current practices'}

3. System-wide Recommendations:
   - {'Consider expanding healthcare infrastructure' if insights['facility_utilization']['trend'] == 'increasing' else 'Optimize existing infrastructure'}
   - {'Implement quality enhancement programs' if insights['healthcare_quality']['trend'] == 'decreasing' else 'Maintain quality improvement initiatives'}
"""
    return report

def main():
    """Main function to run the simulation and generate analysis."""
    try:
        # Set up and run simulation
        logger.info("Setting up simulation...")
        simulation = setup_simulation()
        
        logger.info("Running simulation...")
        simulation.run()
        
        # Analyze results
        logger.info("Analyzing results...")
        insights = analyze_results(simulation)
        
        # Generate plots
        logger.info("Generating plots...")
        plot_metrics(simulation.get_metrics())
        
        # Generate and save report
        logger.info("Generating report...")
        report = generate_report(insights)
        with open("simulation_report.txt", "w") as f:
            f.write(report)
        
        logger.info("Analysis complete. Results saved to simulation_report.txt and simulation_metrics.png")
        
    except Exception as e:
        logger.error(f"Error in simulation: {str(e)}")
        raise

if __name__ == "__main__":
    main() 