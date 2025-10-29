# Quantum Error Correction Frameworks: Loom vs Deltakit

## Overview Comparison

### Loom by Entropica Labs
- **Type**: Open-source Python library + Visual GUI (Entwine)
- **Focus**: Design, simulation, and validation of QEC schemes
- **Specialty**: Lattice surgery operations and surface codes
- **Core Architecture**: EKA data structure (single source of truth)
- **GitHub**: https://github.com/entropicalabs/el-loom
- **Best For**: Research, education, and QEC code prototyping

### Deltakit by Riverlane
- **Type**: Comprehensive SDK + Interactive Textbook
- **Focus**: Learning, developing, and deploying QEC
- **Specialty**: Real-time decoding and hardware deployment
- **Core Architecture**: Cloud-connected with proprietary decoders
- **Website**: https://deltakit.riverlane.com/
- **Best For**: Production deployment, learning QEC, hardware integration

---

## Key Features Comparison

| Feature | Loom | Deltakit |
|---------|------|----------|
| **Installation** | `pip install loom` or Poetry | `pip install deltakit` + free token |
| **Visual GUI** | ✅ Entwine (browser-based) | ❌ (CLI/code only) |
| **Interactive Textbook** | ❌ | ✅ 4 learning modules |
| **Surface Codes** | ✅ Primary focus | ✅ Supported |
| **qLDPC Codes** | ⚠️ Limited | ✅ Full support |
| **Lattice Surgery** | ✅ Extensive support | ⚠️ Basic |
| **Cloud Decoders** | ❌ | ✅ LCD, BP-AC |
| **Hardware Integration** | ⚠️ Via backends | ✅ Deltaflow integration |
| **Leakage Modeling** | ❌ | ✅ Advanced tools |
| **Open Source** | ✅ Fully open | ✅ SDK open, cloud proprietary |
| **Learning Resources** | Documentation + examples | Interactive textbook + docs |

---

## Architecture Comparison

### Loom Architecture

```
┌─────────────────────────────────────────────┐
│              Entwine (Visual GUI)           │
│         Lattice Surgery Designer            │
└──────────────────┬──────────────────────────┘
                   │ Exports Loom code
                   ▼
┌─────────────────────────────────────────────┐
│              Loom Core Library              │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐ │
│  │   EKA   │  │  Blocks  │  │  Circuits  │ │
│  │  Data   │  │ Logical  │  │  Physical  │ │
│  │Structure│  │Operations│  │   Level    │ │
│  └─────────┘  └──────────┘  └────────────┘ │
└──────────────────┬──────────────────────────┘
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│   Stim   │ │  Qiskit  │ │ OpenQASM │
│ Backend  │ │ Backend  │ │ Backend  │
└──────────┘ └──────────┘ └──────────┘
```

**Key Concepts:**
- **EKA**: Central data structure storing all QEC context
- **Blocks**: Modular logical operations
- **Interpretation**: Maps logical to physical circuits
- **Code Factories**: Pre-built QEC codes (Surface, Shor, Steane, etc.)

### Deltakit Architecture

```
┌─────────────────────────────────────────────┐
│        Deltakit Textbook (Learning)         │
│    Interactive Modules + Code Exercises     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│            Deltakit SDK (Local)             │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐ │
│  │  Codes   │  │  Noise   │  │Experiments│ │
│  │ Surface  │  │ Models   │  │  Memory   │ │
│  │  qLDPC   │  │ Leakage  │  │ Stability │ │
│  └──────────┘  └──────────┘  └───────────┘ │
└──────────────────┬──────────────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐   ┌─────────────────────┐
│ Cloud Services  │   │  Deltaflow Stack    │
│  - LCD Decoder  │   │  (Real-time QEC)    │
│  - BP-AC        │   │   - Fast decoding   │
│  - Leakage      │   │   - 250+ qubits     │
│    Simulation   │   │   - Hardware ready  │
└─────────────────┘   └─────────────────────┘
```

**Key Concepts:**
- **Experiments**: Pre-built workflows (Memory, Stability)
- **Cloud Services**: High-performance decoders via API
- **Deltaflow**: Real-time QEC hardware stack
- **Transpiler**: Hardware-aware circuit optimization

---

## Use Case Recommendations

### Choose Loom if you want to:
1. **Design custom QEC codes** - Flexible architecture for novel codes
2. **Work with lattice surgery** - Extensive support for surface code operations
3. **Visual prototyping** - Entwine GUI for drag-and-drop design
4. **Academic research** - Full control over QEC primitives
5. **Integration with PennyLane/Catalyst** - Works well with Xanadu tools

### Choose Deltakit if you want to:
1. **Learn QEC from scratch** - Interactive textbook with guided exercises
2. **Production deployment** - Designed for real hardware integration
3. **State-of-the-art decoders** - Access to Riverlane's proprietary LCD and BP-AC
4. **Leakage modeling** - Advanced tools for realistic noise
5. **qLDPC codes** - Better support for next-gen codes
6. **Hardware deployment** - Seamless Deltaflow integration

---

## Code Example Comparison

### Creating a Surface Code

