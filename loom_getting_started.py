"""
LOOM - Quantum Error Correction Framework
by Entropica Labs

This guide provides getting started examples for working with Loom,
an open-source Python library for building Quantum Error Correction (QEC) 
code primitives and simulating fault-tolerant quantum circuits.

GitHub: https://github.com/entropicalabs/el-loom
Documentation: https://loom-api-docs.entropicalabs.com/
Loom Design: https://loom-docs.entropicalabs.com/
"""

# ============================================================================
# INSTALLATION
# ============================================================================
"""
To install Loom, run:
    pip install loom

Or install from source using Poetry:
    git clone https://github.com/entropicalabs/el-loom.git
    cd el-loom
    poetry install
"""

# ============================================================================
# EXAMPLE 1: Creating a Simple Repetition Code
# ============================================================================
"""
The repetition code is one of the simplest QEC codes. It protects against
bit-flip errors by encoding a logical qubit into multiple physical qubits.
"""

from loom.code_factory import RepetitionCodeFactory
from loom.backends.stim import StimBackend
from loom.visualizer import plot_stabilizers

def example_repetition_code():
    """Create and visualize a repetition code"""
    
    # Create a distance-3 repetition code (3 physical qubits)
    code_factory = RepetitionCodeFactory(distance=3, orientation='horizontal')
    
    # Generate the code structure
    code = code_factory.generate_code()
    
    # Create an EKA data structure (Entropica's single source of truth)
    # EKA stores all QEC context including stabilizers, qubits, and operations
    eka = code.to_eka()
    
    # Visualize the stabilizer structure
    plot_stabilizers(eka)
    
    # Print code properties
    print(f"Number of data qubits: {len(eka.data_qubits)}")
    print(f"Number of stabilizers: {len(eka.stabilizers)}")
    print(f"Code distance: {code.distance}")
    
    return eka


# ============================================================================
# EXAMPLE 2: Working with the Rotated Surface Code
# ============================================================================
"""
The rotated surface code is a popular topological code used in many quantum
computing implementations. It provides better distance scaling than the
standard surface code.
"""

from loom.code_factory import RotatedSurfaceCodeFactory

def example_surface_code():
    """Create a rotated surface code"""
    
    # Create a distance-3 rotated surface code
    code_factory = RotatedSurfaceCodeFactory(distance=3)
    
    # Generate the code
    code = code_factory.generate_code()
    eka = code.to_eka()
    
    # The surface code has both X and Z stabilizers
    print(f"Total stabilizers: {len(eka.stabilizers)}")
    
    # Extract stabilizer information
    for idx, stabilizer in enumerate(eka.stabilizers[:3]):  # Show first 3
        print(f"Stabilizer {idx}: {stabilizer}")
    
    return eka


# ============================================================================
# EXAMPLE 3: Building a Quantum Memory Experiment
# ============================================================================
"""
A quantum memory experiment runs QEC cycles to maintain quantum information
over time. This involves repeatedly measuring syndrome qubits and applying
corrections.
"""

from loom.eka import Eka
from loom.circuit import Circuit
from loom.interpretation import Interpretation

def example_memory_experiment(num_cycles=5):
    """Run a basic memory experiment with multiple QEC cycles"""
    
    # Create a repetition code
    code_factory = RepetitionCodeFactory(distance=5)
    code = code_factory.generate_code()
    eka = code.to_eka()
    
    # Create a circuit for syndrome extraction
    circuit = Circuit(eka)
    
    # Initialize logical qubit in |0⟩ state
    circuit.add_logical_initialization('Z')
    
    # Perform multiple QEC cycles
    for cycle in range(num_cycles):
        # Measure stabilizers (syndrome extraction)
        circuit.add_syndrome_measurement_round()
        
    # Final measurement of the logical qubit
    circuit.add_logical_measurement('Z')
    
    # Create interpretation (maps logical operations to physical circuit)
    interpretation = Interpretation(circuit)
    
    print(f"Total QEC cycles: {num_cycles}")
    print(f"Total circuit depth: {interpretation.depth}")
    print(f"Number of measurements: {interpretation.num_measurements}")
    
    return circuit, interpretation


