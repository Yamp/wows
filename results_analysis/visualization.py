from matplotlib import pyplot as plt


class TradingResultVisualizer:
    def plot_result(self) -> None:
        """Строим график того, что получилось."""
        data = self.history['active'][4:] / self.history['passive'][4:]
        plt.plot(data)

        max_passive = self.history['passive'][4:].max()

        plt.plot(self.history['passive'][4:] / max_passive, label='Пассивная стратегия.')
        plt.plot(self.history['active'][4:] / max_passive, label='Активная стратегия.')

        plt.xlabel('День эксперимента.')
        plt.ylabel('Общее количество денег.')
        plt.legend()
        plt.show()
