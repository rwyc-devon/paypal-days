#paypal-days

simple parser that takes a PayPal history file and turns it into a list of
daily totals.

##Requirements

- Python2.7+ (probably 3.x as well, not tested)

##Usage

- In PayPal, navigate to My Account > History > Download History
- Enter your date range. I find that I get errors (gateway timeout) from PayPal
  if I request more than a few months at a time, which is pretty annoying
- For "File Types for Download", choose "Comma Delimited - Completed Payments"
- Download the file
- Run `paypal-days <name-of-file>`
	- To save the output, try `paypal-days <name-of-file> > out.csv`
