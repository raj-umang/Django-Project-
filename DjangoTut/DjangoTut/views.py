from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter


# Create your views here.

def table_of_squares(request, s, n):
    result=""
    for i in range(1, n+1):
        result += "<p>"+ str(s) + "*" + str(i)+ "=" +str((s*i))+ "</p>"
    return HttpResponse(result)

def greet(request, user):
    uname = user
    d={'user':user}
    return render(request, 'greet.html',d)
def hello(request):
    resp="<h1> Hello World </h1>"
    return HttpResponse(resp)
def squares(request, num1, num2):
    squares = [(i, i**2) for i in range(num1, num2+1)]
    return render(request, 'squares.html', {'squares': squares})
def book_list(request):
    books = [
        {
            'title': 'Book 1',
            'author': 'Author 1',
            'reviews': [
                {'review_text': 'Review 1', 'rating': 5},
                {'review_text': 'Review 2', 'rating': 4},
            ]
        },
        {
            'title': 'Book 2',
            'author': 'Author 2',
            'reviews': [
                {'review_text': 'Review 3', 'rating': 5},
                {'review_text': 'Review 4', 'rating': 3},
            ]
        },
    ]
    return render(request, 'book_list.html', {'books': books})
def find_mode(request, numbers):
    # Split the numbers from the URL and convert them to integers
    num_list = list(map(int, numbers.split(',')))
    # Calculate the frequency of each number
    num_counts = Counter(num_list)
    # Find the number(s) with the highest frequency
    max_occurrence = max(num_counts.values())
    modes = [num for num, occ in num_counts.items() if occ == max_occurrence]
    
    # Prepare the response
    response_text = ', '.join(f"{mode} occurred {max_occurrence} times" for mode in modes)
    
    return HttpResponse(response_text)


def showlist(request): 
    fruits=["Mango","Apple","Bananan","Jackfruits"] 
    student_names=["Tony","Mony","Sony","Bob"] 
    return render(request,'showlist.html',{"fruits":fruits,"student_names":student_names})


def home(request):
    return render(request,'home.html')