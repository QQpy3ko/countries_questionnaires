from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

from .models import Question, Choice

from PIL import Image


def wvs_point_test(request):
    
    questions_list = Question.objects.all()

    if request.method == 'POST':

        try:
            for question in questions_list:

                check_if_answered = request.POST[question.question_name]
                


        except (KeyError, Choice.DoesNotExist):
            return render(request,
                 'wvs_point/wvs_point_test.html', 
                 {
                     'error_message': "You haven't anwser all questions.",
                     'questions_list': questions_list,
                 }
                 )

        else:

            autonomy = request.POST.getlist('autonomy')
            autonomy_sum = sum(map(float, autonomy))

            # because nonobed = 1 if not picked so its value == 3 in template
            if autonomy_sum >= 3.0:
                autonomy_sum -= 3.0

            elif autonomy_sum == 2.0:
                autonomy_sum += 1

            emancipative_sum = 0
            secular_sum = 0

            #####add voice1, voice2 to loop!
            for question in questions_list:
                if question.question_name == 'autonomy':
                    continue
                if question.question_type == 'secular'
                    secular_sum += request.POST[question.question_name]
                if question.question_type == 'emancipative'
                    emancipative_sum += request.POST[question.question_name]


            emancipative_sum += autonomy_sum

            left_padding = 65.3
            bottom_padding = 519.3
            center_l_coordinate = left_padding + emancipative_sum
            center_b_coordinate = bottom_padding + secular_sum

            point_length = 20
            point_height = 20

            wvs_map = Image.open('/mnt/ssd/ProHeGit/ctrs_quess/countries_questionnares/wvs_point/static/wvs_point/vws_map_template.png')
            point_on_wvs_map = Image.open('/mnt/ssd/ProHeGit/ctrs_quess/countries_questionnares/wvs_point/static/wvs_point/wvs_point_20x20.png')

            wvs_map.paste(
                point_on_wvs_map,
                (
                point_l_coordinate = center_l_coordinate - point_length
                point_t_coordinate = center_b_coordinate + point_height
                point_r_coordinate = center_l_coordinate + point_length
                point_b_coordinate = center_b_coordinate - point_height
                ),
                mask=point_on_wvs_map)
            show_map = wvs_map.show()

            pass       

            return render(
                request,
                'wvs_point/wvs_point_result.html', 
                context={
                    'autonomy_sum': autonomy_sum,
                    'show_map': show_map
                }
            )

    ### for GET-request
    return render(
        request,
        'wvs_point/wvs_point_test.html', 
        context={

            'questions_list': questions_list

        }
    )


def wvs_point_about(request):
    return render(request, 'wvs_point/wvs_test_about.html')


def wvs_point_result(request):
    return render(request, 'wvs_point/wvs_point_result.html')
    