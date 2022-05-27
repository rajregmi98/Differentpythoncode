import wolframalpha

input = input("Question: ")
app_id = "2XGA3Q-G36V5785TE"
clinet = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
