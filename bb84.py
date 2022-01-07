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


def sampleBits(bits, sampleIndices):
    sampled = []
    for i in sampleIndices:
        sampled.append(bits.pop(mod(i, len(bits))))
    return sampled


# Parametrized function for the entire BB84 quantum key distribution protocol

def bb84(n, sampleSize, interception=False):
    aliceBits = [randint(0, 1) for _ in range(n)]
    aliceBases = [randint(0, 1) for _ in range(n)]
    message = encodeMessage(aliceBits, aliceBases)

    if interception:
        eveBases = [randint(0, 1) for _ in range(n)]
        intercepted = measureMessage(message, eveBases)

    bobBases = [randint(0, 1) for _ in range(n)]
    bobResults = measureMessage(message, bobBases)

    aliceKey = pruneInvalid(aliceBases, bobBases, aliceBits)
    bobKey = pruneInvalid(aliceBases, bobBases, bobResults)

    sampledBits = sample(range(n), sampleSize)

    aliceSample = sampleBits(aliceKey, sampledBits)
    bobSample = sampleBits(bobKey, sampledBits)

    if aliceSample == bobSample:
        if interception:
            print("Interception went undetected!")
            return None
        else:
            print("Protocol successful!")
            return aliceKey
