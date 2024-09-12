import requests


print("hello world")
response = requests.get(url="https://vi.wikipedia.org/wiki/S%E1%BB%B1_ki%E1%BB%87n_b%C3%A1n_non_c%E1%BB%95_phi%E1%BA%BFu_GameStop")
with open('response.html', "w") as f:
    f.write(response.text)