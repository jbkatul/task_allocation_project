from django.shortcuts import render

# Create your views here.

# Function to return the list of IPL teams
def get_ipl_teams():
    """
    Returns a list of IPL teams (as of 2024 season).
    """
    teams = [
        "Chennai Super Kings",
        "Mumbai Indians",
        "Royal Challengers Bangalore",
        "Kolkata Knight Riders",
        "Sunrisers Hyderabad",
        "Rajasthan Royals",
        "Punjab Kings",
        "Delhi Capitals",
        "Lucknow Super Giants",
        "Gujarat Titans"
    ]
    return teams


# Function to display the teams in a formatted way
def display_ipl_teams():
    teams = get_ipl_teams()
    print("List of IPL Teams:")
    for idx, team in enumerate(teams, start=1):
        print(f"{idx}. {team}")

