import math
import random


def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


def vector_add(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def vector_sub(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def vector_mul(a, scalar):
    return [x * scalar for x in a]


def vector_length(v):
    return math.sqrt(sum(x * x for x in v))


def vector_distance(a, b):
    return vector_length(vector_sub(a, b))


def normalize(v):
    length = vector_length(v)
    if length == 0:
        return v
    return [x / length for x in v]


def random_vector(n, scale=1.0):
    return [random.random() * scale for _ in range(n)]
