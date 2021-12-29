counties= ['Arapahoe', 'Denver', 'Jefferson']
counties_dict = {}
counties_dict["Arapahoe"] = 422829
# print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.items())
# print( counties_dict.keys())
# print(counties_dict.get("Denver"))
# print(counties_dict['Arapahoe'])
# print(counties_dict["Arapahoe"])
# voting_data = []
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print(f"El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# x = 0
# # while x <= 5:
# #     print(x)
# #     x = x + 1
# numbers = [0, 1, 2, 3, 4]
# for num in range(5):
#     print(num)
# for i in range(len(counties)):
#     print(counties[i])
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
# #     print(counties_dict[county])
# # for county in counties_dict:
# #     print(counties_dict.get(county))
# for county, voters in counties_dict.items():
#     print(f'{county + " county has"} { voters }' " registered voters"  )
    

# Print each county and registered voter form the counties dictionary so that the output looks like this:

# Each county and its registered voters have printed out in the
# following format:Arapahoe County has 422829 registered voters. Denver
# County has 463353 registered voters.Jefferson County has 432438
# registered
# # voters.
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# # for county_dict in voting_data:
# #     print(county_dict)
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)