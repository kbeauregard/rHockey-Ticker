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
    #import ipdb; ipdb.set_trace()
    arguments = docopt(__doc__, version=u'rHockey Ticker 0.1')
    feed = arguments['<name>'] or u'new'
    delay = int(arguments['--delay']) or 5
    limit = int(arguments['--limit']) or 5
    ticker.ticker_runner('hockey', feed, delay, limit)
