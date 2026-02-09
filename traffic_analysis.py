#Author:N.Ashvini
#date:24/11/2024
#IITstudent Id:20240067
#UOW student Id:w2119840

#task A:Input Validation
def validate_date_input():
    while True:#ask the input as the date from the user
     Day_input=input("please enter the day of the survey in the format dd:") 
     if Day_input.isdigit():#check the input is integer or not
      DD=int(Day_input)
       #check if the date is between 1 and 31
      if DD > 31:
        print("Out of range - values must be in the range 1 and 31.")
      elif DD < 1:
        print("Out of range - values must be in the range 1 and 31.")
      else:#if the input is valid, exit the loop
         break
     else:#if the input is not a valid integer
        print("Integer required")
        
    while True:#ask the input as the month from the user
     month_input=input("please enter the month of the survey in the format MM:")   
     if month_input.isdigit():#check the input is integer or not
      MM=int(month_input)
      if MM>12:#check if the date is between 1 and 12
       print("Out of range - values must be in the range 1 to 12.")
      elif MM<1:
       print("Out of range - values must be in the range 1 to 12.")
      else:
          if DD==31:#check 31 days months
              if MM in [1,3,5,7,8,10,12]:
                break
              else:
                print("invalid month")
                continue
          elif MM==2:#february
               if DD>29:
                  print("invalid month")
                  continue
               else:
                  break
          else:
              break
     else:#if the input is not a valid integer
        print("Integer required")
       
    while True:#ask the input as the year from the user
     year_input=input("Please enter the year of the survey in the format YYYY:")   
     if year_input.isdigit():#check the input is integer or not
      YYYY=int(year_input)
      if YYYY>2024:#check if the input is between 2000and 2024
       print("Out of range - values must range from 2000 and 2024.")
      elif YYYY<2000:
            print("Out of range - values must range from 2000 and 2024.")
      else:#if the input is valid,exit the valid
         if DD==29 and MM==2:# chack the leap year
            if YYYY%4==0:
               break
            else:
               print("invalid year")
               continue
         else:   
             break
     else:#if the input is not a valid integer
         print("Integer required")
    return f"{DD:02d}/{MM:02d}/{YYYY}"
def validate_continue_input():
    while True:
        response=input("if you want to load a new dataset press Y or press N to quit: ")
        if response.upper()=="Y":#enter y to continue
            return response
        elif response.upper()=="N":#enter N to exit
            return response
        else:
         print("invalid response")

