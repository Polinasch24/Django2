from django.http import HttpResponse
from django.shortcuts import render


def home_page(request,dish):
    template_name = 'cookbook/home.html'
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }

    if request.GET.get('servings') != None:
        res=int(request.GET.get('servings'))
        recipes = {}
        for ind,amount in DATA[dish].items():
            amount_q=amount*res
            recipes.setdefault(ind,amount_q)
        context = {'dish': recipes}
    else:
        context= {'dish': DATA[dish]}

    return render(request, template_name=template_name, context=context)