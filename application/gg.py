from qiskit_aer import AerProvider
from qiskit.circuit import QuantumCircuit
from qiskit_algorithms import Grover
from qiskit.circuit.library import PhaseOracle

oracle = PhaseOracle(expression='~(a & b)')  # Equivalent to LogicalExpressionOracle
oracle.draw()
