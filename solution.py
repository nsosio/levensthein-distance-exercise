from typing import Set
import pandas as pd
from Levenshtein import distance


def find_names_with_levensthein_distance_equal_to(texts: pd.Series, text: str, d: int) -> Set:
  
  distances = texts.apply(lambda x: distance(x, text))
  return set(texts[distances==d].drop_duplicates())


if __name__ == "__main__":
  df = pd.read_csv("https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv")
  names = find_names_with_levensthein_distance_equal_to(df['HUNDENAME'], text='Luca', d=1)
  print(f"Names with levenshtein distance equal to 1: {', '.join(names)}")
