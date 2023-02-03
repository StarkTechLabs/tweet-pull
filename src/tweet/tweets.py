#
from .util import get


def tweet_by_id(id: str):
    url_path = "/tweets/{0}".format(id)
    result = get(url_path)
    return result["data"]["data"]


def tweets_by_user_id(id: str):
    return {}


if __name__ == "__main__":
    res = tweet_by_id('1592986761705459712')
    print(res)
