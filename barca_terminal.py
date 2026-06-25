import requests

# Your API-Sports Setup
API_KEY = 'a27c78fc2e3bbda35b2cc5311680ad94' # Paste your key here again
BARCA_TEAM_ID = 529 
SEASON = 2024 

# Ask the API for ALL matches in the current season
API_URL = f"https://v3.football.api-sports.io/fixtures?team={BARCA_TEAM_ID}&season={SEASON}"

headers = {
    'x-apisports-key': API_KEY
}

def get_last_match():
    print("Fetching FC Barcelona match data...\n")
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status() 
        data = response.json()
        
        # Check for API errors
        if data.get('errors'):
            print("🚨 API Error Detected:")
            if isinstance(data['errors'], dict):
                for key, value in data['errors'].items():
                    print(f" - {key.capitalize()}: {value}")
            else:
                print(data['errors'])
            return
            
        fixtures = data.get('response', [])
        
        if not fixtures:
            print("No matches found for this team/season.")
            return
            
        # 1. Filter out matches that haven't finished yet
        # 'FT' = Full Time, 'AET' = After Extra Time, 'PEN' = Penalties
        finished_statuses = ['FT', 'AET', 'PEN']
        completed_matches = [
            match for match in fixtures 
            if match['fixture']['status']['short'] in finished_statuses
        ]
        
        if not completed_matches:
            print("No completed matches found for this season yet.")
            return

        # 2. Sort the completed matches by their timestamp (newest first)
        completed_matches.sort(key=lambda x: x['fixture']['timestamp'], reverse=True)
        
        # 3. Grab the most recent one (the first item in our sorted list)
        match = completed_matches[0]
        
        # Extract the details
        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        home_goals = match['goals']['home']
        away_goals = match['goals']['away']
        league = match['league']['name']
        date = match['fixture']['date'][:10]
        venue = match['fixture']['venue']['name']
        
        # Print the scorecard
        print("-" * 40)
        print(f"🏆 League: {league}")
        print(f"📅 Date:   {date}")
        print(f"🏟️  Venue:  {venue}")
        print("-" * 40)
        print(f"   {home_team}  {home_goals} - {away_goals}  {away_team}")
        print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"Network Error fetching data: {e}")

if __name__ == '__main__':
    get_last_match()