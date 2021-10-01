import re

urls = [ "iab-oantagonista.min.js", "iab.min.js", "sign/pormaisvacina/gabriel_spina.png", "", "sign/pormaisvacina/victor_canas.png", "sign/pormaisvacina/debora_monteiro.png", "", "sign/pormaisvacina/thadeu_aires.png", "sign/pormaisvacina/joao_victor.png", "sign/pormaisvacina/leticia_santos.png", "sign/pormaisvacina/diego_muntowyler.png", "sign/pormaisvacina/marcos_venancio.png", "sign/gleice_santana.jpg", "sign/pormaisvacina/thiago_toffoli.png", "sign/pormaisvacina/ricardo_rodrigues.png", "sign/pormaisvacina/alexandre_germano.png", "nobeta.iquilibrio.js", "sign/lgbtqia/sign_diego_muntowyler.png", "robots.txt", "midia/midiakit_2020_nobeta.pdf", "sign/pormaisvacina/andre_pontual.png", "sign/pormaisvacina/priscila_cabral.png", "sign/pormaisvacina/renato_yan.png", "creatives/dell/assets/sent.png", "sign/natal/diego_muntowyler.jpg", "creatives/dell/assets/dell_logo.png", "sign/diego_muntowyler.jpg", "creatives/dell/index.html", "sign/novembroazul/diego_muntowyler.png" ]

def extractSiteCdn( txt ):
    # vazio
    if len( txt ) == 0:
        return 'outros'

    # identificar tag iab.min.js
    if txt == 'iab.min.js':
        return txt

    # identificar assinaturas
    x = re.search("^sign/.*/(.*)\.", txt)
    if x is not None:
        res = x[1].replace('sign_', '')
        return 'sign-' + res

    x = re.search("^sign/(.*)\.", txt)
    if x is not None:
        res = x[1].replace('sign_', '')
        return 'sign-' + res

    # idenfificar tag iab de parceiro
    x = re.search("^iab-(.*)\.min\.js", txt)
    if x is not None:
        return x[1]

    # identificar versão cdn da tag nobeta
    x = re.search("^sign/(.*)\.", txt)
    if x is not None:
        return x[1]

    # midia kit
    if txt == 'midia/midiakit_2020_nobeta.pdf':
        return 'midia'

    # agrupar se não encaixar em nenhum item
    return 'outros'

for url in urls:
    res = extractSiteCdn( url )
    if res is not None:
        print ( url, ' | ', res )