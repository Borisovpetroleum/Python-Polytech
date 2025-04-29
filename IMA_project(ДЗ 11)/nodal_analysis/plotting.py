import matplotlib.pyplot as plt
from .solver.inflow_performance.ipr_model import IPRmodel
from .solver.outflow_performance.vlp_model import VLPmodel


def total_plot(ipr: IPRmodel, vlp: VLPmodel, q_max: int):
    q_values = list(range(0, q_max + 1, 10))

    # Расчет данных
    ipr_pressures = [ipr.p_e - q / ipr.k_prod for q in q_values]
    vlp_pressures = [vlp.buffer + vlp.coeff_hydro * q for q in q_values]

    # Точка пересечения
    numerator = ipr.p_e - vlp.buffer
    denominator = (1 / ipr.k_prod) + vlp.coeff_hydro
    intersection_q = numerator / denominator
    intersection_p = ipr.p_e - intersection_q / ipr.k_prod

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(q_values, ipr_pressures, color="black", label="IPR")
    plt.plot(q_values, vlp_pressures, color="blue", label="VLP")

    plt.scatter(
        intersection_q,
        intersection_p,
        color="red",
        s=50,
        label=f"Точка совместной работы пласта и лифта\nQ={intersection_q:.1f}\nPw={intersection_p:.1f}",
    )

    plt.xlabel("Oil_rate, м$^3$/сут", fontsize=10)
    plt.ylabel("Well_pressure, atm", fontsize=10)
    plt.title("Узловой анализ(совместное решение пласт + подъемник)", fontsize=20)
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
