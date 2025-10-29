"""
DELTAKIT - Quantum Error Correction SDK
by Riverlane

This guide provides getting started examples for working with Deltakit,
Riverlane's comprehensive SDK for learning, developing, and implementing
quantum error correction (QEC).

Website: https://deltakit.riverlane.com/
Textbook: https://deltakit.riverlane.com/ (interactive learning modules)
Documentation: https://deltakit.riverlane.com/docs
"""

# ============================================================================
# INSTALLATION AND SETUP
# ============================================================================
"""
Step 1: Create a free access token at https://deltakit.riverlane.com/

Step 2: Install Deltakit
    pip install deltakit

Step 3: Configure your token
    from deltakit import Client
    Client.set_token("YOUR_TOKEN")
    
This token allows access to Riverlane's cloud services including:
- High-performance proprietary decoders (LCD, BP-AC)
- Additional error-correcting codes
- Leakage-aware simulation tools
"""

# ============================================================================
# EXAMPLE 1: Basic Setup and Configuration
# ============================================================================

from deltakit import Client

def example_setup():
    """Configure Deltakit with your access token"""
    
    # Set your access token (get it from https://deltakit.riverlane.com/)
    # Client.set_token("YOUR_TOKEN_HERE")
    
    # Verify connection
    client = Client()
    
    print("Deltakit Configuration:")
    print(f"  Client initialized: {client is not None}")
    print(f"  Cloud services available: {client.has_token}")
    print("\nReady to start building QEC experiments!")
    
    return client


# ============================================================================
# EXAMPLE 2: Creating a Simple Repetition Code Circuit
# ============================================================================

from deltakit import RepetitionCode, MemoryExperiment

def example_repetition_code():
    """
    Create a basic repetition code for bit-flip error correction.
    The repetition code is the simplest QEC code and great for learning.
    """
    
    # Create a distance-3 repetition code
    # Distance determines error correction capability
    code = RepetitionCode(distance=3)
    
    print(f"Repetition Code Properties:")
    print(f"  Distance: {code.distance}")
    print(f"  Physical qubits: {code.num_physical_qubits}")
    print(f"  Data qubits: {code.num_data_qubits}")
    print(f"  Ancilla qubits: {code.num_ancilla_qubits}")
    
    # Generate the QEC circuit for one cycle
    circuit = code.generate_circuit()
    
    print(f"\nCircuit Properties:")
    print(f"  Gates: {circuit.num_gates}")
    print(f"  Depth: {circuit.depth}")
    print(f"  Measurements: {circuit.num_measurements}")
    
    return code, circuit


# ============================================================================
# EXAMPLE 3: Surface Code - The Industry Standard
# ============================================================================

from deltakit import SurfaceCode, Stabilizer

def example_surface_code():
    """
    The surface code is the leading QEC code for near-term quantum computers.
    It has a high threshold and can be implemented on 2D qubit arrays.
    """
    
    # Create a distance-3 surface code
    code = SurfaceCode(distance=3)
    
    print(f"Surface Code Properties:")
    print(f"  Distance: {code.distance}")
    print(f"  Physical qubits: {code.num_physical_qubits}")
    print(f"  Logical qubits: {code.num_logical_qubits}")
    
    # Surface codes have both X and Z stabilizers
    print(f"  X-type stabilizers: {code.num_x_stabilizers}")
    print(f"  Z-type stabilizers: {code.num_z_stabilizers}")
    
    # Generate syndrome extraction circuit
    syndrome_circuit = code.syndrome_extraction_circuit()
    
    print(f"\nSyndrome Extraction:")
    print(f"  Circuit depth: {syndrome_circuit.depth}")
    print(f"  Stabilizer measurements: {len(code.stabilizers)}")
    
    return code


# ============================================================================
# EXAMPLE 4: Running a Memory Experiment
# ============================================================================

from deltakit import MemoryExperiment, NoiseModel

