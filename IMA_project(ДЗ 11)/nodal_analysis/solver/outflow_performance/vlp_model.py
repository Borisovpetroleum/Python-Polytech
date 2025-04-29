class VLPmodel:
    "Для нахождения забойного давления на скважине, который позволяет поднимать продукцию на поверхность"

    def __init__(self, buffer, coeff_hydro):
        self.buffer = buffer
        self.coeff_hydro = coeff_hydro

    def get_pressure(self, rate: float):
        return self.buffer + self.coeff_hydro * rate
