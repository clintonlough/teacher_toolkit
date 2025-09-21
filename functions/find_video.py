import os
import googleapiclient.discovery
import googleapiclient.errors


def build_api_client(YT_API_KEY):
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=YT_API_KEY)
    return youtube

def get_credentials():
    YT_API_KEY = os.getenv("YOUTUBE_API_KEY")
    if not YT_API_KEY:
        raise RuntimeError("YOUTUBE_API_KEY is not set or empty")
    return YT_API_KEY

def get_search_criteria():
    search_criteria = "volcanoes"
    return search_criteria

def search_video(youtube, search_criteria):
    request = youtube.search().list(
        part="snippet",
        channelType="any",
        q=search_criteria,
        type="video",
        maxResults=3
    )
    return request.execute()

def display_results(response):
    results = []
    for item in response.get("items", []):
        vid = item["id"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        url = f"https://www.youtube.com/watch?v={vid}"
        results.append({"title": title, "description": description, "url": url})

    for r in results:
        print(f"{r['title']} — {r['description']} - {r['url']}")

def main():
    
    YT_API_KEY = get_credentials()
    youtube = build_api_client(YT_API_KEY)

    search_criteria = get_search_criteria()

    response = search_video(youtube, search_criteria)

    display_results(response)

    

if __name__ == "__main__": 
    main()