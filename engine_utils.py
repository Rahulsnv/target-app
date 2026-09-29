import ctypes

def q_rsqrt(number: float) -> float:
    threehalfs = 1.5
    x2 = number * 0.5
    y = ctypes.c_float(number)

    i = ctypes.c_int32.from_address(ctypes.addressof(y)).value
    i = 0x5f3759df - (i >> 1)
    ctypes.c_int32.from_address(ctypes.addressof(y)).value = i

    y_val = y.value
    return y_val * (threehalfs - (x2 * y_val * y_val))
	y=10