#Task B:processed outcomes
import csv
def process_csv_data(file_path):
  try:  
    with open(file_path,'r')as csvfile:#open the selected csv file 
         reader=csv.DictReader(csvfile)
         data=list(reader)
         if not data:
           return None
  #initialize counters the variables
         total_vehicles=0
         total_trucks=0
         total_electric_vehicles=0
         two_wheeled=0
         buses_north=0
         no_turn_vehicles=0
         over_speed_vehicles=0
         Hanly_total_vehicles=0
         elm_total_vehicles=0
         elm_scooter=0
         total_bicycle=0
         max_hour=0
         Rainy_Hours=[]
         busiest_hour={}
        # count the total vehicles
         for row in data:
             total_vehicles+=1
             
             # count the trucks
             if row["VehicleType"].lower()=='truck':
                 total_trucks+=1

             # count electric vehicles    
             if row["elctricHybrid"]=='True':
                 total_electric_vehicles+=1

             # two wheeled vehicles count   
             if row["VehicleType"].lower()in['bicycle','scooter','motorcycle']:
                 two_wheeled+=1

             #total number of busses leaving ELM Avenue/Rabbit Road junction heading north    
             if row["VehicleType"]=='Buss':
                 if row["JunctionName"].lower()=='elm avenue/rabbit road':
                    if row["travel_Direction_out"]=='N':
                         buses_north+=1

             #total number of vehicles passing through both junction without turning
             if row["travel_Direction_in"]==row["travel_Direction_out"]:
                 no_turn_vehicles+=1

             # count the overspeed vehicle    
             if int( row["JunctionSpeedLimit"])< int(row["VehicleSpeed"]):
                 over_speed_vehicles+=1

             #count the vehicles recorded through only Elm Avenue/Rabbit Road junction    
             if row["JunctionName"].lower()=='elm avenue/rabbit road':
                 elm_total_vehicles+=1

             #The percentage of scooters through Elm Avenue/Rabbit Road (rounded to integer)
                 if row["VehicleType"].lower()=='scooter':
                   elm_scooter+=1
                 scooters_perc=(elm_scooter/elm_total_vehicles)*100
                 percentage_scooters=round(scooters_perc)

             #count the vehicles recorded through only Hanly Highway/Westway junction    
             elif row["JunctionName"]=='Hanley Highway/Westway':
                 Hanly_total_vehicles+=1

             #count the vehicles recorded in the peak hour on Hanley Highway/Westway   
             if row["JunctionName"]=='Hanley Highway/Westway':
                 hour=row["timeOfDay"].split(':')[0]
                 if hour in busiest_hour:
                     busiest_hour[hour]+=1
                 else:
                     busiest_hour[hour]=1
             if busiest_hour:
              max_hour =max(busiest_hour, key=busiest_hour.get)
              no_vehicle_busiest_hour= busiest_hour[max_hour]
             else:
                 max_hour=0
                 no_vehicle_busiest_hour=0        

             #count total number of hours of rain on this day        
             if row["Weather_Conditions"] in['Heavy Rain','Light Rain']:
                Hour=row["timeOfDay"].split(':')[0]
                if Hour not in Rainy_Hours:
                  Rainy_Hours.append(Hour)
             total_rainyhours=len(Rainy_Hours)

             #Count trucks as a percentage of all vehicles recorded
             trucks_perc=(total_trucks/total_vehicles)*100
             percentage_trucks=round(trucks_perc)

             #count average number bicycle per hour for the selected date
             if row["VehicleType"]=='Bicycle':
                total_bicycle+=1
             Avg_bicycle=round(total_bicycle/24)

             #retun calculated outcomes
             outcomes={
                 "total_vehicles":total_vehicles,
                 "total_trucks":total_trucks,
                 "total_electric_vehicles":total_electric_vehicles,
                 "two_wheeled":two_wheeled,
                 "buses_north":buses_north,
                 "no_turn_vehicles":no_turn_vehicles,
                 "percentage_trucks":percentage_trucks,
                 "Avg_bicycle":Avg_bicycle,
                 "over_speed_vehicles":over_speed_vehicles,
                 "elm_total_vehicles":elm_total_vehicles,
                 "Hanly_total_vehicles":Hanly_total_vehicles,
                 "percentage_scooters":percentage_scooters,
                 "no_vehicle_busiest_hour":no_vehicle_busiest_hour,
                 "total_rainyhours":total_rainyhours,
                 "max_hour":max_hour,
              }   
         
    return outcomes
  except FileNotFoundError:
      print(f"file not found")
      return None
            
