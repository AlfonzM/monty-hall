# Monty Hall

I couldn't believe the [Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem) strategy actually works, so I wrote a script to simulate it. It __does__ work.

```
$ python montyhall.py
```

The script will simulate 100,000 Monty Hall games where the "player" switches after the first goat reveal, and another 100,000 where the player does not switch.

Sample Result:

```
Monty Hall with switch == True
Win Count: 66456/100000
Win Rate: 66.456%
---
Monty Hall with switch == False
Win Count: 33181/100000
Win Rate: 33.181%
```

### MIND == BLOWN.