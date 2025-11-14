#BMI = Body Mass I ndex(Measure of height and weight to estimate body fat %)
#general estimate that doesn't account muscle vs fat
#children have a different BMI chart

weight = float(input ("Enter your weight in kilograms: "))
height = float(input ("Enter your height in meters: "))

#BMI = weight(lbs/kg) / height(in/m)^2
bmi = weight / height **2

print(f"Your BMI is: {bmi:.1f}")

#categories BMI
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
