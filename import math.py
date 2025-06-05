import math
from import_numpy_as_np import serie_cos

# language: python

def test_serie_cos_zero():
    # cos(0) = 1, então para x1=0, n=0 deve ser 1
    assert serie_cos(0, 0) == 1

def test_serie_cos_primeiros_termos():
    # Para x1=1, n=0: termo deve ser 1
    assert serie_cos(1, 0) == 1
    # Para x1=1, n=1: termo deve ser -0.5
    assert math.isclose(serie_cos(1, 1), -0.5, rel_tol=1e-9)
    # Para x1=1, n=2: termo deve ser 1/24
    assert math.isclose(serie_cos(1, 2), 1/24, rel_tol=1e-9)

def test_aproximacao_cos():
    x1 = 1
    soma = sum(serie_cos(x1, n) for n in range(10))
    assert math.isclose(soma, math.cos(x1), rel_tol=1e-7)

def test_erro_diminui():
    x1 = 1
    soma_3 = sum(serie_cos(x1, n) for n in range(3))
    soma_6 = sum(serie_cos(x1, n) for n in range(6))
    soma_10 = sum(serie_cos(x1, n) for n in range(10))
    true_val = math.cos(x1)
    err_3 = abs(true_val - soma_3)
    err_6 = abs(true_val - soma_6)
    err_10 = abs(true_val - soma_10)
    assert err_6 < err_3
    assert err_10 < err_6