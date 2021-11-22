"""
Simple ML models
"""

class HousePriceModel:
    def __init__(self) -> None:
        pass
    def __call__(self, *, n_floors: int, area: float, heating: str) -> float:
        heating_bonus_dict = {
            "A":100,
            "B":20,
            "C":10,
            "D":0
            }
        return 100 * n_floors + 5 * area + heating_bonus_dict[heating]

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
        
        return 1 if total > 0 else 0 if total == 0 else -1