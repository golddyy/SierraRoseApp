import io
import os
import PySimpleGUI as sg
from PIL import Image
import requests
import wget
import shutil

file_types = [('JPEG (*.jpg)', '*.jpg'),
              ('All files (*.*)', '*.*')]



image_url = 'https://imgprd19.hobbylobby.com/2/4f/57/24f57e245a879cb2543edd1df4e090bfebf24a45/700Wx700H-1013689-0320.jpg' #replace this with whatever url you want
filename = image_url.split("/")[-1]
r = requests.get(image_url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')

image_url = 'https://imgs.michaels.com/MAM/assets/1/726D45CA1C364650A39CD1B336F03305/img/91F89859AE004153A24E7852F8666F0F/10093625_r.jpg' #replace this with whatever url you want
filename2 = image_url.split("/")[-1]
r = requests.get(image_url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename2,'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print('Image sucessfully Downloaded: ',filename2)
else:
    print('Image Couldn\'t be retreived')


# img = ImageQt.Image.open(response.raw)
# data = image_to_data(img)
cart = []
price = 0
item1 = 'ARTICLE ONE'
item2 = 'ARTICLE TWO'

def item(img, name, p):
    while True:
        if img != '':
            layout3 = [
                [sg.Button('Back', key = 'w2back')],
                [sg.Text('\n\n' + str(name)), sg.Text('\n\n\t' + str(p))], 
                [sg.Image(key = 'w2image')], [sg.Button('Add to cart')]
            ]
        else:
            layout3 = [
                [sg.Button('Back', key = 'w2back')],
                [sg.Text('\n\n' + str(name)), sg.Text('\n\n\t' + str(p))], 
                [sg.Button('Proceed to checkout', key = 'Add to cart')]
            ]
        win = sg.Window(str(name), layout3, finalize = True)

        if img != '':
            win['w2image'].update(data=img.getvalue())

        event3 = win.read()

        if event3 == ('w2back', {}) or event3 == sg.WIN_CLOSED:
            win.close()
            return [0, '']
            break

        if event3 == ('Add to cart', {}):
            if  img == '':
                quit()
            win.close()
            return [p, str(name)]
            break  

def main():
    
    cart = []
    price = 0
    
    layout = [
        [sg.Image(key='-IMAGE-')],
        [sg.Text('Welcome to the store!')],
        [sg.Button('Browse catalogue')],
    ]
    window = sg.Window('Clothing Store', layout)
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        
        if event ==  'Browse catalogue':

            
            
            #layout
            layout2 = [
                [sg.Button('Back')], [sg.Text('\n\n\n')],
                [sg.Image(key='img1'), sg.Image(key='img2')],
                [sg.Text('\t'), sg.Button('View', key = 'v1'), sg.Text('\t\t\t'), sg.Button('View', key = 'v2'), sg.Text('\n\n\n\n\n\n\n')],
                [sg.Text('\t\t\t'), sg.Button('Cart', s=(5, 2))],
            ]
            
            win2 = sg.Window('Fall collection', layout2, finalize = True, size=(500, 600))
            
            while True:
                                
                #image loading
                image = Image.open(filename)
                image.thumbnail((200, 420))
                bio = io.BytesIO()
                image.save(bio, format='PNG')
                win2['img1'].update(data=bio.getvalue())

                image2 = Image.open(filename2)
                image2.thumbnail((200, 200))
                bio2 = io.BytesIO()
                image2.save(bio2, format='PNG')
                win2['img2'].update(data=bio2.getvalue())

                
                #event reading
                event2, values = win2.read()

                print(price)

                if event2 == 'v1':
                    i = item(bio, item1, 19.99)
                    if i[0] > 0:
                        price += i[0]
                        cart.append(i[1])
                    print(str(cart) + ' ' + str(price))

                    

                if event2 == 'v2':
                    i = item(bio2, item2, 24.99)
                    if i[0] > 0:
                        price += i[0]
                        cart.append(i[1])
                    print(str(cart) + ' ' + str(price))


                if event2 == 'Cart':
                    item('', '\n'.join(cart) + '\n\n $' + str(price), '')

                
                if event2 == 'Back' or event2 == sg.WIN_CLOSED:
                    event = 'nothing'
                    break
            win2.close()
            
    window.close()
    
if __name__ == '__main__':
    main()

