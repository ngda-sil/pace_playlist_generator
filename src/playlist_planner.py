def select_matching_songs(interval, items, matching_songs):
    for item in items:
        if (
            interval.effort_duration_ms - 5000
            < item["track"]["duration_ms"]
            < interval.effort_duration_ms + 5000
        ):
            print(item["track"]["name"])
            matching_songs.append(item["track"]["uri"])
        if len(matching_songs) == interval.rep:
            break
    return matching_songs
