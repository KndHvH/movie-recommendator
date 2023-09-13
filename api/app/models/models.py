from dataclasses import dataclass
    
@dataclass
class MovieRecommendation:
    movie: str
    blacklist: list[str] = []
