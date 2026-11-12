from tools.travily_tool import travily_search
from tools.flight_tool import search_flights


res = travily_search("Best hotles in India")
print(res)

res = search_flights("Plan a 7 days Nepal trip from India")
print(res)