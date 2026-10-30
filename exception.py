def validate(age):
    if age >= 18:
        print("Eligible for voting")
    else:
        raise valueError("age must be greater than 18")
age = int(input())
validate(age)