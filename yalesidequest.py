import random

# Nature activities
nature_activities = [
    "Visit Marsh Botanical Gardens", "Relax at the koi fish pond between the greenhouses",
    "Take the Yale Nature Walk", "Walk around Science Park", "Visit Yale Farm on Edwards Street",
    "Leitner Observatory", "Urban Meadows in front of Bett’s House",
    "Explore Memorial Garden behind School of Management",
    "Yale Divinity Farm", "Sage Rain Garden", "West Campus Urban Farm", "Explore Biowales on Chapel Street",
    "Yale Community Forest Garden", "Yale Experimental Watershed", "Visit the Little garden area on Old Campus",
    "Hike the Canal Trail", "Visit East Rock and hike the park", "Go to the Dam by East Rock",
    "Walk Long Wharf Nature Preserve", "Visit Wharf Beach and the food trucks",
    "Go to Lighthouse Point", "Visit Sleeping Giant (get ice cream at Wentworth’s)",
    "Relax at Scantlebury Park", "Visit Edgerton Park and see the chickens", "Explore St. Ronan Street",
    "Visit Albertus Magnus College Library", "Explore Beaver Pond Lagoon", "Visit Bowen Field", "Relax at Bayview Park",
    "Climb St. Joseph’s Church tower", "Take your dog to Saint Ronan Street Dog Park",
    "Explore West Rock Ridge State Park", "Visit East Shore Park"
]

# Building activities
building_activities = [
    "Explore the Chemistry building", "Visit the secret library in Sterling Chemistry Lab",
    "Study in the courtyard of STL",
    "Play piano at Sloane Physics Labs", "Explore Science Hill", "Visit the Marx Library",
    "Explore the 5th floor greenhouse in Marsh Hall", "Visit Wright Lab and check out the whiteboard walls",
    "Explore Osborn Memorial Lab", "Check out Yale Engineering Building", "Visit the CEID and make stickers",
    "Explore the tunnels under CEID", "Visit Watson Hall (CS)", "Study in Harkness Hall",
    "Visit Woolsey Hall", "Check out the President’s House garden", "Explore Horchow Hall",
    "Go to Dwight Hall on Old Campus", "Visit the Classics Library", "Check out Bingham Hall on Old Campus",
    "Visit Battell Chapel", "Check out Linsly Chittenden Hall", "Explore Lanman Wright",
    "Explore Vanderbilt Hall courtyard",
    "Visit the School of Architecture", "Study at Kroon Hall", "Explore the Law School", "Visit the School of Medicine",
    "Visit the Nursing School", "Check out the Yale School of Management", "Visit Berkeley Divinity School",
    "Explore Betts House at Divinity School"
]

# Museum activities
museum_activities = [
    "Visit Yale Art Gallery", "Explore the Peabody Museum", "Visit the Yale Center for British Art",
    "Explore the Beinecke Rare Book and Manuscript Library", "Visit Divinity School Library",
    "Explore the Haas Arts Library", "Visit the Medical Library (Harvey Cushing/John Hay Whitney)",
    "Check out the Music Library", "Visit the Marx Library", "Explore the secret library in the Chemistry building",
    "Visit the Law School Library", "Explore the New Haven Public Library"
]

# Miscellaneous activities
miscellaneous_activities = [
    "Explore the steam tunnels from Trumbull", "Climb the Bell Tower of St. Mary’s Church",
    "Find a rooftop seating spot behind the Chemistry building", "Explore the rooftop on Science Hill",
    "Visit Goodwill Hamden", "Take shortcuts through Old Campus", "Cut through Hillhouse to Murray and see the maze garden",
    "Visit every residential college courtyard", "Go into JE's printing press", "Relax in Trumbull hammocks",
    "Visit Silliman's Good Life Center", "Ride Silliman’s swing", "Visit Berkeley's tire swing",
    "Explore Saybrook and Branford’s connected courtyards", "Visit Morse and Stiles' underground courtyard",
    "Play basketball at the Murray courts", "Check out the pottery wheel in Pauli Murray", "Visit TD’s Roosevelt Hall",
    "Check out food trucks outside Yale School of Medicine", "Find a secret spot at the Slavic Studies Reading Room",
    "Go to the Blue State coffee across from Sterling on Wall St.", "Climb the stairs at Talcott Mountain State Park"
]


# Function to ask fun questions and generate an activity based on preferences
def generate_activity():
    print("Hello, this is your Side Quest generator to see fun things around Yale!'")

    # Fun questions
    nature_pref = input("Would you like to touch grass today? (yes/no): ").lower()
    building_pref = input(
        "Want to explore things around Yale's buildings? (yes/no): ").lower()
    museum_pref = input("Looking for a library or museum? (yes/no): ").lower()
    random_pref = input(
        "Or here is something totally random? (yes/no): ").lower()

    # Based on user inputs, choose an appropriate activity
    if nature_pref == 'yes':
        activity = random.choice(nature_activities)
    elif building_pref == 'yes':
        activity = random.choice(building_activities)
    elif museum_pref == 'yes':
        activity = random.choice(museum_activities)
    elif random_pref == 'yes':
        activity = random.choice(miscellaneous_activities)
    else:
        # If no preference, pick randomly from all lists
        activity = random.choice(nature_activities + building_activities + museum_activities + miscellaneous_activities)

    print("\nHere is your crazy cool Yale side quest: " + activity)

