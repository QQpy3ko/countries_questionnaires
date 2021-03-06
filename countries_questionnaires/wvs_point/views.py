from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

from .models import Question, Choice

from PIL import Image
import base64
import io

# from django.contrib.staticfiles.templatetags.staticfiles import static
# from django.templatetags.static import static
from django.contrib.staticfiles import finders

def wvs_point_test(request):
    
    questions_list = Question.objects.all().order_by('id')

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

            # nonobed, faith = 1 if not picked so its value == 3 in template
            # autonomy_sum >= 6 means obidience and faith are both picked so have to minus them
            # autonomy_sum >= 3 means obidience or faith is picked so have to minus it but add 1 for opposite
            
            autonomy = request.POST.getlist('autonomy')
            autonomy_sum = sum(map(float, autonomy))
            
            if autonomy_sum >= 6.0:
                autonomy_sum -= 6.0

            elif autonomy_sum >= 3.0:
                autonomy_sum -= 2.0

            elif autonomy_sum == 2.0:
                autonomy_sum += 2

            autonomy_sum = autonomy_sum / 4


            # get post_materialist_index from 2 choices
            post_materialist_index = 0

            post_materialist_1 = request.POST.getlist('post_materialist_1')
            post_materialist_2 = request.POST.getlist('post_materialist_2')

            post_materialist_1_sum = sum(map(float, post_materialist_1))
            post_materialist_2_sum = sum(map(float, post_materialist_2))

            if post_materialist_1_sum == 1.0 and post_materialist_2_sum == 1.0:
                post_materialist_index = 1

            elif post_materialist_1_sum == 1 and post_materialist_2_sum == 0:
                post_materialist_index = 0.66

            elif post_materialist_1_sum == 0 and post_materialist_2_sum == 1:
                post_materialist_index = 0.33 

            else:
                post_materialist_index = 0

            survival_self_expr_sum = 0
            traditional_secular_sum = 0


            for question in questions_list:

                if question.question_name == 'autonomy' or \
                    question.question_name == 'post_materialist_1' or \
                    question.question_name == 'post_materialist_2':
                        continue
                if question.question_type == 'traditional_secular':
                    traditional_secular_sum += float(request.POST.get(question.question_name))
                if question.question_type == 'survival_self_expr':
                    survival_self_expr_sum += float(request.POST.get(question.question_name))

            survival_self_expr_sum += post_materialist_index
            traditional_secular_sum += autonomy_sum
            
            # using image size 737x590 px
            # right_padding = 716,5 
            # top_padding = 15 

            left_padding = 65.3
            bottom_minus_padding = 519.3

            scale_length_hor = 651.2
            scale_length_vert = 504.3

            survival_self_expr_scale = survival_self_expr_sum / 5 * scale_length_hor
            traditional_secular_sum_scale = traditional_secular_sum / 5 * scale_length_vert

            center_l_coordinate = int(left_padding + survival_self_expr_scale)
            center_b_coordinate = int(bottom_minus_padding - traditional_secular_sum_scale)

            # wvs_map = Image.open('/mnt/ssd/ProHeGit/ctrs_quess/countries_questionnares/wvs_point/static/wvs_point/vws_map_template.png')
            # point_on_wvs_map = Image.open('/mnt/ssd/ProHeGit/ctrs_quess/countries_questionnares/wvs_point/static/wvs_point/wvs_point_20x20.png')

            wvs_map = Image.open(finders.find('wvs_point/vws_map_template.png'))
            point_on_wvs_map = Image.open(finders.find('wvs_point/wvs_point_20x20.png'))

            half_of_point_img = 10

            point_l_coordinate = center_l_coordinate - half_of_point_img
            point_t_coordinate = center_b_coordinate - half_of_point_img

            wvs_map.paste(
                point_on_wvs_map,
                (point_l_coordinate,
                point_t_coordinate,
                ),
                mask=point_on_wvs_map)
            # show_map = wvs_map.show()

            

            pass       

            response = HttpResponse(content_type='image/png')
            wvs_map.save(response, "PNG")
            # to return as download
            # response['Content-Disposition'] = 'attachment; filename="result.png"'
            return response


            # to  open reuslt in graphical program 

            # return render(
            #     request,
            #     'wvs_point/wvs_point_result.html', 
            #     context={
            #         'response': response
            #     }
            # )




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
    