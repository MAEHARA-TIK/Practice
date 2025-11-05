from django.shortcuts import render
from .models import Calculation

def index(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        op = request.POST.get("op")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "エラー (0で割れない)"

        expression = f"{num1} {op} {num2}"
        Calculation.objects.create(expression=expression, result=str(result))

    history = Calculation.objects.order_by("-created_at")[:10]  # 最新10件
    return render(request, "calculator/index.html", {"result": result, "history": history})