def example_memory_experiment(num_rounds=10, num_shots=1000):
    """
    A memory experiment tests how well a code preserves quantum information.
    We initialize a logical state, run QEC cycles, then measure.
    """
    
    # Create a surface code
    code = SurfaceCode(distance=3)
    
    # Setup a memory experiment
    experiment = MemoryExperiment(
        code=code,
        num_rounds=num_rounds,  # Number of QEC cycles
        initial_state='|0⟩'      # Initial logical state
    )
    
    # Define a noise model
    noise = NoiseModel(
        gate_error_rate=0.001,        # 0.1% error per gate
        measurement_error_rate=0.001,  # 0.1% measurement error
        idle_error_rate=0.0001         # Idle qubit error rate
    )
    
    # Add noise to the experiment
    experiment.add_noise(noise)
    
    # Run the experiment
    results = experiment.run(shots=num_shots)
    
    # Analyze results
    print(f"Memory Experiment Results:")
    print(f"  QEC rounds: {num_rounds}")
    print(f"  Shots: {num_shots}")
    print(f"  Logical error rate: {results.logical_error_rate:.4f}")
    print(f"  Physical error rate: {noise.gate_error_rate}")
    print(f"  Error suppression: {noise.gate_error_rate/results.logical_error_rate:.2f}x")
    
    return results


# ============================================================================
# EXAMPLE 5: Decoding with Multiple Decoders
# ============================================================================

from deltakit import Decoder, LCDDecoder, BPACDecoder

def example_decoding_comparison():
    """
    Compare different decoders on the same QEC problem.
    Deltakit provides access to multiple decoding algorithms.
    """
    
    code = SurfaceCode(distance=5)
    
    # Create different decoders
    decoders = {
        'MWPM': Decoder('minimum_weight_perfect_matching'),
        'LCD': LCDDecoder(),  # Riverlane's Local Clustering Decoder
        'BP-AC': BPACDecoder()  # Belief Propagation with Automorphism Clustering
    }
    
    # Setup experiment
    experiment = MemoryExperiment(code=code, num_rounds=3)
    noise = NoiseModel(gate_error_rate=0.001)
    experiment.add_noise(noise)
    
    results_comparison = {}
    
    for decoder_name, decoder in decoders.items():
        # Run experiment with this decoder
        results = experiment.run(shots=1000, decoder=decoder)
        results_comparison[decoder_name] = {
            'logical_error_rate': results.logical_error_rate,
            'decode_time': results.decode_time_ms
        }
        
        print(f"\n{decoder_name} Decoder:")
        print(f"  Logical error rate: {results.logical_error_rate:.6f}")
        print(f"  Average decode time: {results.decode_time_ms:.2f} ms")
    
    return results_comparison


# ============================================================================
# EXAMPLE 6: Advanced Noise Models
# ============================================================================

from deltakit import NoiseModel, DepolarizingNoise, BiasedNoise

def example_noise_models():
    """
    Model realistic noise sources in quantum hardware.
    Different noise models can dramatically affect QEC performance.
    """
    
    # 1. Depolarizing noise (equal probability of X, Y, Z errors)
    depolarizing = NoiseModel(
        noise_type='depolarizing',
        error_rate=0.001
    )
    
    # 2. Biased noise (more common in some qubit types)
    # Example: Phase-flip (Z) errors are 10x more likely than bit-flip (X)
    biased = NoiseModel(
        noise_type='biased',
        error_rate=0.001,
        bias_ratio=10.0,  # Z errors are 10x more likely
        bias_type='Z'
    )
    
    # 3. Circuit-level noise (gate-dependent)
    circuit_noise = NoiseModel(
        single_qubit_gate_error=0.0001,
        two_qubit_gate_error=0.001,
        measurement_error=0.001,
        idle_error=0.00001
    )
    
    # 4. Leakage noise (transitions to non-computational states)
    leakage_noise = NoiseModel(
        gate_error_rate=0.001,
        leakage_rate=0.0001  # 0.01% probability of leakage
    )
    
    print("Noise Models in Deltakit:")
    print("1. Depolarizing: Equal X, Y, Z errors")
    print("2. Biased: Asymmetric error rates (common in superconducting qubits)")
    print("3. Circuit-level: Different rates for different operations")
    print("4. Leakage: Models transitions beyond computational space")
    
    return {
        'depolarizing': depolarizing,
        'biased': biased,
        'circuit': circuit_noise,
        'leakage': leakage_noise
    }


