class game:
    """Initialize a Game class"""
    team: str
    date: str
    time: str
    location: str

    def __init__(self, team: str, date: str, time: str, location: str):
        self.team = team
        self.date = date
        self.time = time
        self.location = location