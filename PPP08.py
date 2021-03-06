# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:07:08 2020

@author: matth
"""

import sympy

from Crypto.PublicKey import RSA

privateKey = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAzU6g/of54RvchTm5Qq0ec9Ve/BYikcYbsdvNk8/FFzhOicQ6
BseSOuvgbnuLxcJVW5gWgpOWqlu/tMOESquIoPbdnI1joIaVnDRfzzj5ZABuncnM
joU8FrD73q03LQILT6MgQBQKAY1BZnnfDikUe2cQXY/ZddVz2EexNejAd/qr1XlV
IPOPvZt5Irj23a366Hz/J0tbPmzdEeYZGJCDW4qPqG73Z4CKv+AN4K5vMNI2uRnJ
RXlvCGgNs2KM8WCDelzL0MNwEfIbxIjigA+zZ4AsHsfdGc4l9ukiytd463wscaPz
l2/A1g7rBd2jSDoN+FqgNQTDQKwRLGz76cLsTwIDAQABAoIBAAon+5rbyyaxpCUL
B/kea0U7puk9hxRDApe30eGgA5X0eR4jkONI+BjmFkIg5ncv990CFwr6lhdzVnZw
vZicB7Q+whO+gtEsFzaU+LBdlyi1RMOVegMK4EAXHT6UvwgA8+JKpYvF8gDFphiV
qs0ehx7bqFmYhh9oIcTvNvr9upe0vgN69jvTjrlnZRZ5LJazgtCPuShq0Y0cl3fi
u3idx3NzqMRLz5LJo6Os8QI7b2IhG4UhAuDAZimSxNGtWPIPGpeMqGrVDof+Ss7J
I4hS3V5gFIrIk+QuMa+r51kDVl+4EKqOCUDLEaG8kzttCRGampYZZs3D9bRnD51P
+Z7yJeECgYEA/XOnrI15kviSSyZRMxIU0B4f75nyiU+1Cch9ktF3ElIOMhz+FoGO
rQcqq5OV2qJqzO4+ixII1MdDNI0k4rdFVX0caXB6WXGBMxHE2zBxQzP6ixUAaWcG
JZA0QFUYMCtJ5NT/PxKW4LR9MaazgfZ6VEWw3+/DX5EXu7X/TNlkNskCgYEAz18O
pBeFKB+tOighZ0KCdr9sj03csRbR/tZDdmDmlWvJaqf66szlg5lkoRBCTa5spwyr
jGTFLesocxfbOiVBgSpR6rUiSd7B3MTGDnXOUISVCJH7W1FVW2C828Euq9h7hwy3
WxEPpIdqe05nNXvIjeWEQEHg8A31nZsZl8ai3lcCgYBNTLzS78MohA96RBF31gfr
AYUT+ovyPREmDrPd12zNdaFGv3jvPExbkVf+RGDr8aVJI1CH8dQnsS5aFMIvM14+
GI5VyixGo0uYW88CWt/wcyXyzVD21KkXQ8fr5wgdiNZcqGnAvtatad7VCdatyJK+
qRKs+d9IgmQOqA9ZTOQ3oQKBgB+PQfUrNzKyD3UIYn0KnDxiSa1NlkbFSFRWW5IK
kU0wSEkZI5DUeiGbGLuCc/TKlPKfdQQ62d9xKIjLmquwu9VikXD8/Cjt4+crc1EE
ENAkPWI+hViSekEb6eIv9mBk4/fbsZQEdrL9gPEfL4nuOsmNoqD85bTjCvxffHei
3WqlAoGAPkZAcTwNY6Yo5XdTFzh355ekB6SX+MFAQOOU+evYcPBhxS5Zk3SqkbaW
ENIxtkNfhpcb7H5ZGvegKyNrXj2cVg4B9q1KRakqt57Hl48dkntp/FsB8LHxXUm2
JSh2OHzk62JR/F7mlFk99QaSgHpImS4+To4mzYnqdyk1cOneVic=
-----END RSA PRIVATE KEY-----"""

key = RSA.importKey(privateKey)

