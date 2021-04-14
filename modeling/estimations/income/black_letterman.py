from pypfopt import BlackLittermanModel


class BlackLittermanEstimator:
    """Оценка доходности акций по модели black-litterman."""

    def __init__(self):
        self.model = BlackLittermanModel(
            cov_matrix=...,
            pi=...,
            absolute_views=...,
            Q=...,
            P=...,
            omega=...,
            view_confidences=...,
            tau=...,
            risk_aversion=...,
        )

    def estimate():
        pass
