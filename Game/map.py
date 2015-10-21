from items import *
from characters import *

room_home = {
    "name": "Home",

    "description":
    """You are at home, in your hall of residence at Cardiff University. It's
freshers week, and you want to go out, party and have a great time!""",

    "exits": {"north": "Students Union", "east": "Tiger Tiger"},

    "items": [item_keys, item_money, item_id, item_phone]
    
    # No character entry in this room as 'James' is the role of the player.
}

room_students_union = {
    "name": "Student's Union",

    "description":
    """The Union isn't looking too busy. There are a few people over by the bar
but the dance floor is virtually empty! A lot quieter than some of the other
nightclubs tonight!""",

    "exits":  {"south": "Home", "east": "Retros"},

    "items": [item_fedora, item_beer],
    
    "character": character_Jam, # Jaymi
    
    "game": {"id": "hangman", "name": "hangman"}
}

room_retros = {
    "name": "Retros",

    "description":
    """The flashing lights and the upbeat tunes of the 1970s sweep over you.
You notice some guys in the corner drinking bottles of Tequilla; while on the
dance floor, two fluttering lovebirds are experiencing their first kiss together.""",

    "exits": {"west": "Students Union", "south": "Pryzm"},

    "items": [item_warmers],
    
    "character": character_Gigi, # Georgi
    
    "game": {"id": "fetch", "name": "the fetch game"}
}

room_pryzm = {
    "name": "Pryzm",

    "description":
    """This nightclub looks very similar to other nightclubs you've been too
before, though the music seems to be worse... You see a good number of people
out on the dance floor dancing their socks off, and a few people at the bar
(including Jaz) having some drinks...""",

    "exits": {"east": "Live Lounge", "south": "Tiger Tiger", "north": "Retros"},

    "items": [item_umbrella],
    
    "character": character_Jaz, # Jasmine
    
    "game": {"id": "riddle", "name": "the riddle game"}
}

room_tigertiger = {
    "name": "Tiger Tiger",

    "description":
    """As you enter the nightclub you notice the flashing lights and feel the
bass of the music. There are many people. But you notice a man over by the bar,
whom you wish to talk to. """,

    "exits": {"west": "Home", "north": "Pryzm", "south": "Glam"},

    "items": [item_gloves],

    "character": character_Joe, # Josh M
    
    "game": {"id": "rps", "name": "rock, paper, scissors"}
}

room_glam = {
    "name": "Glam",
    
    "description":
    """The room is L shaped, expansive and strangely well lit, without using
disco lighting. You can see a group of drunk students over by the bar, oblivious
to what is happening around them.""",
    
    "exits": {"east": "Unse Unse Unse", "north": "Tiger Tiger"},

    "items": [item_scarf],

    "character": character_Jam, # Jaymi
    
    "game": {"id": "numberguesser", "name": "the number guessing game"}
}
    
room_livelounge = {
    "name" : "Live Lounge",
    
    "description":
    """A somewhat shockingly decent place, though it is an awful lot quieter
than the previous nightclubs. A fellow student is nursing a beer near the door,
you can go over to talk to them.""",
    
    "exits": {"west": "Pryzm", "south": "Unse Unse Unse"},

    "items": [item_socks],
    
    "character": character_Josh, # Josh S
    
    "game": {"id": "blackjack", "name": "blackjack"}
}

room_unse = {
    "name" : "Unse Unse Unse",
    
    "description":
    """This nightclub is awfully strange; there are blinking lights everywhere
you look, giving people epilepsy. Aside from that, there are some 3rd year students
having a 'smashing' time on the dance floor!""",
    
    "exits": {"west": "Glam", "north": "Live Lounge"},
    
    "items": [item_glasses],

    "character": character_Pete, # The Other Random Person
    
    "game": {"id": "mastermind", "name": "Mastermind"}
}



rooms = {
    "Home": room_home,
    "Students Union": room_students_union,
    "Retros": room_retros,
    "Pryzm": room_pryzm,
    "Tiger Tiger": room_tigertiger,
    "Glam": room_glam,
    "Live Lounge": room_livelounge,
    "Unse Unse Unse": room_unse
}
