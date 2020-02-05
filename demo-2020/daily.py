import twint
c = twint.Config()

filename = './candidates.txt'

with open(filename, 'r') as f:
  name = f.readline()
  while name:
    name = name.strip()
    print(f"scraping tweets of {name}.")
    c.Username = name
    c.Store_json = True
    c.Output = f"{name}.json"
    twint.run.Search(c)

    print(f"scraping followers of {name}.")
    c.Output = f"{name}_flr.json"
    c.User_full = True
    twint.run.followers(c)

    name = f.readline()