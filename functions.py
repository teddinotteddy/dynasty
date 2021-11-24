import json
import time
import random


# All Data Commands
class Data:

    @staticmethod
    def read(key):
        with open("data.json", "r") as f:
            data = json.load(f)

        return data[key]

    @staticmethod
    def pull(context, number):
        array = context

        return array[number]

    @staticmethod
    def list_random(context):
        array = context
        product = []

        for i in range(len(array)):
            product.append(i - 1)

        return random.choice(product)

    @staticmethod
    def list_length(context):
        array = context

        return len(array)

    @staticmethod
    def read_stat(stat):
        with open("data.json", "r") as f:
            data = json.load(f)

        return data["stats"][stat]

    @staticmethod
    def update_stats(result, number):
        all_stats = ["people", "army", "money"]

        for i in range(len(all_stats)):
            with open("data.json", "r") as f:
                data = json.load(f)

            stat = all_stats[i - 1]
            current_stat = data["stats"][stat]
            update_stat = data[f"result data {result}"][number][stat]
            new_stat = current_stat + update_stat

            data["stats"][stat] = new_stat

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

    @staticmethod
    def check_stats():
        all_stats = ["people", "army", "money"]

        for i in range(len(all_stats)):
            with open("data.json", "r") as f:
                data = json.load(f)

            stat = all_stats[i - 1]
            current_stat = data["stats"][stat]

            if current_stat == 0 or current_stat > 0:
                if current_stat == all_stats[0]:
                    Text.write(Data.pull(Data.read("endings"), 0))
                elif current_stat == all_stats[1]:
                    Text.write(Data.pull(Data.read("endings"), 1))
                elif current_stat == all_stats[2]:
                    Text.write(Data.pull(Data.read("endings"), 2))

    @staticmethod
    def reset_data():
        stats = {
            "people": 50,
            "army": 50,
            "money": 50
        }

        with open("data.json",  "r") as f:
            data = json.load(f)

        data["stats"] = stats

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)


# All Text Based Commands
class Text:

    @staticmethod
    def write(sentence):
        letters = list(sentence)
        length = len(letters)
        total_length = length - 1

        for i in range(length):
            if total_length == i:
                print(letters[i])
            else:
                print(letters[i], end="", flush=True)

            if "." in letters[i]:
                time.sleep(.15)
            elif "!" in letters[i]:
                time.sleep(.15)
            elif "?" in letters[i]:
                time.sleep(.15)
            else:
                time.sleep(.1)

    @staticmethod
    def wait(seconds):
        for i in range(seconds):
            print(".")
            time.sleep(1)

    @staticmethod
    def ask():
        number = Data.list_random(Data.read("questions"))

        Text.write(Data.pull(Data.read("questions"), number) + " [Y]/[N]")

        output = input("> ")

        return output, number

    @staticmethod
    def result(context, number):
        Text.write(Data.pull(Data.read("result " + context), number))
        Text.write(
            "People: " + str(Data.read_stat("people")) + " Army: " + str(Data.read_stat("army")) + " Money: " + str(Data.read_stat("money"))
        )
