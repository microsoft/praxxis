"""
This file returns the raw git url from url data, depending on the hosting 
service.
"""


def get_raw_url_for_file(url, name, subdirectory):
    """calls relevant parser to get raw url from git url"""
    from urllib.parse import urlparse

    url_data = urlparse(url)
    netloc = url_data.netloc

    if netloc == "github.com":
        return get_raw_url_github(url_data, name, subdirectory)
    elif netloc == "gitlab.com":
        return get_raw_url_gitlab(url_data, name, subdirectory)
    elif netloc == "bitbucket.org":
        return get_raw_url_bitbucket(url_data, name, subdirectory)
    elif netloc == "":
        return 1


def get_raw_url_github(url_data, name, subdirectory, token=""):
    """returns raw url from github url data"""
    return ("raw.githubusercontent.com%s/master%s%s%s" % (url_data.path.split('.')[0], subdirectory, name, token))


def get_raw_url_gitlab(url_data, name, subdirectory):
    """returns raw url from gitlab url data"""
    return ("%s%s/raw/master%s%s" % (url_data.netloc, url_data.path.split('.')[0], subdirectory, name))


def get_raw_url_bitbucket(url_data, name, subdirectory):
    """returns raw url from bitbucket url data"""
    return ("%s%s/raw/master/%s%s" % (url_data.netloc, url_data.path.split('.')[0], subdirectory, name))
