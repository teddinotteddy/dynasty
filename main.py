from functions import Text
from functions import Data


# Rename Classes
data = Data()
text = Text()

# Setup Data
data.reset_data()

# Setup
text.write(data.pull(data.read("context"), 0))
text.wait(5)

# Asks the questions
for i in range(data.list_length(data.read("questions"))):
    answer, number = text.ask()
    data.update_stats(answer, number)
    text.result(answer, number)
    data.check_stats()

text.write(data.pull(data.read("context"), 1))
