from pyscript import display
from js import document

# club data
clubs = {
    "club1": {
        "Club name": "Science Club",
        "Location": "Science Lab",
        "Meeting date": "Every Tuesday",
        "Meeting time": "3 - 4 PM",
        "Description": "Will do experiments every week",
        "Club moderator": "Mr. Calpo",
        "Max members": 25
    },

    "club2": {
        "Club name": "Math Club",
        "Location": "Room 701",
        "Meeting date": "Every Wednesday",
        "Meeting time": "2 - 3 PM",
        "Description": "Will solve math equations every week",
        "Club moderator": "Mr. Ferma",
        "Max members": 30
    },

    "club3": {
        "Club name": "Social Science Club",
        "Location": "Room 506",
        "Meeting date": "Every Wednesday",
        "Meeting time": "2 - 3 PM",
        "Description": "Will talk about political topics every week",
        "Club moderator": "Mr. Temperante",
        "Max members": 20
    },

    "varsity1": {
        "Club name": "Basketball Varsity",
        "Location": "Quadrangle",
        "Meeting date": "Every Monday",
        "Meeting time": "3:30 - 5 PM",
        "Description": "Will practice basketball every week",
        "Club moderator": "Mr. Gervacio",
        "Max members": 15
    },

    "varsity2": {
        "Club name": "Volleyball Varsity",
        "Location": "Gym",
        "Meeting date": "Every Thursday",
        "Meeting time": "2 - 3 PM",
        "Description": "Will practice volleyball every week",
        "Club moderator": "Mr. Gervacio",
        "Max members": 15
    }
}


# function to show club info
def show_club_info(event):
    selected = document.getElementById("Clubs").value
    output = document.getElementById("output")
    output.innerHTML = "" 

    if selected in clubs:""