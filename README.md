# gearbot

gearbot is a CLI application that checks a local music store, Hank's Music Exchange to see if a piece of music gear you want is available.
The idea started from my desire to be on social media less. Now you won't have to waste time logging on to instagram daily to check for updates.
You'll just get notified as soon as the gear you want is avaiable!

## Requirements
Python 3.6+

## Installation

```
# clone repo
git clone git@github.com:christiangmartinez/gearbot.git

cd path-to-repo

# install dependencies
pip install .

# install playwright required browsers
playwright install

# install package application
pipx install .

```

## Usage
`gearbot <gear-you-want>`

## TODO
- Add SMS notifications for gear matches
- Create web crawler for Reverb.com to show similar items to any matches + their average price
- Create web scraper for Sweetwater.com to show cost of similar item new
- Add search functionality for just Reverb (probably more useful to most people)
- Keep track of multiple gear queries at once
