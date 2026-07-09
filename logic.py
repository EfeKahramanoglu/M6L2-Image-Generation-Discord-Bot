import requests  # HTTP istekleri göndermek için gerekli kütüphaneyi içe aktarıyoruz.
from urllib.parse import quote  # URL'yi güvenli hale getirmek için quote fonksiyonunu içe aktarıyoruz.

TOKEN = "YOUR_TOKEN_HERE"  # Botunuzun token'ını buraya ekleyin.

class Imgapi:

    def download_image(self, prompt):

        url = f"https://image.pollinations.ai/image/{prompt}"
        

        response = requests.get(url)
        
        encoded_prompt = quote(prompt) 
        url = f"https://image.pollinations.ai/image/{encoded_prompt}" 


        with open('generated_image.jpg', 'wb') as file:
      
            file.write(response.content)
            
      
        print('Resim indirildi!')
        return "generated_image.jpg"  
    
api = Imgapi()  

if __name__ == "__main__":

    prompt = input("Resim için bir prompt girin: ")
    api.download_image(prompt)