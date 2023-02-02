from expert import Expert

def main():
    print("Testing, I'm in main.")
    e1 = Expert('data/kb_new.json','data/dialogue_new.json')
    e1.start()

if __name__ == "__main__":
    main()