# ============================================================================
# EXAMPLE 4: Simulating with Stim Backend
# ============================================================================
"""
Loom supports multiple backends for simulation. Stim is a fast stabilizer
circuit simulator that's perfect for QEC experiments.
"""

from loom.backends.stim import StimBackend
from loom.executor import Executor
import numpy as np

def example_stim_simulation(num_shots=1000):
    """Simulate a QEC experiment using Stim backend"""
    
    # Create a simple repetition code
    code_factory = RepetitionCodeFactory(distance=3)
    code = code_factory.generate_code()
    eka = code.to_eka()
    
    # Build a memory circuit
    circuit = Circuit(eka)
    circuit.add_logical_initialization('Z')
    circuit.add_syndrome_measurement_round()
    circuit.add_logical_measurement('Z')
    
    # Convert to Stim circuit
    stim_backend = StimBackend()
    stim_circuit = stim_backend.from_loom_circuit(circuit)
    
    # Add noise model (depolarizing noise)
    physical_error_rate = 0.001
    stim_circuit = stim_backend.add_noise(
        stim_circuit, 
        error_rate=physical_error_rate
    )
    
    # Execute the simulation
    executor = Executor(backend=stim_backend)
    results = executor.run(stim_circuit, shots=num_shots)
    
    # Analyze results
    logical_error_rate = np.mean(results.logical_errors)
    print(f"Physical error rate: {physical_error_rate}")
    print(f"Logical error rate: {logical_error_rate:.4f}")
    print(f"Error suppression: {physical_error_rate/logical_error_rate:.2f}x")
    
    return results


# ============================================================================
# EXAMPLE 5: Working with Other QEC Codes
# ============================================================================
"""
Loom includes several pre-built QEC codes out of the box.
"""

from loom.code_factory import (
    ShorCodeFactory,
    SteaneCodeFactory,
    FiveQubitPerfectCodeFactory
)

def example_various_codes():
    """Demonstrate various QEC codes available in Loom"""
    
    codes = {
        'Shor Code (9 qubits)': ShorCodeFactory(),
        'Steane Code (7 qubits)': SteaneCodeFactory(),
        'Five Qubit Perfect Code': FiveQubitPerfectCodeFactory(),
    }
    
    for name, factory in codes.items():
        code = factory.generate_code()
        eka = code.to_eka()
        
        print(f"\n{name}:")
        print(f"  Data qubits: {len(eka.data_qubits)}")
        print(f"  Ancilla qubits: {len(eka.ancilla_qubits)}")
        print(f"  Stabilizers: {len(eka.stabilizers)}")
        print(f"  Code distance: {code.distance}")


# ============================================================================
# EXAMPLE 6: Lattice Surgery Operations
# ============================================================================
"""
Loom supports lattice surgery, a technique for performing logical operations
on surface code patches. This is particularly useful when working with the
Entwine GUI.
"""

from loom.lattice_surgery import LatticeSurgeryBlock

def example_lattice_surgery():
    """Demonstrate lattice surgery operations"""
    
    # Create two surface code patches
    patch1_factory = RotatedSurfaceCodeFactory(distance=3)
    patch2_factory = RotatedSurfaceCodeFactory(distance=3)
    
    patch1 = patch1_factory.generate_code()
    patch2 = patch2_factory.generate_code()
    
    # Create a lattice surgery block for CNOT operation
    ls_block = LatticeSurgeryBlock()
    
    # Add patches
    ls_block.add_patch(patch1, position=(0, 0))
    ls_block.add_patch(patch2, position=(3, 0))
    
    # Perform logical CNOT via lattice surgery
    # This involves: merge patches -> measure stabilizers -> split patches
    ls_block.add_cnot_operation(control=patch1, target=patch2)
    
    # Convert to executable circuit
    circuit = ls_block.to_circuit()
    
    print(f"Lattice surgery circuit depth: {circuit.depth}")
    print(f"Number of operations: {len(circuit.operations)}")
    
    return circuit


