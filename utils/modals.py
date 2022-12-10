from typing import Optional

__all__ = (
    "City",
    "Word",
)


class City:
    def __init__(self, name: str,  country: str, search_count: int, state: Optional[str] = ""):
        self.name = name
        self.country = country
        self.state = state
        self.search_count = search_count

    def __repr__(self) -> str:
        return f"<City name={self.name} country={self.country} state={self.state} search_count={self.search_count}>"

    def __str__(self) -> str:
        return f"{self.name}, {self.state}, {self.country}" if self.state else f"{self.name}, {self.country}"


class Word:
    def __init__(self, word: str, search_count: int):
        self.word = word
        self.search_count = search_count

    def __repr__(self) -> str:
        return f"<Word word={self.word} search_count={self.search_count}>"

    def __str__(self) -> str:
        return f"{self.word}"
