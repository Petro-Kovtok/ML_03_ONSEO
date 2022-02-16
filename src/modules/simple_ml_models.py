"""
Simple ML models
"""

class HousePriceModel:

    def __init__(self) -> None:
        self.heating_map = {
            "A":100,
            "B":20,
            "C":10,
            "D":1
            }

    def __call__(self, *, n_floors: int, area: float, heating: str) -> float:
        return 100 * n_floors + 5 * area + self.heating_map.get(heating, 0)

class SentimentModel:
    def __init__(self) -> None:
        self.word_map = {
            "nice": 10,
            "bad": -5,
            "fine": 5,
            "good": 2,
            "disgusting": -10,
            "hate": -3
        }
    
    def __call__(self, text: str):
        lower_text = text.lower()
        total = 0

        for key, val in self.word_map.items():
                if key in lower_text:
                    total += val
        
        sentiment = 'positive' if total > 0 else 'neutral' if total == 0 else 'negative'
        return {"sentiment": sentiment, "score": total}