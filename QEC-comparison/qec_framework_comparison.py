"""
Quantum Error Correction Framework Comparison
Loom (Entropica Labs) vs Deltakit (Riverlane)

This script demonstrates basic usage patterns for both frameworks
and provides a comparison of their capabilities.
"""

# ==============================================================================
# LOOM (Entropica Labs) - Example Usage
# ==============================================================================

def loom_example():
    """
    Example of using Loom for quantum error correction.
    
    Loom provides:
    - QEC code primitives
    - Lattice surgery operations
    - Integration with Stim and other simulators
    - Visual design through Entwine GUI
    """
    print("=" * 80)
    print("LOOM (Entropica Labs) Example")
    print("=" * 80)
    
    try:
        # Note: Actual import would require Loom to be installed
        # from loom import RepetitionCode, RotatedSurfaceCode, Eka
        # from loom.visualizer import plot_stabilizers
        
        print("\n1. Creating a Repetition Code:")
        print("   - Distance: 3")
        print("   - Code type: Bit-flip repetition code")
        print("""
   Example code:
   ```python
   from loom.code_factories import RepetitionCode
   
   # Create a distance-3 repetition code
   rep_code = RepetitionCode(distance=3, basis='Z')
   
   # Get the stabilizer measurements
   stabilizers = rep_code.get_stabilizers()
   
   # Build syndrome extraction circuit
   circuit = rep_code.build_syndrome_circuit()
   ```
        """)
        
        print("\n2. Creating a Surface Code:")
        print("   - Code type: Rotated surface code")
        print("   - Distance: 5")
        print("""
   Example code:
   ```python
   from loom.code_factories import RotatedSurfaceCode
   
   # Create a distance-5 rotated surface code
   surface_code = RotatedSurfaceCode(distance=5)
   
   # Generate logical operations using lattice surgery
   logical_x = surface_code.logical_x_operation()
   logical_z = surface_code.logical_z_operation()
   ```
        """)
        
        print("\n3. Lattice Surgery with Entwine:")
        print("   - Visual drag-and-drop interface")
        print("   - Browser-based (no installation)")
        print("   - Exports to Loom code")
        print("   - URL: https://entwine.entropicalabs.io/")
        
        print("\n4. Running with Stim Backend:")
        print("""
   Example code:
   ```python
   from loom.backends import StimBackend
   from loom.executor import Executor
   
   # Create backend and executor
   backend = StimBackend()
   executor = Executor(backend)
   
   # Run QEC experiment
   results = executor.run(circuit, num_shots=10000)
   
   # Analyze error rates
   logical_error_rate = results.compute_logical_error_rate()
   ```
        """)
        
        print("\n5. Integration with PennyLane/Catalyst:")
        print("   - Seamless integration for fault-tolerant quantum ML")
        print("   - Hybrid quantum-classical workflows")
        
        print("\nKey Features of Loom:")
        print("- ✓ Open-source Python library")
        print("- ✓ Visual IDE (Entwine) for lattice surgery")
        print("- ✓ Pre-built QEC codes (surface, repetition, Steane, Shor)")
        print("- ✓ Integration with Stim, OpenQASM 3.0")
        print("- ✓ EKA data structure for QEC state management")
        print("- ✓ Supports up to 60-70 patches in visual designer")
        
    except ImportError as e:
        print(f"\n[Note: Loom not installed. Install with: pip install loom]")
        print(f"Error: {e}")
    
    print("\n" + "=" * 80 + "\n")


# ==============================================================================
# DELTAKIT (Riverlane) - Example Usage
# ==============================================================================

