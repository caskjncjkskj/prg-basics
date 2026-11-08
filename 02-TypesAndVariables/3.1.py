company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees
variables = {
    "company": company,
    "phone": phone,
    "employees": employees,
    "remote_work": remote_work,
    "big_company": big_company,
    "income": income,
    "income_per_person": income_per_person,
}
for name, value in variables.items():
    print(name, value, type(value))
