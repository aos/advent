def addr(R, A, B, C):
    R[C] = R[A] + R[B]
    return R


def addi(R, A, B, C):
    R[C] = R[A] + B
    return R


def mulr(R, A, B, C):
    R[C] = R[A] * R[B]
    return R


def muli(R, A, B, C):
    R[C] = R[A] * B
    return R


def banr(R, A, B, C):
    R[C] = R[A] & R[B]
    return R


def bani(R, A, B, C):
    R[C] = R[A] & B
    return R


def borr(R, A, B, C):
    R[C] = R[A] | R[B]
    return R


def bori(R, A, B, C):
    R[C] = R[A] | B
    return R


def setr(R, A, B, C):
    R[C] = R[A]
    return R


def seti(R, A, B, C):
    R[C] = A
    return R


def gtir(R, A, B, C):
    R[C] = 1 if A > R[B] else 0
    return R


def gtri(R, A, B, C):
    R[C] = 1 if R[A] > B else 0
    return R


def gtrr(R, A, B, C):
    R[C] = 1 if R[A] > R[B] else 0
    return R


def eqir(R, A, B, C):
    R[C] = 1 if A == R[B] else 0
    return R


def eqri(R, A, B, C):
    R[C] = 1 if R[A] == B else 0
    return R


def eqrr(R, A, B, C):
    R[C] = 1 if R[A] == R[B] else 0
    return R
