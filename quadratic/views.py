# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
from django.http import HttpRequest
from quadratic.utils import QuadraticEquation
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    discr = 'Дискриминант: %d'
    dis_less_null = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    dis_eq_null = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s'
    two_roots = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s'
    empty_str = ''
    comment_dsc = empty_str
    comment_result = empty_str
    
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            got_data = form.cleaned_data
            qe =  QuadraticEquation(got_data) 
            dsc = qe.get_discr()
            print int(dsc) 
            if dsc > 0:
                x1 = qe.get_eq_root()
                x2 = qe.get_eq_root(order=2)
                comment_dsc = discr % dsc
                comment_result = two_roots % (round(x1,1), round(x2,1))
            elif dsc < 0:
                comment_dsc = discr % dsc
                comment_result = dis_less_null
            elif dsc == 0:
                x1 = qe.get_eq_root()
                comment_dsc = discr % dsc
                comment_result = dis_eq_null % round(x1,1)
        else:
            form = QuadraticForm(request.GET)
    else:
        form = QuadraticForm()

    site_view = {
        'comment_discr': comment_dsc,
        'comment_result': comment_result,
        'form': form,
    }
    

    return render(request, 'quadratic/results.html', site_view)
