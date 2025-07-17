weather_condition = input("what's the weather like toay? (sunny/rainy/cold): ")
sunny ="Wear a t-shirt and sunglasses."
rainy ="Don't forget your umbrella and a raincoat."
cold ="Make sure to wear a warm coat and a scarf."

if weather_condition == "sunny":
    print(f"recommendation:{sunny}")
elif weather_condition =="rainy":
    print(f"recommendation:{rainy}")
elif weather_condition =="cold":
    print(f"recommendation:{cold}")
else:
    print("Sorry, I don't have recommendations for this weather.")