# ============================================================================
# EXAMPLE 7: Custom Circuit Building with EKA
# ============================================================================
"""
EKA (from Sanskrit "one, first") is Loom's core data structure that serves
as a single source of truth for QEC experiments. You can build custom
circuits by directly manipulating EKA.
"""

from loom.eka import Eka, Qubit, Stabilizer
from loom.block import Block

def example_custom_eka():
    """Build a custom QEC setup using EKA"""
    
    # Create an empty EKA
    eka = Eka()
    
    # Define qubits
    data_qubits = [Qubit(idx=i, type='data') for i in range(3)]
    ancilla_qubits = [Qubit(idx=i+3, type='ancilla') for i in range(2)]
    
    # Add qubits to EKA
    eka.add_qubits(data_qubits)
    eka.add_qubits(ancilla_qubits)
    
    # Define stabilizers (e.g., Z1Z2 and Z2Z3 for repetition code)
    stab1 = Stabilizer(
        qubits=[data_qubits[0], data_qubits[1]],
        pauli_string='ZZ',
        ancilla=ancilla_qubits[0]
    )
    stab2 = Stabilizer(
        qubits=[data_qubits[1], data_qubits[2]],
        pauli_string='ZZ',
        ancilla=ancilla_qubits[1]
    )
    
    eka.add_stabilizers([stab1, stab2])
    
    # Create blocks (logical operations)
    init_block = Block('initialization')
    init_block.add_operation('init', target=data_qubits)
    
    measurement_block = Block('syndrome_measurement')
    measurement_block.add_syndrome_measurements(eka.stabilizers)
    
    eka.add_blocks([init_block, measurement_block])
    
    print(f"Custom EKA created with:")
    print(f"  {len(eka.data_qubits)} data qubits")
    print(f"  {len(eka.ancilla_qubits)} ancilla qubits")
    print(f"  {len(eka.stabilizers)} stabilizers")
    
    return eka


# ============================================================================
# EXAMPLE 8: Integration with Entwine (Visual GUI)
# ============================================================================
"""
Entwine is Loom's browser-based GUI for designing lattice surgery circuits.
You can export designs from Entwine and import them into Loom for simulation.
"""

def example_entwine_integration():
    """
    Example workflow with Entwine:
    
    1. Design your circuit visually in Entwine (https://entwine.entropicalabs.com/)
    2. Export the design as Loom code
    3. Import and simulate in Python using Loom
    
    Entwine will generate code like:
    """
    
    # This is example code that would be generated by Entwine
    entwine_generated_code = '''
    from loom.code_factory import RotatedSurfaceCodeFactory
    from loom.lattice_surgery import LatticeSurgeryBlock
    
    # Patches defined in Entwine
    patch_A = RotatedSurfaceCodeFactory(distance=3).generate_code()
    patch_B = RotatedSurfaceCodeFactory(distance=3).generate_code()
    
    # Operations defined in Entwine
    ls_block = LatticeSurgeryBlock()
    ls_block.add_patch(patch_A, position=(0, 0))
    ls_block.add_patch(patch_B, position=(4, 0))
    ls_block.add_cnot_operation(control=patch_A, target=patch_B)
    
    # Convert to circuit and simulate
    circuit = ls_block.to_circuit()
    '''
    
    print("Entwine Integration Workflow:")
    print("1. Design circuits visually at https://entwine.entropicalabs.com/")
    print("2. Export as Loom Python code")
    print("3. Run simulations with your choice of backend")
    print("\nExample generated code:")
    print(entwine_generated_code)


# ============================================================================
# EXAMPLE 9: Decoder Integration
# ============================================================================
"""
Decoders analyze syndrome measurements to determine the most likely errors
and corrections. Loom supports various decoding strategies.
"""

from loom.decoder import MinimumWeightPerfectMatching

