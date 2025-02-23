# import requests

# def lookup_events(event_ids):
#     for event_id in event_ids:
#         # api_call = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/search_all_seasons.php?id={event_id}")
#         # api_call = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={event_id}")
#         api_call = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Ferrari")
#         storage = api_call.json()
#         # for event in storage["events"]:
#         #     print(event)
#         team = storage['teams'][0]
#         teamDescription = team['strDescriptionEN']
#         print(teamDescription)
#             # date_event = event["dateEvent"]
#             # home_team = event["strHomeTeam"]
#             # away_team = event["strAwayTeam"]

#         # print(f"{date_event}: {home_team} vs {away_team}")

# event_ids = [4370]

# lookup_events(event_ids)


from urllib.request import urlopen
import json
import streamlit as st
from datetime import datetime
import pandas as pd
import urllib.request as urlRequest

st.title("Sports Calendar")

# Formula 1
# f1Response = urlopen('https://api.openf1.org/v1/drivers?driver_number=1&session_key=latest')
current_year = datetime.now().year
f1Response = urlopen('https://api.openf1.org/v1/meetings?year={current_year}')
data = json.loads(f1Response.read().decode('utf-8'))
filtered_data = []
for meeting in data:
    filtered_data.append({
        'country_name': meeting['country_name'],
        'meeting_official_name': meeting['meeting_official_name'],
        'date_start': meeting['date_start'],
        'year': meeting['year']
    })
data = filtered_data
for meeting in data:
    meeting['date_start'] = datetime.strptime(meeting['date_start'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d-%m-%Y Time: %H:%M')
df = pd.DataFrame(data)
if not df.empty:
    st.header(f"Formula 1 {current_year} schedule")
    st.table(df)
    
# FOOTBALL
# UEFA Champions League
st.header("Football ⚽️")
API_KEY = "2da5d43064dc403294805f5841e3e49b"
championsLeagueURL = urlRequest.Request('https://api.football-data.org/v4/competitions/CL/matches?status=SCHEDULED')
championsLeagueURL.add_header('X-Auth-Token', API_KEY)
CLResponse = urlopen(championsLeagueURL)
data = json.loads(CLResponse.read().decode('utf-8'))
df = pd.DataFrame(data['matches'])
resultSetCount = data["resultSet"]["count"]
resultSetFirst = datetime.strptime(data["resultSet"]["first"], '%Y-%m-%d').strftime('%d-%m-%Y')
resultSetLast = datetime.strptime(data["resultSet"]["last"], '%Y-%m-%d').strftime('%d-%m-%Y')
st.subheader("UEFA Champions League")
st.write(f"Total Scheduled Matches: {resultSetCount}")
st.write(f"First Scheduled Match: {resultSetFirst}")
st.write(f"Last Scheduled Match: {resultSetLast}")
CLMatches = []
for match in data['matches']:
    CLMatches.append({
        'Home Team': match['homeTeam']['name'],
        'Away Team': match['awayTeam']['name'],
        'Date': datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%Y')
    })
data = pd.DataFrame(CLMatches).dropna()
if df.empty:
    st.write("No football matches today")
else:
    st.subheader("Next Match")
    st.table(data.head(1))
    
    
# Premier League
API_KEY = "2da5d43064dc403294805f5841e3e49b"
premierLeagueURL = urlRequest.Request('https://api.football-data.org/v4/competitions/PL/matches?status=SCHEDULED')
premierLeagueURL.add_header('X-Auth-Token', API_KEY)
PLResponse = urlopen(premierLeagueURL)
data = json.loads(PLResponse.read().decode('utf-8'))
df = pd.DataFrame(data['matches'])
resultSetCount = data["resultSet"]["count"]
resultSetFirst = datetime.strptime(data["resultSet"]["first"], '%Y-%m-%d').strftime('%d-%m-%Y')
resultSetLast = datetime.strptime(data["resultSet"]["last"], '%Y-%m-%d').strftime('%d-%m-%Y')
st.subheader("Premier Champions League")
st.write(f"Total Scheduled Matches: {resultSetCount}")
st.write(f"First Scheduled Match: {resultSetFirst}")
st.write(f"Last Scheduled Match: {resultSetLast}")
CLMatches = []
for match in data['matches']:
    CLMatches.append({
        'Home Team': match['homeTeam']['name'],
        'Away Team': match['awayTeam']['name'],
        'Date': datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%Y')
    })
data = pd.DataFrame(CLMatches).dropna()
if df.empty:
    st.write("No football matches today")
else:
    st.subheader("Next Match")
    st.table(data.head(1))
    

# Cricket
API_KEY = 'deb5a00c-1dff-4ab6-b54e-8c19c4c56deb'
cricketURL = urlRequest.Request('https://api.cricapi.com/v1/currentMatches?apikey=deb5a00c-1dff-4ab6-b54e-8c19c4c56deb&offset=0')
CResponse = urlopen(cricketURL)
data = json.loads(CResponse.read().decode('utf-8'))
todayMatches = []
for match in data['data']:
    scores = []
    for score in match['score']:
        scores.append(f"{score['inning']}: {score['r']}/{score['w']} in {score['o']} overs")
    todayMatches.append({
        'Match': match['name'],
        'Match Type': match['matchType'],
        'Status': match['status'],
        'Teams': match['teams'][0] + ' vs ' + match['teams'][1],
        'Venue': match['venue'],
        'Date': datetime.strptime(match['date'], '%Y-%m-%d').strftime('%d-%m-%Y'),
        'Score': ' | '.join(scores)
    })
data = pd.DataFrame(todayMatches).dropna()
st.header("Cricket 🏏")
if df.empty:
    st.write("No Cricket matches today")
else:
    st.subheader("Current Matches")
    st.dataframe(data)