# ============================================================================
# EXAMPLE 7: Working with qLDPC Codes
# ============================================================================

from deltakit import qLDPCCode, BivariateProductCode

def example_qldpc_codes():
    """
    Quantum Low-Density Parity-Check (qLDPC) codes are promising for
    large-scale quantum computing due to better encoding rates.
    """
    
    # Bivariate bicycle code (a type of qLDPC code)
    code = BivariateProductCode(
        l=6,  # Code parameter
        m=6   # Code parameter
    )
    
    print(f"qLDPC Code Properties:")
    print(f"  Physical qubits: {code.num_physical_qubits}")
    print(f"  Logical qubits: {code.num_logical_qubits}")
    print(f"  Distance: {code.distance}")
    print(f"  Encoding rate: {code.encoding_rate:.3f}")
    
    # qLDPC codes have sparse check matrices
    print(f"  Check matrix sparsity: {code.check_sparsity:.3f}")
    
    # Generate circuit
    circuit = code.generate_circuit()
    
    print(f"\nCircuit Properties:")
    print(f"  Depth: {circuit.depth}")
    print(f"  Two-qubit gates: {circuit.num_two_qubit_gates}")
    
    return code


# ============================================================================
# EXAMPLE 8: Leakage-Aware Simulation
# ============================================================================

from deltakit import LeakageSimulator, AdaptiveDecoder

def example_leakage_simulation():
    """
    Leakage (transitions to non-computational states) is a critical
    issue in superconducting qubits. Deltakit provides tools to
    model and mitigate leakage effects.
    """
    
    code = SurfaceCode(distance=3)
    
    # Create leakage simulator
    simulator = LeakageSimulator(
        code=code,
        leakage_rate=0.0001,
        leakage_detection=True,  # Model leakage detection
        herald_efficiency=0.9     # Detection efficiency
    )
    
    # Run simulation
    experiment = MemoryExperiment(code=code, num_rounds=5)
    experiment.set_simulator(simulator)
    
    results = experiment.run(shots=1000)
    
    print(f"Leakage-Aware Simulation:")
    print(f"  Leakage events detected: {results.num_leakage_events}")
    print(f"  Leakage rate: {results.leakage_rate:.6f}")
    print(f"  Logical error rate (with leakage): {results.logical_error_rate:.6f}")
    
    # Use leakage-aware decoder
    adaptive_decoder = AdaptiveDecoder(leakage_aware=True)
    results_adaptive = experiment.run(shots=1000, decoder=adaptive_decoder)
    
    print(f"\nWith Leakage-Aware Decoding:")
    print(f"  Logical error rate: {results_adaptive.logical_error_rate:.6f}")
    print(f"  Improvement: {(1 - results_adaptive.logical_error_rate/results.logical_error_rate)*100:.1f}%")
    
    return results_adaptive


# ============================================================================
# EXAMPLE 9: Stability Experiments
# ============================================================================

from deltakit import StabilityExperiment

def example_stability_experiment():
    """
    Stability experiments measure the fidelity of QEC over many cycles.
    They help characterize the error threshold.
    """
    
    code = SurfaceCode(distance=5)
    
    # Define range of error rates to test
    error_rates = [0.0001, 0.0003, 0.001, 0.003, 0.01]
    
    results_by_rate = {}
    
    for error_rate in error_rates:
        # Create experiment
        experiment = StabilityExperiment(
            code=code,
            num_rounds=10,
            target_fidelity=0.99  # Target logical fidelity
        )
        
        # Add noise
        noise = NoiseModel(gate_error_rate=error_rate)
        experiment.add_noise(noise)
        
        # Run
        results = experiment.run(shots=500)
        results_by_rate[error_rate] = results.logical_fidelity
        
        print(f"Error rate {error_rate:.4f}: Fidelity = {results.logical_fidelity:.4f}")
    
    # Estimate threshold
    threshold = experiment.estimate_threshold(results_by_rate)
    print(f"\nEstimated error threshold: ~{threshold:.4f}")
    
    return results_by_rate


