from items import *

room_home = {
    "name": "Home",

    "description":
    """                """,

    "exits": {"north": "Students Union", "east": "Tiger Tiger"},

    "items": [item_keys, item_money, item_id, item_phone]
}

room_students_union = {
    "name": "Student's Union",

    "description":
    """               """,

    "exits":  {"south": "Home", "east": "Retros"},

}

room_retros = {
    "name": "Retros",

    "description":
    """           """,

    "exits": {"west": "Students Union", "south": "Pryzm"},

}

room_prysm = {
    "name": "Prysm",

    "description":
    """This nightclub looks exactly the same as the last, 
    though the music seems to be worse… You see a girl 
    that you want to TALK to on the dancefloor..""",

    "exits": {"east": "Live Lounge", "south": "Tiger Tiger", "north": "Retros"},

}

room_tigertiger = {
    "name": "Tiger Tiger",

    "description":
    """As you enter the nightclub you notice the 
    flashing lights and feel the base of the music. 
    There are many people. But you notice a man over 
    by the bar, whom you wish to TALK to. """,

    "exits": {"west": "Home", "north": "Pryzm", "south": "Glam"},

}

room_glam = {
    "name": "Glam",
    
    "description":
    """             """,
    
    "exits": {"east": "Unse Unse Unse", "north": "Tiger Tiger"},

}
    
room_livelounge = {
    "name" : "Live Lounge",
    
    "description":
    """A somewhat shockingly decent place, though it is an awful 
    lot quieter than the previous nightclubs. A fellow student is
    nursing a beer near the door, you can go over to TALK to them.""",
    
    "exits": {"west": "Prysm", "south": "Unse Unse Unse"},
        
}
room_unse = {
    "name" : "Unse Unse Unse",
    
    "description":
    """            """,
    
    "exits": {"west": "Glam", "north": "Live Lounge"},
    
}



rooms = {
    "Home": room_home,
    "Students Union": room_studentsunion,
    "Retros": room_retros,
    "Pryzm": room_pryzm,
    "Tiger Tiger": room_tigertiger,
    "Glam": room_glam,
    "Live Lounge": room_livelounge,
    "Unse Unse Unse": room_unse
}
