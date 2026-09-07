# ''''''
# from openai import OpenAI 
# import json
# client = OpenAI()
# def analyse_resuma (user_resuma_text,user_goal):
#     promt = f'''
# your a senior devloper and hairing Manager .
# Evaluat the resuma based on the user's gaol.
# user goal : "{user_goal}"
# STRICT RULES :
# -Excertonly relevent skills for this goal 
# -REMOVE irrelevent tools[excel for backend, etc]
# -identify real gaps
# -Generate roadmap only for missing fileds
# -make output DIFFRENT based on goal
# retun only JSON:
# {{
# "skills":[],
# "missing_skills":[],
# "roadmap":[],
# "interview_questens":[]
# }}
# Resuma:{user_resuma_text}
# '''
#     try :
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             temperature=0.3,
#             messages=[{"role":"system","content":"you're a strict hiring manager."},{"role":"user","content":promt}]
#             )
#         content = response.choices[0].message.content.strip()

#         start = content.find("{")
#         end = content.find("}")
#         return json.loads(content[start:end])
#     except Exception as e:
#         return {
#             "skills":[],
#             "missing_skills":[],
#             "roadmap":[],
#             "interview_questens":[],
#             "error":str(e)
#         }

# ''''''

import spacy
import json

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def analyse_resuma(user_resuma_text, user_goal):
    """
    Analyse resume text locally using spaCy.
    Extract skills, detect missing skills vs goal, and generate roadmap.
    """
    try:
        doc = nlp(user_resuma_text)

        # Extract candidate skills (simple: nouns + proper nouns)
        skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

        # Example: define required skills for the goal
        goal_skills_map = {
            "data analyst": ["Python", "SQL", "Power BI", "Excel", "pandas"],
            "backend developer": ["Python", "Django", "SQL", "APIs", "Git"],
            "network security": ["Linux", "Shell scripting", "SQL", "Grafana"]
        }

        required_skills = goal_skills_map.get(user_goal.lower(), [])

        # Find missing skills
        missing_skills = [s for s in required_skills if s not in skills]

        # Roadmap suggestion (basic)
        roadmap = [f"Learn {s} with hands-on projects" for s in missing_skills]

        # Interview questions (basic placeholders)
        interview_questions = [f"Explain your experience with {s}" for s in required_skills]

        return {
            "skills": list(set(skills)),
            "missing_skills": missing_skills,
            "roadmap": roadmap,
            "interview_questions": interview_questions
        }

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }
