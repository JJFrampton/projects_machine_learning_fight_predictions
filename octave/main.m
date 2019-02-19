# import
# issues: fights.csv should only have 20 columns, according to the headings in the file
# fights = dlmread('/home/josephframpton/projects_machine_learning_fight_predictions/ufc_fights__sherdog_2_23_2016.csv',',',2,0) 
# fighters = dlmread('/home/josephframpton/projects_machine_learning_fight_predictions/ufc_fighters__sherdog_2_23_2016.csv',',',2,0) 
fights = csvread("/home/josephframpton/projects_machine_learning_fight_predictions/ufc_fights__sherdog_2_23_2016.csv");
fighters = csvread("/home/josephframpton/projects_machine_learning_fight_predictions/ufc_fighters__sherdog_2_23_2016.csv");

fights(:,12)

# X = fights(:,1:)

size(fights)
size(fighters)
