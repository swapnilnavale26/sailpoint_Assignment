import requests
import datetime
from prettytable import PrettyTable


# function to format date
def get_date_days_ago(days_ago):
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=days_ago)
    print("Date range selected: ", last_week, " to ", today)
    return last_week


last_date = get_date_days_ago(8)


# function to display email content
def print_mail(sender, receiver):
    print("FROM: ", sender)
    print("TO: ", receiver)
    print("SUBJECT: ", "Pull request summary from", last_date.__str__(), " to ", datetime.date.today().__str__())
    print("BODY: \nPlease find below pull request summary:\n", table)


# Create table to store the summery fields from the API response
table = PrettyTable()
table.field_names = ["Request Status", "Created Date", "Title", "user", "url"]

# search for the pull request from random public github repository
api_url = f"https://api.github.com/repos/ange-yaghi/engine-sim/pulls?state=all"

print("The github url used is: " + api_url)

# send get request
response = requests.get(api_url)

# get the json data
data = response.json()


is_data = False
for pull_request in range(len(data)):

    state = data[pull_request]["state"]
    created_date_str = data[pull_request]["created_at"]
    created_date = datetime.datetime.strptime(created_date_str, '%Y-%m-%dT%H:%M:%SZ').date()
    if created_date >= last_date:
        is_data = True
        Title = data[pull_request]["title"]
        user = data[pull_request]["user"]["login"]
        url = data[pull_request]["url"]
        table.add_row([state, created_date_str, Title, user, url])
if not is_data:
    print("Sorry! there is no pull request between selected date range.")
from_email = "from@gmail.com"
to_email = "to@gmail.com"

if is_data:
    print_mail(from_email, to_email)
