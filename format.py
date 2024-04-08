def convert_to_hyphen_separated(text):
  """Converts a string to hyphen-separated words.

  Args:
    text: The input string.

  Returns:
    The string with spaces replaced by hyphens.
  """
  return text.lower().replace(" ", "-")

# Example usage
text = input("Input text: \n")
hyphen_separated_text = convert_to_hyphen_separated(text)
print(hyphen_separated_text)
