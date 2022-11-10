class Institution:
    def __init__(
        self,
        has_collegiate_link: bool,
        has_mobile_checkins: bool,
        has_rsvp_questions_enabled: bool,
        host_name: str,
        _id: int,
        latitude: float,
        longitude: float,
        location_id: int,
        name: str,
    ):
        self.has_collegiate_link = has_collegiate_link
        self.has_mobile_checkins = has_mobile_checkins
        self.has_rsvp_questions_enabled = (has_rsvp_questions_enabled,)
        self.host_name = host_name
        self.id = _id
        self.latitude = latitude
        self.longitude = longitude
        self.location_id = location_id
        self.name = name

