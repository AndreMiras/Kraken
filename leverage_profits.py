#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extracts the NET profit/loss from the ledgers.csv file.
The file contains the following header:
txid, refid, time, typ, aclass, asset, amount, fee, balance

For given assets (XETH, ZUSD and ZEUR), we sum all the "margin" column.
Then we substract the trading and rollover fees.

To get the export go to:

    History > Export > Select "ledgers" in "Export Data" >
    Select a date > in "Fields" tick "Select All" > Submit
"""
from __future__ import print_function
import csv
import sys


def do():
    # this is the asset for which we are interested in checking
    # the margin profit
    assets = ["XETH", "ZUSD", "ZEUR"]
    total_margin = 0
    # normal trade fees
    total_trading_fees = 0
    # rollover fees
    total_rollover_fees = 0
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for line in reader:
            amount = 0
            fee = 0
            rollover_fee = 0
            # we are only interested in some specific assets
            if line["asset"] not in assets:
                continue
            if line["type"] == "margin":
                amount = line["amount"]
                fee = line["fee"]
                # print("amount: " + amount)
                # print("fee: " + fee)
                amount = float(amount)
                fee = float(fee)
            elif line["type"] == "rollover":
                rollover_fee = line["fee"]
                # print("rollover_fee: " + rollover_fee)
                rollover_fee = float(rollover_fee)
            # let's sum that up
            total_margin += amount
            total_trading_fees += fee
            total_rollover_fees += rollover_fee

    total_fees = total_trading_fees + total_rollover_fees
    net_profit = total_margin - total_fees
    total_margin = total_margin
    print("total_margin: %.2f euros" % total_margin)
    print("total_trading_fees: %.2f euros" % total_trading_fees)
    print("total_rollover_fees: %.2f euros" % total_rollover_fees)
    print("total_fees: %.2f euros" % total_fees)
    print("net_profit: %.2f euros" % net_profit)


def main():
    do()

if __name__ == '__main__':
    main()
