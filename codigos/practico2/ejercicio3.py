def rnewton(fun, x_0, err, mit):
    hx = []
    hf = []
    v, dv = fun(x_0)

    for it in range(mit):
        if abs(dv) == 0:
            print("no puedo dividir por cero")
            break
        x_k = x_0 - v / dv
        v, dv = fun(x_k)
        hx.append(x_k)
        hf.append(v)
        if abs(v) < err or (abs(x_0 - x_k) / abs(x_k)) < err:
            print("salimos")
            break
        x_0 = x_k

    return hx, hf
