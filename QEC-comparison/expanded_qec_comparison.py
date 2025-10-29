"""
EXPANDED Quantum Error Correction Framework Comparison
Including: Loom, Deltakit, Stim, PyMatching, qLDPC, and others

This expanded analysis includes the broader ecosystem of open-source QEC tools.
"""

def print_comprehensive_comparison():
    """Print comprehensive comparison of all major QEC frameworks."""
    
    print("=" * 100)
    print("COMPREHENSIVE QEC FRAMEWORK COMPARISON")
    print("=" * 100)
    print()
    
    frameworks = {
        "Loom": {
            "Developer": "Entropica Labs (Singapore)",
            "Type": "Full-stack QEC toolkit",
            "Primary Focus": "Visual design & lattice surgery",
            "Language": "Python",
            "License": "Open-source",
            "Launch Date": "2024-2025",
            "Unique Strength": "Entwine visual GUI for lattice surgery",
            "Integration": "Stim, OpenQASM, PennyLane/Catalyst",
            "Best For": "Research, visual prototyping, education",
            "Installation": "pip/poetry",
            "Documentation": "7/10 - Good API docs, needs more tutorials",
            "Community": "Growing, QEC Challenge 2025",
            "Backend/Layer": "High-level design layer"
        },
        "Deltakit": {
            "Developer": "Riverlane (UK)",
            "Type": "SDK + Learning platform",
            "Primary Focus": "Learning & deployment pipeline",
            "Language": "Python",
            "License": "Open-source + proprietary cloud",
            "Launch Date": "September 2025",
            "Unique Strength": "Comprehensive interactive textbook",
            "Integration": "Deltaflow hardware, cloud decoders",
            "Best For": "Learning, production deployment",
            "Installation": "pip + cloud token",
            "Documentation": "9/10 - Excellent textbook",
            "Community": "Backed by established QEC leader",
            "Backend/Layer": "High-level with hardware focus"
        },
        "Stim": {
            "Developer": "Craig Gidney (Google)",
            "Type": "Stabilizer circuit simulator",
            "Primary Focus": "High-performance QEC simulation",
            "Language": "C++ with Python bindings",
            "License": "Open-source (Apache 2.0)",
            "Launch Date": "2021",
            "Unique Strength": "Extreme speed (198 papers in 2024)",
            "Integration": "Used by Loom, Deltakit, PyMatching",
            "Best For": "Fast simulation, research backbone",
            "Installation": "pip install stim",
            "Documentation": "8/10 - Good technical docs",
            "Community": "Industry standard, widely adopted",
            "Backend/Layer": "Low-level simulation engine"
        },
        "PyMatching": {
            "Developer": "Oscar Higgott & Craig Gidney",
            "Type": "Decoder library",
            "Primary Focus": "Minimum-weight perfect matching",
            "Language": "Python/C++",
            "License": "Open-source",
            "Launch Date": "2021 (v2 in 2023)",
            "Unique Strength": "100-1000x faster than v1",
            "Integration": "Designed for Stim, used with Sinter",
            "Best For": "Fast decoding of surface codes",
            "Installation": "pip install pymatching",
            "Documentation": "8/10 - Clear API docs",
            "Community": "Standard decoder in research",
            "Backend/Layer": "Decoder layer"
        },
        "qLDPC": {
            "Developer": "Infleqtion & JPMorgan Chase",
            "Type": "LDPC code library",
            "Primary Focus": "Hardware-efficient codes",
            "Language": "Python",
            "License": "Open-source",
            "Launch Date": "May 2025",
            "Unique Strength": "10-100x qubit reduction",
            "Integration": "Neutral atom hardware",
            "Best For": "Hardware-aware optimization",
            "Installation": "GitHub (qLDPCOrg/qldpc)",
            "Documentation": "New, documentation growing",
            "Community": "New, backed by major players",
            "Backend/Layer": "Code design layer"
        },
        "MQT QECC": {
            "Developer": "TU Munich",
            "Type": "QEC toolkit",
            "Primary Focus": "Design automation",
            "Language": "Python/C++",
            "License": "Open-source",
            "Launch Date": "Ongoing development",
            "Unique Strength": "Full stack coverage",
            "Integration": "Part of Munich Quantum Toolkit",
            "Best For": "Research, compilation",
            "Installation": "pip install mqt.qecc",
            "Documentation": "Good, academic focus",
            "Community": "Academic community",
            "Backend/Layer": "Multi-layer toolkit"
        },
        "Qiskit": {
            "Developer": "IBM",
            "Type": "General quantum framework",
            "Primary Focus": "Full quantum computing stack",
            "Language": "Python",
            "License": "Open-source (Apache 2.0)",
            "Launch Date": "2017",
            "Unique Strength": "Industry standard, IBM hardware",
            "Integration": "IBM Quantum, Aer simulator",
            "Best For": "IBM ecosystem, general QC",
            "Installation": "pip install qiskit",
            "Documentation": "10/10 - Comprehensive",
            "Community": "Largest quantum community",
            "Backend/Layer": "Full stack platform"
        }
    }
    
    # Print detailed comparison
    for category in ["Type", "Primary Focus", "Unique Strength", "Best For", "Backend/Layer"]:
        print(f"\n{'=' * 100}")
        print(f"{category.upper()}")
        print(f"{'=' * 100}")
        for name, details in frameworks.items():
            print(f"{name:15} | {details[category]}")
    
    print("\n" + "=" * 100)
    print("ECOSYSTEM LAYERS AND RELATIONSHIPS")
    print("=" * 100)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │  HIGH-LEVEL DESIGN & LEARNING                                   │
    │  • Loom (visual design, lattice surgery)                        │
    │  • Deltakit (learning, textbook)                                │
    │  • Qiskit (full platform)                                       │
    └────────────────────────┬────────────────────────────────────────┘
                             │
    ┌────────────────────────┴────────────────────────────────────────┐
    │  CODE DESIGN & OPTIMIZATION                                     │
    │  • qLDPC (hardware-efficient LDPC codes)                        │
    │  • MQT QECC (synthesis & compilation)                           │
    └────────────────────────┬────────────────────────────────────────┘
                             │
    ┌────────────────────────┴────────────────────────────────────────┐
    │  SIMULATION ENGINE                                              │
    │  • Stim (high-performance stabilizer simulation)                │
    │  • Qiskit Aer (general quantum simulation with noise)           │
    └────────────────────────┬────────────────────────────────────────┘
                             │
    ┌────────────────────────┴────────────────────────────────────────┐
    │  DECODING                                                       │
    │  • PyMatching (MWPM decoder)                                    │
    │  • Deltakit cloud decoders (proprietary)                        │
    │  • Various other decoder implementations                        │
    └─────────────────────────────────────────────────────────────────┘
    """)
    
    print("\n" + "=" * 100)
    print("KEY DISTINCTIONS")
    print("=" * 100)
    print("""
    DIFFERENT SCOPE LEVELS:
    
    1. FULL PLATFORMS (End-to-end solutions):
       • Loom: Design → Simulation (via Stim backend)
       • Deltakit: Learning → Hardware deployment
       • Qiskit: General quantum computing with QEC features
    
    2. SPECIALIZED LIBRARIES (Specific tasks):
       • Stim: THE simulation engine (used by many others)
       • PyMatching: THE decoder library (used by many others)
       • qLDPC: Code design for hardware efficiency
       • MQT: Compilation and synthesis tools
    
    3. NOT DIRECTLY COMPARABLE:
       Comparing Loom vs Stim is like comparing:
       • A car (full vehicle) vs an engine (component)
       • Loom USES Stim as its backend
       • Deltakit can also use Stim for simulation
    """)
    
    print("\n" + "=" * 100)
    print("REVISED COMPARISON FRAMEWORK")
    print("=" * 100)
    print("""
    TIER 1: High-Level Platforms (Direct Competitors)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Compare THESE directly:
    
    • Loom vs Deltakit vs Qiskit QEC features
      - All provide end-to-end QEC workflows
      - Different approaches: visual vs textbook vs enterprise
      - Choice depends on: research vs learning vs production
    
    TIER 2: Core Infrastructure (Complementary, Not Competing)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    These are USED BY Tier 1 platforms:
    
    • Stim: Simulation backbone (nearly universal)
    • PyMatching: Decoder standard (widely used)
    • qLDPC: Specialized code library
    • MQT: Compilation toolkit
    
    → You typically use Tier 1 platforms which internally use Tier 2 libraries
    → Or use Tier 2 directly if building custom solutions
    """)
    
    print("\n" + "=" * 100)
    print("USAGE RECOMMENDATIONS BY SCENARIO")
    print("=" * 100)
    print("""
    SCENARIO 1: "I want to learn QEC from scratch"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: Deltakit
    - Structured textbook from basics to advanced
    - Interactive exercises
    - Clear learning path
    
    ALSO CONSIDER: Qiskit tutorials
    - Extensive documentation
    - Large community support
    
    SCENARIO 2: "I need to design and visualize lattice surgery"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: Loom (Entwine)
    - Only platform with visual GUI
    - Drag-and-drop interface
    - Exports to code
    
    NO ALTERNATIVE: This is Loom's unique feature
    
    SCENARIO 3: "I need maximum simulation performance"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: Stim directly
    - Fastest available (industry standard)
    - Can simulate huge circuits
    - Used in 198 papers (2024)
    
    HIGH-LEVEL WRAPPER: Use Loom or Deltakit
    - They use Stim backend anyway
    - Add convenience features
    
    SCENARIO 4: "I need to decode surface codes fast"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: PyMatching
    - Industry standard decoder
    - 100-1000x faster than alternatives
    - Works seamlessly with Stim
    
    CLOUD ALTERNATIVE: Deltakit
    - Access to proprietary decoders
    - May be faster for some cases
    
    SCENARIO 5: "I want hardware-efficient codes"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: qLDPC
    - 10-100x qubit reduction
    - Optimized for neutral atoms
    - Cutting-edge research
    
    SCENARIO 6: "I'm preparing for production deployment"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    BEST CHOICE: Deltakit
    - Designed for Deltaflow hardware
    - Production-ready workflows
    - Cloud decoder integration
    
    ALSO CONSIDER: Qiskit
    - If using IBM hardware
    - Enterprise support available
    
    SCENARIO 7: "I'm doing academic QEC research"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    STACK APPROACH: Use multiple tools
    - Stim + PyMatching: Core simulation/decoding
    - Loom: Visual design when needed
    - qLDPC: Explore new code families
    - MQT: Compilation research
    
    SCENARIO 8: "I'm building custom QEC solutions"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    TOOLKIT APPROACH:
    - Stim: Simulation engine
    - PyMatching: Decoder
    - Custom high-level logic
    - Or fork/extend existing platforms
    """)
    
    print("\n" + "=" * 100)
    print("THE VERDICT: WHAT SHOULD YOU COMPARE?")
    print("=" * 100)
    print("""
    COMPARING HIGH-LEVEL PLATFORMS (Apples to Apples):
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Loom vs Deltakit:
    ✓ FAIR COMPARISON - Both are end-to-end platforms
    ✓ Different strengths: visual design vs learning
    ✓ Choice depends on use case
    
    Loom/Deltakit vs Qiskit:
    ✓ FAIR but different scales
    ✓ Qiskit is broader platform (general QC + QEC)
    ✓ Loom/Deltakit are QEC-specialized
    
    COMPARING INFRASTRUCTURE (Context Required):
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Stim vs Loom:
    ✗ UNFAIR - Different layers
    ✓ Better: "Loom uses Stim backend"
    ✓ Note: You can use Stim directly OR through Loom
    
    PyMatching vs Deltakit decoders:
    ~ PARTIALLY FAIR - Both do decoding
    ✓ PyMatching: Open-source, standard
    ✓ Deltakit: Proprietary cloud, possibly faster
    ✓ Context: Different architectural approaches
    
    ORIGINAL COMPARISON WAS CORRECT:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Your initial Loom vs Deltakit comparison WAS appropriate:
    • Both are high-level platforms
    • Similar scope and ambitions
    • Different approaches to same problem
    • Direct competitors in the market
    
    BUT now you have broader context:
    • Stim is the engine many platforms use
    • PyMatching is standard decoder
    • qLDPC offers alternative code approach
    • Each tool serves specific purpose
    """)
    
    print("\n" + "=" * 100)
    print("UPDATED RECOMMENDATION")
    print("=" * 100)
    print("""
    FOR YOUR COMPARISON DOCUMENT:
    
    PRIMARY COMPARISON: Loom vs Deltakit (as originally done)
    → This remains valid and useful
    
    ADD CONTEXT SECTION: "Relationship to Core Infrastructure"
    → Explain that both use Stim
    → Mention PyMatching as standard decoder
    → Note qLDPC as emerging alternative approach
    → Position Qiskit as broader platform alternative
    
    ADD ECOSYSTEM DIAGRAM: Show layers
    → High-level platforms (Loom, Deltakit)
    → Core infrastructure (Stim, PyMatching)
    → Specialized tools (qLDPC, MQT)
    
    CONCLUSION:
    Your original comparison was on-target. The additional frameworks
    provide important context but don't invalidate the core comparison.
    They operate at different layers or serve complementary purposes.
    """)
    
    print("\n" + "=" * 100)


if __name__ == "__main__":
    print_comprehensive_comparison()
