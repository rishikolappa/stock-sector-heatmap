"""
src/sectors.py

Central place for sector -> ticker mappings for the Stock Sector Heatmap project.

- Edit SECTOR_TICKERS to add/remove tickers or sectors.
- Use the helper functions `all_tickers()` and `sector_for_ticker()` in pipelines and notebooks.
"""

SECTOR_TICKERS = {
    "Technology": [
        "AAPL","MSFT","NVDA","AMD","INTC","QCOM",
        "AVGO","CRM","ORCL","GOOG","META","ADBE"
    ],
    "Healthcare": [
        "JNJ","PFE","MRK","ABT","TMO","UNH",
        "LLY","BMY","AMGN","GILD","CVS","CI"
    ],
    "Financials": [
        "JPM","BAC","WFC","C","GS","MS",
        "BLK","AXP","SCHW","BK","USB","PNC"
    ],
    "Consumer Discretionary": [
        "AMZN","TSLA","HD","NKE","MCD","SBUX",
        "TGT","LOW","BKNG","RCL","EBAY","DG"
    ],
    "Energy": [
        "XOM","CVX","COP","SLB","EOG","PSX",
        "MPC","HAL","OXY","KMI","DVN","PXD"
    ],
    "Industrials": [
        "BA","CAT","GE","HON","UPS","UNP",
        "DE","MMM","LMT","RTX","GD","NOC"
    ],
}

def all_tickers():
    """
    Return a sorted list of unique tickers across all sectors.
    """
    tickers = set()
    for lst in SECTOR_TICKERS.values():
        tickers.update(lst)
    return sorted(tickers)

def sector_for_ticker(ticker):
    """
    Return the sector name for a given ticker (case-insensitive).
    If not found, returns None.
    """
    ticker_up = ticker.upper()
    for sector, lst in SECTOR_TICKERS.items():
        if ticker_up in (t.upper() for t in lst):
            return sector
    return None

__all__ = ["SECTOR_TICKERS", "all_tickers", "sector_for_ticker"]
