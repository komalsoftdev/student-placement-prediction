# =========================================
# STUDENT SKILL GAP ANALYZER
# =========================================

# Required Skills for Different Roles

required_skills = {

    "Data Analyst": [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Statistics"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "SQL"
    ],

    "Backend Developer": [
        "Java",
        "SQL",
        "API",
        "System Design",
        "Git"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ]
}

# =========================================
# USER INPUT
# =========================================

print("Available Roles:")

for role in required_skills:
    print("-", role)

# Take target role input
target_role = input("\nEnter Target Role: ")

# Take student skills input
student_skills = input(
    "Enter Your Skills (comma separated): "
)

# =========================================
# PROCESS USER SKILLS
# =========================================

# Convert skills into list
student_skills = student_skills.split(",")

# Remove extra spaces
student_skills = [
    skill.strip()
    for skill in student_skills
]

# =========================================
# FIND MISSING SKILLS
# =========================================

missing_skills = []

for skill in required_skills[target_role]:

    if skill not in student_skills:

        missing_skills.append(skill)

# =========================================
# DISPLAY RESULTS
# =========================================

print("\n===================================")
print("      SKILL GAP ANALYSIS")
print("===================================")

print("\nTarget Role:")
print(target_role)

print("\nYour Skills:")
print(student_skills)

print("\nMissing Skills:")

if len(missing_skills) == 0:

    print("No missing skills detected.")
    print("You are well prepared for this role.")

else:

    for skill in missing_skills:
        print("-", skill)

# =========================================
# CAREER SUGGESTIONS
# =========================================

print("\n===================================")
print("      RECOMMENDATIONS")
print("===================================")

if len(missing_skills) > 0:

    print("\nSuggested Skills To Learn:")

    for skill in missing_skills:
        print("-> Learn", skill)

else:

    print("\nKeep improving through projects and internships.")

print("\nSkill Gap Analysis Completed Successfully.")