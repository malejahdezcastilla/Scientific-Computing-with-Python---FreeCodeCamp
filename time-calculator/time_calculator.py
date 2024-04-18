def add_time (start, duration, starting_day = None):

    start = convert_start_time_to_24_hours (start)
    duration = duration_to_integer (duration)
    
   
    hours = start [0], duration [0]
    minutes = start [1], duration [1]
    sum_hours = start [0] + duration [0]
    sum_minutes = start [1] + duration [1]
   
    
    one_minute = 60
    minutes_to_hours = sum_minutes / one_minute
    hours_to_minutes = sum_minutes % one_minute
    total_hours = (sum_hours) + (minutes_to_hours)
    passed_hours = int(total_hours), int(hours_to_minutes)
    

    one_day = 24
    passed_days = int(passed_hours [0]) / one_day
    int_passed_hours = int (passed_hours [0])
    new_hour = int_passed_hours % one_day


    end_hour = new_hour
    end_minutes = int (hours_to_minutes)
    new_time_24_format = '{:02}:{:02}'.format (end_hour, end_minutes)
    passed_days_formatt = '({:.0f} days later)'.format (passed_days)
    
    
    if starting_day is not None:
        final_day = starting_day_to_final_day (starting_day,passed_days)

    
    if end_hour > 12 :
        end_hour = end_hour - 12
        am_pm = 'PM'
                
    elif end_hour == 0 :
        end_hour = end_hour + 12
        am_pm = 'AM'
        
    elif end_hour == 12 :
         am_pm = 'PM'
            
    else :
        am_pm = 'AM'
        


    if starting_day is not None :

        if int (passed_days) == 1 :
            new_time_12_format = '{}:{:02} {},'.format (end_hour, end_minutes,am_pm)
            passed_days_formatt = '(next day)'. format (passed_days)
            final_day = '{} '.format (final_day)
            new_time = new_time_12_format + ' ' + final_day +  passed_days_formatt
        elif int (passed_days) <=1 :
            new_time_12_format = '{}:{:02} {},'.format (end_hour, end_minutes,am_pm)
            new_time = new_time_12_format + ' ' + final_day 
        else :
            new_time_12_format = '{}:{:02} {},'.format (end_hour, end_minutes,am_pm)
            passed_days_formatt = '({:.0f} days later)'.format (passed_days)
            final_day = '{}'.format (final_day)
            new_time = new_time_12_format + ' ' + final_day + ' ' + passed_days_formatt

    else : 
        if int (passed_days) == 1 :
            new_time_12_format = '{}:{:02} {}'.format (end_hour, end_minutes,am_pm)
            passed_days_formatt = '(next day)'. format (passed_days)
            new_time = new_time_12_format + ' ' + passed_days_formatt
        elif int (passed_days) <=1 :
            new_time_12_format = '{}:{:02} {}'.format (end_hour, end_minutes,am_pm)
            new_time = new_time_12_format      
        else :
            new_time_12_format = '{}:{:02} {}'.format (end_hour, end_minutes,am_pm)
            passed_days_formatt = '({:.0f} days later)'.format (passed_days)
            new_time = new_time_12_format + ' ' + passed_days_formatt
    
    return new_time


def starting_day_to_final_day (starting_day, passed_days) :
    week = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday" : 4, "Friday" :5,
            "Saturday": 6,"Sunday" : 0}
    
    key = starting_day.lower().capitalize ()
    starting_day = week [key]
    end_day = int(starting_day) +int(passed_days)
    end_day = end_day % 7

    for key,value in week.items ():
        if value == end_day:
            end_day = key
            end_day = str (key)
    return end_day    
    


def convert_start_time_to_24_hours (start) :
    if start.find('PM') != -1 :
        start = start.replace (' ', ':')
        start = start.split (':')
        start = [int (start[0]), int (start [1])]
        
        hour_to_24 = int (start [0]) 
        hour_to_24 = hour_to_24 + 12
        hour_to_24 = hour_to_24, int (start [1])
    
    else :  
            start = start.replace (' ', ':')
            start = start.split (':')
            hour_to_24 = int (start[0]), int (start [1])   
    
    return hour_to_24           
        


def duration_to_integer (duration) :
    duration = duration.split (':')
    duration = int (duration [0]), int (duration [1])
    
    return duration
