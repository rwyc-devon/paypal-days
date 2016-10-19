"""
Types of transactions to include in the total. You may have to alter this to
include whatever apps you may use.

If you sometimes send manual payments to refund customers, you will need to
include "Payment Sent" in this array. Otherwise, definitely remove it; it
introduces a lot of problems! See below for more details.
"""
types=[
        "Mobile Express Checkout Payment Received",
        "Express Checkout Payment Received",
        "Web Accept Payment Received",
        "Website Payments Pro API Solution",
        "Refund",
        "Payment Sent",
        ]
"""
If you sometimes send manual payments to refund customers, you will need to
include "Payment Sent" in the types array. If you do this though, payments to
others (suppliers, etc) will be counted as refunds; definitely not desirable!

Unfortunately, there doesn't seem to be an unambiguous way to differentiate
between these, so you'll need to put the names of everyone you've sent payment
to who is not a customer in this array. This is a bad solution of course, but
this is also not meant to be more than a hack anyways, so beware!
"""
excludeNames=[
        "Person 1",
        "Person 2",
        "Person 3",
        ]
