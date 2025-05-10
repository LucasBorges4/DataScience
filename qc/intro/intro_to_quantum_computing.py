from qiskit import QuantumCircuit
from qiskit_aer import Aer  
import matplotlib.pyplot as plt

# Step 1: Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1, 1)

# Step 2: Put the qubit in a superposition (like a swirled ice cream mix)
qc.h(0)  # Hadamard gate puts qubit in 50/50 superposition

# Step 3: Measure the qubit (forcing it to choose chocolate or vanilla)
qc.measure(0, 0)

# Step 4: Simulate the quantum experiment
simulator = Aer.get_backend('aer_simulator')  
qc = qc.copy()
qc.save_statevector()  
job = simulator.run(qc, shots=100)  
result = job.result()
counts = result.get_counts()

# Step 5: Display the results
flavors = {"0": "🍫 Chocolate", "1": "🍦 Vanilla"}
labels = [flavors.get(key, key) for key in counts.keys()]

plt.bar(labels, counts.values(), color=['brown', 'gold'])
plt.xlabel("Flavor")
plt.ylabel("Count")
plt.title("Quantum Ice Cream Machine Results")
plt.show()