title_page = 'THE BOOK OF MORMON AN ACCOUNT WRITTEN BY THE HAND OF MORMON UPON PLATES TAKEN FROM THE PLATES OF NEPHI WHEREFORE IT IS AN ABRIDGMENT OF THE RECORD OF THE PEOPLE OF NEPHI AND ALSO OF THE LAMANITES WRITTEN TO THE LAMANITES WHO ARE A REMNANT OF THE HOUSE OF ISRAEL AND ALSO TO JEW AND GENTILE WRITTEN BY WAY OF COMMANDMENT AND ALSO BY THE SPIRIT OF PROPHECY AND OF REVELATION WRITTEN AND SEALED UP AND HID UP UNTO THE LORD THAT THEY MIGHT NOT BE DESTROYED TO COME FORTH BY THE GIFT AND POWER OF GOD UNTO THE INTERPRETATION THEREOF SEALED BY THE HAND OF MORONI AND HID UP UNTO THE LORD TO COME FORTH IN DUE TIME BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANTS OF THE LORD THAT THEY ARE NOT CAST OFF FOREVER AND ALSO TO THE CONVINCING OF THE JEW AND GENTILE THAT JESUS IS THE CHRIST THE ETERNAL GOD MANIFESTING HIMSELF UNTO ALL NATIONS AND NOW IF THERE ARE FAULTS THEY ARE THE MISTAKES OF MEN WHEREFORE CONDEMN NOT THE THINGS OF GOD THAT YE MAY BE FOUND SPOTLESS AT THE JUDGMENT SEAT OF CHRIST'

def abr(n, b):
      d = n // b
      m = n % b
      if (d == 0):
          return [m]
      else:
          l = abr(d, b)
          l.append(m)
          return l

def reconstruct_number_from_abr(list_of_coefficients, base):
      result = 0
      power = 1
      for coeff in list_of_coefficients:
          result += coeff * power
          power *= base
      return result

def from27to10(alphabetic_message):
      l = list(map(lambda n: int(ord(n) - ord('@')), alphabetic_message))
      l.reverse()
      return reconstruct_number_from_abr(l, 27)

def to27from10(decimal_number):
      l = list(map(lambda n: chr(n + ord('@')), abr(decimal_number, 27)))
      return ''.join(l)

def igcd(b, n):
      x0, x1, y0, y1 = 1, 0, 0, 1
      while n != 0:
          q, b, n = b // n, n, b % n
          x0, x1 = x1, x0 - q * x1
          y0, y1 = y1, y0 - q * y1
      return b, x0, y0

def TUMMI(e, t):
      hcf, x, y = igcd(e, t)
      if hcf != 1:
          raise ValueError(f"TUMMI does not exist for e = {e} and t = {t}.")
      return x % t

def RSAencrypt(m, e, n, encoder=lambda x: x):
      message_encoded = encoder(m)
      encrypted = pow(message_encoded, e, n)
      return encrypted

def RSAdecrypt(encrypted, d, n, decoder=lambda x: x):
      decrypted = pow(encrypted, d, n)
      message_decoded = decoder(decrypted)
      return message_decoded

RSAplayers = {}

def populateRSAplayers(p, q, e = 2 ** 16 + 1):
      global RSAplayers
      n = p * q
      t = (p - 1) * (q - 1)
      d = TUMMI(e, t)
      RSAplayers['p'] = p
      RSAplayers['q'] = q
      RSAplayers['n'] = n
      RSAplayers['t'] = t
      RSAplayers['e'] = e
      RSAplayers['d'] = d

def round_trip(message, n, e, d, encoder=lambda x: x, decoder=lambda x: x):
      return message == RSAdecrypt(RSAencrypt(message, e, n, encoder), d, n, decoder)

x = 177979890619473945197204479753610471412080471556695548170777130366743840076039502662876748076963100473304963352590545433016597654993502523750394723485226239613519787056873595194902850137382499662419928837003477175462658073618318069595209725376131494946301812427316858866682753117975608975871345623801742505673
y = 145621091099427821970355196426414899695448605313736047637292312641594120085318624088348378001393944019065335296367166589879330552584041557870666727258326498014315349660563186678271377614788059065223777868863406904969330950903096977665577757319923494479055778350175391403999223156138440588539141065367091338839

