# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
from django.http import HttpRequest
from utils import QuadraticEquation

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    not_spec = 'коэффициент не определен'
    not_int = 'коэффициент не целое число'
    not_null = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    discr = 'Дискриминант: %d'
    dis_less_null = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    dis_eq_null = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %g'
    two_roots = 'Квадратное уравнение имеет два действительных корня: x1 = %g, x2 = %g'
    empty_str = ''
    site_view = {
        'head_line': 'Квадратное уравнение a*x*x + b*y + c = 0',
        'a_str': 'a = %s' % a,
        'comment_a': empty_str,
        'b_str': 'b = %s' % b,
        'comment_b': empty_str,
        'c_str': 'c = %s' % c,
        'comment_c': empty_str,
        #'comment_discr': discr % 144,
        'comment_discr': empty_str,
        #'comment_result': two_roots % (2.5, 3.4),
        'comment_result': empty_str,
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
            x2 = qe.get_eq_root(order=2)
            if x1 == x2:
                res_mes = dis_eq_null % x1
            else:
                res_mes = two_roots % (x1, x2)
        site_view['comment_result'] = res_mes
    else:
        site_view['comment_a'] = chk_gigit_a(a)[0]
        site_view['comment_b'] = chk_gigit(b)[0]
        site_view['comment_c'] = chk_gigit(c)[0]

    return render(request, 'results.html', site_view)