def get_raw_url_for_file(url, name, subdirectory):
    from urllib.parse import urlparse

    url_data = urlparse(url)
    if url_data.netloc == "github.com":
        return get_raw_url_github(url_data, name, subdirectory)
    elif url_data.netloc == "gitlab.com":
        return get_raw_url_gitlab(url_data, name, subdirectory)
    elif url_data.netloc == "bitbucket.org":
        return get_raw_url_bitbucket(url_data, name, subdirectory)
    else:
        return 1

def get_raw_url_github(url_data, name, subdirectory, token=""):
    return(f"https://raw.githubusercontent.com{url_data.path.split('.')[0]}/master{subdirectory}{name}{token}") 


def get_raw_url_gitlab(url_data, name, subdirectory):
    return(f"https:/{url_data.netloc}{url_data.path.split('.')[0]}/raw/master{subdirectory}{name}")


def get_raw_url_bitbucket(url_data, name, subdirectory):
    return(f"https:/{url_data.netloc}{url_data.path.split('.')[0]}/raw/master/{subdirectory}{name}")