# ============================================================================
# EXAMPLE 10: Circuit Transpilation
# ============================================================================

from deltakit import Transpiler, NativeGateSet

def example_transpilation():
    """
    Transpile QEC circuits to match your hardware's native gate set.
    Deltakit intelligently handles gate decomposition.
    """
    
    code = SurfaceCode(distance=3)
    circuit = code.syndrome_extraction_circuit()
    
    # Define native gate sets for different platforms
    gate_sets = {
        'Superconducting': NativeGateSet(
            single_qubit=['RZ', 'SX'],
            two_qubit=['CZ']
        ),
        'Trapped Ion': NativeGateSet(
            single_qubit=['RZ', 'RX', 'RY'],
            two_qubit=['XX']
        ),
        'Neutral Atom': NativeGateSet(
            single_qubit=['RZ', 'RX'],
            two_qubit=['CZ']
        )
    }
    
    for platform, gate_set in gate_sets.items():
        # Transpile circuit
        transpiler = Transpiler(gate_set)
        transpiled = transpiler.transpile(circuit)
        
        print(f"\n{platform} Platform:")
        print(f"  Original gates: {circuit.num_gates}")
        print(f"  Transpiled gates: {transpiled.num_gates}")
        print(f"  Gate overhead: {transpiled.num_gates/circuit.num_gates:.2f}x")
        print(f"  Estimated fidelity: {transpiled.estimated_fidelity:.6f}")
    
    return transpiled


# ============================================================================
# EXAMPLE 11: Visualization and Analysis
# ============================================================================

from deltakit import Visualizer, AnalysisTools

def example_visualization():
    """
    Visualize QEC circuits, codes, and results.
    """
    
    code = SurfaceCode(distance=3)
    experiment = MemoryExperiment(code=code, num_rounds=5)
    
    # Add noise and run
    noise = NoiseModel(gate_error_rate=0.001)
    experiment.add_noise(noise)
    results = experiment.run(shots=100)
    
    # Create visualizer
    viz = Visualizer()
    
    # 1. Visualize the code structure
    viz.plot_code_layout(code, save_path='surface_code_layout.png')
    print("Code layout saved to: surface_code_layout.png")
    
    # 2. Visualize a syndrome pattern
    viz.plot_syndrome_pattern(
        results.syndromes[0],  # First shot
        code=code,
        save_path='syndrome_pattern.png'
    )
    print("Syndrome pattern saved to: syndrome_pattern.png")
    
    # 3. Plot logical error rates over rounds
    viz.plot_error_rate_evolution(
        results,
        save_path='error_evolution.png'
    )
    print("Error evolution saved to: error_evolution.png")
    
    # Analysis tools
    analysis = AnalysisTools()
    
    # Calculate error statistics
    stats = analysis.error_statistics(results)
    print(f"\nError Statistics:")
    print(f"  Mean logical error rate: {stats['mean_error_rate']:.6f}")
    print(f"  Std deviation: {stats['std_error_rate']:.6f}")
    print(f"  95% confidence interval: [{stats['ci_lower']:.6f}, {stats['ci_upper']:.6f}]")
    
    return viz, analysis


# ============================================================================
# EXAMPLE 12: Integration with Deltaflow (Hardware Deployment)
# ============================================================================

from deltakit import DeltaflowConnector

def example_deltaflow_integration():
    """
    Deltakit seamlessly integrates with Deltaflow, Riverlane's real-time
    QEC hardware stack. This enables deployment to actual quantum hardware.
    """
    
    # Note: This requires access to Deltaflow hardware
    # For simulation purposes, this example shows the workflow
    
    code = SurfaceCode(distance=5)
    experiment = MemoryExperiment(code=code, num_rounds=10)
    
    # Connect to Deltaflow
    connector = DeltaflowConnector()
    
    # Compile experiment for Deltaflow
    deltaflow_job = connector.compile(
        experiment=experiment,
        target_hardware='deltaflow_v2',
        optimization_level=2
    )
    
    print("Deltaflow Integration:")
    print(f"  Target: Deltaflow v2")
    print(f"  Compiled circuit depth: {deltaflow_job.circuit_depth}")
    print(f"  Estimated runtime: {deltaflow_job.estimated_runtime_ms} ms")
    print(f"  Real-time decoder: Local Clustering Decoder (LCD)")
    
    # Submit to hardware (when available)
    # job_id = connector.submit(deltaflow_job)
    # results = connector.get_results(job_id)
    
    print("\nNote: Hardware execution requires Deltaflow access")
    print("Contact Riverlane for deployment partnerships")
    
    return deltaflow_job


