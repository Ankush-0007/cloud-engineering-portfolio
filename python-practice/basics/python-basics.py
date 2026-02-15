# =========================
# PYTHON BASICS
# =========================

# -------- Day 1 --------
# Variables, Data Types, Lists, Dictionaries, Loops, Functions
# Cloud-focused examples (AWS services)


# 1️⃣ Variables and Data Types

service_name = "EC2"          # string
max_instances = 5             # integer
instance_price = 0.023        # float
is_production = True          # boolean

print("Service:", service_name)
print("Max instances:", max_instances)
print("Price per hour:", instance_price)
print("Production environment:", is_production)


print("\n------------------\n")


# 2️⃣ Lists

aws_services = ["EC2", "S3", "Lambda", "RDS"]

print("AWS Services:")
for service in aws_services:
    print("-", service)


print("\n------------------\n")


# 3️⃣ Dictionaries

service_category = {
    "EC2": "Compute",
    "S3": "Storage",
    "Lambda": "Serverless",
    "RDS": "Database"
}

print("Service Categories:")
for service, category in service_category.items():
    print(service, "->", category)


print("\n------------------\n")


# 4️⃣ Simple Function

def print_service_info(service_name):
    category = service_category.get(service_name, "Unknown")
    print("Service:", service_name)
    print("Category:", category)


print_service_info("EC2")
print_service_info("S3")
print_service_info("CloudFront")   # not in dictionary
