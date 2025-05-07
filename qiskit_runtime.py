from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.


from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

def get_client():
    return QiskitRuntimeService(channel="ibm_quantum", token=os.getenv('QISKIT_IBM_TOKEN'))

# # 1. A quantum circuit for preparing the quantum state (|00> + |11>)/rt{2}
# bell = QuantumCircuit(2)
# bell.h(0)
# bell.cx(0, 1)
# bell.measure_all()
#
# # 2: Optimize problem for quantum execution.
# backend = service.least_busy(operational=True, simulator=False)
# pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
# isa_circuit = pm.run(bell)
#
# # 3. Execute using the Sampler primitive
# sampler = Sampler(mode=backend)
# sampler.options.default_shots = 1024  # Options can be set using auto-complete.
# job = sampler.run([isa_circuit])
# print(f"Job ID is {job.job_id()}")
# pub_result = job.result()[0]
# print(f"Counts for the meas output register: {pub_result.data.meas.get_counts()}")