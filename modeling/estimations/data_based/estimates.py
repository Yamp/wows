from dataclasses import dataclass
from typing import Optional


@dataclass
class StockEstimate:
    """Оценки акций."""
    ticker: str
    consensus: tuple[float, float, float]  # buy, hold, sell
    estimates: list[tuple[float, float]]  # value, weight

    my_estimate: Optional[float]
    my_risk_estimate: Optional[float]


class AssetEstimates:
    """Оценка роста акций."""

    def __init__(self):
        self.estimates: list[StockEstimate] = []

    def add_estimates(self):
        """Добавляем все оценки."""
        self.estimates += [StockEstimate(
            ticker='AAPL',
            consensus=(33, 4, 2),
            my_estimate=None,
            my_risk_estimate=None,
            estimates=[
                (171, 1),  # rbc capital
                (160, 1),  # deutsche
                (170, 1),  # monnes
                (167, 1),  # d.a davidson
                (170, 1),  # needham
                (175, 1),  # wedbush
                (155, 1),  # Well fargo
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='BIDU',
            consensus=(32, 4, 2),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (385, 1),  # benchmark co
                (390, 1),  # keybanc
                (400, 1),  # barclays
                (364, 1),  # citigroup
                (355, 1),  # openheyimer
                (367, 1),  # clsa
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='TPTX',
            consensus=(10, 0, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (175, 1),  # roth capital
                (186, 1),  # H.C. wainwright
                (156, 1),  # Leerink
                (145, 1),  # Cannacord genuity
                (160, 1),  # JMP securities
                (150, 1),  # Oppenheimer
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='SDGR',
            consensus=(3, 1, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (104, 1),  # bmo capital
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='SDGR',
            consensus=(3, 1, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (104, 1),  # bmo capital
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='SBUX',
            consensus=(19, 15, 1),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (124, 1),  # wed bush
                (120, 1),  # Cowen & co
                (130, 1),  # BTIG
                (100, 1),  # stephens
                (104, 1),  # piper sandler
                (122, 1),  # Oppenhimer
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='RUAL',
            consensus=(0, 0, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[
                (61.5, 0.3),  # finam
                (65, 0.3),  # Велес капитал
                (65, 0.15),  # ВТБ
                (62, 0.2),  # stephens
                (62, 0.1),  # Фридом финанс
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='INTC',
            consensus=(14, 17, 10),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[

                # tinkoff оценки
                (81, 1),  # Cowen & co
                (48, 1),  # Northland securites
                (75, 1),  # UBS
                (86, 1),  # KeyBanc
                (80, 1),  # Credis suisse
            ]
        )]

        self.estimates += [StockEstimate(
            ticker='GM',
            consensus=(19, 2, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[

                # tinkoff оценки
                (48, 1),  # Citigroup
                (62, 1),  # Jefferies
                (65, 1),  # Deutsche
                (68, 1),  # Credis suisse
                (80, 1),  # Morgan Stanley
            ],
        )]

        self.estimates += [StockEstimate(
            ticker='NEE',
            consensus=(19, 2, 0),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[

                # tinkoff оценки
                (48, 1),  # Citigroup
                (62, 1),  # Jefferies
                (65, 1),  # Deutsche
                (68, 1),  # Credis suisse
                (80, 1),  # Morgan Stanley

                # tinkoff ideas
                (55, 0.5),  # Index group
            ],
        )]

        self.estimates += [StockEstimate(
            ticker='WMT',
            consensus=(29, 5, 2),
            my_estimate=None,
            my_risk_estimate=0.1,
            estimates=[

                # tinkoff оценки
                (160, 1),  # UBS
                (162, 1),  # RBC capital
                (160, 1),  # Robert W. baird

                # tinkoff ideas
                (55, 0.5),  # БКС
            ],
        )]
