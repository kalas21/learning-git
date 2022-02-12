import datetime

def calculate_and_decide_time_to_show():
    time_till = deadline_date - today_date

    time_till_in_secs = int(time_till.total_seconds())
    time_till_in_mins = int(time_till.total_seconds() / 60)
    time_till_in_hrs = int(time_till.total_seconds() / 60 / 60)
    time_till_in_days = int(time_till.total_seconds() / 60 / 60 / 24)

    if time_till_in_hrs < 48 and time_till_in_hrs >= 0:  # 0-2days
        return f'{time_till_in_mins} minutes'
    elif time_till_in_hrs < 96 and time_till_in_hrs >= 48:  # 2-4days
        return f'{time_till_in_hrs} hours'
    elif time_till_in_hrs >= 96:
        return f'{time_till_in_days} days'


user_input = ""
while user_input != "exit":
    user_input = input("Enter your goal with a deadline separated by colon\n")
    input_list = user_input.split(":")

    goal = input_list[0]
    deadline = input_list[1]

    deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
    today_date = datetime.datetime.today()


    if deadline_date > today_date:
        time_left_for_deadline = calculate_and_decide_time_to_show()
        print(f'Dear user time remaining for your goal: {goal} is {time_left_for_deadline}')

    else:
        print("Deadline for goal can't be a value previous than current time")