# ============================================================================
# EXAMPLE 13: Learning Path - Following the Textbook
# ============================================================================

def example_textbook_workflow():
    """
    Deltakit includes an interactive textbook with 4 learning modules.
    This example shows how to progress through the curriculum.
    """
    
    print("Deltakit Learning Modules:\n")
    
    print("Module 1: Introduction to QEC")
    print("  - Why quantum error correction is essential")
    print("  - Classical error correction as intuition")
    print("  - The threshold theorem")
    
    print("\nModule 2: Repetition Codes")
    print("  - Bit-flip and phase-flip codes")
    print("  - Syndrome extraction circuits")
    print("  - Hands-on: Build a 3-qubit repetition code")
    code_module2 = RepetitionCode(distance=3)
    
    print("\nModule 3: Surface Codes")
    print("  - Stabilizer formalism")
    print("  - 2D lattice structure")
    print("  - Hands-on: Implement a surface code memory")
    code_module3 = SurfaceCode(distance=3)
    
    print("\nModule 4: Decoding")
    print("  - Minimum weight perfect matching")
    print("  - Belief propagation")
    print("  - Hands-on: Compare decoder performance")
    
    print("\nAccess the full interactive textbook at:")
    print("https://deltakit.riverlane.com/textbook")
    
    return {
        'module2_code': code_module2,
        'module3_code': code_module3
    }


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DELTAKIT - Quantum Error Correction SDK by Riverlane")
    print("=" * 70)
    
    print("\n--- Example 1: Setup ---")
    print("First, get your free token at https://deltakit.riverlane.com/")
    
    print("\n--- Example 2: Repetition Code ---")
    print("The simplest QEC code, great for learning the basics")
    
    print("\n--- Example 3: Surface Code ---")
    print("Industry standard for near-term quantum computers")
    
    print("\n--- Example 4: Memory Experiment ---")
    print("Test how well codes preserve quantum information")
    
    print("\n--- Example 5: Decoder Comparison ---")
    print("Deltakit provides multiple state-of-the-art decoders:")
    print("  - MWPM: Minimum Weight Perfect Matching")
    print("  - LCD: Local Clustering Decoder (Riverlane proprietary)")
    print("  - BP-AC: Belief Propagation with Automorphism Clustering")
    
    print("\n--- Example 6: Noise Models ---")
    print("Model realistic quantum hardware noise")
    
    print("\n--- Example 7: qLDPC Codes ---")
    print("Next-generation codes with better encoding rates")
    
    print("\n--- Example 8: Leakage Simulation ---")
    print("Model and mitigate leakage to non-computational states")
    
    print("\n--- Example 9: Stability Experiments ---")
    print("Characterize error thresholds and fidelity")
    
    print("\n--- Example 10: Transpilation ---")
    print("Adapt circuits to different hardware platforms")
    
    print("\n--- Example 11: Visualization ---")
    print("Analyze and visualize QEC experiments")
    
    print("\n--- Example 12: Deltaflow Integration ---")
    print("Deploy to real quantum hardware with Riverlane's Deltaflow")
    
    print("\n--- Example 13: Learning Modules ---")
    example_textbook_workflow()
    
    print("\n" + "=" * 70)
    print("Resources:")
    print("  Website: https://deltakit.riverlane.com/")
    print("  Documentation: https://deltakit.riverlane.com/docs")
    print("  Textbook: https://deltakit.riverlane.com/textbook")
    print("  GitHub: Check Riverlane's GitHub for examples")
    print("  Community: Join the Deltakit community forums")
    print("\nDeltakit bridges the gap from learning QEC fundamentals")
    print("to deploying on real quantum hardware!")
    print("=" * 70)
