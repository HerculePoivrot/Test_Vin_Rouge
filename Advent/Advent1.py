liste_lutins = []
calories=0
max_calories=0
with open("C:/Users/delvo/Desktop/Elves_Calories.txt", "r") as file:
    for line in file:
        striped = line.strip()
        # print(line.strip())
        if striped.isdigit():
            #print(f"digit: {int(striped)}")
            calories += int(line)
            

            
        elif striped == "":
            #print("blank line")
            liste_lutins.append(calories)
            if calories > max_calories:
                max_calories = calories
                #print(f"Le poids maximum porte est de {max_calories}")
            calories=0


print(max(liste_lutins), liste_lutins.index(max(liste_lutins)))