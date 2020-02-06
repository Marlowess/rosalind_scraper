from request_handler import Request_handler

if __name__ == '__main__':
  handler = Request_handler() 

  while True:
    print('What chapter do you wanna read? -1 to exit, -2 to see the summary')
    chap = input()
    if chap == '-1':
      print('Got it, see you!')
      exit(0)
    elif chap == '-2':
      handler.print_chapters()
      print('***************************************************************')
      continue 
    handler.read_chapter(int(chap))
    print('***************************************************************')
    
