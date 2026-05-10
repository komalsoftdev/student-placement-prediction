from flask import Flask, render_template, request
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("student_placement_synthetic.csv")

df = df.drop('salary_package_lpa', axis=1)

df_encoded = pd.get_dummies(df, drop_first=True)

# =====================================
# FEATURES & TARGET
# =====================================

X = df_encoded.drop('placement_status', axis=1)

y = df_encoded['placement_status']

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# SCALING
# =====================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# =====================================
# TRAIN MODEL
# =====================================

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# =====================================
# SKILL REQUIREMENTS
# =====================================

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

# =====================================
# HOME ROUTE
# =====================================

@app.route('/')

def home():

    return render_template('index.html')

# =====================================
# PREDICTION ROUTE
# =====================================

@app.route('/predict', methods=['POST'])

def predict():

    cgpa = float(request.form['cgpa'])
    coding_skills = int(request.form['coding_skills'])
    dsa_score = int(request.form['dsa_score'])
    aptitude_score = int(request.form['aptitude_score'])
    communication_skills = int(
        request.form['communication_skills']
    )
    internships = int(request.form['internships'])
    projects_count = int(request.form['projects_count'])
    certifications = int(request.form['certifications'])
    hackathons = int(request.form['hackathons'])
    open_source_contributions = int(
        request.form['open_source_contributions']
    )

    target_role = request.form['target_role']

    student_skills = request.form['student_skills']

    student_skill_list = student_skills.split(',')

    student_skill_list = [
        skill.strip()
        for skill in student_skill_list
    ]

    # =================================
    # INPUT DATAFRAME
    # =================================
    input_data = pd.DataFrame({

    'cgpa': [cgpa],
    'backlogs': [0],
    'coding_skills': [coding_skills],
    'dsa_score': [dsa_score],
    'aptitude_score': [aptitude_score],
    'communication_skills': [
        communication_skills
    ],
    'ml_knowledge': [5],
    'system_design': [5],
    'internships': [internships],
    'projects_count': [projects_count],
    'certifications': [certifications],
    'hackathons': [hackathons],
    'open_source_contributions': [
        open_source_contributions
    ],
    'extracurriculars': [1],

    # EXACT SAME FEATURES
    # AS TRAINING DATASET

    'branch_Chemical': [0],
    'branch_CSE': [1],
    'branch_ECE': [0],
    'branch_EE': [0],
    'branch_IT': [0],
    'branch_ME': [0],

    'college_tier_Tier-2': [1],
    'college_tier_Tier-3': [0]

})
   

    # =================================
    # SCALE DATA
    # =================================
    # Match exact training columns

    input_data = input_data.reindex(
    columns=X.columns,
    fill_value=0
)

    input_scaled = scaler.transform(input_data)

    # =================================
    # PREDICTION
    # =================================

    prediction = model.predict(input_scaled)

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    # =================================
    # SKILL GAP ANALYSIS
    # =================================

    missing_skills = []

    for skill in required_skills[target_role]:

        if skill not in student_skill_list:

            missing_skills.append(skill)

    # =================================
    # RESULT
    # =================================

    if prediction[0] == 1:

        result = "Likely To Be Placed"

    else:

        result = "Less Chances Of Placement"

    return render_template(
        'index.html',
        prediction_text=result,
        probability=round(probability * 100, 2),
        missing_skills=missing_skills,
        target_role=target_role
    )

# =====================================
# RUN APP
# =====================================

if __name__ == '__main__':

    app.run(debug=True)