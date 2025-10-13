from datetime import datetime, timedelta
from models.event.age_rating import AgeRating
from models.event.event import Event
from models.event.event_attendence import EventAttendence
from models.event.attraction import Attraction
from models.location.location import Location
from models.user.user import User
from models.user.connection import Connection


user1 = User("Marlon Simas", "senha_marlon", "marlon@mail.com")
user2 = User("Rodiro Santos", "senha_rodrigo", "rodrigo@mail.com")
user3 = User("Marcelo Tonho", "senha_marcelo", "marcelo@mail.com")
user4 = User("Joao Macedo", "senha_joao", "joao@mail.com")
user5 = User("Lauro Lino", "senha_lauro", "lauro@mail.com")

all_users = [user1, user2, user3, user4, user5]


c1 = Connection(user2, user1)
c2 = Connection(user3, user1)
c3 = Connection(user4, user1)
c4 = Connection(user5, user1)
c5 = Connection(user2, user4)

all_connections = [c1, c2, c3, c4, c5]


location = Location("Praça do PIDA", "Rua lauro", "90A", "trindade", "floripa", "0909")

a = Attraction("O Terno", "banda")
a2 = Attraction("Roda punk", "banda")

e = Event(
    "Festa na praça",
    user1,
    datetime.now(),
    "Oii gente vamo na festa?",
    AgeRating.ADULTS_ONLY,
    location,
)

e2 = Event(
    "Show de Rock",
    user1,
    datetime.now() + timedelta(days=2),
    "Banda maneira, venham!",
    AgeRating.ALL_AGES,
    location,
)

e2.add_attraction(a)
e2.add_attraction(a2)

e3 = Event(
    "Festa de criança",
    user1,
    datetime.now() + timedelta(days=5),
    "COMO é bom",
    AgeRating.CHILDREN,
    location,
)

e4 = Event(
    "Evento de Teste",
    user1,
    datetime.now() + timedelta(days=10),
    "Testando a criação de eventos",
    AgeRating.ADULTS_ONLY,
    location,
)

e5 = Event(
    "Rave #1",
    user2,
    datetime.now() + timedelta(days=7),
    "Rave muito show!",
    AgeRating.ADULTS_ONLY,
    location,
)

all_events = [e, e2, e3, e4, e5]

all_attendences = []

for event in all_events:
    for user in all_users:
        a = EventAttendence(user, event)
        all_attendences.append(a)
