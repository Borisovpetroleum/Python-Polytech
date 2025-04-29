from typing import Optional
from nodal_analysis.solver.inflow_performance.ipr_model import IPRmodel
from nodal_analysis.solver.outflow_performance.vlp_model import VLPmodel
from nodal_analysis.plotting import total_plot


class NodalAnalysis:
    "Узловой анализ пласт + скважина"

    def __init__(self, ipr: IPRmodel, vlp: VLPmodel):
        self.ipr = ipr
        self.vlp = vlp
        self.nodal_rate: Optional[float] = None
        self.nodal_pressure: Optional[float] = None

    def calculate_nodal_point(self) -> tuple[float, float]:

        numerator = self.ipr.p_e - self.vlp.buffer
        denominator = (1 / self.ipr.k_prod) + self.vlp.coeff_hydro

        if denominator <= 0:
            raise ValueError("Невозможно найти точку")

        self.nodal_rate = numerator / denominator
        self.nodal_pressure = self.ipr.p_e - self.nodal_rate / self.ipr.k_prod

        return self.nodal_rate, self.nodal_pressure

    def plot_results(self, q_max: int) -> None:
        total_plot(ipr=self.ipr, vlp=self.vlp, q_max=q_max)

    def get_results(self) -> dict:
        return {
            "nodal_rate": self.nodal_rate,
            "nodal_pressure": self.nodal_pressure,
            "ipr_params": {"k_pr": self.ipr.k_prod, "p_e": self.ipr.p_e},
            "vlp_params": {
                "buffer": self.vlp.buffer,
                "coeff_hydro": self.vlp.coeff_hydro,
            },
        }

    def __repr__(self):
        return (
            f"NodalAnalysis(IPR: k_pr={self.ipr.k_prod}, p_e={self.ipr.p_e} | "
            f"VLP: p_wh={self.vlp.buffer}, C={self.vlp.coeff_hydro})"
        )
