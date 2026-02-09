import json
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    with open(csv_file, 'w') as f:
        # Write the header
        header = ['name', 'username', 'organisationUnits', 'userRoles']
        f.write(','.join(header) + '\n')

    #     # Write the data
        for item in data["users"]:
            #row = [str(item[key]) for key in header]
            #f.write(','.join(row) + '\n') 
            name = item["name"]
            username = item["username"]
            orgUnits = item["organisationUnits"][0]["name"] if item["organisationUnits"] else "None"
            roles = item["userRoles"][0]["name"] if item["userRoles"] else "None"
            
            row = [name, username, orgUnits, roles]
            f.write(','.join(row) + '\n')

# Example usage
json_to_csv('response.json', 'response.csv')