#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


def main():
    # "Trade Balance" in Kraken
    trade_balance = 5000
    trade_balance = 29000
    # "Opening Cost" in Kraken
    borrowed = 25000
    margin_ratio = 5 # 1/5
    margin = borrowed / margin_ratio
    print("trade_balance:", trade_balance)
    print("margin:", margin)
    # "Current Valuation" in Kraken
    current_valuation = 18600
    profit_loss = current_valuation - borrowed
    print("profit_loss:", profit_loss)
    equity = trade_balance + profit_loss
    print("equity:", equity)
    # ($5,000 ÷ $2,000)×100 = 250%
    margin_level = (float(equity) / margin) * 100
    print("margin_level: %s%%" % margin_level)


if __name__ == '__main__':
    main()
