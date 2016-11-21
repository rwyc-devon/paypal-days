#paypal-days

A simple parser that takes a PayPal history file and turns it into a list of
daily totals.

##Requirements

- Python3

##Usage

- In PayPal, navigate to My Account > History > Download History
- Enter your date range. I find that I get errors (gateway timeout) from PayPal
  if I request more than a few months at a time, which is pretty annoying
- For "File Types for Download", choose "Comma Delimited - All Activity"
- Download the file
- Before running the script for the first time, copy `config.example.py` to
  `config.py` and edit it according to the instructions within
- Run `paypal-days <name-of-file>`
	- To save the output, try `paypal-days <name-of-file> > out.csv`

If you want to just see donations, add run `paypal-days <name-of-file>
donations`
