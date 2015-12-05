# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
from django.http import HttpRequest
from quadratic.utils import QuadraticEquation
from quadratic.forms import QuadraticForm


def quadratic_results(request):

    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    not_spec = 'коэффициент не определен'
    not_int = 'коэффициент не целое число'
    not_null = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    discr = 'Дискриминант: %d'
    dis_less_null = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    dis_eq_null = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s'
    two_roots = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s'
    empty_str = ''
    form = QuadraticForm()
    print request.POST

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuadraticForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print 'is valid'
            # process the data in form.cleaned_data as required
            # ...
            # messages for success form data:
            #messages.success(request, 'Form is saved!')
            # redirect to a new URL:
            #return redirect('/thanks/')  # redirect возвращает код 302 вместо 200

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            print 'Get is valid'
        else:
            form = QuadraticForm(request.GET)

    
    site_view = {
        'head_line': 'Квадратное уравнение a*x*x + b*y + c = 0',
        'a_str': 'a = %s' % a,
        'comment_a': empty_str,
        'b_str': 'b = %s' % b,
        'comment_b': empty_str,
        'c_str': 'c = %s' % c,
        'comment_c': empty_str,
        'comment_discr': empty_str,
        'comment_result': empty_str,
        'form': form,
    }
    
    def chk_gigit(d='', dig=False):
        if not d:
            ret = not_spec
        elif not re.match(r'^-?\d+', d):
            ret = not_int
        else:
            ret = empty_str
            dig = True
        return [ret, dig]
    
    def chk_gigit_a(a='', dig=False):
        if a.isdigit() and int(a) == 0:
            ret = not_null
            dig = False
        else:
            ret = chk_gigit(a)[0]
            dig = chk_gigit(a)[1]
        return [ret, dig]
    
    if chk_gigit_a(a)[1] and chk_gigit(b)[1] and chk_gigit(c)[1]:
        qe =  QuadraticEquation(int(a), int(b), int(c)) 
        dsc = qe.get_discr()
        site_view['comment_discr'] = discr % dsc
        if dsc < 0:
            res_mes = dis_less_null
        else:
            x1 = qe.get_eq_root()
            print x1
            x2 = qe.get_eq_root(order=2)
            print x1
            if x1 == x2:
                res_mes = dis_eq_null % round(x1,1)
            else:
                res_mes = two_roots % (round(x1,1), round(x2,1))
        site_view['comment_result'] = res_mes
    else:
        site_view['comment_a'] = chk_gigit_a(a)[0]
        site_view['comment_b'] = chk_gigit(b)[0]
        site_view['comment_c'] = chk_gigit(c)[0]

    return render(request, 'quadratic/results.html', site_view)
