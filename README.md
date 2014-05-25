WorldCup2014
============

BeautifulSoup Wikipedia scrapers for FIFA World Cup 2014 

## Groups

From http://en.wikipedia.org/wiki/2014_FIFA_World_Cup

```
{
    "Group A": [
        "Brazil",
        "Croatia",
        "Mexico",
        "Cameroon"
    ],
    "Group B": [
        "Spain",
        "Netherlands",
        "Chile",
        "Australia"
    ],
    .
    .
    .
```

Also with stats:

```
{
    "Group A": [
        {
            "Drawn": 0,
            "Goal difference": 0,
            "Goals against": 0,
            "Goals for": 0,
            "Lost": 0,
            "Played": 0,
            "Points": 0,
            "Team": "Brazil",
            "Won": 0
        },
        {
            "Drawn": 0,
            "Goal difference": 0,
            "Goals against": 0,
            "Goals for": 0,
            "Lost": 0,
            "Played": 0,
            "Points": 0,
            "Team": "Croatia",
            "Won": 0
        },
        .
        .
        .
```

## Matches

From http://en.wikipedia.org/wiki/2014_FIFA_World_Cup

Dates in UTC

```
{
    "Group A": [
        {
            "Away Team": "Croatia",
            "Date": "2014-06-12T20:00:00",
            "Home Team": "Brazil",
            "Match": 1,
            "Venue": "Arena de S\u00e3o Paulo, S\u00e3o Paulo"
        },
        {
            "Away Team": "Cameroon",
            "Date": "2014-06-13T16:00:00",
            "Home Team": "Mexico",
            "Match": 2,
            "Venue": "Arena das Dunas, Natal"
        },
        .
        .
        .
```

## Squads

From http://en.wikipedia.org/wiki/2014_FIFA_World_Cup_squads

```
{
    "Group A": {
        "Brazil": {
            "Coach": "Luiz Felipe Scolari",
            "Players": [
                {
                    "Caps": 78,
                    "Club": "Toronto FC",
                    "DoB/Age": "3 September 1979 (aged 34)",
                    "No.": null,
                    "Player": "J\u00falio C\u00e9sar",
                    "Pos.": "GK"
                },
                {
                    "Caps": 9,
                    "Club": "Botafogo",
                    "DoB/Age": "2 January 1983 (aged 31)",
                    "No.": null,
                    "Player": "Jefferson",
                    "Pos.": "GK"
                },
                .
                .
                .
```
