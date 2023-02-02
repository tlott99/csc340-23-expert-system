import json

class Expert:
    def __init__(self, kb_path, dialogue_path):
        self.kb_path = kb_path
        self.dialogue_path = dialogue_path
        with open(self.kb_path) as kb_file:
            self.kb = json.load(kb_file)
        with open(self.dialogue_path) as d_file:
            self.dialogue = json.load(d_file)

    def start(self):
        keep_going = True
        has_contributed = False
        print(self.dialogue["intro"])
        while keep_going:
            r1 = input(f'{self.dialogue["q1"]}\n').lower()
            r2 = input(f'{self.dialogue["q2"]}\n')
            fruit_key = f"{r1}-{r2}"
            fruit_value = self.kb.get(fruit_key)
            if fruit_value: 
                print(f'\n{self.dialogue["conclusion"]} {fruit_value.get("name")}.\n')
            else:
                new_fruit = input(f'\n{self.dialogue["not_found"]}\n').lower()
                self.kb[fruit_key] = {"name": new_fruit}
                with open(self.kb_path, 'w') as kb_file:
                    json.dump(self.kb, kb_file)
                has_contributed = True

            



            keep_going = input(f'{self.dialogue["repeat"]}\n').upper()[0] == "Y"
            if has_contributed:
                print(self.dialogue["contribution"])

def main():
    pass

if __name__ == "__main__":
    main()