def deltakit_example():
    """
    Example of using Deltakit for quantum error correction.
    
    Deltakit provides:
    - SDK for QEC circuit generation
    - Noise models and simulation
    - Decoders (including proprietary cloud decoders)
    - Integrated textbook for learning
    """
    print("=" * 80)
    print("DELTAKIT (Riverlane) Example")
    print("=" * 80)
    
    try:
        # Note: Actual import would require Deltakit to be installed
        # from deltakit import Client, RepetitionCode, SurfaceCode
        # from deltakit.decoders import LocalClusteringDecoder
        
        print("\n1. Setup and Authentication:")
        print("""
   Example code:
   ```python
   from deltakit import Client
   
   # Set up access token (free from deltakit.riverlane.com)
   Client.set_token("YOUR_TOKEN")
   ```
        """)
        
        print("\n2. Creating a QEC Circuit:")
        print("   - Define error correction code")
        print("   - Add noise model")
        print("   - Simulate execution")
        print("""
   Example code:
   ```python
   from deltakit import SurfaceCode
   from deltakit.noise import DepolarizingNoise
   
   # Create a surface code
   code = SurfaceCode(distance=5)
   
   # Generate the QEC circuit
   circuit = code.generate_circuit(num_rounds=10)
   
   # Add realistic noise model
   noise_model = DepolarizingNoise(
       gate_error=0.001,
       measurement_error=0.01
   )
   noisy_circuit = circuit.add_noise(noise_model)
   ```
        """)
        
        print("\n3. Running Simulation and Decoding:")
        print("""
   Example code:
   ```python
   from deltakit.simulation import Simulator
   from deltakit.decoders import MinimumWeightDecoder
   
   # Simulate the circuit
   simulator = Simulator()
   results = simulator.run(noisy_circuit, shots=1000)
   
   # Decode the syndrome measurements
   decoder = MinimumWeightDecoder()
   corrections = decoder.decode(results.syndromes)
   
   # Calculate logical error rate
   logical_errors = results.compute_logical_errors(corrections)
   error_rate = logical_errors / 1000
   ```
        """)
        
        print("\n4. Cloud Decoders:")
        print("   - Access to Riverlane's proprietary decoders")
        print("   - Local Clustering Decoder (LCD)")
        print("   - High-performance decoding")
        print("""
   Example code:
   ```python
   from deltakit.cloud import CloudDecoder
   
   # Use cloud-based proprietary decoder
   cloud_decoder = CloudDecoder(decoder_type='LCD')
   corrections = cloud_decoder.decode(results.syndromes)
   ```
        """)
        
        print("\n5. Learning with Deltakit Textbook:")
        print("   - Interactive tutorials from basics to advanced")
        print("   - Module 1: Why QEC is essential")
        print("   - Module 2: Repetition codes")
        print("   - Module 3: Surface codes and stabilizers")
        print("   - Module 4: Decoding techniques")
        print("   - URL: https://textbook.riverlane.com/")
        
        print("\nKey Features of Deltakit:")
        print("- ✓ Open-source SDK with cloud integration")
        print("- ✓ Comprehensive textbook for learning")
        print("- ✓ Realistic noise models")
        print("- ✓ Multiple decoder implementations")
        print("- ✓ Cloud access to proprietary decoders")
        print("- ✓ Designed for Deltaflow hardware integration")
        print("- ✓ Targets real hardware deployment")
        
    except ImportError as e:
        print(f"\n[Note: Deltakit not installed. Install with: pip install deltakit]")
        print(f"Error: {e}")
    
    print("\n" + "=" * 80 + "\n")


# ==============================================================================
# COMPARISON METRICS
# ==============================================================================

def print_comparison_table():
    """Print a comparison table of key features."""
    print("=" * 80)
    print("FEATURE COMPARISON")
    print("=" * 80)
    
    comparison = {
        "Feature": [
            "License",
            "Primary Focus",
            "Installation",
            "Visual Design Tool",
            "Code Types Supported",
            "Backend Support",
            "Lattice Surgery",
            "Cloud Integration",
            "Documentation Quality",
            "Learning Resources",
            "Hardware Integration",
            "Community/Maturity",
            "Company Focus",
            "Best For"
        ],
        "Loom (Entropica Labs)": [
            "Open-source",
            "QEC circuit design & lattice surgery",
            "pip/poetry, local install",
            "Yes - Entwine (browser-based)",
            "Surface, Repetition, Steane, Shor, 5-qubit",
            "Stim, OpenQASM 3.0, PennyLane",
            "Yes - Visual and programmatic",
            "No - Fully local",
            "Good - API docs, tutorials",
            "Entwine GUI, examples, blog posts",
            "Hardware-agnostic, research focus",
            "Newer, growing (Singapore-based)",
            "Software tools for FTQC",
            "Research, prototyping, education, visual design"
        ],
        "Deltakit (Riverlane)": [
            "Open-source SDK + proprietary cloud",
            "QEC learning & deployment pipeline",
            "pip install + cloud token",
            "No - Code-based only",
            "Repetition, Surface codes",
            "Python SDK, cloud simulators",
            "No - Focus on decoding",
            "Yes - Proprietary decoders",
            "Excellent - Comprehensive textbook",
            "Full textbook, interactive tutorials",
            "Deltaflow hardware stack integration",
            "Newer, backed by Riverlane (UK-based)",
            "Real-time QEC hardware + software",
            "Learning QEC, production deployment, hardware"
        ]
    }
    
    # Print table
    print(f"\n{'Feature':<30} | {'Loom':<40} | {'Deltakit':<40}")
    print("-" * 115)
    
    for i, feature in enumerate(comparison["Feature"]):
        loom_val = comparison["Loom (Entropica Labs)"][i]
        delta_val = comparison["Deltakit (Riverlane)"][i]
        print(f"{feature:<30} | {loom_val:<40} | {delta_val:<40}")
    
    print("\n" + "=" * 80 + "\n")


# ==============================================================================
# DETAILED COMPARISON
# ==============================================================================

