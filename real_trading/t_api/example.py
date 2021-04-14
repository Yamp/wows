import asyncio

import tinvest as ti

TOKEN = "t.AytH8QfPutOgPvzp07obTMQR8kAq4eh-cKx0FE5pRUDEwKjVl1yH-SPqBiDPAF7Y2LCdyfVbZMu3nmeONqiJ1g"


class TradingTerminal:
    """Класс, который отвечает за связь с биржей."""

    def __init__(self):
        self.a_client = ti.AsyncClient(TOKEN)
        self.s_client = ti.SyncClient(TOKEN)
        # self.streaming = ti.Streaming(TOKEN)

    def get_figi(self, ticker: str):
        """Получаем бумагу по тикеру."""
        return self.s_client.get_market_search_by_ticker('BABA')

    def get_portfolio(self):
        """Получаем портфель."""
        return self.s_client.get_portfolio('BABA')



async def main():
    async with ti.Streaming(TOKEN) as streaming:
        await streaming.candle.subscribe('BBG006G2JVL2', ti.CandleResolution.min1)
        # await streaming.orderbook.subscribe('BBG0013HGFT4', 5)
        # await streaming.instrument_info.subscribe('BBG0013HGFT4')

        async for event in streaming:
            print(event.payload)
            print(event.)
            print(event)


if __name__ == "__main__":
    asyncio.run(main())