**Loom:**
```python
from loom.code_factory import RotatedSurfaceCodeFactory

# Create code
code_factory = RotatedSurfaceCodeFactory(distance=3)
code = code_factory.generate_code()
eka = code.to_eka()

# Build circuit
circuit = Circuit(eka)
circuit.add_logical_initialization('Z')
circuit.add_syndrome_measurement_round()

# Simulate with Stim
stim_backend = StimBackend()
stim_circuit = stim_backend.from_loom_circuit(circuit)
```

**Deltakit:**
```python
from deltakit import SurfaceCode, MemoryExperiment, NoiseModel

# Create code
code = SurfaceCode(distance=3)

# Setup experiment
experiment = MemoryExperiment(code=code, num_rounds=5)
noise = NoiseModel(gate_error_rate=0.001)
experiment.add_noise(noise)

# Run with cloud decoder
results = experiment.run(shots=1000, decoder='LCD')
```

### Key Differences:
- **Loom**: More explicit control over circuit construction
- **Deltakit**: Higher-level experiment abstraction
- **Loom**: Focus on EKA data structure
- **Deltakit**: Focus on end-to-end workflows

---

## Community and Support

### Loom
- **Documentation**: https://loom-api-docs.entropicalabs.com/
- **Visual Design**: https://loom-docs.entropicalabs.com/
- **Entwine GUI**: https://entwine.entropicalabs.com/
- **Contact**: info@entropicalabs.com
- **Community**: GitHub issues and discussions
- **Competitions**: Annual QEC challenges

### Deltakit
- **Website**: https://deltakit.riverlane.com/
- **Textbook**: Interactive learning modules on site
- **Documentation**: Comprehensive API docs
- **Community**: Forums and user groups
- **Support**: Dedicated QEC Community VP (Liz Durst)
- **Hardware Partners**: Integration with leading quantum companies

---

## Performance Considerations

### Loom Strengths:
- ⚡ **Fast prototyping** with visual GUI
- 🔧 **Fine-grained control** over QEC primitives
- 🎨 **Visual debugging** with Entwine
- 📚 **Modular design** easy to extend

### Deltakit Strengths:
- 🚀 **Production-ready** workflows
- ⚡ **High-performance decoders** (LCD, BP-AC)
- 🔬 **Realistic noise models** including leakage
- 🏭 **Hardware integration** via Deltaflow
- 📊 **Built-in analytics** and visualization

---

## Integration with Other Tools

### Loom Integrations:
- **Stim**: Fast stabilizer simulation
- **Qiskit**: IBM quantum ecosystem
- **PennyLane/Catalyst**: Quantum ML and hybrid algorithms
- **Crumble**: Circuit visualization
- **OpenQASM**: Circuit exchange format

### Deltakit Integrations:
- **Deltaflow**: Riverlane's real-time QEC stack
- **Cloud Services**: Proprietary decoders
- **Hardware Backends**: Leading quantum computers
- **Visualization Tools**: Built-in plotting
- **Transpilers**: Hardware-specific optimization

---

## Licensing

### Loom
- **License**: Apache 2.0
- **Open Source**: Fully open, community-driven
- **Commercial Use**: Permitted without restrictions

### Deltakit
- **License**: Open source SDK + Proprietary cloud services
- **Free Tier**: Basic features with free token
- **Cloud Services**: May require commercial licensing for production
- **Enterprise**: Custom solutions via Riverlane partnership

---

## Getting Started Recommendations

### For Students/Educators:
- **Start with**: Deltakit (interactive textbook)
- **Then try**: Loom (for visual design with Entwine)

### For Researchers:
- **Start with**: Loom (flexibility for novel codes)
- **Complement with**: Deltakit (benchmarking decoders)

### For Industry/Hardware Teams:
- **Start with**: Deltakit (production readiness)
- **Path to**: Deltaflow integration for hardware deployment

### For Quantum Software Developers:
- **Learn both**: Different strengths for different tasks
- **Loom**: Algorithm development and lattice surgery
- **Deltakit**: Performance optimization and deployment

---

## Future Roadmap

### Loom (Entropica Labs Vision):
- **Quilt**: Full Fault-Tolerance Operating System (FTOS)
- Deeper hardware integration
- More pre-built codes
- Enhanced Entwine features
- Expanded PennyLane integration

### Deltakit (Riverlane Vision):
- **MegaQuOp**: Million-scale quantum operations by 2026
- Advanced qLDPC support
- More hardware backends
- Enhanced learning modules
- Tighter Deltaflow coupling

---

## Conclusion

Both frameworks are excellent choices for quantum error correction:

- **Loom** excels at visual design, lattice surgery, and research flexibility
- **Deltakit** excels at learning, production deployment, and hardware integration

For maximum benefit, consider using both:
- Use **Deltakit's textbook** to learn QEC fundamentals
- Use **Loom's Entwine** for visual circuit design
- Use **Deltakit's decoders** for performance-critical applications
- Use **Loom's EKA** for custom code development

The quantum error correction ecosystem benefits from both approaches,
and many practitioners use elements of each in their workflows.
