from django.shortcuts import render
from rest_framework.views import APIView
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.response import Response
from getCoverage import getCoverage
from models import CustomUser


def logout_view(request):
    logout(request)
    return redirect('http://localhost:3000')


class ResumeSubmit(APIView):
    def post(self, request, *args, **kwargs):

        data = json.loads(request.body.decode('utf-8'))

        user = request.user
        # workExperience =
        # porjects =
        # certifications =
        # technicalSkills =
        # educationalDetails =

        features, postModel = pickle.load(open('classify.pkl', 'wb'))
        test_data = []
        for i in features:
            if i in technicalSkills:
                test_data.append(1)
            else:
                test_data.append(0)
        df = pd.DataFrame(test_data, columns=features)
        classes = postModel.classes_
        pred_list = postModel.predict_proba(df)
        res = [{"class": classes[i], "prob": pred_list[i]}
               for i in range(len(classes))]
        res = sorted(res, key=lambda x: res["prob"], reverse=True)[:4]

        user.technicalSkills = json.dumps(technicalSkills)
        user.workExperience = json.dumps(workExperience)
        user.projects = json.dumps(porjects)
        user.certifications = json.dumps(certifications)
        user.possiblePost = json.dumps(res)
        user.educationalDetails = json.dumps(educationalDetails)
        return Respnse({'success': True}, status=status.HTTP_200_OK)

    # def get(self, request, *args, **kwargs):

    #     skills.recommendation =

class SearchQuery(APIView):
    def post(self, request, *args, **kwargs):
        """
        Fetch form data
        """
        data = json.loads(request.body.decode('utf-8'))

        user = request.user
        # workExperience =
        # porjects =
        # certifications =
        # technicalSkills =
        # educationalDetails =

        query_dict = {}

        all_users = CustomUser.objects.filter(recruiter=False)
        coverage_list = []
        for user in all_users:
            coverage = getCoverage(user, query_dict)
            if coverage['coverage'] > 0:
                coverage_list.append(coverage)
        coverage_list = sorted(coverage_list, key = lambda x : x['coverage'], reverse=True)

        return Response({
            "applicants": coverage_list
        })


    # def get(self, request, *args, **kwargs):
