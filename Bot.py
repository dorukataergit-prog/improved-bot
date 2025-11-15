import random
import discord
import os
import requests
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

def get_duck_image_url():    
    url = ' https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def cevre_resimleri(ctx):
    cevre_files = os.listdir("cevre_images")
    selected_cevre_file = random.choice(cevre_files)

    with open(f"cevre_images/{selected_cevre_file}", 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        cevre_picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=cevre_picture)


@bot.command()
async def cevre_onerileri(ctx):
    oneriler = ["Kullanmadığın lambaları, bilgisayarları ve cihazları kapat. Enerji tasarruflu LED ampuller kullan.",
                "Dişlerini fırçalarken musluğu kapat, kısa duş al, damlayan muslukları tamir ettir.",
                "Plastik, cam, metal ve kağıt atıkları ayrı kutularda topla. Geri dönüşüm kutularına at.",
                "Plastik şişe, poşet, pipet gibi şeyler yerine cam şişe, bez çanta ve metal pipet kullan.",
                "Kısa mesafelere yürüyebilir veya bisiklet sürebilirsin. Toplu taşıma da çevreye daha az zarar verir.",
                "Evinde saksıda bitki yetiştirmek bile doğaya katkı sağlar. Mümkünse bir fidan dik.",
                "Yakında üretilen gıdalar hem daha taze olur hem de taşımada az karbon salınır.",
                "Kullanılmış pilleri çöpe atma, atık pil toplama kutularına ver.",
                "Kıyafetleri, oyuncakları veya kutuları başka işlerde değerlendir. “Atmak yerine dönüştür.”",
                "Arkadaşlarına da çevreyi korumanın önemini anlat. Küçük adımlar birleşince büyük etki yaratır"]
    oneri_secimi = random.choice(oneriler)
    await ctx.send(oneri_secimi)

@bot.command()
async def mem(ctx):
    files = os.listdir("meme_images")
    selected_file = random.choice(files)

    with open(f"meme_images/{selected_file}", 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


bot.run("Add Your Discord Token Here")
