def convert_number_base(number, base):
  """Converts the number from decimal system to a numeral system with given base. Returns a list of with each element representing one digit"""
  arr = []
  number_to_convert = number
  req_bytes = math.floor(math.log(number_to_convert, base))
  for i in range(req_bytes, -1, -1):
    arr.append(number_to_convert // base ** i)
    number_to_convert -= base ** i * (number_to_convert // base ** i)
  return arr
