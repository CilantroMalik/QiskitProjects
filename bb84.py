from qiskit import Aer, QuantumCircuit, assemble
from numpy import mod
from random import randint, sample

# Helper function definitions


def encodeMessage(bits, bases):
    message = []
    for bit, base in zip(bits, bases):
        qc = QuantumCircuit(1, 1)
        if base == 0:
            if bit == 1:
                qc.x(0)
        else:
            if bit == 1:
                qc.x(0)
            qc.h(0)
        qc.barrier()
        message.append(qc)
    return message
