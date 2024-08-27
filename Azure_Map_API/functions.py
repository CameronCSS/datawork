import numpy as np

def map_splitter(upper_left, upper_right, lower_right, step_size=0.1):
    # Extract coordinates
    x_min, y_max = upper_left
    x_max, y_min = upper_right[0], lower_right[1]

    # Generate x and y points with increased step_size for wider spread
    x_points = np.arange(x_min, x_max + step_size, step_size)
    y_points = np.arange(y_max, y_min - step_size, -step_size)

    # Create grid of points
    points = [[x, y] for x in x_points for y in y_points]

    # Calculate the middle point
    x_middle = (x_min + x_max) / 2
    y_middle = (y_max + y_min) / 2
    middle_point = [x_middle, y_middle]

    # Include the middle point in the output
    output = points + [middle_point]

    return output


def azure_maps_query(center_point_long, center_point_lat, limit, entity_input, AZURE_MAP_KEY):
    import requests

    # Convert numerical inputs to strings
    center_point_long = str(center_point_long)
    center_point_lat = str(center_point_lat)
    limit = str(limit)
    entity_input = str(entity_input)

    limit = str(limit)
    entity_type = str(entity_input)

    sample_query = "https://atlas.microsoft.com/search/poi/json?subscription-key=" + AZURE_MAP_KEY + "&api-version=1.0&query=" + entity_type + "&limit=+" + limit + "&lat=" + center_point_lat + "&lon=" + center_point_long

    URL = sample_query

    r = requests.get(URL)
    # results = pd.DataFrame(r.json().get("d").get("results")) # Just save the raw JSONs
    results = r.json()

    return results