def display_outcomes(outcomes,file_path):
    #creating a formatted report with traffic data
         if not outcomes:
             return
         results=("                                                                          \n"
              "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
             f"data file selected is {file_path}\n"
             f"The total number of vehicles recorded for this date: {outcomes['total_vehicles']}\n"
             f"The total number of trucks recorded for this date: {outcomes['total_trucks']}\n"
             f"The total number of electic vehicles for this date is: {outcomes['total_electric_vehicles']}\n"
             f"The total number of two-wheeled vehicles for this date is: {outcomes['two_wheeled']}\n"
             f"The total number of buses leaving Elm Avenue/Rabbit Road heading North is: {outcomes['buses_north']}\n"
             f"The total number of vehicles through both junctions not turning left or right is: {outcomes['no_turn_vehicles']}\n"
             f"The percentage of total vehicles recorded that are trucks for this date: {outcomes['percentage_trucks']}%\n"
             f"The average number of bicycle  per hour for this date is: {outcomes['Avg_bicycle']}\n"
             f"The total number of vehicles recorded as over the speed limit for this date is: {outcomes['over_speed_vehicles']}\n"
             f"The total number of vehicles recorded through ElmAvenue/Rabbit Road junction is: {outcomes['elm_total_vehicles']}\n"
             f"The total number of vehicles recorded through HanlyHighway/westway junction is: {outcomes['Hanly_total_vehicles']}\n"
             f"{outcomes['percentage_scooters']}% of vehicles recorded through Elm Avenue/Rabbit road are scooters\n"
             f"The highest number of vehicles in an hour onHanly Highway/Westway is: {outcomes['no_vehicle_busiest_hour']}\n"
             f"the most vehicle through Hanly Highway/Westway were recorded between{outcomes['max_hour']}:00 and {int(outcomes['max_hour'])+1}:00\n"       
             f"The number of hours of rain for this date is: {outcomes['total_rainyhours']}\n"
             "                                                                          \n"
             "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"     
                 )
         print(results)#print the report
         save_results_to_file(results)
#Task C: Save Results to Text File         
def save_results_to_file(outcomes,filename="results.txt"):
    with open(filename,"a")as file:#open the file in append mode 
        file.write(outcomes)#write the report into the file

# Task D: Histogram Display
import tkinter as tk
class HistogramApp:
    def __init__(self, traffic_data, date):
        # Initialize with traffic data and formatted date
        self.traffic_data = traffic_data
        self.date = f"{date[:2]}/{date[2:4]}/{date[4:]}"
        self.root = tk.Tk()# Initialize Tkinter window
        self.canvas = None  # Initialize canvas to draw the histogram
    def setup_window(self):
        # Set up the main window for the histogram display
        self.root.title("Histogram")
        self.root.geometry("1400x600") # Window size
        self.canvas = tk.Canvas(self.root, width=1300, height=500, bg="white")
        self.canvas.pack(pady=20) # Pack the canvas with padding
        self.draw_histogram()# Call the method to draw the histogram
        self.add_legend()# Call the method to add a legend
    def draw_histogram(self):
        # Initialize a dictionary to store traffic data per hour for each junction
        junction_data={
         "Elm Avenue/Rabbit Road": [0] * 24, # 24 hours, initially 0 traffic count
         "Hanley Highway/Westway": [0] * 24   
        }

        #process traffic data
        for row in self.traffic_data:
            try:
                hour = int(row["timeOfDay"].split(":")[0])# Extract the hour from timeOfDay
                junction_name = row["JunctionName"]# Extract the junction name
                if junction_name in junction_data:# If the junction is valid
                  junction_data[junction_name][hour] += 1# Increment the vehicle count for that hour
            except (ValueError, KeyError):
                continue
         
        #calculate maximum volume for scaling 
        max_volume = max(
         max(max(junction_data["Elm Avenue/Rabbit Road"]),
             max(junction_data["Hanley Highway/Westway"])),
         1 # avoid division by zero
        )
        

       #graph dimension  and margin setting
        margin_left = 50
        margin_bottom = 50
        graph_height = 300
        graph_width = 1200
        bar_width = 15
        bar_spacing =2
        hour_spacing=15
        hour_group_spacing=10

        #add tittle of histogram
        self.canvas.create_text(
            margin_left + graph_width/2, 30,
            text=f"Histogram of Vehicle Frequency per Hour ({self.date})",
            font=("Arial", 12, "bold")
        )


        
        #draw horizontal axis
        self.canvas.create_line(
            margin_left,400,
            margin_left+graph_width,400,
            width=1
        )
        
       # Draw bars for each hour of the day
        for hour in range(24):
            # Calculate the position of the bar for each hour
            base_x = margin_left+hour *(2 * bar_width + bar_spacing+hour_group_spacing)

            # Draw the hour label at the bottom of each group of bars
            
            self.canvas.create_text(
              base_x + bar_width,420,
              text=f"{hour:02d}",
              font=("Arial", 8)
            )

            #  calculate the hight of bar for Elm Avenue/Rabbit Road bar
            elm_height = (junction_data["Elm Avenue/Rabbit Road"][hour] / max_volume)*graph_height
            self.canvas.create_rectangle(
                base_x,400,
                base_x + bar_width,400-elm_height,
                fill="blue"#blue colour for Elm avenue
                
            )             
            # Display the traffic count above the Elm Avenue bar if greater than zero
            if junction_data["Elm Avenue/Rabbit Road"][hour] > 0:
                self.canvas.create_text(
                    base_x + bar_width/2, 395- elm_height,
                    text=str(junction_data["Elm Avenue/Rabbit Road"][hour]),
                    font=("Arial", 8)
                )


             # calculate the height of bar for Hanley Highway/Westway bar
            hanley_height = (junction_data["Hanley Highway/Westway"][hour] / max_volume) * graph_height
            hanley_x = base_x + bar_width + bar_spacing
            self.canvas.create_rectangle(
                hanley_x, 400,
                hanley_x+ bar_width, 400- hanley_height,
                fill="Light pink" #light pink for  Hanley Highway/Westway bar 
            )
           # Display the traffic count above the Hanley Highway bar if greater than zero
            if junction_data["Hanley Highway/Westway"][hour] > 0:
                self.canvas.create_text(
                    hanley_x+ bar_width/2, 395- hanley_height,
                    text=str(junction_data["Hanley Highway/Westway"][hour]),
                    font=("Arial", 7)
                )

        #x-axis label    
        self.canvas.create_text(
            margin_left + graph_width/2, 500-margin_bottom + 40,
            text="Hours (00:00 to 24:00)",
            font=("Arial", 10)
        )
                     

    def add_legend(self):
        # add legend
        legend_x = 150
        legend_y = 50
        # Elm Avenue legend
        self.canvas.create_rectangle( legend_x, legend_y,  legend_x+20, legend_y + 10, 
                                   fill="blue", outline="blue")
        self.canvas.create_text( legend_x+25, legend_y + 5,
                              text="Elm Avenue/Rabbit Road",
                              anchor="w", font=("Arial", 9))
        # Hanley Highway legend
        self.canvas.create_rectangle( legend_x+200, legend_y , legend_x+220, legend_y + 10, 
                                   fill="light pink", outline="light pink")
        self.canvas.create_text( legend_x+225, legend_y + 5,
                              text="Hanley Highway/Westway",
                              anchor="w", font=("Arial", 10))
        
        

    def run(self):
        self.setup_window()
        self.add_legend()
        self.root.mainloop()#start the tkinter event loop

