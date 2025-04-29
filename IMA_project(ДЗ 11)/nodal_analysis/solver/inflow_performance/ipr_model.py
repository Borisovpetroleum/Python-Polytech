class IPRmodel:
    "Для нахождения притока в скажину из пласта"

    def __init__(self, k_prod: float, p_e: float, p_w: float, total_oil: float = 0):
        self.k_prod = k_prod
        self.p_e = p_e
        self.p_w = p_w
        self.total_oil = total_oil
        self.depression = p_e - p_w

    def get_oil_rate(self):
        if self.depression > 0:
            oil_rate = self.k_prod * self.depression
            return oil_rate
        return 0.0

    def get_total_oil(self, time):
        if time >= 0:
            total_oil += self.k_prod * self.depression * time
        return total_oil