def example_decoding():
    """Demonstrate syndrome decoding"""
    
    # Create a surface code
    code_factory = RotatedSurfaceCodeFactory(distance=3)
    code = code_factory.generate_code()
    eka = code.to_eka()
    
    # Build and run a circuit with errors
    circuit = Circuit(eka)
    circuit.add_logical_initialization('Z')
    circuit.add_syndrome_measurement_round()
    
    # Simulate with noise
    stim_backend = StimBackend()
    stim_circuit = stim_backend.from_loom_circuit(circuit)
    stim_circuit = stim_backend.add_noise(stim_circuit, error_rate=0.01)
    
    # Get syndrome measurements
    executor = Executor(backend=stim_backend)
    results = executor.run(stim_circuit, shots=1)
    syndromes = results.syndromes[0]
    
    # Decode the syndromes
    decoder = MinimumWeightPerfectMatching(eka)
    correction = decoder.decode(syndromes)
    
    print(f"Measured syndromes: {syndromes}")
    print(f"Proposed correction: {correction}")
    
    return correction


# ============================================================================
# EXAMPLE 10: Advanced - Multi-Code Distance Comparison
# ============================================================================
"""
Compare the performance of different code distances to observe
the threshold behavior of QEC.
"""

def example_threshold_analysis():
    """Analyze logical error rates across different code distances"""
    
    distances = [3, 5, 7]
    error_rate = 0.001
    num_shots = 1000
    
    results_by_distance = {}
    
    for d in distances:
        # Create code
        code_factory = RotatedSurfaceCodeFactory(distance=d)
        code = code_factory.generate_code()
        eka = code.to_eka()
        
        # Build circuit
        circuit = Circuit(eka)
        circuit.add_logical_initialization('Z')
        for _ in range(d):  # QEC cycles scale with distance
            circuit.add_syndrome_measurement_round()
        circuit.add_logical_measurement('Z')
        
        # Simulate
        stim_backend = StimBackend()
        stim_circuit = stim_backend.from_loom_circuit(circuit)
        stim_circuit = stim_backend.add_noise(stim_circuit, error_rate=error_rate)
        
        executor = Executor(backend=stim_backend)
        result = executor.run(stim_circuit, shots=num_shots)
        
        logical_error_rate = np.mean(result.logical_errors)
        results_by_distance[d] = logical_error_rate
        
        print(f"Distance {d}: Logical error rate = {logical_error_rate:.6f}")
    
    print("\nAs distance increases, logical error rate should decrease")
    print("(below the error threshold)")
    
    return results_by_distance


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("LOOM - Quantum Error Correction Framework by Entropica Labs")
    print("=" * 70)
    
    print("\n--- Example 1: Repetition Code ---")
    try:
        example_repetition_code()
    except Exception as e:
        print(f"Note: {e}")
        print("This example requires Loom to be installed: pip install loom")
    
    print("\n--- Example 2: Surface Code ---")
    print("The rotated surface code is widely used in QEC implementations")
    
    print("\n--- Example 3: Memory Experiment ---")
    print("Memory experiments test how long we can preserve quantum information")
    
    print("\n--- Example 4: Stim Simulation ---")
    print("Stim provides fast stabilizer circuit simulation for QEC")
    
    print("\n--- Example 5: Various QEC Codes ---")
    print("Loom supports multiple QEC codes out of the box")
    
    print("\n--- Example 6: Lattice Surgery ---")
    print("Lattice surgery enables logical operations on surface codes")
    
    print("\n--- Example 7: Custom EKA ---")
    print("EKA provides fine-grained control over QEC primitives")
    
    print("\n--- Example 8: Entwine Integration ---")
    example_entwine_integration()
    
    print("\n--- Example 9: Decoding ---")
    print("Decoders determine corrections from syndrome measurements")
    
    print("\n--- Example 10: Threshold Analysis ---")
    print("Comparing different code distances reveals QEC threshold behavior")
    
    print("\n" + "=" * 70)
    print("For more information:")
    print("  Documentation: https://loom-api-docs.entropicalabs.com/")
    print("  GitHub: https://github.com/entropicalabs/el-loom")
    print("  Visual Design: https://loom-docs.entropicalabs.com/")
    print("  Entwine GUI: https://entwine.entropicalabs.com/")
    print("=" * 70)