def testRSA(message_with_spaces):
    global RSAplayers   
    populateRSAplayers(x, y)
    message = '@'.join(message_with_spaces.split(' '))
    n = RSAplayers['n']
    e = RSAplayers['e']
    d = RSAplayers['d']
    encrypted = RSAencrypt(message, e, n, from27to10)
    decrypted = RSAdecrypt(encrypted, d, n, to27from10)
    decrypted_message_with_spaces = ' '.join(decrypted.split('@'))
    success = (message_with_spaces == decrypted_message_with_spaces)
    # if success:
    #     print('"{}" was encoded and encrypted as\n\n{}\n\nthen decrypted and decoded as\n\n"{}"\n'.
    #           format(message_with_spaces, encrypted, decrypted_message_with_spaces))
    #     print(f'successfully with {w} and {w+1}')
    if success:
        print(f"{message_with_spaces} \n\n")

def sequence_size(size):
    for q in range(len(title_page) - size - 500):
        modified_message = title_page[q:q+size]
        testRSA(modified_message)
       
       
#sequence_size(431)

# print('e: {}\n' .format(key.e))
# print('d: {}\n' .format(key.d))
# print('p: {}\n' .format(key.p))
# print('q: {}\n' .format(key.q))


#AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANTS OF THE LORD THAT THEY ARE NOT CAST OFF FOREVER AND ALSO TO THE CONVINCING OF THE JEW AND GENTILE THAT JESUS IS THE CHRIST THE ETERNAL GOD MANIFESTING HIMSELF UNTO ALL NATIONS 
#GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANTS OF THE LORD
#BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANT 
#DUE TIME BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE 
#COME FORTH IN DUE TIME BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THE 
#BY THE HAND OF MORONI AND HID UP UNTO THE LORD TO COME FORTH IN DUE TIME BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS 
#BY THE GIFT AND POWER OF GOD UNTO THE INTERPRETATION THEREOF SEALED BY THE HAND OF MORONI AND HID UP UNTO THE LORD TO COME FORTH IN DUE TIME BY WAY OF THE GENTILE THE INTERPRETATION THEREOF BY THE GIFT OF GOD AN ABRIDGMENT TAKEN FROM THE BOOK OF ETHER ALSO WHICH IS A RECORD OF THE PEOPLE OF JARED WHO WERE SCATTERED AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH  
#BOOK OF MORMON AN ACCOUNT WRITTEN BY THE HAND OF MORMON UPON PLATES TAKEN FROM THE PLATES OF NEPHI WHEREFORE IT IS AN ABRIDGMENT OF THE RECORD OF THE PEOPLE OF NEPHI AND ALSO OF THE LAMANITES WRITTEN TO THE LAMANITES WHO ARE A REMNANT OF THE HOUSE OF ISRAEL AND ALSO TO JEW AND GENTILE WRITTEN BY WAY OF COMMANDMENT AND ALSO BY THE SPIRIT OF PROPHECY AND OF REVELATION WRITTEN AND SEALED UP AND HID UP UNTO THE LORD THAT THEY MIGHT 


#most likely answer
#AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANTS OF THE LORD THAT THEY ARE NOT CAST OFF FOREVER AND ALSO TO THE CONVINCING OF THE JEW AND GENTILE THAT JESUS IS THE CHRIST THE ETERNAL GOD MANIFESTING HIMSELF UNTO ALL NATIONS

string = "AT THE TIME THE LORD CONFOUNDED THE LANGUAGE OF THE PEOPLE WHEN THEY WERE BUILDING A TOWER TO GET TO HEAVEN WHICH IS TO SHOW UNTO THE REMNANT OF THE HOUSE OF ISRAEL WHAT GREAT THINGS THE LORD HATH DONE FOR THEIR FATHERS AND THAT THEY MAY KNOW THE COVENANTS OF THE LORD THAT THEY ARE NOT CAST OFF FOREVER AND ALSO TO THE CONVINCING OF THE JEW AND GENTILE THAT JESUS IS THE CHRIST THE ETERNAL GOD MANIFESTING HIMSELF UNTO ALL NATIONS"
print(len(string))
print(len(title_page))