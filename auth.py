from main import preprocess_image, authenticate
import os

original = 'amber.png'
auth = 'amber-edited.png'

original_img = preprocess_image(os.path.join('signature authentication',original))
auth_img = preprocess_image(os.path.join('signature authentication',auth))
authenticate(original_img, auth_img)



