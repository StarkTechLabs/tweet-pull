#
from .util import get


def tweet_by_id(id: str):
    url_path = "/tweets/{0}".format(id)
    result = get(url_path)
    if not result["ok"]:
        raise Exception(result["error"])
    return result["data"]["data"]


# https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev
def tweets_by_user(username: str):
    url_path = "/tweets/search/recent"
    params = {
        "query": "from:{0} -is:retweet".format(username),
    }
    result = get(url_path, params=params)
    if not result["ok"]:
        raise Exception(result["error"])
    if "data" in result and "data" in result["data"]:
        return result["data"]["data"]
    return []


if __name__ == "__main__":
    res = tweet_by_id('1592986761705459712')
    print(res)