#task E:
class MultiCSVProcessor:
    def __init__(self):
    
        self.current_data = None #hold the currently loaded  CSV data
        self.current_outcomes = None# holds the outcomes of processing the current data

    def load_csv_file(self, file_path):
        
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.current_data = list(reader) # Store the data as a list of dictionaries
            self.current_outcomes = process_csv_data(file_path) # Process the data
            return True
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return False

    def clear_previous_data(self):
        # Clear any previously loaded data
        self.current_data = None
        self.current_outcomes = None

    def process_files(self):
       
        while True:
            #get the date input
            date = validate_date_input().replace("/", "")
            file_path = f"traffic_data{date}.csv"  # Construct the file path based on date

             # Try to load and process the file
            if self.load_csv_file(file_path):
                if self.current_outcomes:
                    #display outcomes and create histogram 
                    display_outcomes(self.current_outcomes, file_path)
                    app = HistogramApp(self.current_data, date)
                    app.run()
        
             #  Ask the user if they want to continue
            response = validate_continue_input()
            if response.upper() == "N":
               print("End of run")
               break
        # Clear data after processing all files    
        self.clear_previous_data()

def main():
    
    processor = MultiCSVProcessor()# Create an instance of the processor
    processor.process_files()# Start processing files


if __name__ == "__main__":
    main()# Run the program


    






        

      
