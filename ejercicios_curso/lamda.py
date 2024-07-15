def run():
  palindrome = lambda string: string == string[::-1]

  print(palindrome('ana'))


if __name__ =='__main__':
  run()