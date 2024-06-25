import os

line_swaps = {
   "'type':'pairs',":"        'type':['make_items_question_from_pairs'],\n",
   "'type':'correct incorrect',":"        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],\n",
}

def swap_lines(file, line_swaps):
   new_lines = []
   for line in open(file, "r", encoding="utf8").readlines():
      added = False
      for key, value in line_swaps.items():
         if key in line:
            new_lines.append(value)
            added = True
            continue
      if added is False:
         new_lines.append(line)

   with open(f"new_{file}", "w") as f:   
      f.writelines(new_lines)

   

for file in os.listdir():
   if file[-3:]!=".py":
      continue
   swap_lines(file, line_swaps)

   
