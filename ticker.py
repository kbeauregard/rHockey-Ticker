from praw import Reddit
from time import sleep, strftime, localtime


class BadFeedError(Exception):
    pass


def ticker_runner(subreddit, feed, limit=5, delay=5):
    if feed not in [u'hot', u'new', u'top']:
        raise BadFeedError(u"Feed must be one of hot, new or top")
    try:
        reddit = Reddit(u'crawler')
        subreddit = reddit.subreddit(subreddit)
        while (True):
            submissions = getattr(subreddit, feed)(limit=int(limit))
            _print_submissions(submissions)
            for i in range(delay * 60):
                sleep(1)
    except KeyboardInterrupt:
        print(u'Exiting rHockey ticker ...')


def _print_submissions(submissions):
    submissions = list(submissions)
    for index, submission in enumerate(reversed(submissions)):
        if not submission.stickied:
            ratio = submission.upvote_ratio
            score = submission.score
            ups, downs = _calculate_votes(score, ratio)
            index = len(submissions) - index - 1
            print(u"{}. {}".format(index, submission.title))
            print(u"    {}  \u02C4{}  \u02C5{}  ({}%)".format(
                                                score, ups, downs, ratio*100))
            print(strftime(u'    %Y-%m-%d %H:%M:%S', localtime(submission.created)))
            print(u"---------------------------------\n")
    print(u"---------------------------------\n")


def _calculate_votes(score, ratio):
    ups = round(
        (ratio * score) / (2 * ratio - 1)
        ) if ratio != 0.5 else round(score / 2)
    downs = ups - score
    return ups, downs
