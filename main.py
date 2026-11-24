#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, 140 characters at most, for a city
that does not exist, to /output/entry.txt. The city is named, the weather
is given in broadcast register, and the joke lands on the commuter's bus:
it arrives exactly when you stop checking your watch.
"""

CITY = "Widdershins"
FORECAST = (
    f"Today in {CITY}: scattered applause, a high of 21\u00b0, "
    "and the 8:15 bus comes exactly when you stop checking your watch."
)
CHAR_LIMIT = 140
DESTINATION = "/output/entry.txt"


def build_forecast() -> str:
    text = FORECAST.strip()
    assert text, "forecast must not be empty"
    assert "\n" not in text, "forecast must be a single line"
    assert len(text) <= CHAR_LIMIT, f"{len(text)} chars exceeds {CHAR_LIMIT}"
    assert CITY in text, "forecast must name the invented city"
    return text


def main() -> None:
    text = build_forecast()
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")
    print(f"{len(text)} chars written to {DESTINATION}")


if __name__ == "__main__":
    main()
