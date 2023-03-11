correctInput = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
playerInput = str(input("Write the entire ABC here: ")).lower()
success = 0
failed = 0


# loop through the string
for pos, char in enumerate(playerInput):
  if char == correctInput[pos]:
    success += 1
  else:
    failed += 1

print(f"You entered: {playerInput}. Out of {len(correctInput)} characters you got {success} right and {failed} wrong. That's {round(success/len(correctInput)*100)}%")