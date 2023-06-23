from django.shortcuts import render
import requests
# Create your views here.

def fetch_auto(query):
    url = f"http://suggestqueries.google.com/complete/search?output=chrome&q={query}"
    r = requests.get(url)
    suggestions = r.json()[1]
    return suggestions

def autocomplete(request):
    query=request.GET.get('query','')
    suggestions=[]

    if query:
        suggestions = fetch_auto(query)

    return render(request,'auto/index.html',{'suggestions':suggestions})
