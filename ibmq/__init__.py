import os

from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit import QuantumCircuit

class IBMQClient:
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        self.client = self.__get_client()

    def __get_client(self):
        return QiskitRuntimeService(channel="ibm_quantum", token=os.getenv('QISKIT_IBM_TOKEN'))

    def execute(self, qc: QuantumCircuit, shots: int = 1024):
        backend = self.client.least_busy()
        print(f"Least busy backend: {backend.name}")
        pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
        isa_circuit = pm.run(qc)

        sampler = Sampler(backend)

        job = sampler.run([isa_circuit],shots=shots)

        print(f"Job ID is {job.job_id()}")
        return job.result()
