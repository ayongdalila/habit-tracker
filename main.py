import requests

USERNAME = "ayongdalila"
TOKEN = "SEHIJAUdaun23"

##_________________________________CREATE NEW USER_______________________________________##

create_user_endpoint = "https://pixe.la/v1/users"
create_user_parameter = { 
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# create_user = requests.post(url=create_user_endpoint, json=create_user_parameter)
# print(create_user.text)

##_________________________________VIEW USER PROFILE____________________________________##

# view_profile_endpoint = f"https://pixe.la/@{USERNAME}"
# view_profile = requests.get(url=view_profile_endpoint)

##________________________________CREATE NEW PIXEL GRAPH_________________________________##

create_new_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
create_new_graph_parameter = {
    "id" : "read1",
    "name" : "Number of Pages Read Daily",
    "unit" : "pages",
    "type" : "int",
    "color" : "momiji"

}
create_new_graph_header = {
    "X-USER-TOKEN" : TOKEN
}

# create_new_graph = requests.post(url=create_new_graph_endpoint, json=create_new_graph_parameter, headers=create_new_graph_header)
# print(create_new_graph.text)

##______________________________________POST A PIXEL______________________________________##
graph_id = "read1"

create_new_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"
create_new_pixel_parameter = {
    "date" : "20261126",
    "quantity" : "312" 
}
create_new_pixel_header = {
    "X-USER-TOKEN" : TOKEN
}
# create_new_pixel = requests.post(url=create_new_pixel_endpoint, json=create_new_pixel_parameter, headers=create_new_pixel_header)
# print(create_new_pixel.text)

##______________________________________UPDATE A PIXEL______________________________________##

update_new_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/20261126"
update_new_pixel_parameter = {
    "quantity" : "2000" 
}
update_new_pixel_header = {
    "X-USER-TOKEN" : TOKEN
}
update_new_pixel = requests.put(url=update_new_pixel_endpoint, json=update_new_pixel_parameter, headers=update_new_pixel_header)
print(update_new_pixel.text)