def print_detailed_comparison():
    """Print detailed analysis of each framework."""
    
    print("=" * 80)
    print("DETAILED ANALYSIS")
    print("=" * 80)
    
    print("\n1. EASE OF USE")
    print("-" * 80)
    print("\nLoom:")
    print("  ✓ Entwine visual interface makes lattice surgery intuitive")
    print("  ✓ No authentication or cloud setup required")
    print("  ✓ Poetry-based installation, standard Python workflow")
    print("  - Steeper learning curve for programmatic API")
    print("  - Less structured learning path")
    
    print("\nDeltakit:")
    print("  ✓ Structured textbook provides clear learning progression")
    print("  ✓ Simple pip install + token setup")
    print("  ✓ Interactive tutorials with code exercises")
    print("  ✓ Well-documented SDK with examples")
    print("  - Requires cloud token registration")
    print("  - No visual design interface")
    
    print("\n\n2. CAPABILITIES")
    print("-" * 80)
    print("\nLoom:")
    print("  ✓ Strong focus on lattice surgery operations")
    print("  ✓ Multiple pre-built QEC codes")
    print("  ✓ Visual circuit design up to 60-70 patches")
    print("  ✓ EKA data structure for state management")
    print("  ✓ Integration with PennyLane/Catalyst for QML")
    print("  ✓ Exports to multiple backends (Stim, OpenQASM)")
    
    print("\nDeltakit:")
    print("  ✓ Comprehensive noise modeling")
    print("  ✓ Multiple decoder implementations")
    print("  ✓ Access to proprietary cloud decoders (LCD)")
    print("  ✓ Designed for hardware deployment pipeline")
    print("  ✓ Integration with Deltaflow hardware")
    print("  ✓ Focus on real-time QEC execution")
    
    print("\n\n3. MATURITY")
    print("-" * 80)
    print("\nLoom:")
    print("  - Newer framework (launched 2024-2025)")
    print("  - Growing community")
    print("  - Active development by Entropica Labs")
    print("  - Used in QEC Challenge (May-June 2025)")
    print("  - Part of larger vision: Quilt FTOS")
    
    print("\nDeltakit:")
    print("  - Launched September 2025")
    print("  - Backed by Riverlane (established QEC leader)")
    print("  - VP Liz Durst (ex-IBM Qiskit lead)")
    print("  - Designed to complement Deltaflow hardware")
    print("  - Targets MegaQuOp scale by 2026")
    
    print("\n\n4. DOCUMENTATION QUALITY")
    print("-" * 80)
    print("\nLoom:")
    print("  Rating: 7/10")
    print("  ✓ API reference documentation")
    print("  ✓ Installation guides")
    print("  ✓ Example notebooks")
    print("  ✓ Blog posts and technical papers")
    print("  - Less comprehensive learning materials")
    print("  - Could benefit from more tutorials")
    
    print("\nDeltakit:")
    print("  Rating: 9/10")
    print("  ✓ Comprehensive interactive textbook")
    print("  ✓ Module-by-module progression")
    print("  ✓ Code exercises with explanations")
    print("  ✓ Practical examples throughout")
    print("  ✓ Clear API documentation")
    print("  ✓ Addresses 82% barrier of lack of training")
    
    print("\n\n5. USE CASE RECOMMENDATIONS")
    print("-" * 80)
    print("\nChoose Loom if you:")
    print("  • Want visual, intuitive circuit design")
    print("  • Focus on lattice surgery research")
    print("  • Need to prototype complex QEC schemes quickly")
    print("  • Prefer local-only tools (no cloud)")
    print("  • Work on quantum machine learning with QEC")
    print("  • Are in academic/research environment")
    
    print("\nChoose Deltakit if you:")
    print("  • Are learning QEC from scratch")
    print("  • Plan to deploy on real hardware")
    print("  • Need access to advanced decoders")
    print("  • Want structured, textbook-driven learning")
    print("  • Are preparing for hardware integration")
    print("  • Work with Riverlane's Deltaflow stack")
    
    print("\n" + "=" * 80 + "\n")


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    """Run the full comparison."""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  QUANTUM ERROR CORRECTION FRAMEWORK COMPARISON".center(78) + "║")
    print("║" + "  Loom (Entropica Labs) vs Deltakit (Riverlane)".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    print("\n")
    
    # Run examples
    loom_example()
    deltakit_example()
    
    # Print comparison tables
    print_comparison_table()
    print_detailed_comparison()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("""
Both frameworks are excellent tools for quantum error correction, but serve
different primary purposes:

LOOM excels at:
  - Visual design and rapid prototyping
  - Lattice surgery operations
  - Academic research and exploration
  - Integration with quantum ML frameworks

DELTAKIT excels at:
  - Structured learning and skill development
  - Path to hardware deployment
  - Advanced decoding with cloud resources
  - Production-ready QEC workflows

Many practitioners may benefit from using BOTH:
  - Use Deltakit to learn QEC fundamentals
  - Use Loom's Entwine for visual design and lattice surgery
  - Leverage each tool's strengths for different aspects of QEC work

Both are actively developed and represent the cutting edge of QEC software tools.
    """)
    print("=" * 80)
    
    print("\nFor more information:")
    print("  Loom: https://loom-docs.entropicalabs.com/")
    print("  Deltakit: https://deltakit.riverlane.com/")
    print()


if __name__ == "__main__":
    main()
