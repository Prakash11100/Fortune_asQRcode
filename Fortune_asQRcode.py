import qrcode
import image
import random

class msgr:
    def __init__(self,name,rd):
        self.name=name
        self.rd=rd
    def message(self):
        if self.rd == 1:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Your patience will soon be rewarded with unexpected joy '
        elif self.rd==2:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n A new opportunity will present itself seize it with confidence '
        elif self.rd==3:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Great Things are on the horizon keep your eyes open'
        elif self.rd==4:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Trust in your instincts They will guide you toward success '
        elif self.rd==5:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n A pleasant surprise awaits you in the near future'
        elif self.rd==6:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Your hardwork will soon pay off Bringing you closer to your dreams'
        elif self.rd==7:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n The road ahead is bright Continue moving forward with courage '
        elif self.rd==8:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n An Exciting adventure is just around the corner '
        elif self.rd==9:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Now is the perfect time to start something New!'
        elif self.rd==10:
            return f'{self.name} got Lucky Number {self.rd} and Your Fortune:\n Happiness is within your reach keep striving toward it '

name=input("Enter your Good name: ")
rd=random.randint(1,10)
obj_msgr=msgr(name,rd)
result=obj_msgr.message()

qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture.
    box_size = 10, # size of the box where qr code will be displayed
    border = 5 #it is the white part of image . . border in all 4 sides with white color

)

data = result

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill='black',back_color = 'white')
img.save('Message.png')