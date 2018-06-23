'''rHockey Ticker
Usage:
    rHockey.py
    rHockey.py [--limit=<number>] [--delay=<minutes>]
    rHockey.py feed <name> [--limit=<number>] [--delay=<minutes>]

Options:
    -h --help                Show this screen.
    --limit=<number>         Limit for submission downloads
    --delay=<minutes>        Delay to wait between downloads in minutes

'''
import ticker
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='rHockey Ticker 0.1')
    feed = 'new' or arguments['<name>']
    delay = 5 or arguments['--delay']
    limit = 5 or arguments['--limit']
    ticker.ticker_runner('hockey', feed, delay, limit)
