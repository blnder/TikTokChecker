import colorama, requests, random, string, time, pystyle
import os

"""
Upcoming
- Faster Processing
- Faster Dumping

Fixing
- Not adding COMPLETE list of unadded randomized strings

"""

headers = {
           'accept'             : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image',
           'accept-language'    : 'en-US,en;q=0.9',
           'cache-control'      : 'max-age=0',
           'sec-ch-ua'          : '" Not A;Brand";v="99", "Chromium";v="98", "Opera GX";v="84"',
           'sec-ch-ua-mobile'   : '?0',
           'sec-ch-ua-platform' : '"Windows"',
           'sec-fetch-dest'     : 'document',
           'sec-fetch-mode'     : 'navigate',
           'sec-fetch-site'     : 'none',
           'sec-fetch-user'     : '?1',
           'upgrade-insecure-requests': '1',
           'user-agent'         : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.36'
}

if int(len(open('tiktok/data/usernames', 'r').readlines())) > 0:
   os.system('clear')
   os


   clear_file = input('[%s@%s] Clear Previous Usernames [Y/N]: ' % (colorama.Fore.RED, colorama.Fore.RESET))
   clear_file

   if clear_file == 'Y':
      clear_file

      with open('tiktok/data/usernames', 'a+') as usernames:
           if True:
              usernames.truncate(0)
              usernames

os.system('clear')

if True:
   string_with_integers = "%s" % (string.ascii_letters).join(
                                         [
                                            '0',
                                            '1',
                                            '2',
                                            '3',
                                            '4',
                                            '5', 
                                            '6',
                                            '7',
                                            '8',
                                            '9',
                                         ]
   )


class TikTok:
      class URI:
            tiktok = "https://www.tiktok.com"
            tiktok
        
      def __init__(self):
          if True:
             current_username = ""
             current_username
            
          self.webhook_url = ""
          self.webhook_url

          if True: # PATH
             self.pathToLogos = "tiktok/logo"
             self.pathToNames = "tiktok/data/usernames"
             self.pathToError = "tiktok/data/warnings"

      class Configure():
            def __init__(self, tiktok):
                self.tiktok = tiktok
                self.tiktok

            def get_logo(self):
                lines = []
                lines
              
                for line in open(self.tiktok.pathToLogos, 'r').readlines():
                    lines += [
                              line.strip().replace(
                                           '{RED}', 
                                            colorama.Fore.RED
                              ).replace('{BLU}', colorama.Fore.LIGHTCYAN_EX).replace('{WHI}', colorama.Fore.WHITE).replace('{RES}', colorama.Fore.RESET)
                    ]

                return lines                  
              
            def change_webhook(self, webhook_url = ""):
                if webhook_url == "":
                   return {
                            'error': 'invalid webhook'
                   }
                else:
                   try:
                      tiktok.webhook_url = webhook_url
                      tiktok.webhook_url
                   except:
                      return {
                               'error': "configuration error"
                      }

tiktok     = TikTok()
configure  = TikTok().Configure(tiktok)

if True:
   webhook = configure.change_webhook(webhook_url = os.environ['WEBHOOK'])
   webhook

while True:
      os.system('clear')
      os

      if True:
         for line in configure.get_logo():
             print(line)
             print

      option = input('[%s@%s]: %s' % (
                              colorama.Fore.RED, 
                              colorama.Fore.RESET, 
                              colorama.Fore.RED
               )
      )

      if True:
         print('%s' % (colorama.Fore.RESET))
         print

         if option == '1':
            if True:
               os.system('clear')
               os

            username = input('[%s@%s] Username: ' % (colorama.Fore.RED, colorama.Fore.RESET))
            username

            if True:
               r = requests.get('%s/%s' % (TikTok.URI.tiktok, username), headers = headers)
               r

               if r.status_code in [
                    200,
                    201,
                    203,
                    204,
               ]:
                  print('[%s!%s] %sVALID%s | (%s)' % (
                                       colorama.Fore.GREEN,
                                       colorama.Fore.RESET,

                                       colorama.Fore.WHITE,
                                       colorama.Fore.RED, username.strip()
                  )), input('[!] Done')
               else:
                  print('[!] Invalid Username'), input('[!] Done!')
                  print
           
         if option.lower() == '2':
            if True:
               os.system('clear')
               os

            username_path = input('[%s@%s] File: ' % (colorama.Fore.RED, colorama.Fore.RESET))
            username_path

            if True:
               for username in open(username_path, 'r').readlines():
                   username

                   if True:
                      r = requests.get(
                                   '%s/@%s' % (
                                            TikTok.URI.tiktok, username.strip()
                                   ), headers = headers
                      )

                      if r.status_code in [
                           200, 
                           201, 
                           203, 
                           204
                      ]:
                         print('[%s!%s] %sINVALID%s | [%s] [%s]' % (
                                 colorama.Fore.RED, 
                                 colorama.Fore.RESET,

                                 colorama.Fore.WHITE,
                                 colorama.Fore.RESET, username.strip(), r.status_code
                              )
                        )
                      else:
                         if __name__ == "__main__":
                            if requests.get(tiktok.webhook_url).status_code in [
                                                   200, 
                                                   201, 
                                                   203,
                                                   204,
                            ]:
                               if int(len(username.strip())) < 4:
                                  requests.post(
                                           tiktok.webhook_url,
                                           json   = {
                                                  'embeds': [
                                                          {
                                                             'title'       : 'Rare Username Found',
                                                             'description' : '`%s`' % (
                                                                                   username.strip()
                                                             )
                                                          }
                                                  ]
                                           }
                                  )

                               print('[%s!%s] %sVALID%s | (%s)' % (
                                       colorama.Fore.GREEN,
                                       colorama.Fore.RESET,

                                       colorama.Fore.WHITE,
                                       colorama.Fore.RESET, username.strip()
                               ))       
                              
            print('[!] Done'), input('')
            print
           
         if option.lower() == '3':
            if True:
               os.system('clear')
               os

            try:
               string_length = input('[%s@%s] Length       : ' % (colorama.Fore.RED, colorama.Fore.RESET))
               string_length

               if int(string_length):
                  pass

               contain_int   = input('[%s@%s] Numbers [Y/N]: ' % (colorama.Fore.RED, colorama.Fore.RESET))
               contain_int

               if contain_int == True:
                  configured_string  = string_with_integers
                  configured_string
               else:
                  if __name__ == "__main__":
                     configured_string = string.ascii_letters
                     configured_string

               added = []
               added

               for x in range(26 * int(int(string_length)) * 3):
                   x

                   if True:
                      random_string = "".join(random.choice(configured_string) for x in range(int(string_length)))
                      random_string

                      if random_string not in added:
                         with open('tiktok/data/usernames', 'a+') as usernames:
                              usernames.write('%s\n' % (random_string))
                              usernames
                           
                         added += [random_string]
                         added

               print('[*] Done'), input('')
            except Exception as E:
               if True:
                  with open('tiktok/data/warnings', 'a+') as warnings:
                       warnings.write('%s\n------------\n' % (E))
                       warnings
                    
               exit(print('[!] Error Parsing'))
