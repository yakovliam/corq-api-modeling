import requests
import json
from model.event import (
    EventSearchRequest,
    EventSearchFilter,
    DISTANCE_FILTERS,
    TIME_FILTERS,
)
from model.institution import Institution

# URL constants
BASE_API_URL = "https://corqapi.campuslabs.com/"
GET_INSTITUTIONS_PATH = "institutions"
GET_EVENTS_PATH = "events/"
GET_BRANCHES_PATH = "branches"
GET_EVENTS_CATRORIES_PATH = "events/category"

# Other constants

## UC GEO DATA
# 	<InstitutionGeoData>
# 		<Distance>0</Distance>
# 		<Id>4323</Id>
# 		<InstitutionId>4412</InstitutionId>
# 		<Latitude>39.1331454</Latitude>
# 		<Longitude>-84.509213</Longitude>
# 		<Name>University of Cincinnati</Name>
# 		<RegionCode>usa</RegionCode>
# 		<Score>4.528366</Score>
# 	</InstitutionGeoData>

UNIVERSITY_OF_CINCINNATI_INSTITUTION = Institution(
    False,
    False,
    False,
    "Unknown",
    _id=4412,
    latitude=39.1331454,
    longitude=84.509213,
    location_id=4323,
    name="University of Cincinnati",
)

GET_BRANCHES_REQUEST_HEADERS = {
    "x-filter-institutionid": str(UNIVERSITY_OF_CINCINNATI_INSTITUTION.id),
}

EVENT_SEARCH_REQUEST = EventSearchRequest(
    institution=UNIVERSITY_OF_CINCINNATI_INSTITUTION,
    longitude=UNIVERSITY_OF_CINCINNATI_INSTITUTION.longitude,
    latitude=UNIVERSITY_OF_CINCINNATI_INSTITUTION.latitude,
    event_search_filter=EventSearchFilter(
        branch_filters=[],
        category_filters=[],
        perk_filters=[],
        theme_filters=[],
        time_filter=TIME_FILTERS[0],
        distance_filter=DISTANCE_FILTERS[2],
        query=None,
    ),
    page=1,
    radius=None,
    distance=None,
)

GET_EVENTS_REQUEST_HEADERS = {
    "x-filter-institutionid": str(UNIVERSITY_OF_CINCINNATI_INSTITUTION.id),
    "x-filter-startdate": str(EVENT_SEARCH_REQUEST.start_date.isoformat()),
    "Cache-Control": "no-cache",
}

GET_EVENTS_CATEGORIES_REQUEST_HEADERS = {
    "x-filter-institutionid": str(UNIVERSITY_OF_CINCINNATI_INSTITUTION.id),
}


def get_events_page():
    # start at page #1 (paginated requests)
    current_page = 1
    return requests.get(
        BASE_API_URL + GET_EVENTS_PATH + current_page,
        headers=GET_EVENTS_REQUEST_HEADERS,
    )


def get_branches():
    return requests.get(
        BASE_API_URL + GET_BRANCHES_PATH, headers=GET_BRANCHES_REQUEST_HEADERS
    )


def get_events_categories():
    return requests.get(
        BASE_API_URL + GET_EVENTS_CATRORIES_PATH,
        headers=GET_EVENTS_CATEGORIES_REQUEST_HEADERS,
    )


with open("events_page_output.json", "w") as f:
    f.write(json.dumps(get_events_page().json()))
