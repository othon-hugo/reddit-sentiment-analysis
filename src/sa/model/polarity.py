from enum import Enum
from typing import Dict, List

KeywordsByPolarity = Dict["Polarity", List[str]]


class Polarity(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
