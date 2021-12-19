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


def measureMessage(messageBits, bases):
    sim = Aer.get_backend("aer_simulator")
    meas = []
    for messageBit, base in zip(messageBits, bases):
        if base == 0:
            messageBit.measure(0, 0)
        else:
            messageBit.h(0)
            messageBit.measure(0, 0)
        qobj = assemble(messageBit, shots=1, memory=True)
        meas.append(int(sim.run(qobj).result().get_memory()[0]))
    return meas


def pruneInvalid(aBases, bBases, bits):
    validBits = []
    for aliceBase, bobBase, bit in zip(aBases, bBases, bits):
        if aliceBase == bobBase:
            validBits.append(bit)
    return validBits

