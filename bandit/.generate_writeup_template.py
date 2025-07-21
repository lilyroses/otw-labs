import sys



def create_template_file(level_start, level_end):

  URL = f"https://overthewire.org/wargames/bandit{level_start}.html"
  URL_TEXT = f"Level {level_start}-{level_end} Page"
  TITLE = f"# Bandit Level {level_start}-{level_end} Write-Up"
  PATH = "./write_ups"
  FILENAME = f"{level_start}-{level_end}.md"
  FILEPATH = f"{PATH}/{FILENAME}"

  template_text = f"""{TITLE}

---

## About

[{URL_TEXT}]({URL})

[...]

---

## Steps

1. Log into the server:

*If you followed the shortcut instructions in `pre-req.md`:*

`$ ssh bandit{level_start}@otw`


*If not:*

`$ ssh bandit{level_start}@bandit.labs.overthewire.org -p 2220`


2.   [...]

[`command`]


4.  Copy the password and log out of the server:

`Ctrl-D`


---

## Commands & Tactics Used

---

### Commands

1. [...]

---

### Tactics

1.  [...]
"""


  with open(FILEPATH, "w") as f:
    f.write(template_text)


  print(f"\n{FILEPATH} successfully created.")


if __name__ == "__main__":
  level_start, level_end = sys.argv[1:]
  create_template_file(level_start, level_end)
