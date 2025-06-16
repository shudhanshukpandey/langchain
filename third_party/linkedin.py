import requests
import os


EDEN_MARCO_GIST_URL = "https://gist.githubusercontent.com/shudhanshukpandey/f7454183754dfbc8fa56c56e947c86b6/raw/36a2ce86f39853720e7eef1a680d5c05f8aa1ba4/eden_marco"
SHUDHANSHU_PANDEY_URL = "https://www.linkedin.com/in/shudhanshu-pandey-58412618b/"
SHUDHANSHU_PANDEY_GIST_URL = "https://gist.githubusercontent.com/shudhanshukpandey/a5e5ed125fe26c0684792d92f0cc9069/raw/b0b25a28681488ada2c0f4419ac4d27286bac15f/sp_linkedIn.json"

def scraoe_linkedin(linkedin_profile_url:str, mock:bool=False):
    """scrape information from linkedin profile,
    Manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url = SHUDHANSHU_PANDEY_GIST_URL

        return_data = requests.get(linkedin_profile_url, timeout=10).json()
    else:
        # api_endpoint = "https://api.scrapin.io/enrichment/profile"
        # params={
        #     "apikey":os.environ.get("SCRAPIN_API_KEY"),
        #     "linkedInUrl":linkedin_profile_url
        # }

        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic={"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic,
        timeout=10,
        )

        return_data = response.json()

    return return_data



if __name__== "__main__":
    linkedin_data = scraoe_linkedin(linkedin_profile_url=SHUDHANSHU_PANDEY_URL, mock=True)
    print(linkedin_data)