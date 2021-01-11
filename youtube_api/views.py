from django.shortcuts import render, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings

import requests


def search_response_json(request):
    youtube_search_api_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'part': 'snippet',
        'q': request.POST['search'],
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 20,
        'type': 'video',
    }

    search_response = requests.get(youtube_search_api_url, params=search_params)
    if search_response.status_code == 403:
        raise PermissionDenied
    else:
        search_json_results = search_response.json()['items']
        return search_json_results


def video_response_json(request):
    youtube_video_api_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_response = search_response_json(request)

    video_ids = []

    for search_res in search_response:
        video_ids.append(search_res['id']['videoId'])

    video_params = {
        'part': 'snippet',
        'id': ','.join(video_ids),
        'key': settings.YOUTUBE_DATA_API_KEY,
    }

    video_response = requests.get(youtube_video_api_url, params=video_params)
    video_response_results = video_response.json()['items']
    return video_response_results


def home(request):
    if request.method == 'POST':
        search_response_jsons = search_response_json(request)
        video_response_jsons = video_response_json(request)
        videos = []

        for search, video in zip(search_response_jsons, video_response_jsons):
            video_data = {
                'title': search['snippet']['title'],
                'thumbnail': search['snippet']['thumbnails']['high']['url'],
                'id': video['id'],
            }
            videos.append(video_data)

        context = {
            'videos': videos,
        }
        return render(request, 'youtube_api/index.html', context=context)
    else:
        return render(request, 'youtube_api/index.html')
