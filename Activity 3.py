hours_plane=int(input("Enter the total amount of hours on the flight."))
minutes_plane=int(input("Enter the total amount of minutes on the flight."))
minutes_flight=minutes_plane/60
total_time_flight=hours_plane+minutes_flight
print("You have flown for",total_time_flight,"hours.")
print("Each hour you travel is equal to 50$.")
total_cost_flight=50*total_time_flight
print("Your total cost of the flight will be",total_cost_flight,"$.")
hotel_per_day=int(input("How many days will you be staying at the hotel?"))
print("Each day you stay at the hotal costs you 100$.")
total_cost_hotel=hotel_per_day*100
print("The total cost for staying at the hotal is",total_cost_hotel,"$." )
print("Your total bill for both the hotel and the flight costs",total_cost_hotel+total_cost_flight,"$.")