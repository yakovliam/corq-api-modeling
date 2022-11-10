from typing import Union, List
from enum import Enum
from datetime import datetime
from datetime import date
from datetime import timedelta
from .institution import Institution

Num = Union[int, float]


class EventFilterType(Enum):
    Distance = "distance"
    _None = "none"
    Perk = "perk"
    Theme = "theme"
    Time = "time"


class EventFilter:
    def __init__(self, title: str, value: str, filter_type: EventFilterType):
        self.title = title
        self.value = value
        self.filter_type = filter_type


class EventSearchFilter:
    def __init__(
        self,
        branch_filters: List[Num],
        category_filters: List[Num],
        perk_filters: List[EventFilter],
        theme_filters: List[EventFilter],
        time_filter: EventFilter,
        distance_filter: EventFilter,
        query: str,
    ):
        self.branch_filters = branch_filters
        self.category_filters = category_filters
        self.perk_filters = perk_filters
        self.theme_filters = theme_filters
        self.time_filter = time_filter
        self.distance_filter = distance_filter
        self.query = query


class EventSearchRequest:
    def __init__(
        self,
        # community_member_id: int,
        distance: int,
        event_search_filter: EventSearchFilter,
        institution: Institution,
        latitude: float,
        longitude: float,
        # max_distance: int,
        # min_distance: int,
        page: int,
        radius: float,
        # start_date: datetime,
        # time: int,
    ):
        # self.community_member_id = community_member_id
        self.distance = distance
        self.event_search_filter = event_search_filter
        self.institution = institution
        self.latitude = latitude
        self.longitude = longitude
        # self.max_distance = max_distance
        # self.min_distance = min_distance
        self.page = page
        self.radius = radius
        # self.start_date = start_date
        # self.time = time

        self.configure_distance_values()
        self.configure_time_values()

    def get_filters_values_by_filters(self, filters: List[EventFilter]):
        filters_value_list = []
        for fil in filters:
            filters_value_list.append(fil.value)
        return filters_value_list

    def get_benefit_filters(self):
        return self.get_filters_values_by_filters(self.event_search_filter.perk_filters)

    def get_branch_filters(self):
        return self.get_filters_values_by_filters(
            self.event_search_filter.branch_filters
        )

    def get_categories_filters(self):
        return self.get_filters_values_by_filters(
            self.event_search_filter.category_filters
        )

    def get_themes_filters(self):
        return self.get_filters_values_by_filters(
            self.event_search_filter.theme_filters
        )

    def configure_time_values(self):
        time_filter = self.event_search_filter.time_filter

        if time_filter is None:
            return

        if time_filter.value == "today":
            self.start_date = datetime.combine(date.today(), datetime.min.time())
            self.time = 24
        elif time_filter.value == "tomorrow":
            self.start_date = datetime.combine(
                date.today() + timedelta(days=7), datetime.min.time()
            )
            self.time = 24
        else:
            # fuck it this is wrong and idk why
            #     end_of_week = date.today() - timedelta(days=date.today().weekday())
            #     value = datetime.timestamp(end_of_week) * 1000

            #     n: int = 4 % value

            #     if n > 0:
            #         n = 4 % (value + 7)

            #     self.start_date = date.today() + timedelta(days=n)
            self.start_date = date.today()
            self.time = 72

    def configure_distance_values(self):
        distance_filter = self.event_search_filter.distance_filter

        if distance_filter is None:
            return

        if distance_filter.value == "walk":
            self.distance = 2
            self.min_distance = 0
            self.max_distance = 2
        elif distance_filter.value == "bike":
            self.distance = 5
            self.min_distance = 2
            self.max_distance = 7
        else:
            self.distance = 7
            self.min_distance = 7
            self.max_distance = None


BENEFIT_FILTERS = [
    EventFilter("FreeFood", "FREE FOOD", EventFilterType.Perk),
    EventFilter(
        "Merchandise",
        "FREE STUFF",
        EventFilterType.Perk,
    ),
    EventFilter("Credit", "CREDIT", EventFilterType.Perk),
]

DISTANCE_FILTERS = [
    EventFilter("walk", "WALK", EventFilterType.Distance),
    EventFilter(
        "bike",
        "BIKE",
        EventFilterType.Distance,
    ),
    EventFilter("roadtrip", "ROAD TRIP", EventFilterType.Distance),
]

THEME_FILTERS = [
    EventFilter("Arts", "ARTS & MUSIC", EventFilterType.Theme),
    EventFilter("Athletics", "ATHLETICS", EventFilterType.Theme),
    EventFilter("Cultural", "CULTURAL", EventFilterType.Theme),
    EventFilter("Fundraising", "FUNDRAISING", EventFilterType.Theme),
    EventFilter("GroupBusinesss", "GROUP BUSINESS", EventFilterType.Theme),
    EventFilter("ThoughtfulLearning", "LEARNING", EventFilterType.Theme),
    EventFilter("CommunityService", "SERVICE", EventFilterType.Theme),
    EventFilter("Social", "SOCIAL", EventFilterType.Theme),
    EventFilter("Spirituality", "SPIRITUALITY", EventFilterType.Theme),
]

TIME_FILTERS = [
    EventFilter("today", "TODAY", EventFilterType.Time),
    EventFilter("tomorrow", "TOMORROW", EventFilterType.Time),
    EventFilter("weekend", "WEEKEND", EventFilterType.Time),
]
