# =============================================================================================================================
# PYTHON BASICS (DAY-WISE)
# =============================================================================================================================

# =============================================================================================================================
# Day 1 — Variables, Types, Lists, Dictionaries, Loops, Functions (REFERENCE)
# NOTE: Commented out for history so only Day 2 runs today.
# =============================================================================================================================

# # Store an AWS service name as a string
# service_name = "EC2"
# # Store a maximum instance count as an integer
# max_instances = 5
# # Store an instance price as a float
# instance_price = 0.023
# # Store whether we are in production as a boolean
# is_production = True
# # Print the service name
# print("Service:", service_name)
# # Print the max instances
# print("Max instances:", max_instances)
# # Print the price per hour
# print("Price per hour:", instance_price)
# # Print whether this is production
# print("Production environment:", is_production)
# # Print a separator line
# print("\n------------------\n")
# # Create a list of AWS services
# aws_services = ["EC2", "S3", "Lambda", "RDS"]
# # Print a heading
# print("AWS Services:")
# # Loop through the list of services
# for service in aws_services:
#     # Print each service
#     print("-", service)
# # Print a separator line
# print("\n------------------\n")
# # Create a dictionary mapping services to categories
# service_category = {
#     # Map EC2 to Compute
#     "EC2": "Compute",
#     # Map S3 to Storage
#     "S3": "Storage",
#     # Map Lambda to Serverless
#     "Lambda": "Serverless",
#     # Map RDS to Database
#     "RDS": "Database"
# }
# # Print a heading
# print("Service Categories:")
# # Loop through dictionary items (key, value)
# for service, category in service_category.items():
#     # Print service and its category
#     print(service, "->", category)
# # Print a separator line
# print("\n------------------\n")
# # Define a function to print info about a service
# def print_service_info(service_name):
#     # Get the category from the dictionary (or "Unknown" if missing)
#     category = service_category.get(service_name, "Unknown")
#     # Print the service name
#     print("Service:", service_name)
#     # Print the category
#     print("Category:", category)
# # Call the function for EC2
# print_service_info("EC2")
# # Call the function for S3
# print_service_info("S3")
# # Call the function for a service not in the dictionary
# print_service_info("CloudFront")


# =============================================================================================================================
# Day 2 — Conditions + Safe Parsing + Simple Aggregations (ACTIVE)
# =============================================================================================================================

# Print a Day 2 heading so output is clearly separated
print("Day 2 — Conditions + Safe Parsing + Simple Aggregations")
# Print a separator line
print("------------------")

# Create a list of dictionaries representing “cloud instances”
instances = [
    # Define the first instance record
    {"id": "i-001", "state": "running", "type": "t3.micro", "cost_per_hour": "0.0104"},
    # Define the second instance record
    {"id": "i-002", "state": "stopped", "type": "t3.small", "cost_per_hour": "0.0208"},
    # Define the third instance record
    {"id": "i-003", "state": "running", "type": "t3.medium", "cost_per_hour": "0.0416"},
]

# Create a counter for running instances
running_count = 0
# Create a counter for stopped instances
stopped_count = 0
# Create a total cost accumulator (float)
total_cost_per_hour = 0.0

# Loop over each instance dictionary in the list
for instance in instances:
    # Read the instance state from the dictionary
    state = instance["state"]
    # Read the cost per hour string from the dictionary
    cost_str = instance["cost_per_hour"]

    # Safely convert the cost string into a float
    try:
        # Convert the string to float so we can add it
        cost = float(cost_str)
    # Handle cases where conversion fails
    except ValueError:
        # Default to 0.0 if cost is invalid
        cost = 0.0

    # Add cost into the total cost per hour accumulator
    total_cost_per_hour += cost

    # If the instance is running, increment running count
    if state == "running":
        # Increase the running counter by 1
        running_count += 1
    # Otherwise if the instance is stopped, increment stopped count
    elif state == "stopped":
        # Increase the stopped counter by 1
        stopped_count += 1
    # Otherwise handle any other unexpected state
    else:
        # Print a warning for unknown state
        print("Unknown state for instance:", instance["id"], "state:", state)

# Calculate estimated daily cost (24 hours)
estimated_daily_cost = total_cost_per_hour * 24

# Print how many instances are running
print("Running instances:", running_count)
# Print how many instances are stopped
print("Stopped instances:", stopped_count)
# Print total cost per hour
print("Total cost per hour:", total_cost_per_hour)
# Print estimated daily cost
print("Estimated daily cost:", estimated_daily_cost)

# Define a function that labels cost level using simple thresholds
def cost_label(daily_cost):
    # If daily cost is less than 1, label as cheap
    if daily_cost < 1:
        # Return the label
        return "cheap"
    # Else if daily cost is less than 3, label as normal
    elif daily_cost < 3:
        # Return the label
        return "normal"
    # Otherwise label as expensive
    else:
        # Return the label
        return "expensive"

# Compute a label for today’s estimated daily cost
label = cost_label(estimated_daily_cost)
# Print the label result
print("Cost label:", label)

# Create a list of regions with duplicates (common in real logs/config)
regions = ["eu-west-2", "us-east-1", "eu-west-2", "ap-south-1"]
# Convert the list to a set to remove duplicates
unique_regions = set(regions)
# Print unique regions (set order may vary)
print("Unique regions:", unique_regions)
