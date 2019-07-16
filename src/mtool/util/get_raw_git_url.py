def get_raw_url_for_file(url, name, subdirectory):
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
    return(f"raw.githubusercontent.com{url_data.path.split('.')[0]}/master{subdirectory}{name}{token}") 


def get_raw_url_gitlab(url_data, name, subdirectory):
    return(f"{url_data.netloc}{url_data.path.split('.')[0]}/raw/master{subdirectory}{name}")


def get_raw_url_bitbucket(url_data, name, subdirectory):
    return(f"{url_data.netloc}{url_data.path.split('.')[0]}/raw/master/{subdirectory}{name}")
