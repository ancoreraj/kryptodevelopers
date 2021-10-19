from PIL import Image, ImageOps
from IPython.display import display
import json

# READ METADATA
with open("../traitsgeneration/traits.json", 'r') as f:
        traits = json.load(f)

backgroundfiles = {
    "Bedroom": "bg1",
    "Mint": "bg2",
    "Pink": "bg3",
    "Grey": "bg4",
    "Baby Blue": "bg5",
    "Amber": "bg6",
    "Purple Haze": "bg7",
    "Sherbert": "bg8",
    "Northern Lights": "bg9",
    "Downtown": "bg10",
    "Tag it": "bg11",
    "Gold": "bg12"
}

#### IMAGE GENERATION
for trait in traits:

    im1 = Image.open(f'../images/backgrounds/{backgroundfiles[trait["Background"]]}.jpg').convert('RGBA')
    im1 = Image.open(f'../images/backgrounds/{backgroundfiles[trait["Background"]]}.jpg').convert('RGBA')


    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    #Convert to RGB
    rgb_im = com4.convert('RGB')
#     display(rgb_im.resize((400,400), Image.NEAREST))

    file_name = str(trait["tokenId"]) + ".jpg"
    rgb_im.save("./output/" + file_name)
    print(f'{str(trait["tokenId"])} done')





## ADD IPFS HASH TO JSON, ASSUMING YOU HAVE A JSON FILE LIKE THIS:

# '''
# {
# "QmeBdP4zNCEEbqm9Y2UZb6skg8RVLkgDzQ2ojgZf71cBc8": "0",
# "QmWBLUBgVJfSGQDHDR5LNyccRatnsBDjUwtCv7DpiQ9N11": "1",
# "QmejsSBzpYyeG8SgyZejrCxrABS4t7e1fjysstBJkNr6Bg": "10",
# "QmSVRL6dGQVzUXXy6Q4dPa3mebS755Xeek1b9ZejMyfY8L": "11",
# "QmZYBEBbR3SBA56UVSdcGyRKQqceQ2s35paoGrtuixqP6F": "12",
# "QmYHZkLv8EAfz3PW8Sfoxb9q64Dp5GZDrsA3soZhteJcLZ": "13",
# "QmfHendumMaxewRf6WHCwqGdqbQMSyjv2BvHRVbKNfSfLm": "14",
# "QmaAzUXKmpmu85yprJG4RDj8b1DdKxS6r3rbarCHAjtrZX": "15",
# "QmS4auQV9y8agQCatWYcBKWPEHbyX2CXS1qAxFoGnGmE7W": "16",
# "Qmd98fff2dWLxuUbt2sCMmtcGMGHh93Cfc8Qi3nrieG1FC": "17",
# "QmWKTi9tH4HsukveKQ4NnzzV2R9RwPtV158iac9ttnD7Si": "18",
# "QmXXD5p2NTS4JtuQiJPJQRdm7fNb69d9siAMzKHr7EPkJj": "19",
# "QmQMUzcnFwxCDx9UAPditJ77BRHaPri9eooBxxZKZgQXCN": "2",
# "QmQPyYCPuzTLkfGRXnsDV599vi5myc1wByVYAtiS3pa8Da": "20",
# "QmNobN7UAchYkGtKB4smCcpvS8KtHjmizqgYNJjzx4dbkx": "3",
# "QmQoYWWUfjrgKTmCpTizLh4wiSQb6UcLwRPEwLJfHskj7h": "4",
# "Qmf4paFPr1bm73gMf5jnC5Z63gD5dz4Dhn8Vc2tAznx51w": "5",
# "QmUFxGMvdnL3EgFMqxfuv8WjuUKLeUtycJ8bnryRuj5yWg": "6",
# "QmV5gjEaXDiLP8baFiVZFvg5KjXDEyrGjukgoXaLmz95Jf": "7",
# "QmbmiZi87dyi6ujwwtSLkR8D3hkM14PeRCpQg4UcR5aeyJ": "8",
# "QmddrDppXDqhsVxtEMKvvzZCFZGZVToHRQGqyzeCsbo49e": "9"
# ...
# }
        
with open("jsonlocation", 'r') as f:
    hashes = json.load(f)
    
for k,v in hashes.items():
    print(k,v)
    traits[v]["imageIPFS"] = k


with open('traitsfinal.json', 'w') as outfile:
json.dump(traits, outfile, indent=4)