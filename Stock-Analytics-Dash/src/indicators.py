import pandas as pd

def add_moving_averages(
        
        df:pd.DataFrame,
        sma_windows: tuple[int,...] = (20,50),
        ema_spans: tuple[int, ...] = (20,50),
    ) -> pd.DataFrame:
    """Return price data with SMA EMA trend indicator columns."""

    result = df.copy()

    for window in sma_windows:
        result[f"SMA_{window}"] = result["Close"].rolling(window=window).mean()

    for span in ema_spans:
        result[f"EMA_{span}"] = result["Close"].ewm(
            span = span,
            adjust=False,
        ).mean()

        return result
    