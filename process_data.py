import json

train_file = "train.json"
valid_file = "valid.json"
context_file = "context.json"

span_train_file = "train_span.json"
span_valid_file = "valid_span.json"

with open(train_file, 'r') as file:
    train = json.load(file)
with open(valid_file, 'r') as file:
    valid = json.load(file)
with open(context_file, 'r') as file:
    context = json.load(file)

train_list = []
for i in train:
    dictionary = {
        "id": i["id"],
        "question": i["question"],
        "context": context[i["relevant"]],
        "answers": {'answer_start': [i["answer"]["start"]], 'text': [i["answer"]["text"]]},
    }
    train_list.append(dictionary)

with open(span_train_file, "w", encoding="utf8") as outfile:
    json.dump(train_list, outfile, ensure_ascii=False, indent=4)

valid_list = []
for i in valid:
    dictionary = {
        "id": i["id"],
        "question": i["question"],
        "context": context[i["relevant"]],
        "answers": {'answer_start': [i["answer"]["start"]], 'text': [i["answer"]["text"]]},
    }
    valid_list.append(dictionary)

with open(span_valid_file, "w", encoding="utf8") as outfile:
    json.dump(valid_list, outfile, ensure_ascii=False, indent=4)