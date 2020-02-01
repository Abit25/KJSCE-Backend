from models import Weightage
import json
"""
{
    "job": ["Web Developer", ...],
    "skills: ["sql","django"....],
    "work_experience" : 2, #mean 2 >= years
    "education" : "Postgraduate",
}
"""
def getCoverage(user, requirement_filter):
    coverage_score = 0

    weights = Weightage.objects.get(user = user)
    user_skills = json.loads(user.technicalSkills)
    educational_details = json.loads(user.educationalDetails)
    workExperience = json.loads(user.workExperience)
    projects = json.loads(user.projects)
    certifications = json.loads(user.certifications)
    possiblePost = json.loads(user.possiblePost)

    intersect = list(set(requirement_filter['job']) & set(possiblePost.keys()))


    """
    ADD EDUCATIONAL DETAILS CONSIDERATION
    """

    if len(intersect) > 0 :
        for post in intersect:
            coverage_score = coverage_score + possiblePost[post]

        skill_match = 0
        experience_match = 0
        project_match = 0
        for skill in requirement_filter['skills']:
            if skill in user_skills:
                skill_match += 1
        skill_match = skill_match / len(requirement_filter["skills"])
        coverage_score = coverage_score + skill_match


        experience_match = 0
        chosenExperience = []
        for post in workExperience:
            skill_in_post = 0
            for skill in requirement_filter['skills']:
                if skill in post['description']:
                    skill_in_post += 1
            if skill_in_post > 0:
                chosenExperience.append(post)
        experience_match = len(chosenExperience)
        coverage_score = coverage_score + experience_match*weights.workExperience

        project_match = 0
        chosenProject = []
        for proj in projects:
            skill_in_proj = 0
            for skill in requirement_filter['skills']:
                if skill in proj['description']:
                    skill_in_post += 1
            if skill_in_post > 0:
                chosenProject.append(post)
        project_match = len(chosenProject)
        coverage_score = coverage_score + project_match*weights.projects

        certification_match = 0
        chosenCertification = []
        for certificate in certification:
            skill_in_cert = 0
            for skill in requirement_filter['skills']:
                if skill in certificate['description']:
                    skill_in_cert += 1
            if skill_in_cert > 0:
                chosenCertification.append(certificate)
        certification_match = len(chosenCertification)
        coverage_score = coverage_score + certification_match*weights.certification

        return {
            "chosenExperience": chosenExperience,
            "chosenProjects": chosenProject,
            "chosenCertification": chosenCertification,
            "coverage": coverage_score
        }
    return {"coverage": 0}

